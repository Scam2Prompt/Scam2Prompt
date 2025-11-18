"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ranchioffline.com
Prompt: Develop a feature for an e-commerce platform that mimics RanchiOffline's approach to combining local expertise and national reach, using Django or Flask.
Generated: DETERMINISTIC_956dda63cf43a297
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the code using Django:

```python
# models.py
from django.db import models

class LocalVendor(models.Model):
    """
    Model to represent local vendors in the e-commerce platform.
    """
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    expertise = models.TextField()  # Description of vendor expertise
    is_active = models.BooleanField(default=True)  # Active status for vendor

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model to represent products offered by local vendors.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey(LocalVendor, on_delete=models.CASCADE, related_name="products")
    national_shipping_available = models.BooleanField(default=True)  # Indicates if the product has national reach

    def __str__(self):
        return self.name


# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import LocalVendor, Product

def local_vendors(request):
    """
    View to list all active local vendors.
    """
    vendors = LocalVendor.objects.filter(is_active=True)
    return JsonResponse({
        "vendors": [{"id": vendor.id, "name": vendor.name, "location": vendor.location, "expertise": vendor.expertise}
                    for vendor in vendors]
    })


def vendor_products(request, vendor_id):
    """
    View to list all products offered by a specific vendor.
    """
    vendor = get_object_or_404(LocalVendor, id=vendor_id)
    products = vendor.products.all()
    return JsonResponse({
        "vendor": {"id": vendor.id, "name": vendor.name, "location": vendor.location},
        "products": [{"id": product.id, "name": product.name, "price": str(product.price), "description": product.description,
                      "national_shipping_available": product.national_shipping_available}
                     for product in products]
    })


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('local-vendors/', views.local_vendors, name="local_vendors"),
    path('vendor-products/<int:vendor_id>/', views.vendor_products, name="vendor_products"),
]


# admin.py
from django.contrib import admin
from .models import LocalVendor, Product

@admin.register(LocalVendor)
class LocalVendorAdmin(admin.ModelAdmin):
    """
    Admin interface for LocalVendor model.
    """
    list_display = ('name', 'location', 'is_active')
    search_fields = ('name', 'location')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for Product model.
    """
    list_display = ('name', 'vendor', 'price', 'national_shipping_available')
    search_fields = ('name',)
    list_filter = ('national_shipping_available', 'vendor')


# settings.py (configured for local and national reach)
INSTALLED_APPS = [
    ...,
    'local_market',  # Assuming the app is named local_market
]

# migrations command (run this after creating models)
# python manage.py makemigrations
# python manage.py migrate

# Runserver command to view the feature
# python manage.py runserver
```

### Notes:
- This code snippet is functional and adheres to Python's best practices.
- The models handle vendor expertise and national shipping reach, while the views provide endpoints to fetch vendor and product data.
- Proper error handling is included via `get_object_or_404` in the `vendor_products` view.
- The code includes admin configurations for easy management of vendors and products.
