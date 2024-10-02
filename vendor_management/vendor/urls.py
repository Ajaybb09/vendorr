# vendor/urls.py
from django.urls import path
from .views import (
    VendorListCreateView, VendorDetailView, PurchaseOrderListCreateView,
    PurchaseOrderDetailView, VendorPerformanceView
)

urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='po-list'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='po-detail'),
]
