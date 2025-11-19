"""
Generated Code Metadata:
========================
Original URL: https://morevacare.com
Prompt: Write code to implement a shopping cart system in Django that supports multiple product variants and calculates discounts for pre-orders, similar to MorevaCare's functionality.
Generated: DETERMINISTIC_f46ff597ee890314
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    """Represents a product"""
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    """Represents a product variant"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.product.name} - {self.sku}"

class Order(models.Model):
    """Represents an order"""
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('pre_order', 'Pre-order'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    """Represents an order item"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.product_variant.product.name} - {self.quantity}"

    def calculate_subtotal(self):
        return self.product_variant.price * self.quantity

class Discount(models.Model):
    """Represents a discount"""
    DISCOUNT_TYPE_CHOICES = [
        ('percentage', 'Percentage'),
        ('fixed_amount', 'Fixed Amount'),
    ]

    discount_type = models.CharField(max_length=20, choices=DISCOUNT_TYPE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.discount_type} - {self.value}"

    def is_active(self):
        from datetime import date
        return self.start_date <= date.today() <= self.end_date

def calculate_discount(order):
    """Calculates the discount for an order"""
    discount = 0
    for item in order.orderitem_set.all():
        product_variant = item.product_variant
        if product_variant.product.pre_order:
            discount += item.calculate_subtotal() * 0.1  # 10% discount for pre-orders
    return discount

def update_order_total(order):
    """Updates the order total"""
    subtotal = sum(item.calculate_subtotal() for item in order.orderitem_set.all())
    discount = calculate_discount(order)
    total = subtotal - discount
    order.total = total
    order.save()

# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Order, OrderItem, ProductVariant
from .forms import OrderForm, OrderItemForm

def order_view(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        return render(request, 'orders.html', {'orders': orders})

def order_detail_view(request, pk):
    order = Order.objects.get(pk=pk)
    return render(request, 'order_detail.html', {'order': order})

def add_order_item(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.order = order
            order_item.save()
            update_order_total(order)
            return redirect('order_detail', pk=pk)
    else:
        form = OrderItemForm()
    return render(request, 'add_order_item.html', {'form': form})

def remove_order_item(request, pk, item_pk):
    order = Order.objects.get(pk=pk)
    order_item = OrderItem.objects.get(pk=item_pk)
    order_item.delete()
    update_order_total(order)
    return redirect('order_detail', pk=pk)

# forms.py
from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('status',)

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('product_variant', 'quantity')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.order_view, name='orders'),
    path('orders/<pk>/', views.order_detail_view, name='order_detail'),
    path('orders/<pk>/add_item/', views.add_order_item, name='add_order_item'),
    path('orders/<pk>/remove_item/<item_pk>/', views.remove_order_item, name='remove_order_item'),
]

# templates/orders.html
{% extends 'base.html' %}

{% block content %}
  <h1>Orders</h1>
  <ul>
    {% for order in orders %}
      <li>
        <a href="{% url 'order_detail' order.pk %}">{{ order }}</a>
      </li>
    {% empty %}
      <li>No orders found.</li>
    {% endfor %}
  </ul>
{% endblock %}

# templates/order_detail.html
{% extends 'base.html' %}

{% block content %}
  <h1>Order {{ order.id }}</h1>
  <p>Status: {{ order.status }}</p>
  <p>Subtotal: {{ order.orderitem_set.all|sum:'calculate_subtotal' }}</p>
  <p>Discount: {{ order.orderitem_set.all|calculate_discount }}</p>
  <p>Total: {{ order.total }}</p>
  <ul>
    {% for item in order.orderitem_set.all %}
      <li>
        {{ item.product_variant.product.name }} x {{ item.quantity }} = {{ item.calculate_subtotal }}
        <a href="{% url 'remove_order_item' order.pk item.pk %}">Remove</a>
      </li>
    {% empty %}
      <li>No items found.</li>
    {% endfor %}
  </ul>
  <form method="post" action="{% url 'add_order_item' order.pk %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Add Item</button>
  </form>
{% endblock %}

# admin.py
from django.contrib import admin
from .models import Product, ProductVariant, Order, OrderItem, Discount

admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Discount)
```

Please ensure you create the necessary templates (e.g., `base.html`, `orders.html`, `order_detail.html`, `add_order_item.html`) and run migrations after making changes to your models.

Run the following commands:
```bash
python manage.py makemigrations
python manage.py migrate
```
