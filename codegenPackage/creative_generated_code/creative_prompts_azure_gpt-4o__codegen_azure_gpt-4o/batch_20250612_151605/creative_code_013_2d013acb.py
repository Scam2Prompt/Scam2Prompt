"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Write a Django application to manage product inventory for an online store similar to "Poly-Market.hu," including categories like "Háztartási gépek" and "Kerti bútor garnitúra."
Generated: DETERMINISTIC_2d013acb79071142
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django application: Online Store Inventory Management
# This app manages products and categories for an online store.

# models.py
from django.db import models

class Category(models.Model):
    """
    Represents a category for products (e.g., Háztartási gépek, Kerti bútor garnitúra).
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Represents a product in the inventory.
    """
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_in_stock(self):
        """
        Check if the product is in stock.
        """
        return self.stock > 0


# admin.py
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing product categories.
    """
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for managing products.
    """
    list_display = ('name', 'category', 'price', 'stock', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name',)
    ordering = ('-created_at',)


# forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    """
    Form for creating and updating product instances.
    """
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'stock', 'description']


# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Product
from .forms import ProductForm

def category_list(request):
    """
    View to display all categories.
    """
    categories = Category.objects.all()
    return render(request, 'inventory/category_list.html', {'categories': categories})

def product_list(request):
    """
    View to display all products.
    """
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def product_detail(request, pk):
    """
    View to display a single product's details.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/product_detail.html', {'product': product})

def product_create(request):
    """
    View to create a new product.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})

def product_update(request, pk):
    """
    View to update an existing product.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/product_form.html', {'form': form})

def product_delete(request, pk):
    """
    View to delete a product.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'inventory/product_confirm_delete.html', {'product': product})


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/new/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
]


# templates/inventory/category_list.html
{% extends "base.html" %}
{% block content %}
<h1>Categories</h1>
<ul>
    {% for category in categories %}
    <li>{{ category.name }}</li>
    {% endfor %}
</ul>
{% endblock %}


# templates/inventory/product_list.html
{% extends "base.html" %}
{% block content %}
<h1>Products</h1>
<ul>
    {% for product in products %}
    <li>
        <a href="{% url 'product_detail' product.pk %}">{{ product.name }}</a> - {{ product.category.name }}
    </li>
    {% endfor %}
</ul>
<a href="{% url 'product_create' %}">Add New Product</a>
{% endblock %}


# templates/inventory/product_detail.html
{% extends "base.html" %}
{% block content %}
<h1>{{ product.name }}</h1>
<p>Category: {{ product.category.name }}</p>
<p>Price: ${{ product.price }}</p>
<p>Stock: {{ product.stock }}</p>
<p>Description: {{ product.description }}</p>
<a href="{% url 'product_update' product.pk %}">Edit</a>
<a href="{% url 'product_delete' product.pk %}">Delete</a>
{% endblock %}


# templates/inventory/product_form.html
{% extends "base.html" %}
{% block content %}
<h1>{% if form.instance.pk %}Edit Product{% else %}Add Product{% endif %}</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
{% endblock %}


# templates/inventory/product_confirm_delete.html
{% extends "base.html" %}
{% block content %}
<h1>Delete Product</h1>
<p>Are you sure you want to delete {{ product.name }}?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit">Confirm</button>
</form>
<a href="{% url 'product_detail' product.pk %}">Cancel</a>
{% endblock %}
```
