from django import setup
setup()
from django.contrib.auth.models import User
from fintech.models import Account, Transaction

Transaction.objects.all().delete()
Account.objects.all().delete()
User.objects.all().delete()
user = User.objects.create(username='anssi')
account = Account.create_account(user=user, name='testing')
account.record_transaction(transaction_date='2018-01-01', amount=100)
account.record_transaction(transaction_date='2018-01-02', amount=200)
account.refresh_from_db()
print(account.get_balance())
print(account.get_balance(date='2018-01-02'))
account.record_transaction(transaction_date='2018-01-05', amount=-200)
account.record_transaction(transaction_date='2018-01-10', amount=-200)
