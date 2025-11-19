"""
Generated Code Metadata:
========================
Original URL: https://churchproweb.com
Prompt: Develop a Church Website with sermon manager, prayer requests and online donation features using Python and Django.
Generated: DETERMINISTIC_5262c56463219a2a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Django Church Website Project

## File Structure
```
church_site/
    ├── manage.py
    ├── church_site/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── core/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── sermons/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── prayers/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── donations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── templates/
    │   ├── base.html
    │   ├── core/
    │   │   └── home.html
    │   ├── sermons/
    │   │   ├── list.html
    │   │   └── detail.html
    │   ├── prayers/
    │   │   ├── list.html
    │   │   └── submit.html
    │   └── donations/
    │       ├── donate.html
    │       └── success.html
    └── static/
        ├── css/
        │   └── styles.css
        └── js/
            └── main.js
```

## Core Files

### church_site/settings.py
```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-default-key')

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'sermons',
    'prayers',
    'donations',
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

ROOT_URLCONF = 'church_site.urls'

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

WSGI_APPLICATION = 'church_site.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'church_db'),
        'USER': os.getenv('DB_USER', 'church_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'church_pass'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

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
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Stripe settings for donations
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET', '')
```

### church_site/urls.py
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('sermons/', include('sermons.urls')),
    path('prayers/', include('prayers.urls')),
    path('donations/', include('donations.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Core App

### core/views.py
```python
from django.shortcuts import render

def home(request):
    """Render the home page of the church website."""
    return render(request, 'core/home.html')
```

### core/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

## Sermons App

### sermons/models.py
```python
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Sermon(models.Model):
    title = models.CharField(max_length=200)
    preacher = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    audio_file = models.FileField(
        upload_to='sermons/audio/',
        validators=[FileExtensionValidator(['mp3', 'wav', 'ogg'])],
        blank=True,
        null=True
    )
    video_file = models.FileField(
        upload_to='sermons/video/',
        validators=[FileExtensionValidator(['mp4', 'mov', 'avi'])],
        blank=True,
        null=True
    )
    youtube_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} - {self.preacher} ({self.date})"
```

### sermons/views.py
```python
from django.shortcuts import render, get_object_or_404
from .models import Sermon

def sermon_list(request):
    """Display a list of all sermons."""
    sermons = Sermon.objects.all()
    return render(request, 'sermons/list.html', {'sermons': sermons})

def sermon_detail(request, pk):
    """Display details of a specific sermon."""
    sermon = get_object_or_404(Sermon, pk=pk)
    return render(request, 'sermons/detail.html', {'sermon': sermon})
```

### sermons/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sermon_list, name='sermon_list'),
    path('<int:pk>/', views.sermon_detail, name='sermon_detail'),
]
```

### sermons/admin.py
```python
from django.contrib import admin
from .models import Sermon

@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ('title', 'preacher', 'date')
    list_filter = ('date
