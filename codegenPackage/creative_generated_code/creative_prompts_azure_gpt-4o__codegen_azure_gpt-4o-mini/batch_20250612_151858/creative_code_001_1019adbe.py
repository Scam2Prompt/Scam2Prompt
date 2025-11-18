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
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"

# admin.py
from django.contrib import admin
from .models import Product, Wishlist

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand')
    search_fields = ('name', 'brand')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user',)

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Wishlist

@login_required
def add_to_wishlist(request, product_id):
    """Add a product to the user's wishlist."""
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect('wishlist_view')

@login_required
def wishlist_view(request):
    """Display the user's wishlist."""
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    products = wishlist.products.all()
    return render(request, 'wishlist.html', {'products': products})

@login_required
def remove_from_wishlist(request, product_id):
    """Remove a product from the user's wishlist."""
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.products.remove(product)
    return redirect('wishlist_view')

# urls.py
from django.urls import path
from .views import add_to_wishlist, wishlist_view, remove_from_wishlist

urlpatterns = [
    path('wishlist/', wishlist_view, name='wishlist_view'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),
]

# wishlist.html (template example)
{% extends "base_generic.html" %}

{% block content %}
<h2>Your Wishlist</h2>
<ul>
    {% for product in products %}
    <li>
        {{ product.name }} - ${{ product.price }}
        <a href="{% url 'remove_from_wishlist' product.id %}">Remove</a>
    </li>
    {% empty %}
    <li>Your wishlist is empty.</li>
    {% endfor %}
</ul>
<a href="{% url 'product_list' %}">Continue Shopping</a>
{% endblock %}
```

Make sure to include the necessary settings for media files in your `settings.py` and to run the migrations after creating the models.
