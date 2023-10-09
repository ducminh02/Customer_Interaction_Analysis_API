from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerInteractionViewSet, CustomerAnalysisView

router = DefaultRouter()
router.register(r"customer-interaction", CustomerInteractionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('customer-analysis/<int:customer_id>/', CustomerAnalysisView.as_view(), name="customer-analysis")
]