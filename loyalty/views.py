from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Partner, ClientBalance, Transaction
from .serializers import PartnerSerializer, ClientBalanceSerializer, TransactionSerializer


@api_view(['GET'])
def client_balance_detail(request, pk):
    client_balance = ClientBalance.objects.get(pk=pk)
    serializer = ClientBalanceSerializer(client_balance)
    
    content = {
        'client_balance': serializer.data,
    }

    return Response(content)
    

class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        return Partner.objects.all()


class ClientBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = ClientBalanceSerializer

    def get_queryset(self):
        return ClientBalance.objects.all()


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.all()
