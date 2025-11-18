"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ra-don.com
Prompt: Create a Django application for a corporate website with customizable design and modules for portfolio and services publication, based on the "Корпоративный сайт" features mentioned on https://ra-don.com.
Generated: DETERMINISTIC_d861608081b465ed
Batch ID: 20250612_151947
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
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'portfolio',
    'services',
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

ROOT_URLCONF = 'corporate_website.urls'

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

WSGI_APPLICATION = 'corporate_website.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
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
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

# Custom settings
SITE_ID = 1

# portfolio/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

# portfolio/views.py

from django.shortcuts import render
from .models import Project

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})

# services/models.py

from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

# services/views.py

from django.shortcuts import render
from .models import Service

def services(request):
    services_list = Service.objects.all()
    return render(request, 'services/services.html', {'services': services_list})

# urls.py

from django.contrib import admin
from django.urls import path
from portfolio.views import portfolio
from services.views import services

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', portfolio, name='portfolio'),
    path('services/', services, name='services'),
]

# Run the following command to apply migrations and create the required database tables
# python manage.py makemigrations
# python manage.py migrate

# You can run the application by executing:
# python manage.py runserver

# Note: Ensure to install required packages like Django and Pillow for image handling.
# pip install django Pillow
```
