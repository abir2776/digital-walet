from decimal import Decimal

from rest_framework import serializers

from core.models import User
from manage_walet.helpers import WalletService
from manage_walet.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    transfer_user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Transaction
        fields = [
            "id",
            "user",
            "transaction_type",
            "amount",
            "description",
            "status",
            "transfer_user",
        ]
        read_only_fields = ["id", "status", "user"]

    def validate_amount(self, value):
        if value < Decimal("0.00"):
            raise serializers.ValidationError("Amount cannot be negative.")
        return value

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user if request else None
        return WalletService.wallet_transaction(user, validated_data)
