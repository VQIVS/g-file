from rest_framework import viewsets
from services.bank_accounts.models import BankAccount
from rest_framework.permissions import IsAuthenticated
from .serializers import BankAccountSerializer


class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]
