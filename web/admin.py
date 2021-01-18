from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_class', 'entry_date']

admin.site.register(Product, ProductAdmin)
