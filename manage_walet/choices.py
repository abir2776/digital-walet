from django.db import models


class Status(models.TextChoices):
    PENDING = "PENDING", "Pending"
    COMPLETED = "COMPLETED", "Completed"
    FAILED = "FAILED", "Failed"


class Type(models.TextChoices):
    TOPUP = "TOPUP", "TopUp"
    WITHDRAWAL = "WITHDRAWAL", "Withdrawal"
    TRANSFER = "TRANSFER", "Transfer"
