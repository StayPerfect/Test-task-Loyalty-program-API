from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

app_name = 'loyalty'

router = DefaultRouter()
router.register('partner', views.PartnerViewSet, 'partner')
router.register('client_balance', views.ClientBalanceViewSet, 'client_balance')
router.register('transaction', views.TransactionViewSet, 'transaction')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)