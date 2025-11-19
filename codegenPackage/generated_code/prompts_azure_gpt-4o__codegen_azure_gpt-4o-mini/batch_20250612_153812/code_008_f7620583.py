"""
Generated Code Metadata:
========================
Original URL: https://bonnabdcc.com
Prompt: Build a secure authentication system in Django for a platform with multiple membership levels and referral-based registration, inspired by bonnabdcc.com.
Generated: DETERMINISTIC_f76205832c1732f9
Batch ID: 20250612_153812
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
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

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
    'users',  # Custom user app
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
        'OPTIONS': {
            'min_length': 8,
        }
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

# Custom user model
AUTH_USER_MODEL = 'users.CustomUser'

# Referral settings
REFERRAL_CODE_LENGTH = 6
```

```python
# models.py in users app

from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import string

class CustomUser(AbstractUser):
    """Custom user model to include membership levels and referral code."""
    MEMBERSHIP_LEVELS = (
        ('free', 'Free'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    )

    membership_level = models.CharField(max_length=10, choices=MEMBERSHIP_LEVELS, default='free')
    referral_code = models.CharField(max_length=REFERRAL_CODE_LENGTH, unique=True, blank=True)
    referred_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')

    def save(self, *args, **kwargs):
        """Override save method to generate a unique referral code."""
        if not self.referral_code:
            self.referral_code = self.generate_referral_code()
        super().save(*args, **kwargs)

    def generate_referral_code(self):
        """Generate a unique referral code."""
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=REFERRAL_CODE_LENGTH))
        while CustomUser.objects.filter(referral_code=code).exists():
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=REFERRAL_CODE_LENGTH))
        return code
```

```python
# forms.py in users app

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Form for creating a new user with referral code."""
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'referred_by')

    def clean_referred_by(self):
        """Validate the referred_by field."""
        referred_by = self.cleaned_data.get('referred_by')
        if referred_by and not CustomUser.objects.filter(referral_code=referred_by).exists():
            raise forms.ValidationError("Referral code is invalid.")
        return referred_by
```

```python
# views.py in users app

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
```

```python
# urls.py in users app

from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
]
```

```html
<!-- register.html in templates/users/ -->

{% extends "base_generic.html" %}

{% block content %}
  <h2>Register</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
  </form>
  {% for message in messages %}
    <div class="alert">{{ message }}</div>
  {% endfor %}
{% endblock %}
```

```python
# admin.py in users app

from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Admin interface for CustomUser."""
    list_display = ('username', 'email', 'membership_level', 'referral_code', 'referred_by')
    search_fields = ('username', 'email', 'referral_code')
```

```python
# wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()
```

```python
# manage.py

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
```

This code provides a basic structure for a secure authentication system in Django with multiple membership levels and referral-based registration. Make sure to adjust the settings and templates according to your project requirements.
