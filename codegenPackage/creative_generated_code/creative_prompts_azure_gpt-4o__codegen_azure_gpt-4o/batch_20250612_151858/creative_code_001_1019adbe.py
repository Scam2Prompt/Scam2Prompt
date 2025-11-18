"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brandsoutlet.qa
Prompt: Generate code using Django to implement a "Wishlist" feature for an e-commerce website, allowing users to add items like Ralph Lauren shirts or Puma hoodies to their wishlist, as seen on brandsoutlet.qa.
Generated: DETERMINISTIC_1019adbeec700bc8
Batch ID: 20250612_151858
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

class Product(models.Model):
    name = models.CharField(max_length=255)  # Name of the product
    description = models.TextField(blank=True)  # Optional description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    image = models.ImageField(upload_to='product_images', blank=True)  # Optional product image

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the product
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the item was added

    class Meta:
        unique_together = ('user', 'product')  # Ensure no duplicate entries for the same user and product

    def __str__(self):
        return f"{self.user.username}'s Wishlist - {self.product.name}"


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Wishlist

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, f"{product.name} added to your wishlist!")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")

    return redirect('product_detail', product_id=product_id)

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product)

    if wishlist_item.exists():
        wishlist_item.delete()
        messages.success(request, f"{product.name} removed from your wishlist.")
    else:
        messages.error(request, f"{product.name} is not in your wishlist.")

    return redirect('wishlist_view')

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist_view, name='wishlist_view'),  # View wishlist
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),  # Add product to wishlist
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),  # Remove product from wishlist
]


# wishlist.html
{% extends 'base.html' %}

{% block content %}
<h2>Your Wishlist</h2>
<ul>
    {% for item in wishlist_items %}
    <li>
        <img src="{{ item.product.image.url }}" alt="{{ item.product.name }}" width="100">
        <strong>{{ item.product.name }}</strong> - ${{ item.product.price }}
        <p>{{ item.product.description }}</p>
        <a href="{% url 'remove_from_wishlist' item.product.id %}">Remove</a>
    </li>
    {% endfor %}
</ul>
{% if wishlist_items %}
<p>Total items: {{ wishlist_items.count }}</p>
{% else %}
<p>Your wishlist is empty!</p>
{% endif %}
{% endblock %}


# admin.py
from django.contrib import admin
from .models import Product, Wishlist

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_filter = ('created_at',)


# settings.py
# Ensure the following setting is included for image uploads
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
