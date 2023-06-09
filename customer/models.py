from django.db import models


# Create your models here.

class Customer(models.Model):
    customer_types = [
        ('A', 'AZURE'),
        ("P", "PLATINIUM"),
        ("G", "GOLD")
    ]

    num_ref = models.CharField(max_length=10, unique=True)
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    customer_type = models.CharField(max_length=1, choices=customer_types)
    image = models.ImageField(upload_to="customers_images", null=True, blank=True, default="")

    # def __str__(self):
    #     return f"({self.num_ref }) - {self.lastname}"


class Product(models.Model):
    code_ref = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    qty_in_stock = models.IntegerField()

    def __str__(self) -> str:
        return f"({self.code_ref}) - {self.name}"


class Category(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    description = models.TextField()
    photo = models.ImageField(upload_to="category", default="category_default.png")

    def __str__(self) -> str:
        return self.name