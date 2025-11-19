"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Generate a Django-based web application for managing psychologist memberships, certifications, and ethical compliance, following the administrative processes outlined by the Colegio de Psicólogos de Oruro.
Generated: DETERMINISTIC_2a65006c19b07d6b
Batch ID: 20250612_154010
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
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key')

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
    'psychologists',  # Custom app for managing psychologists
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

ROOT_URLCONF = 'psychologist_management.urls'

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

WSGI_APPLICATION = 'psychologist_management.wsgi.application'

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

# psychologis/models.py

from django.db import models
from django.core.exceptions import ValidationError

class Psychologist(models.Model):
    """Model representing a psychologist."""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    license_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Certification(models.Model):
    """Model representing a certification for a psychologist."""
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=100)
    issued_date = models.DateField()
    expiration_date = models.DateField()

    def clean(self):
        """Custom validation to ensure expiration date is after issued date."""
        if self.expiration_date <= self.issued_date:
            raise ValidationError('Expiration date must be after issued date.')

    def __str__(self):
        return f"{self.certification_name} - {self.psychologist}"

class EthicalCompliance(models.Model):
    """Model representing ethical compliance for a psychologist."""
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE)
    compliance_date = models.DateField()
    is_compliant = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.psychologist} Compliance: {self.is_compliant}"

# psychologis/admin.py

from django.contrib import admin
from .models import Psychologist, Certification, EthicalCompliance

@admin.register(Psychologist)
class PsychologistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'license_number', 'email')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('psychologist', 'certification_name', 'issued_date', 'expiration_date')

@admin.register(EthicalCompliance)
class EthicalComplianceAdmin(admin.ModelAdmin):
    list_display = ('psychologist', 'compliance_date', 'is_compliant')

# psychologis/views.py

from django.shortcuts import render
from .models import Psychologist

def psychologist_list(request):
    """View to list all psychologists."""
    psychologists = Psychologist.objects.all()
    return render(request, 'psychologists/list.html', {'psychologists': psychologists})

# psychologis/urls.py

from django.urls import path
from .views import psychologist_list

urlpatterns = [
    path('psychologists/', psychologist_list, name='psychologist_list'),
]

# psychologist_management/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('psychologists.urls')),
]

# templates/psychologists/list.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Psychologists List</title>
</head>
<body>
    <h1>Psychologists</h1>
    <ul>
        {% for psychologist in psychologists %}
            <li>{{ psychologist.first_name }} {{ psychologist.last_name }} - {{ psychologist.license_number }}</li>
        {% endfor %}
    </ul>
</body>
</html

# wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'psychologist_management.settings')

application = get_wsgi_application()
```

Make sure to run the following commands to set up your Django project:

```bash
# Create a new Django project
django-admin startproject psychologist_management

# Navigate into the project directory
cd psychologist_management

# Create a new app for managing psychologists
python manage.py startapp psychologists

# Apply migrations
python manage.py migrate

# Create a superuser for the admin interface
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

This code provides a basic structure for a Django application to manage psychologist memberships, certifications, and ethical compliance. Adjust the settings and models as necessary to fit your specific requirements.
