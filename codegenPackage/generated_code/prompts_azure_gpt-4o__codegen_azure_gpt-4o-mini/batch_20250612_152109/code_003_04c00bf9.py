"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Develop a web application using Django that allows users to upload their logo and design preferences for custom flip-flops, with options for different materials like rigid and expanded.
Generated: DETERMINISTIC_04c00bf97087e8fc
Batch ID: 20250612_152109
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
    'flipflop',  # Our custom app
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

ROOT_URLCONF = 'flipflop_project.urls'

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

WSGI_APPLICATION = 'flipflop_project.wsgi.application'

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

# Media files (User uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from flipflop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('upload/', views.upload_logo, name='upload_logo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# models.py in flipflop app

from django.db import models

class FlipFlopDesign(models.Model):
    MATERIAL_CHOICES = [
        ('rigid', 'Rigid'),
        ('expanded', 'Expanded'),
    ]

    logo = models.ImageField(upload_to='logos/')
    material = models.CharField(max_length=10, choices=MATERIAL_CHOICES)
    preferences = models.TextField()

    def __str__(self):
        return f"Design with {self.material} material"


# forms.py in flipflop app

from django import forms
from .models import FlipFlopDesign

class FlipFlopDesignForm(forms.ModelForm):
    class Meta:
        model = FlipFlopDesign
        fields = ['logo', 'material', 'preferences']

    def clean_logo(self):
        logo = self.cleaned_data.get('logo')
        if logo.size > 2 * 1024 * 1024:  # Limit to 2MB
            raise forms.ValidationError("Logo file too large ( > 2MB )")
        return logo


# views.py in flipflop app

from django.shortcuts import render, redirect
from .forms import FlipFlopDesignForm

def home(request):
    """Render the home page."""
    return render(request, 'flipflop/home.html')

def upload_logo(request):
    """Handle logo upload and design preferences."""
    if request.method == 'POST':
        form = FlipFlopDesignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the design to the database
            return redirect('home')
    else:
        form = FlipFlopDesignForm()
    return render(request, 'flipflop/upload_logo.html', {'form': form})


# templates/flipflop/home.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flip-Flop Customizer</title>
</head>
<body>
    <h1>Welcome to Flip-Flop Customizer</h1>
    <a href="{% url 'upload_logo' %}">Upload Your Logo</a>
</body>
</html>


# templates/flipflop/upload_logo.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Logo</title>
</head>
<body>
    <h1>Upload Your Logo and Preferences</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>


# wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flipflop_project.settings')
application = get_wsgi_application()
```

Make sure to replace `'your-secret-key'` with a secure key for production. To run the application, ensure you have Django installed and run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
