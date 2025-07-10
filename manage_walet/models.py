from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from common.models import BaseModelWithUID

from .choices import Status, Type


class Wallet(BaseModelWithUID):
    user = models.OneToOneField("core.User", on_delete=models.CASCADE)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
        help_text="Amount must be zero or positive",
    )

    def __str__(self):
        return f"User: {self.user.first_name}, Balance: {self.balance}"


class Transaction(BaseModelWithUID):
    user = models.ForeignKey(
        "core.User", on_delete=models.CASCADE, related_name="transactions"
    )
    transfer_user = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        related_name="received_transactions",
        blank=True,
        null=True,
    )
    transaction_type = models.CharField(max_length=20, choices=Type.choices)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
        help_text="Amount must be zero or positive",
    )
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    def __str__(self):
        return f"Amount: {self.amount}, Type: {self.transaction_type}, Status: {self.status}"
