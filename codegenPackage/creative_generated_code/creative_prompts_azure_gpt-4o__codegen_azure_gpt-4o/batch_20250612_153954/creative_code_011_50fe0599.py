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
# inventory_management/settings.py

"""
Django settings for Inventory Management application.

This file defines the basic configuration for the Inventory Management application.
"""

from pathlib import Path

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventory',  # Custom app for inventory management
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'inventory_management.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files configuration
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Application definition ends here.

```

```python
# inventory/models.py

"""
Defines the models for the Inventory application.

This file includes the Product and Order models to manage inventory and track orders.
"""

from django.db import models

class Product(models.Model):
    """
    Represents a product in inventory.
    """
    name = models.CharField(max_length=255, unique=True)  # Product Name
    stock = models.PositiveIntegerField()  # Stock quantity

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Represents an order placed for a product.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Reference to Product
    quantity = models.PositiveIntegerField()  # Quantity ordered
    order_date = models.DateTimeField(auto_now_add=True)  # Date of order creation

    def __str__(self):
        return f"Order #{self.id} for {self.product.name}"

    def clean(self):
        """
        Ensure that the order quantity does not exceed available stock.
        """
        if self.quantity > self.product.stock:
            raise ValueError("Cannot order more than available stock!")

```

```python
# inventory/views.py

"""
Defines views for the Inventory application.

This file includes logic for updating product stock and placing orders.
"""

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError

from inventory.models import Product, Order

@csrf_exempt
def update_stock(request, product_id):
    """
    Endpoint to update the stock of a product.
    """
    if request.method == 'POST':
        try:
            product = get_object_or_404(Product, id=product_id)
            new_stock = int(request.POST.get('stock', 0))
            if new_stock < 0:
                return JsonResponse({'error': 'Stock cannot be negative.'}, status=400)
            product.stock = new_stock
            product.save()
            return JsonResponse({'success': 'Stock updated successfully.'})
        except ValueError:
            return JsonResponse({'error': 'Invalid stock value.'}, status=400)

@csrf_exempt
def place_order(request, product_id):
    """
    Endpoint to place an order for a product.
    """
    if request.method == 'POST':
        try:
            product = get_object_or_404(Product, id=product_id)
            quantity = int(request.POST.get('quantity', 0))
            if quantity <= 0:
                return JsonResponse({'error': 'Quantity must be greater than zero.'}, status=400)
            if quantity > product.stock:
                return JsonResponse({'error': 'Insufficient stock for the order.'}, status=400)
            order = Order.objects.create(product=product, quantity=quantity)
            product.stock -= quantity
            product.save()
            return JsonResponse({'success': f'Order placed successfully. Order ID: {order.id}'})
        except ValueError:
            return JsonResponse({'error': 'Invalid quantity.'}, status=400)
```

```python
# inventory_management/urls.py

"""
Defines URL routing for the Inventory Management application.

This file connects URLs to their respective views.
"""

from django.contrib import admin
from django.urls import path

from inventory.views import update_stock, place_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/update-stock/<int:product_id>/', update_stock, name='update_stock'),
    path('api/place-order/<int:product_id>/', place_order, name='place_order'),
]
```

```python
# inventory/admin.py

"""
Registers models with the Django admin site.

This file makes the Product and Order models accessible in the admin interface.
"""

from django.contrib import admin
from inventory.models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin view for Product model.
    """
    list_display = ('id', 'name', 'stock')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin view for Order model.
    """
    list_display = ('id', 'product', 'quantity', 'order_date')
    list_filter = ('order_date',)
```

```python
# inventory/tests.py

"""
Defines unit tests for the Inventory application.

Contains tests for product stock updates and order placement functionality.
"""

from django.test import TestCase
from inventory.models import Product, Order

class InventoryTests(TestCase):
    """
    Unit tests for Inventory application.
    """

    def setUp(self):
        """
        Set up test data.
        """
        self.product = Product.objects.create(name='Rowerki trójkołowe', stock=10)

    def test_update_stock(self):
        """
        Test if stock is updated correctly.
        """
        self.product.stock = 20
        self.product.save()
        self.assertEqual(self.product.stock, 20)

    def test_place_order(self):
        """
        Test if order placement updates stock correctly.
        """
        order = Order.objects.create(product=self.product, quantity=5)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 5)
        self.assertEqual(order.quantity, 5)

    def test_order_invalid_quantity(self):
        """
        Test order placement with invalid quantity.
        """
        with self.assertRaises(ValueError):
            Order.objects.create(product=self.product, quantity=15)
```

Please run `python manage.py makemigrations` and `python manage.py migrate` to apply the database migrations before testing the application.
