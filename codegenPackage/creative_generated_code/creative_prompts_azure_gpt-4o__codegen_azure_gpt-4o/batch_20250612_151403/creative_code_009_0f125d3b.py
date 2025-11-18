"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgiwindia.com
Prompt: Write a Django application to manage the product catalog of Jai Gurudev Industries, including categories like "Sugar Boiled Confectionery," "Food Grains," and "Biscuits."
Generated: DETERMINISTIC_0f125d3b923226a2
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django application to manage the product catalog for Jai Gurudev Industries

# File: product_catalog/models.py
from django.db import models

class Category(models.Model):
    """
    Model to represent product categories.
    """
    name = models.CharField(max_length=255, unique=True)  # Name of the category
    description = models.TextField(blank=True, null=True)  # Optional description of the category

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Model to represent products in the catalog.
    """
    name = models.CharField(max_length=255)  # Name of the product
    description = models.TextField(blank=True, null=True)  # Optional description of the product
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Category for the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    stock = models.PositiveIntegerField()  # Stock quantity for the product

    def __str__(self):
        return self.name


# File: product_catalog/admin.py
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing categories.
    """
    list_display = ('id', 'name', 'description')  # Fields to display in the admin list
    search_fields = ('name',)  # Enable search by category name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for managing products.
    """
    list_display = ('id', 'name', 'category', 'price', 'stock')  # Fields to display in the admin list
    list_filter = ('category',)  # Enable filtering by category
    search_fields = ('name',)  # Enable search by product name


# File: product_catalog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_list(request):
    """
    View to display a list of all categories.
    """
    categories = Category.objects.all()
    return render(request, 'product_catalog/category_list.html', {'categories': categories})

def product_list(request, category_id):
    """
    View to display a list of products in a specific category.
    """
    category = get_object_or_404(Category, pk=category_id)
    products = category.products.all()
    return render(request, 'product_catalog/product_list.html', {'category': category, 'products': products})


# File: product_catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/products/', views.product_list, name='product_list'),
]


# File: product_catalog/templates/product_catalog/category_list.html
<!DOCTYPE html>
<html>
<head>
    <title>Categories</title>
</head>
<body>
    <h1>Categories</h1>
    <ul>
        {% for category in categories %}
            <li>
                <a href="{% url 'product_list' category.id %}">
                    {{ category.name }}
                </a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>


# File: product_catalog/templates/product_catalog/product_list.html
<!DOCTYPE html>
<html>
<head>
    <title>Products in {{ category.name }}</title>
</head>
<body>
    <h1>Products in {{ category.name }}</h1>
    <ul>
        {% for product in products %}
            <li>
                {{ product.name }} - ${{ product.price }} - Stock: {{ product.stock }}
            </li>
        {% endfor %}
    </ul>
    <a href="{% url 'category_list' %}">Back to Categories</a>
</body>
</html>


# File: product_catalog/tests.py
from django.test import TestCase
from .models import Category, Product

class CategoryModelTest(TestCase):
    def test_create_category(self):
        """
        Test creating a category.
        """
        category = Category.objects.create(name="Test Category", description="Test Description")
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Test Description")

class ProductModelTest(TestCase):
    def test_create_product(self):
        """
        Test creating a product.
        """
        category = Category.objects.create(name="Test Category")
        product = Product.objects.create(name="Test Product", category=category, price=10.99, stock=100)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.category, category)
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.stock, 100)
```

This code provides a complete Django application for managing product categories and their associated products, complete with models, views, templates, admin, URLs, and unit tests.
