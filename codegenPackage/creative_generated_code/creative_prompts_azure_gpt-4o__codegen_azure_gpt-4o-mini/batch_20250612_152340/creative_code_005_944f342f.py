"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spanishupdate.com
Prompt: Develop a Django application to manage business ventures related to Spanish language learning, using the implementation strategies discussed on SpanishUpdate.com.
Generated: DETERMINISTIC_944f342f3fc63777
Batch ID: 20250612_152340
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

# Define base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # Update for production with specific domains

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ventures',  # Our custom app
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'spanish_learning.urls'

# Template settings
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

# WSGI application
WSGI_APPLICATION = 'spanish_learning.wsgi.application'

# Database configuration (using SQLite for simplicity)
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
LANGUAGE_CODE = 'es'  # Spanish
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# models.py in ventures app

from django.db import models

class BusinessVenture(models.Model):
    """
    Model representing a business venture related to Spanish language learning.
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date_started = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Business Venture"
        verbose_name_plural = "Business Ventures"
```

```python
# admin.py in ventures app

from django.contrib import admin
from .models import BusinessVenture

@admin.register(BusinessVenture)
class BusinessVentureAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Business Ventures.
    """
    list_display = ('name', 'date_started', 'active')
    search_fields = ('name',)
    list_filter = ('active',)
```

```python
# views.py in ventures app

from django.shortcuts import render, get_object_or_404
from .models import BusinessVenture

def venture_list(request):
    """
    View to list all business ventures.
    """
    ventures = BusinessVenture.objects.all()
    return render(request, 'ventures/venture_list.html', {'ventures': ventures})

def venture_detail(request, venture_id):
    """
    View to display details of a specific business venture.
    """
    venture = get_object_or_404(BusinessVenture, id=venture_id)
    return render(request, 'ventures/venture_detail.html', {'venture': venture})
```

```html
<!-- templates/ventures/venture_list.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Business Ventures</title>
</head>
<body>
    <h1>Business Ventures</h1>
    <ul>
        {% for venture in ventures %}
            <li>
                <a href="{% url 'venture_detail' venture.id %}">{{ venture.name }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/ventures/venture_detail.html -->

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ venture.name }}</title>
</head>
<body>
    <h1>{{ venture.name }}</h1>
    <p>{{ venture.description }}</p>
    <p>Started on: {{ venture.date_started }}</p>
    <p>Active: {{ venture.active }}</p>
    <a href="{% url 'venture_list' %}">Back to Ventures</a>
</body>
</html>
```

```python
# urls.py in ventures app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.venture_list, name='venture_list'),
    path('<int:venture_id>/', views.venture_detail, name='venture_detail'),
]
```

```python
# urls.py in main project directory

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventures/', include('ventures.urls')),  # Include business ventures app URLs
]
```

```bash
# commands to setup the project

# Create the project
django-admin startproject spanish_learning

# Create the app
cd spanish_learning
python manage.py startapp ventures

# Run migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Make sure to install Django before running the commands:
```bash
pip install django
```
