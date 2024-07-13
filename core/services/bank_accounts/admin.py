from django.contrib import admin
from .models import BankAccount


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('BankAccountID', 'UserID', 'AccountNumber', 'BankName', 'Branch', 'SwiftCode')
    search_fields = ('AccountNumber', 'BankName', 'Branch', 'SwiftCode')
