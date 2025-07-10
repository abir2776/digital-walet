from decimal import Decimal

from django.core.cache import cache
from django.db import transaction
from rest_framework.exceptions import ValidationError

from .choices import Type
from .models import Transaction


class WalletService:
    @staticmethod
    def get_wallet_balance(user):
        cache_key = f"wallet_balance_{user.id}"
        cached_balance = cache.get(cache_key)

        if cached_balance:
            return Decimal(cached_balance)

        # Get from database
        try:
            wallet = user.wallet
        except:
            raise ValidationError("Wallet not found")

        # Cache the balance for 5 minutes
        cache.set(cache_key, str(wallet.balance), timeout=300)

        return wallet.balance

    @staticmethod
    def wallet_transaction(user, transaction_data):
        with transaction.atomic():
            # Get wallet
            try:
                wallet = user.wallet
            except:
                raise ValidationError("Wallet not found")

            # Create transaction record
            if transaction_data[
                "transaction_type"
            ] == Type.TRANSFER and transaction_data.get("transfer_user", None):
                wallet.balance = wallet.balance - Decimal(transaction_data["amount"])
                wallet.save()
                recipient_wallet = transaction_data["transfer_user"].wallet
                recipient_wallet.balance = recipient_wallet.balance + Decimal(
                    transaction_data["amount"]
                )
                recipient_wallet.save()
                new_transaction = Transaction.objects.create(
                    user_id=user.id,
                    transfer_user=transaction_data["transfer_user"],
                    transaction_type=transaction_data["transaction_type"],
                    amount=Decimal(transaction_data["amount"]),
                    description=transaction_data["description"],
                    status="COMPLETED",
                )
            else:
                if transaction_data["transaction_type"] == Type.WITHDRAWAL:
                    wallet.balance = wallet.balance - Decimal(
                        transaction_data["amount"]
                    )
                else:
                    wallet.balance = wallet.balance + Decimal(
                        transaction_data["amount"]
                    )
                wallet.save()
                new_transaction = Transaction.objects.create(
                    user_id=user.id,
                    transaction_type=transaction_data["transaction_type"],
                    amount=Decimal(transaction_data["amount"]),
                    description=transaction_data["description"],
                    status="COMPLETED",
                )

            # Invalidate cache
            cache_key = f"wallet_balance_{user.id}"
            cache.delete(cache_key)
            if transaction_data.get("transfer_user", None):
                cache_key = f"wallet_balance_{transaction_data['transfer_user'].id}"
                cache.delete(cache_key)

            return new_transaction
