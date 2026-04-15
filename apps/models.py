from django.db.models import Model, CharField, ForeignKey, CASCADE, TextField, DecimalField, IntegerField, DateField
from django.db.models.enums import TextChoices


class Category(Model):
    name = CharField(max_length=255)

class Medicine(Model):
    name = CharField(max_length=255)
    category = ForeignKey('apps.Category', on_delete=CASCADE)
    description = TextField()
    price = DecimalField(max_digits=12, decimal_places=2)
    stock = IntegerField()
    expiry_date = DateField()

class Supplier(Model):
    name = CharField(max_length=255)
    phone = CharField(max_length=20)
    city = ForeignKey('apps.City', on_delete=CASCADE)

class Order(Model):
    class StatusChoice(TextChoices):
        PENDING = "pending"
        CANCELLED = "cancelled"
        COMPLETED = "completed"
    customer_name = CharField(max_length=100)
    total_price = DecimalField(max_digits=12, decimal_places=0)
    status = CharField(
        max_length=10,
        choices=StatusChoice.choices,
        default=StatusChoice.PENDING,
    )
    created_at = DateField(auto_now_add=True)

class City(Model):
    name = CharField(max_length=100)
    country = ForeignKey('apps.Country', on_delete=CASCADE)

class Country(Model):
    name = CharField(max_length=100)
