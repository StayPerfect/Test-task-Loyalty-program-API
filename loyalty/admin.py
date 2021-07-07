from django.contrib import admin
from .models import Partner, ClientBalance, Transaction

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


@admin.register(ClientBalance)
class ClientBalanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'partner', 'points')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('client_balance', 'amount', 'memo', 'date_time')