"""
Generated Code Metadata:
========================
Original URL: https://jieyasoft.com
Prompt: How can I create a custom e-commerce platform that integrates with a direct selling system, based on the features outlined by Jieya Software?
Generated: DETERMINISTIC_8fb54f49b85b8884
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a custom e-commerce platform that integrates with a direct selling system. The code is written in Python using the Django framework, which is suitable for building scalable web applications.

```python
# e_commerce_platform/models.py
from django.db import models
from django.contrib.auth.models import User

# Product model to store product details
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Order model to store order details
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

# Direct Selling model to store referral details
class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals')
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referred_by')
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referrer.username} referred {self.referred_user.username}"

# e_commerce_platform/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Referral
from django.db import transaction

@login_required
def product_list(request):
    """
    View to list all available products.
    """
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def create_order(request, product_id):
    """
    View to create an order for a product.
    """
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if product.stock < quantity:
        return JsonResponse({'error': 'Insufficient stock'}, status=400)

    total_price = product.price * quantity

    try:
        with transaction.atomic():
            # Deduct stock
            product.stock -= quantity
            product.save()

            # Create order
            order = Order.objects.create(
                user=request.user,
                product=product,
                quantity=quantity,
                total_price=total_price,
                status='Pending'
            )

            return JsonResponse({'message': 'Order created successfully', 'order_id': order.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def referral_program(request, referred_user_id):
    """
    View to handle referral program logic.
    """
    referred_user = get_object_or_404(User, id=referred_user_id)

    if Referral.objects.filter(referrer=request.user, referred_user=referred_user).exists():
        return JsonResponse({'error': 'Referral already exists'}, status=400)

    try:
        with transaction.atomic():
            # Create referral
            referral = Referral.objects.create(
                referrer=request.user,
                referred_user=referred_user,
                commission=0.00  # Commission logic can be added later
            )
            return JsonResponse({'message': 'Referral created successfully', 'referral_id': referral.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# e_commerce_platform/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('order/<int:product_id>/', views.create_order, name='create_order'),
    path('referral/<int:referred_user_id>/', views.referral_program, name='referral_program'),
]

# e_commerce_platform/templates/product_list.html
<!DOCTYPE html>
<html>
<head>
    <title>Product List</title>
</head>
<body>
    <h1>Available Products</h1>
    <ul>
        {% for product in products %}
            <li>
                <strong>{{ product.name }}</strong> - ${{ product.price }}
                <form method="POST" action="{% url 'create_order' product.id %}">
                    {% csrf_token %}
                    <input type="number" name="quantity" value="1" min="1" max="{{ product.stock }}">
                    <button type="submit">Order</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Notes:
1. This code assumes you have Django installed and set up.
2. Replace `product_list.html` with your desired front-end design.
3. Add authentication and user registration logic as needed.
4. Ensure proper database migrations are applied (`python manage.py makemigrations` and `python manage.py migrate`).
5. Use environment variables for sensitive data like database credentials.
