"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solandsol.com
Prompt: Generate code using Django to implement a product catalog for nutritional supplements, lactation supplements, and baby cereals, including categories, product descriptions, and a wishlist feature.
Generated: DETERMINISTIC_841b6db2c76b9f33
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Model representing a category (e.g., Nutritional Supplements, Lactation Supplements, Baby Cereals)."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model representing a product."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    """Model representing a user's wishlist."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # Prevent duplicate products in a user's wishlist

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


# admin.py
from django.contrib import admin
from .models import Category, Product, Wishlist

# Register models to the admin site
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'added_at')
    list_filter = ('user',)


# views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Category, Product, Wishlist

def product_catalog(request):
    """View to display the product catalog with categories and products."""
    categories = Category.objects.prefetch_related('products').all()
    return render(request, 'catalog.html', {'categories': categories})


@login_required
def add_to_wishlist(request, product_id):
    """View to add a product to the user's wishlist."""
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if created:
        return JsonResponse({'success': True, 'message': 'Product added to wishlist.'})
    return JsonResponse({'success': False, 'message': 'Product already in wishlist.'})


@login_required
def view_wishlist(request):
    """View to display the user's wishlist."""
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


# urls.py
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_catalog, name='product_catalog'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]


# templates/catalog.html
{% extends "base.html" %}
{% block content %}
<h1>Product Catalog</h1>
{% for category in categories %}
    <h2>{{ category.name }}</h2>
    <p>{{ category.description }}</p>
    <ul>
        {% for product in category.products.all %}
            <li>
                <strong>{{ product.name }}</strong>: {{ product.description }} (${{ product.price }})
                {% if user.is_authenticated %}
                    <a href="{% url 'catalog:add_to_wishlist' product.id %}">Add to Wishlist</a>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
{% endfor %}
{% endblock %}


# templates/wishlist.html
{% extends "base.html" %}
{% block content %}
<h1>My Wishlist</h1>
<ul>
    {% for item in wishlist_items %}
        <li>
            <strong>{{ item.product.name }}</strong>: {{ item.product.description }} (${{ item.product.price }})
            <em>Added on {{ item.added_at }}</em>
        </li>
    {% endfor %}
</ul>
{% endblock %}
```
