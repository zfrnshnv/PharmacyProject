from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from apps.models import Category
from apps.serializers import CategoryModelSerializer


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
    pass

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
    pass

@extend_schema(tags=['supplier'])
class SupplierCreateApiView(CreateAPIView):
    pass

@extend_schema(tags=['order'])
class OrderListApiView(ListAPIView):
    pass

@extend_schema(tags=['order'])
class OrderCreateApiView(CreateAPIView):
    pass

@extend_schema(tags=['order'])
class OrderUpdateApiView(UpdateAPIView):
    pass

@extend_schema(tags=['locations'])
class CityListApiView(ListAPIView):
    pass

@extend_schema(tags=['locations'])
class CountryListApiView(ListAPIView):
    pass