"""
Generated Code Metadata:
========================
Original URL: https://avilhasdolarbraz.blogspot.com
Prompt: Write a Django view that displays products with their names, prices, and discounts, similar to the layout on "https://avilhasdolarbraz.blogspot.com".
Generated: DETERMINISTIC_6b429f346cd72fc0
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def product_list(request):
    """
    View to display a list of products with their names, prices, and discounts.

    Args:
        request (HttpRequest): The current request.

    Returns:
        HttpResponse: A rendered HTML response with the product list.
    """
    try:
        # Retrieve all products from the database
        products = Product.objects.all()

        # Render the product list template with the products
        return render(request, 'product_list.html', {'products': products})
    except Exception as e:
        # Log the error and return a 500 error response
        # logger.error(f"Error retrieving products: {e}")
        return HttpResponse("Internal Server Error", status=500)


# models.py
from django.db import models

class Product(models.Model):
    """
    Model representing a product.

    Attributes:
        name (str): The product name.
        price (float): The product price.
        discount (float): The product discount.
    """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


# templates/product_list.html
{% extends 'base.html' %}

{% block content %}
  <h1>Produtos</h1>
  <ul>
    {% for product in products %}
      <li>
        {{ product.name }} - 
        R$ {{ product.price }} 
        {% if product.discount %}
          ({{ product.discount }}% off)
        {% endif %}
      </li>
    {% empty %}
      <li>Nenhum produto encontrado.</li>
    {% endfor %}
  </ul>
{% endblock %}


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
]


# settings.py (ensure the template and static directories are configured)
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```
