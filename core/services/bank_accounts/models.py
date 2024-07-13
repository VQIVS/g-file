from django.db import models
from django.conf import settings


class BankAccount(models.Model):
    BankAccountID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    AccountNumber = models.CharField(max_length=50)
    BankName = models.CharField(max_length=100)
    Branch = models.CharField(max_length=100)
    SwiftCode = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.BankName} - {self.AccountNumber}"
