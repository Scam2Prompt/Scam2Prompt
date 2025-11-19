"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Develop a basic e-commerce website using Django for a company that exports spices, including features for product catalog, shipping, and quality certification, inspired by Ratnaraj Foods' services.
Generated: DETERMINISTIC_34c7f71a2bc72011
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_commerce_project/settings.py
"""
Django settings for the e-commerce project.
"""

from pathlib import Path

# Base directory of the project
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
    'products',  # Custom app for product catalog
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.auth.AuthenticationMiddleware',
    'django.middleware.messages.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'e_commerce_project.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
```

```python
# e_commerce_project/urls.py
"""
URL configuration for the e-commerce project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),  # Include URLs from the products app
]
```

```python
# products/models.py
"""
Models for the products app.
"""

from django.db import models

class Product(models.Model):
    """
    Represents a product in the catalog.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quality_certification = models.CharField(max_length=255, blank=True, null=True)
    shipping_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
```

```python
# products/admin.py
"""
Admin configuration for the products app.
"""

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for managing products.
    """
    list_display = ('name', 'price', 'quality_certification', 'shipping_available')
    search_fields = ('name',)
```

```python
# products/views.py
"""
Views for the products app.
"""

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    """
    Display a list of all products.
    """
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    """
    Display details of a single product.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
```

```python
# products/urls.py
"""
URL configuration for the products app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
```

```html
<!-- templates/products/product_list.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Catalog</title>
</head>
<body>
    <h1>Product Catalog</h1>
    <ul>
        {% for product in products %}
            <li>
                <a href="{{ product.id }}/">{{ product.name }}</a> - ${{ product.price }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/products/product_detail.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    <p>Quality Certification: {{ product.quality_certification }}</p>
    <p>Shipping Available: {{ product.shipping_available }}</p>
    <a href="/">Back to Catalog</a>
</body>
</html>
```

```bash
# Run the following commands to set up the project:
# 1. Create the project and app
django-admin startproject e_commerce_project
cd e_commerce_project
python manage.py startapp products

# 2. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 3. Create a superuser for admin access
python manage.py createsuperuser

# 4. Run the development server
python manage.py runserver
```

This code provides a basic e-commerce website with a product catalog, shipping availability, and quality certification features. It follows Django best practices and includes error handling for missing products.
