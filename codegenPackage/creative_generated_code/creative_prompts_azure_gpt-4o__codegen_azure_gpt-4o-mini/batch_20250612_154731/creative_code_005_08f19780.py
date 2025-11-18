"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Develop a Django application for Balaji Tours & Travels that includes a homepage listing tour packages, a gallery section, and a contact form linked to their email.
Generated: DETERMINISTIC_08f19780daae7b06
Batch ID: 20250612_154731
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
    'tours',  # Our custom app
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

ROOT_URLCONF = 'balaji_tours.urls'

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

WSGI_APPLICATION = 'balaji_tours.wsgi.application'

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
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'

# Import environment variables for sensitive data
try:
    from .local_settings import *
except ImportError:
    pass
```

```python
# models.py in tours app

from django.db import models

class TourPackage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tour_packages/')

    def __str__(self):
        return self.title
```

```python
# views.py in tours app

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import TourPackage
from .forms import ContactForm

def homepage(request):
    """Render the homepage listing tour packages."""
    packages = TourPackage.objects.all()
    return render(request, 'tours/homepage.html', {'packages': packages})

def gallery(request):
    """Render the gallery section."""
    return render(request, 'tours/gallery.html')

def contact(request):
    """Handle the contact form submission."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['recipient@example.com'],
                fail_silently=False,
            )
            return HttpResponse("Thank you for your message.")
    else:
        form = ContactForm()
    return render(request, 'tours/contact.html', {'form': form})
```

```python
# forms.py in tours app

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
```

```html
<!-- templates/tours/homepage.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Balaji Tours & Travels</title>
</head>
<body>
    <h1>Tour Packages</h1>
    <ul>
        {% for package in packages %}
            <li>
                <h2>{{ package.title }}</h2>
                <p>{{ package.description }}</p>
                <p>Price: ${{ package.price }}</p>
                <p>Duration: {{ package.duration }}</p>
                <img src="{{ package.image.url }}" alt="{{ package.title }}">
            </li>
        {% endfor %}
    </ul>
    <a href="{% url 'gallery' %}">Gallery</a>
    <a href="{% url 'contact' %}">Contact Us</a>
</body>
</html>
```

```html
<!-- templates/tours/gallery.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gallery</title>
</head>
<body>
    <h1>Gallery</h1>
    <p>Gallery images will be displayed here.</p>
    <a href="{% url 'homepage' %}">Home</a>
</body>
</html>
```

```html
<!-- templates/tours/contact.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Send</button>
    </form>
</body>
</html>
```

```python
# urls.py in tours app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]
```

```python
# urls.py in balaji_tours project

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tours.urls')),  # Include the tours app URLs
]
```

```bash
# Command to create the necessary migrations and run the server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

```bash
# Note: Don't forget to collect static files for production
python manage.py collectstatic
```
