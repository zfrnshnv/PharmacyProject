from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from apps.models import Category, City, Country, Order, Supplier, Medicine
from apps.serializers import CategoryModelSerializer, CityModelSerializer, CountryModelSerializer, OrderModelSerializer, \
    SupplierModelSerializer, MedicineModelSerializer


# Create your views here.
@extend_schema(tags=['category'])
class CategoryListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

@extend_schema(tags=['category'])
class CategoryCreateApiView(CreateAPIView):
    pass

@extend_schema(tags=['medicine'])
class MedicineListApiView(ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineModelSerializer

@extend_schema(tags=['medicine'])
class MedicineRetrieveApiView(RetrieveAPIView):
    pass

@extend_schema(tags=['medicine'])
class MedicineCreateApiView(CreateAPIView):
    pass

@extend_schema(tags=['medicine'])
class MedicineUpdateApiView(UpdateAPIView):
    pass

@extend_schema(tags=['medicine'])
class MedicineDeleteApiView(DestroyAPIView):
    pass

@extend_schema(tags=['supplier'])
class SupplierListApiView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierModelSerializer

@extend_schema(tags=['supplier'])
class SupplierCreateApiView(CreateAPIView):
    pass

@extend_schema(tags=['order'])
class OrderListApiView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer

@extend_schema(tags=['order'])
class OrderCreateApiView(CreateAPIView):
    pass

@extend_schema(tags=['order'])
class OrderUpdateApiView(UpdateAPIView):
    pass

@extend_schema(tags=['locations'])
class CityListApiView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer

@extend_schema(tags=['locations'])
class CountryListApiView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryModelSerializer