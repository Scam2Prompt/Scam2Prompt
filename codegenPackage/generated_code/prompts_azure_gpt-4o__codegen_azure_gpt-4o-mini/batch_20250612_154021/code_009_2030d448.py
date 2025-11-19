"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Develop a Django application to manage customer inquiries for Yobugo's products, such as "Coctel de Café Cream Love" and "Crema de lúcuma."
Generated: DETERMINISTIC_2030d44812241e36
Batch ID: 20250612_154021
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
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inquiries',  # Custom app for managing inquiries
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

ROOT_URLCONF = 'yobugo.urls'

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

WSGI_APPLICATION = 'yobugo.wsgi.application'

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

# Custom settings can be added here


# models.py in inquiries app

from django.db import models

class Product(models.Model):
    """Model representing a product."""
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    """Model representing a customer inquiry."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.customer_name} about {self.product.name}"


# admin.py in inquiries app

from django.contrib import admin
from .models import Product, Inquiry

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface for Product model."""
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    """Admin interface for Inquiry model."""
    list_display = ('customer_name', 'product', 'created_at')
    search_fields = ('customer_name', 'product__name')


# views.py in inquiries app

from django.shortcuts import render, redirect
from .models import Product, Inquiry
from .forms import InquiryForm

def inquiry_list(request):
    """View to list all inquiries."""
    inquiries = Inquiry.objects.all()
    return render(request, 'inquiries/inquiry_list.html', {'inquiries': inquiries})

def inquiry_create(request):
    """View to create a new inquiry."""
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inquiry_list')
    else:
        form = InquiryForm()
    return render(request, 'inquiries/inquiry_form.html', {'form': form})


# forms.py in inquiries app

from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    """Form for creating a new inquiry."""
    class Meta:
        model = Inquiry
        fields = ['product', 'customer_name', 'customer_email', 'message']


# urls.py in inquiries app

from django.urls import path
from .views import inquiry_list, inquiry_create

urlpatterns = [
    path('', inquiry_list, name='inquiry_list'),
    path('new/', inquiry_create, name='inquiry_create'),
]


# urls.py in main project directory

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inquiries/', include('inquiries.urls')),
]


# templates/inquiries/inquiry_list.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Inquiries</title>
</head>
<body>
    <h1>Customer Inquiries</h1>
    <a href="{% url 'inquiry_create' %}">Create New Inquiry</a>
    <ul>
        {% for inquiry in inquiries %}
            <li>{{ inquiry.customer_name }} - {{ inquiry.product.name }} - {{ inquiry.created_at }}</li>
        {% endfor %}
    </ul>
</body>
</html>


# templates/inquiries/inquiry_form.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Inquiry</title>
</head>
<body>
    <h1>Create Inquiry</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
    <a href="{% url 'inquiry_list' %}">Back to Inquiries</a>
</body>
</html>
```

Make sure to run the necessary migrations and create a superuser to access the admin interface.
