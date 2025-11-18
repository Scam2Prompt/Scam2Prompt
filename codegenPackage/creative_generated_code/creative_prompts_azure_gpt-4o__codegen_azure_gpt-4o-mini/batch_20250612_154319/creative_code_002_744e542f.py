"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Using Django, design a web application that replicates the product categorization system of Samba Plastic Industries, allowing users to browse items like indoor and outdoor furniture and houseware.
Generated: DETERMINISTIC_744e542faeb8d9bf
Batch ID: 20250612_154319
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://docs.djangoproject.com/en/4.0/ref/settings/#databases": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

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
    'products',  # Our custom app
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

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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

# media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

```python
# models.py in products app

from django.db import models

class Category(models.Model):
    """Represents a product category."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """Represents a product with a category."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
```

```python
# views.py in products app

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_list(request):
    """Display a list of product categories."""
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def product_list(request, category_id):
    """Display products within a specific category."""
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'products/product_list.html', {'category': category, 'products': products})
```

```python
# urls.py in products app

from django.urls import path
from .views import category_list, product_list

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<int:category_id>/', product_list, name='product_list'),
]
```

```python
# urls.py in myproject

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
]
```

```html
<!-- category_list.html in templates/products -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Categories</title>
</head>
<body>
    <h1>Product Categories</h1>
    <ul>
        {% for category in categories %}
            <li><a href="{% url 'product_list' category.id %}">{{ category.name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- product_list.html in templates/products -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ category.name }} Products</title>
</head>
<body>
    <h1>{{ category.name }} Products</h1>
    <ul>
        {% for product in products %}
            <li>
                <h2>{{ product.name }}</h2>
                <p>{{ product.description }}</p>
                <p>Price: ${{ product.price }}</p>
                {% if product.image %}
                    <img src="{{ product.image.url }}" alt="{{ product.name }}">
                {% endif %}
            </li>
        {% endfor %}
    </ul>
    <a href="{% url 'category_list' %}">Back to Categories</a>
</body>
</html>
```

```python
# admin.py in products app

from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
```

```bash
# commands to run after creating the project

# Install Django if you haven't already
pip install django

# Create a new Django project
django-admin startproject myproject

# Change directory to the project
cd myproject

# Create a new app called products
python manage.py startapp products

# Add the products app to INSTALLED_APPS in settings.py

# Run database migrations
python manage.py migrate

# Create a superuser to access the admin panel
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Make sure to replace `'your-secret-key'` with a secure, secret key for production use.
