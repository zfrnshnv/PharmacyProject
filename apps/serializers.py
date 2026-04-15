from rest_framework.serializers import ModelSerializer

from apps.models import Category, Medicine, Supplier, Order, City, Country


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', )

class MedicineModelSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id', 'name', 'category_id', 'description', 'price', 'stock', 'expiry_date', )

class SupplierModelSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'name', 'phone', 'city')

class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'total_price', 'status', )

class CityModelSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'country_id', )

class CountryModelSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', )