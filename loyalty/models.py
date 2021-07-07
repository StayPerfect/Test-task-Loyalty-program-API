from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Partner(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


# class Client(models.Model):
#     """
#     Client's information. It's in the separate class because the same client can be a customer of different partners and
#     we may want to have quick access to all client's accounts by parent class.
#     """
#     first_name = models.CharField(max_length=50, blank=True, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


class ClientBalance(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return f'{self.name} at {self.partner}'

    def add_points(self, points):
        self.points += points
        self.save()

    def add_transaction(self, points, memo):
        transaction = Transaction(client_balance=self, amount=points, memo=memo)
        transaction.save()

    def recalculate_balance(self, exclude_transaction, additional_amount):
        transactions = Transaction.objects.filter(client_balance=self)
        self.points = additional_amount
        for t in transactions:
            if t != exclude_transaction:
                self.points += t.amount
        self.save()


class Transaction(models.Model):
    client_balance = models.ForeignKey(ClientBalance, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    memo = models.CharField(max_length=300, blank=True, null=True, verbose_name='Memo')
    date_time = models.DateTimeField(verbose_name='Date and time', default=datetime.now)

    def __str__(self):
        return f'{self.client_balance.partner}: {self.client_balance.name}, {self.amount} points, {self.memo}, {self.date_time}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # check if it's a new object. If so, simply add points to existing balance without need to recalculate
        # all transactions and waste resources
        if self._state.adding:
            self.client_balance.add_points(self.amount)
        # if we are updating transaction object (self._state.adding is False), then we need to recalculate all balance transactions
        # to avoid errors when 'amount' was changed in transaction
        # we are excluding 'self' transaction because it will recalculate with old amount of points (object isn't updated at the time when
        # we call 'recalculate_balance' function)
        else:
            self.client_balance.recalculate_balance(exclude_transaction=self, additional_amount=self.amount)
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

