from django.urls import path

from manage_walet.rest.views.wallet import UserBalanceView, UserTransactionView

urlpatterns = [
    path(
        "balance",
        UserBalanceView.as_view(),
        name="user-balance",
    ),
    path(
        "transactions",
        UserTransactionView.as_view(),
        name="user-transactions",
    ),
]
