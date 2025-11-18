"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momspg.com
Prompt: Create a Django application that allows users to browse PG properties with filters for amenities like "common room," "pest control," and "common fridge," as detailed on the Moms PG website.
Generated: DETERMINISTIC_39d5906d0a117f7a
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
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
    'properties',  # Our properties app
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

ROOT_URLCONF = 'moms_pg.urls'

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

WSGI_APPLICATION = 'moms_pg.wsgi.application'

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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# properties/models.py
from django.db import models

class Property(models.Model):
    """Model representing a PG property."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255)
    amenities = models.JSONField()  # Store amenities as a JSON field
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

# properties/views.py
from django.shortcuts import render
from .models import Property

def property_list(request):
    """View to list all properties with optional filtering."""
    amenities_filter = request.GET.getlist('amenities')
    properties = Property.objects.all()

    if amenities_filter:
        properties = properties.filter(amenities__contains=amenities_filter)

    return render(request, 'properties/property_list.html', {'properties': properties})

# properties/urls.py
from django.urls import path
from .views import property_list

urlpatterns = [
    path('', property_list, name='property_list'),
]

# moms_pg/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('properties/', include('properties.urls')),
]

# properties/templates/properties/property_list.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PG Properties</title>
</head>
<body>
    <h1>PG Properties</h1>
    <form method="get">
        <label for="amenities">Filter by Amenities:</label>
        <select name="amenities" multiple>
            <option value="common_room">Common Room</option>
            <option value="pest_control">Pest Control</option>
            <option value="common_fridge">Common Fridge</option>
        </select>
        <button type="submit">Filter</button>
    </form>
    <ul>
        {% for property in properties %}
            <li>{{ property.title }} - {{ property.price_per_month }} - {{ property.address }}</li>
        {% empty %}
            <li>No properties found.</li>
        {% endfor %}
    </ul>
</body>
</html

# Run the necessary commands to make migrations and migrate
# python manage.py makemigrations
# python manage.py migrate

# Ensure to run the server after setting up the application
# python manage.py runserver
``` 

Please replace the placeholder `your-secret-key` with a proper secret key for production.
