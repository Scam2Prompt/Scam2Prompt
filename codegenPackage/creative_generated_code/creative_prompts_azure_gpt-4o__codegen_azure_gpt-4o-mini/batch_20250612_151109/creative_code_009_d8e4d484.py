"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Write code using the Django framework to create a shopping cart system for "moveisonlinepelotasbraz," ensuring it supports adding products like "Colchão de Mola Bagé" and "Estofado 3x2 Lugares."
Generated: DETERMINISTIC_d8e4d484e9b25af2
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# settings.py

# Add 'cart' to your installed apps
INSTALLED_APPS = [
    # Other installed apps...
    'cart',
]

# models.py in cart app

from django.db import models

class Product(models.Model):
    """Model representing a product in the store."""
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class CartItem(models.Model):
    """Model representing an item in the shopping cart."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    @property
    def total_price(self):
        """Calculate total price for the cart item."""
        return self.product.price * self.quantity

# views.py in cart app

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem
from django.contrib import messages

def cart_view(request):
    """View to display the shopping cart."""
    cart_items = CartItem.objects.all()
    total = sum(item.total_price for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})

def add_to_cart(request, product_id):
    """View to add a product to the shopping cart."""
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"{product.name} quantity updated.")
    else:
        messages.success(request, f"{product.name} added to cart.")
    
    return redirect('cart_view')

# urls.py in cart app

from django.urls import path
from .views import cart_view, add_to_cart

urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
]

# cart/cart.html (template)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Your Shopping Cart</title>
</head>
<body>
    <h1>Your Shopping Cart</h1>
    {% if cart_items %}
        <ul>
            {% for item in cart_items %}
                <li>{{ item.quantity }} x {{ item.product.name }} - R$ {{ item.total_price|floatformat:2 }}</li>
            {% endfor %}
        </ul>
        <h2>Total: R$ {{ total|floatformat:2 }}</h2>
    {% else %}
        <p>Your cart is empty.</p>
    {% endif %}
</body>
</html>

# Create initial product entries in the Django shell

# python manage.py shell

from cart.models import Product

Product.objects.create(name="Colchão de Mola Bagé", price=1500.00)
Product.objects.create(name="Estofado 3x2 Lugares", price=2500.00)

# Run migrations
# python manage.py makemigrations
# python manage.py migrate
``` 

This code will create a basic shopping cart system in a Django application, allowing users to add selected products to their cart. Ensure that you have set up your Django project correctly and have the necessary templates and static files configured for a complete application.
