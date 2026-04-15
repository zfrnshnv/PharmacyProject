from django.urls import path

from apps.views import (CategoryListApiView, CategoryCreateApiView,
                        MedicineListApiView, MedicineRetrieveApiView,
                        MedicineCreateApiView, MedicineUpdateApiView, MedicineDeleteApiView,
                        SupplierListApiView, SupplierCreateApiView, OrderListApiView,
                        OrderCreateApiView, OrderUpdateApiView, CityListApiView, CountryListApiView)

urlpatterns = [
    path('category/list', CategoryListApiView.as_view()),
    path('category/add', CategoryCreateApiView.as_view()),
    path('medicine/list', MedicineListApiView.as_view()),
    path('medicine/list/<int:id>', MedicineRetrieveApiView.as_view()),
    path('medicine/add', MedicineCreateApiView.as_view()),
    path('medicine/update/<int:id>', MedicineUpdateApiView.as_view()),
    path('medicine/delete/<int:id>', MedicineDeleteApiView.as_view()),
    path('supplier/list', SupplierListApiView.as_view()),
    path('supplier/add', SupplierCreateApiView.as_view()),
    path('order/list', OrderListApiView.as_view()),
    path('order/add', OrderCreateApiView.as_view()),
    path('order/update/<int:id>/status/', OrderUpdateApiView.as_view()),
    path('city/list', CityListApiView.as_view()),
    path('country/list', CountryListApiView.as_view()),
]