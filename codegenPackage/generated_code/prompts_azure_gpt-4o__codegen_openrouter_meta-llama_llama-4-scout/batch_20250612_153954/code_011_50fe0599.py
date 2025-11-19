"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Develop a Django application to manage inventory for products such as "rowerki trójkołowe" and "chodziki," ensuring stock updates and order tracking.
Generated: DETERMINISTIC_50fe059941964cc2
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**models.py**
```python
from django.db import models

class Product(models.Model):
    """Represents a product in the inventory"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    """Represents a customer order"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ], default='pending')

    def __str__(self):
        return f"Order {self.id} for {self.product.name}"

class StockUpdate(models.Model):
    """Represents a stock update"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now_add=True)
    quantity_changed = models.IntegerField()
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"Stock update for {self.product.name}"
```

**admin.py**
```python
from django.contrib import admin
from .models import Product, Order, StockUpdate

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(StockUpdate)
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Order, StockUpdate
from .forms import ProductForm, OrderForm, StockUpdateForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

def update_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', pk=pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'update_order.html', {'form': form})

def stock_update_list(request):
    stock_updates = StockUpdate.objects.all()
    return render(request, 'stock_update_list.html', {'stock_updates': stock_updates})

def create_stock_update(request):
    if request.method == 'POST':
        form = StockUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_update_list')
    else:
        form = StockUpdateForm()
    return render(request, 'create_stock_update.html', {'form': form})
```

**forms.py**
```python
from django import forms
from .models import Product, Order, StockUpdate

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'stock_quantity')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'quantity', 'status')

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = StockUpdate
        fields = ('product', 'quantity_changed', 'reason')
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<pk>/', views.product_detail, name='product_detail'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<pk>/update/', views.update_product, name='update_product'),
    path('products/<pk>/delete/', views.delete_product, name='delete_product'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/<pk>/update/', views.update_order, name='update_order'),
    path('stock-updates/', views.stock_update_list, name='stock_update_list'),
    path('stock-updates/create/', views.create_stock_update, name='create_stock_update'),
]
```

**templates/product_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Product List</h1>
  <ul>
    {% for product in products %}
      <li>
        {{ product.name }} ({{ product.stock_quantity }})
        <a href="{% url 'product_detail' product.pk %}">View</a>
        <a href="{% url 'update_product' product.pk %}">Update</a>
        <a href="{% url 'delete_product' product.pk %}">Delete</a>
      </li>
    {% empty %}
      <li>No products available.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'create_product' %}">Create new product</a></p>
{% endblock %}
```

**templates/product_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ product.name }}</h1>
  <p>{{ product.description }}</p>
  <p>Stock quantity: {{ product.stock_quantity }}</p>
  <p><a href="{% url 'update_product' product.pk %}">Update</a></p>
{% endblock %}
```

**templates/create_product.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create Product</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
{% endblock %}
```

**templates/order_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Order List</h1>
  <ul>
    {% for order in orders %}
      <li>
        {{ order.product.name }} x {{ order.quantity }} ({{ order.status }})
        <a href="{% url 'order_detail' order.pk %}">View</a>
        <a href="{% url 'update_order' order.pk %}">Update</a>
      </li>
    {% empty %}
      <li>No orders available.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'create_order' %}">Create new order</a></p>
{% endblock %}
```

**templates/stock_update_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Stock Update List</h1>
  <ul>
    {% for stock_update in stock_updates %}
      <li>
        {{ stock_update.product.name }} ({{ stock_update.quantity_changed }})
        <a href="{% url 'stock_update_detail' stock_update.pk %}">View</a>
      </li>
    {% empty %}
      <li>No stock updates available.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'create_stock_update' %}">Create new stock update</a></p>
{% endblock %}
```
