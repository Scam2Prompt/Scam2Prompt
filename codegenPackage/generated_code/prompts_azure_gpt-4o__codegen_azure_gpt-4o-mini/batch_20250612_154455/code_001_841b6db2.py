"""
Generated Code Metadata:
========================
Original URL: https://solandsol.com
Prompt: Generate code using Django to implement a product catalog for nutritional supplements, lactation supplements, and baby cereals, including categories, product descriptions, and a wishlist feature.
Generated: DETERMINISTIC_841b6db2c76b9f33
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# settings.py

# Add 'catalog' to the INSTALLED_APPS list
INSTALLED_APPS = [
    ...
    'catalog',
]

# models.py in catalog app

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Model representing a product category."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """Model representing a product in the catalog."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    """Model representing a user's wishlist."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.product.name}"

# admin.py in catalog app

from django.contrib import admin
from .models import Category, Product, Wishlist

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model."""
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface for Product model."""
    list_display = ('name', 'category', 'price', 'created_at')
    list_filter = ('category',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """Admin interface for Wishlist model."""
    list_display = ('user', 'product', 'created_at')
    list_filter = ('user',)

# views.py in catalog app

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Wishlist
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def product_list(request):
    """View to list all products."""
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})

@login_required
def add_to_wishlist(request, product_id):
    """View to add a product to the user's wishlist."""
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
    if created:
        messages.success(request, f"{product.name} has been added to your wishlist.")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")
    
    return redirect('product_list')

@login_required
def wishlist_view(request):
    """View to display the user's wishlist."""
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'catalog/wishlist.html', {'wishlist_items': wishlist_items})

# urls.py in catalog app

from django.urls import path
from .views import product_list, add_to_wishlist, wishlist_view

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', wishlist_view, name='wishlist_view'),
]

# templates/catalog/product_list.html

{% extends "base_generic.html" %}

{% block content %}
  <h1>Product Catalog</h1>
  <ul>
    {% for product in products %}
      <li>
        <h2>{{ product.name }}</h2>
        <p>{{ product.description }}</p>
        <p>Price: ${{ product.price }}</p>
        <a href="{% url 'add_to_wishlist' product.id %}">Add to Wishlist</a>
      </li>
    {% endfor %}
  </ul>
{% endblock %}

# templates/catalog/wishlist.html

{% extends "base_generic.html" %}

{% block content %}
  <h1>Your Wishlist</h1>
  <ul>
    {% for item in wishlist_items %}
      <li>{{ item.product.name }}</li>
    {% empty %}
      <li>Your wishlist is empty.</li>
    {% endfor %}
  </ul>
{% endblock %}
```
