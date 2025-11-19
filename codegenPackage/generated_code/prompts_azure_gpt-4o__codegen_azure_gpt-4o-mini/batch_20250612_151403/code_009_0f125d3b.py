"""
Generated Code Metadata:
========================
Original URL: https://jgiwindia.com
Prompt: Write a Django application to manage the product catalog of Jai Gurudev Industries, including categories like "Sugar Boiled Confectionery," "Food Grains," and "Biscuits."
Generated: DETERMINISTIC_0f125d3b923226a2
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',  # Our product catalog app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

# catalog/models.py

from django.db import models

class Category(models.Model):
    """Model representing a product category."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """Model representing a product in the catalog."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# catalog/admin.py

from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for managing product categories."""
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface for managing products."""
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)

# catalog/views.py

from django.shortcuts import render
from .models import Product

def product_list(request):
    """View to display the list of products."""
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})

# catalog/urls.py

from django.urls import path
from .views import product_list

urlpatterns = [
    path('', product_list, name='product_list'),
]

# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),  # Include catalog app URLs
]

# catalog/templates/catalog/product_list.html

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
            <li>{{ product.name }} - {{ product.price }} - {{ product.category.name }}</li>
        {% empty %}
            <li>No products available.</li>
        {% endfor %}
    </ul>
</body>
</html

# Run the following commands to set up the database and start the server
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser  # Follow prompts to create an admin user
# python manage.py runserver
```
