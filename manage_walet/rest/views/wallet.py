from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from manage_walet.helpers import WalletService
from manage_walet.models import Transaction
from manage_walet.rest.serializers.transactions import TransactionSerializer


class UserBalanceView(APIView):
    def get(self, request):
        balance = WalletService.get_wallet_balance(request.user)
        return Response({"balance": balance})


class UserTransactionView(ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.filter(user_id=user.id)
        return queryset
