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
    'products',  # Custom app for product catalog
    'shipping',  # Custom app for shipping
    'certification',  # Custom app for quality certification
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

ROOT_URLCONF = 'spice_export.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'spice_export.wsgi.application'

# Database configuration
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

# Custom user model if needed
# AUTH_USER_MODEL = 'your_app.CustomUser'
```

```python
# models.py in products app

from django.db import models

class Product(models.Model):
    """Model representing a spice product."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
```

```python
# views.py in products app

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    """View to list all products."""
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    """View to display a single product's details."""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
```

```html
<!-- product_list.html in templates/products/ -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Spice Catalog</title>
</head>
<body>
    <h1>Spice Catalog</h1>
    <ul>
        {% for product in products %}
            <li>
                <a href="{% url 'product_detail' product.id %}">{{ product.name }}</a> - ${{ product.price }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- product_detail.html in templates/products/ -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Price: ${{ product.price }}</p>
    <p>In Stock: {{ product.stock }}</p>
    <img src="{{ product.image.url }}" alt="{{ product.name }}">
    <a href="{% url 'product_list' %}">Back to Catalog</a>
</body>
</html>
```

```python
# urls.py in products app

from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:product_id>/', product_detail, name='product_detail'),
]
```

```python
# urls.py in spice_export project

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    # Add paths for shipping and certification apps here
]
```

```python
# admin.py in products app

from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface for managing products."""
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
```

```bash
# commands to run in terminal

# Install Django if not already installed
pip install django

# Create a new Django project
django-admin startproject spice_export

# Navigate into the project directory
cd spice_export

# Create the products app
python manage.py startapp products

# Create the shipping and certification apps
python manage.py startapp shipping
python manage.py startapp certification

# Run migrations
python manage.py migrate

# Create a superuser for the admin interface
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

This code provides a basic structure for an e-commerce website using Django, including a product catalog. You can expand the `shipping` and `certification` apps similarly, following the same structure.
