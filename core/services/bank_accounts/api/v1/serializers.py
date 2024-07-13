from rest_framework import serializers
from services.bank_accounts.models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['BankAccountID', 'UserID', 'AccountNumber', 'BankName', 'Branch', 'SwiftCode']
