
from django.contrib import admin
from django.urls import path
from customer.views import all_customers, welcome, all_products, all_categories, detail_category
from customer.views import create_customer, show_customer, delete_customer, update_customer

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", welcome, name="home"),
    path("customers", all_customers, name="customers"),
    path("products", all_products, name="products"),
    path("categories", all_categories, name="categories"),
    path("detail-category/<int:id>", detail_category, name="detail_category"),
    path("create-customer", create_customer, name="create_customer"),
    path("show-customer/<int:id>", show_customer, name="show_customer"),
    path("delete-customer/<int:id>", delete_customer, name="delete_customer"),
    path("update-customer/<int:id>",update_customer, name="update_customer"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
