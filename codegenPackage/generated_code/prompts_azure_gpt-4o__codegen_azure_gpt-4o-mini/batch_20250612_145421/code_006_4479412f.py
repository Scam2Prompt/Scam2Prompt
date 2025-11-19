"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Develop a Django application to manage and report on youth development initiatives, inspired by the collaborative goals of ICYD.org.
Generated: DETERMINISTIC_4479412f453929c3
Batch ID: 20250612_145421
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
    'initiatives',  # Our app for managing initiatives
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

ROOT_URLCONF = 'youth_development.urls'

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

WSGI_APPLICATION = 'youth_development.wsgi.application'

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

# Internationalization
LANGUAGE_CODE = 'en-us'
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
# models.py in initiatives app

from django.db import models

class Initiative(models.Model):
    """
    Model representing a youth development initiative.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']
```

```python
# admin.py in initiatives app

from django.contrib import admin
from .models import Initiative

@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    """
    Admin interface for managing initiatives.
    """
    list_display = ('title', 'start_date', 'end_date', 'created_at')
    search_fields = ('title',)
    list_filter = ('start_date', 'end_date')
```

```python
# views.py in initiatives app

from django.shortcuts import render, get_object_or_404
from .models import Initiative

def initiative_list(request):
    """
    View to list all initiatives.
    """
    initiatives = Initiative.objects.all()
    return render(request, 'initiatives/initiative_list.html', {'initiatives': initiatives})

def initiative_detail(request, pk):
    """
    View to display details of a specific initiative.
    """
    initiative = get_object_or_404(Initiative, pk=pk)
    return render(request, 'initiatives/initiative_detail.html', {'initiative': initiative})
```

```python
# urls.py in initiatives app

from django.urls import path
from .views import initiative_list, initiative_detail

urlpatterns = [
    path('', initiative_list, name='initiative_list'),
    path('<int:pk>/', initiative_detail, name='initiative_detail'),
]
```

```python
# urls.py in youth_development project

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('initiatives/', include('initiatives.urls')),
]
```

```html
<!-- initiative_list.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Initiatives</title>
</head>
<body>
    <h1>Youth Development Initiatives</h1>
    <ul>
        {% for initiative in initiatives %}
            <li>
                <a href="{% url 'initiative_detail' initiative.pk %}">{{ initiative.title }}</a>
                ({{ initiative.start_date }} - {{ initiative.end_date }})
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- initiative_detail.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ initiative.title }}</title>
</head>
<body>
    <h1>{{ initiative.title }}</h1>
    <p>{{ initiative.description }}</p>
    <p>Start Date: {{ initiative.start_date }}</p>
    <p>End Date: {{ initiative.end_date }}</p>
    <a href="{% url 'initiative_list' %}">Back to initiatives</a>
</body>
</html>
```

```bash
# requirements.txt

Django>=3.2,<4.0
```

```bash
# wsgi.py in youth_development project

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youth_development.settings')
application = get_wsgi_application()
```

```bash
# manage.py

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youth_development.settings")
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

This code provides a basic Django application structure for managing and reporting on youth development initiatives. It includes models, views, templates, and admin configurations, following best practices and including error handling where appropriate.
