from decimal import Decimal
from django.db import models
from django.db import db_transaction
import uuid


class Account(models.Model):
    """
    Represents a bank account in the system.

    The users of Account and Transaction model should make sure that the
    following conditions are always True:
        account.balance == sum(
           t.amount for t in account.transactions.all() if t.active
        )
        account.balance >= 0
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)

    @classmethod
    def create_account(self, user, name):
        return Account.objects.create(user=user, name=name, balance=0)

    @db_transaction.atomic
    def record_transaction(self, transaction_date, amount, description=''):
        locked_account = Account.objects.select_for_update().get(
            uuid=self.uuid)
        if locked_account.balance + amount < 0:
            raise ValueError(
                "Recording transaction would lead to negative balance!")
        locked_account.balance += amount
        locked_account.save()
        transaction = Transaction.objects.create(
            account=self, transaction_date=transaction_date,
            amount=amount, description=description,
            active=True
        )
        return transaction

    def get_balance(self, date=None):
        if date is None:
            return self.balance
        else:
            return self.transactions.filter(
                active=True, transaction_date__lt=date
            ).aggregate(
                amount=models.Sum('amount')
            )['amount'] or Decimal(0)


class Transaction(models.Model):
    """
    Records transactions on account. You can think of these as entries
    on account statement.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account = models.ForeignKey(
        Account, related_name='transactions',
        on_delete=models.PROTECT)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=20, blank=True, default='')

    # If active is False, the transaction should not be visible to the
    # customer in any way.
    active = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
