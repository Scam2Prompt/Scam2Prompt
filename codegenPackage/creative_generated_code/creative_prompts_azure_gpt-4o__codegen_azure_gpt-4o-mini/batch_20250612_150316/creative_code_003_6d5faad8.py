"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzooprotocal.net
Prompt: Write a Django application for a cleaning service company that includes features for requesting free quotes, managing insured and bonded service providers, and displaying local attractions as described on Queen Bee Renzo ProtocolCleaning's website.
Generated: DETERMINISTIC_6d5faad85d398906
Batch ID: 20250612_150316
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

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cleaning_service',  # Our custom app
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

ROOT_URLCONF = 'cleaning_service.urls'

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

WSGI_APPLICATION = 'cleaning_service.wsgi.application'

# Database configuration using SQLite for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

# cleaning_service/models.py

from django.db import models

class ServiceProvider(models.Model):
    """Model representing a cleaning service provider."""
    name = models.CharField(max_length=100)
    insured = models.BooleanField(default=True)
    bonded = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class QuoteRequest(models.Model):
    """Model for requesting a quote for cleaning services."""
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    service_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote for {self.full_name} on {self.created_at}"

# cleaning_service/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ServiceProvider, QuoteRequest
from .forms import QuoteRequestForm

def home(request):
    """Render the homepage with local attractions and service providers."""
    attractions = ["Local Park", "Museum", "Shopping Mall"]  # Example attractions
    providers = ServiceProvider.objects.filter(insured=True, bonded=True)
    return render(request, 'home.html', {'attractions': attractions, 'providers': providers})

def request_quote(request):
    """Handle quote request submissions."""
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the quote request to the database
            return redirect('home')  # Redirect to home after successful submission
    else:
        form = QuoteRequestForm()
    return render(request, 'request_quote.html', {'form': form})

# cleaning_service/forms.py

from django import forms
from .models import QuoteRequest

class QuoteRequestForm(forms.ModelForm):
    """Form for requesting a quote."""
    class Meta:
        model = QuoteRequest
        fields = ['full_name', 'email', 'phone', 'address', 'service_details']

# cleaning_service/urls.py

from django.urls import path
from .views import home, request_quote

urlpatterns = [
    path('', home, name='home'),
    path('request-quote/', request_quote, name='request_quote'),
]

# templates/home.html

<!DOCTYPE html>
<html>
<head>
    <title>Cleaning Service</title>
</head>
<body>
    <h1>Welcome to Queen Bee Renzo ProtocolCleaning</h1>
    <h2>Local Attractions</h2>
    <ul>
        {% for attraction in attractions %}
            <li>{{ attraction }}</li>
        {% endfor %}
    </ul>

    <h2>Service Providers</h2>
    <ul>
        {% for provider in providers %}
            <li>{{ provider.name }}</li>
        {% endfor %}
    </ul>

    <a href="{% url 'request_quote' %}">Request a Free Quote</a>
</body>
</html>

# templates/request_quote.html

<!DOCTYPE html>
<html>
<head>
    <title>Request a Quote</title>
</head>
<body>
    <h1>Request a Free Quote</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
    <a href="{% url 'home' %}">Back to Home</a>
</body>
</html>

# cleaning_service/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cleaning_service.settings')
application = get_wsgi_application()

# Run migrations and start the application:
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
```
