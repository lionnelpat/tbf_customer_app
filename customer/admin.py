from django.contrib import admin
from customer.views import Customer, Product, Category
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)