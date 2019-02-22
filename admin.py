from django.contrib import admin

# Register your models here.
from website.models.product import Product
from website.models.order import Order


admin.site.register(Product)
admin.site.register(Order)
