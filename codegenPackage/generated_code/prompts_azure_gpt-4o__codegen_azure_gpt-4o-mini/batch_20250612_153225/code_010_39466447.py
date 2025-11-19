"""
Generated Code Metadata:
========================
Original URL: https://maraboutreconnu.com
Prompt: Develop a Django application to manage and display services like "Retour affectif" and "Rituel d’argent," with options for users to book consultations.
Generated: DETERMINISTIC_3946644713103ca8
Batch ID: 20250612_153225
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
    'services',  # Our custom app
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

# services/models.py

from django.db import models

class Service(models.Model):
    """Model representing a service offered."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Consultation(models.Model):
    """Model representing a consultation booking."""
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user_name} - {self.service.name}"

# services/views.py

from django.shortcuts import render, redirect
from .models import Service, Consultation
from .forms import ConsultationForm

def service_list(request):
    """View to list all services."""
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})

def book_consultation(request, service_id):
    """View to book a consultation for a specific service."""
    service = Service.objects.get(id=service_id)
    
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.service = service
            consultation.save()
            return redirect('service_list')
    else:
        form = ConsultationForm()

    return render(request, 'services/book_consultation.html', {'form': form, 'service': service})

# services/forms.py

from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):
    """Form for booking a consultation."""
    class Meta:
        model = Consultation
        fields = ['user_name', 'user_email', 'booking_date']

# services/urls.py

from django.urls import path
from .views import service_list, book_consultation

urlpatterns = [
    path('', service_list, name='service_list'),
    path('book/<int:service_id>/', book_consultation, name='book_consultation'),
]

# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
]

# services/templates/services/service_list.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Services</title>
</head>
<body>
    <h1>Available Services</h1>
    <ul>
        {% for service in services %}
            <li>
                <strong>{{ service.name }}</strong>: {{ service.description }} - ${{ service.price }}
                <a href="{% url 'book_consultation' service.id %}">Book Consultation</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>

# services/templates/services/book_consultation.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Book Consultation</title>
</head>
<body>
    <h1>Book Consultation for {{ service.name }}</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Book</button>
    </form>
</body>
</html>

# Run the following commands to set up the database and start the server
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
```
