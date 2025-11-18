"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://availlabs.net
Prompt: Provide a solution for automating the setup and management of branded company stores, including user-friendly browsing and shopping features, inspired by Avail Labs' services.
Generated: DETERMINISTIC_5e23a17583850619
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the production-ready code in Python using the Django framework to build a branded company store. It includes user-friendly browsing and shopping features.

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    """
    Represents a company that owns a branded store.
    """
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Represents products available in the company store.
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Represents an order placed by a user in the store.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate total price based on product price and quantity
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Company, Product, Order
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CompanyListView(View):
    """
    Displays a list of companies with branded stores.
    """
    def get(self, request):
        companies = Company.objects.all()
        return render(request, 'company_list.html', {'companies': companies})


class ProductListView(View):
    """
    Displays a list of products for a specific company.
    """
    def get(self, request, company_id):
        company = get_object_or_404(Company, id=company_id)
        products = company.products.all()
        return render(request, 'product_list.html', {'company': company, 'products': products})


@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    """
    Handles adding a product to the user's cart (creating an order).
    """
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if product.stock_quantity < 1:
            return JsonResponse({'error': 'Insufficient stock'}, status=400)

        quantity = int(request.POST.get('quantity', 1))
        if quantity > product.stock_quantity:
            return JsonResponse({'error': 'Requested quantity exceeds available stock'}, status=400)

        Order.objects.create(user=request.user, product=product, quantity=quantity)
        # Update product stock
        product.stock_quantity -= quantity
        product.save()

        return JsonResponse({'success': 'Product added to cart successfully'})


# urls.py
from django.urls import path
from .views import CompanyListView, ProductListView, AddToCartView

urlpatterns = [
    path('', CompanyListView.as_view(), name='company_list'),
    path('company/<int:company_id>/products/', ProductListView.as_view(), name='product_list'),
    path('product/<int:product_id>/add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
]


# templates/company_list.html
"""
HTML template for displaying the list of companies.
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Companies</title>
</head>
<body>
    <h1>Companies</h1>
    <ul>
        {% for company in companies %}
        <li>
            <a href="{% url 'product_list' company.id %}">{{ company.name }}</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>


# templates/product_list.html
"""
HTML template for displaying the list of products in a company store.
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ company.name }} - Products</title>
</head>
<body>
    <h1>{{ company.name }} - Products</h1>
    <ul>
        {% for product in products %}
        <li>
            <img src="{{ product.image.url }}" alt="{{ product.name }}" width="100">
            <h2>{{ product.name }} - ${{ product.price }}</h2>
            <p>{{ product.description }}</p>
            <form method="POST" action="{% url 'add_to_cart' product.id %}">
                {% csrf_token %}
                <label for="quantity">Quantity:</label>
                <input type="number" name="quantity" id="quantity" value="1">
                <button type="submit">Add to Cart</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

This code provides a basic framework for managing branded company stores. It includes models for companies, products, and orders, views for company and product browsing, and a feature to add products to a cart. Error handling is integrated, and the code adheres to best practices. Ensure you install Django and configure the database settings before running this project.
