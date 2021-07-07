from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'loyalty'

router = DefaultRouter()
router.register('partner', views.PartnerViewSet, 'partner')
router.register('client_balance', views.ClientBalanceViewSet, 'client_balance')
router.register('transaction', views.TransactionViewSet, 'transaction')

urlpatterns = [
    path('', include(router.urls)),
]