# vendor/views.py
from rest_framework import generics
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
from django.db.models import Avg, Count, F
from django.db.models.functions import Cast
from django.db.models import FloatField

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        vendor = self.get_object()
        total_orders = vendor.purchase_orders.filter(status='completed').count()

        if total_orders > 0:
            on_time_orders = vendor.purchase_orders.filter(
                status='completed',
                delivered_date__lte=F('delivery_date')
            ).count()

            on_time_delivery_rate = (on_time_orders / total_orders) * 100

            quality_rating_avg = vendor.purchase_orders.filter(
                status='completed'
            ).aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0

            vendor.on_time_delivery_rate = on_time_delivery_rate
            vendor.quality_rating_avg = quality_rating_avg
            vendor.save()

        return super().retrieve(request, *args, **kwargs)
