from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView

from apps.models import Category, City, Country, Order, Supplier, Medicine
from apps.serializers import CategoryModelSerializer, CityModelSerializer, CountryModelSerializer, OrderModelSerializer, \
    SupplierModelSerializer, MedicineModelSerializer


# Create your views here.
@extend_schema(tags=['category'])
class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

@extend_schema(tags=['category'])
class CategoryCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

@extend_schema(tags=['medicine'])
class MedicineListApiView(ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineModelSerializer

@extend_schema(tags=['medicine'])
class MedicineRetrieveApiView(RetrieveAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineModelSerializer

@extend_schema(tags=['medicine'])
class MedicineCreateApiView(ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineModelSerializer

@extend_schema(tags=['medicine'])
class MedicineUpdateApiView(UpdateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineModelSerializer

@extend_schema(tags=['medicine'])
class MedicineDeleteApiView(DestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineModelSerializer

@extend_schema(tags=['supplier'])
class SupplierListApiView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer

@extend_schema(tags=['supplier'])
class SupplierCreateApiView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer

@extend_schema(tags=['order'])
class OrderListApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

@extend_schema(tags=['order'])
class OrderCreateApiView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

@extend_schema(tags=['order'])
class OrderUpdateApiView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

@extend_schema(tags=['locations'])
class CityListApiView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer

@extend_schema(tags=['locations'])
class CountryListApiView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer