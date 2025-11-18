"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Create a Python script using the Django framework to implement a "new arrivals" feature for an e-commerce site. Include functionality for displaying recently added products with their prices and categories.
Generated: DETERMINISTIC_ec84734f2310baa0
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django application: new_arrivals
# This application implements a "new arrivals" feature for an e-commerce site.

# models.py
from django.db import models
from django.utils.timezone import now

class Category(models.Model):
    """
    Model representing product categories.
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model representing products in the e-commerce system.
    """
    name = models.CharField(max_length=255)  # Name of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")  # Associated category
    date_added = models.DateTimeField(default=now)  # Timestamp of when the product was added

    def __str__(self):
        return f"{self.name} - {self.price} USD"


# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def new_arrivals(request):
    """
    View to display recently added products.
    """
    try:
        # Fetch products added in the last 30 days
        from django.utils.timezone import now
        from datetime import timedelta

        thirty_days_ago = now() - timedelta(days=30)
        new_products = Product.objects.filter(date_added__gte=thirty_days_ago).order_by('-date_added')

        # Prepare data for rendering
        product_data = [
            {
                "name": product.name,
                "price": str(product.price),
                "category": product.category.name,
                "date_added": product.date_added.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for product in new_products
        ]

        return JsonResponse({"new_arrivals": product_data}, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the new arrivals page
    path('new-arrivals/', views.new_arrivals, name='new_arrivals'),
]


# admin.py
from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing product categories.
    """
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for managing products.
    """
    list_display = ('id', 'name', 'price', 'category', 'date_added')
    list_filter = ('category', 'date_added')
    search_fields = ('name',)


# templates/new_arrivals.html (Optional if using a template)
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Arrivals</title>
</head>
<body>
    <h1>New Arrivals</h1>
    <ul id="product-list">
        <!-- JavaScript or Backend should populate this list -->
    </ul>
</body>
</html>
"""

# settings.py (Ensure the app is added to INSTALLED_APPS)
INSTALLED_APPS = [
    ...,
    'new_arrivals',  # Add the application to Django settings
]

# Run migrations to apply models to the database:
# python manage.py makemigrations
# python manage.py migrate
```
