"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Develop a Django application to manage inventory for products such as "rowerki trójkołowe" and "chodziki," ensuring stock updates and order tracking.
Generated: DETERMINISTIC_50fe059941964cc2
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_app/models.py

from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    """Model to represent a product in the inventory."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def clean(self):
        """Custom validation to ensure stock can't be negative."""
        if self.stock < 0:
            raise ValidationError('Stock cannot be negative.')

    def update_stock(self, quantity):
        """Update the stock of the product."""
        if self.stock + quantity < 0:
            raise ValidationError('Cannot reduce stock below zero.')
        self.stock += quantity
        self.save()


class Order(models.Model):
    """Model to represent an order of products."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order for {self.product} (Quantity: {self.quantity})'

    def clean(self):
        """Custom validation to ensure enough stock is available for the order."""
        if self.quantity > self.product.stock:
            raise ValidationError('Not enough stock available for this order.')

    def save(self, *args, **kwargs):
        """Override save method to update product stock when an order is created."""
        self.clean()  # Call clean to validate before saving
        self.product.update_stock(-self.quantity)  # Reduce stock
        super().save(*args, **kwargs)


# inventory_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Order
from .forms import ProductForm, OrderForm


def product_list(request):
    """View to list all products in the inventory."""
    products = Product.objects.all()
    return render(request, 'inventory_app/product_list.html', {'products': products})


def create_product(request):
    """View to create a new product."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully.')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory_app/product_form.html', {'form': form})


def create_order(request):
    """View to create a new order for a product."""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Order placed successfully.')
                return redirect('product_list')
            except ValidationError as e:
                form.add_error(None, str(e))
    else:
        form = OrderForm()
    return render(request, 'inventory_app/order_form.html', {'form': form})


# inventory_app/forms.py

from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm):
    """Form to create or update a product."""
    class Meta:
        model = Product
        fields = ['name', 'description', 'stock']


class OrderForm(forms.ModelForm):
    """Form to create a new order."""
    class Meta:
        model = Order
        fields = ['product', 'quantity']


# inventory_app/urls.py

from django.urls import path
from .views import product_list, create_product, create_order

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/new/', create_product, name='create_product'),
    path('order/new/', create_order, name='create_order'),
]


# inventory_app/templates/inventory_app/product_list.html

{% extends "base_generic.html" %}

{% block content %}
  <h2>Product List</h2>
  <a href="{% url 'create_product' %}">Add New Product</a>
  <ul>
    {% for product in products %}
      <li>{{ product.name }} - Stock: {{ product.stock }}</li>
    {% endfor %}
  </ul>
{% endblock %}


# inventory_app/templates/inventory_app/product_form.html

{% extends "base_generic.html" %}

{% block content %}
  <h2>Create Product</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
  </form>
{% endblock %}


# inventory_app/templates/inventory_app/order_form.html

{% extends "base_generic.html" %}

{% block content %}
  <h2>Create Order</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Place Order</button>
  </form>
{% endblock %}


# inventory_app/admin.py

from django.contrib import admin
from .models import Product, Order

admin.site.register(Product)
admin.site.register(Order)

# Ensure to include `inventory_app` in `INSTALLED_APPS` in your `settings.py` file.
```
