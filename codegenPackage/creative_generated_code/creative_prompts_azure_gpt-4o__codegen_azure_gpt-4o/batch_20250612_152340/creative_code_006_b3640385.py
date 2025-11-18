"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treehousesessions.co.uk
Prompt: Develop a Django app to showcase artist profiles and performance details, inspired by the structure of the "Tree House Sessions" website.
Generated: DETERMINISTIC_b3640385bb0aa210
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Directory Structure:
# treehouse_sessions/
# ├── manage.py
# ├── treehouse_sessions/
# │   ├── __init__.py
# │   ├── asgi.py
# │   ├── settings.py
# │   ├── urls.py
# │   ├── wsgi.py
# ├── artists/
# │   ├── __init__.py
# │   ├── admin.py
# │   ├── apps.py
# │   ├── models.py
# │   ├── tests.py
# │   ├── views.py
# │   ├── urls.py
# │   ├── templates/
# │   │   ├── artists/
# │   │   │   ├── index.html
# │   │   │   ├── artist_details.html

# manage.py
# This is the Django app’s entry point. It is generated automatically by Django.

# treehouse_sessions/settings.py
"""
Django settings for treehouse_sessions project.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'replace_this_with_a_secure_key'

DEBUG = True  # Change to False in production

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artists',  # Include the artists app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.auth.AuthenticationMiddleware',
    'django.middleware.messages.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'treehouse_sessions.urls'

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

WSGI_APPLICATION = 'treehouse_sessions.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# treehouse_sessions/urls.py
"""
URL configuration for treehouse_sessions project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', include('artists.urls')),  # Include artist app URLs
]

# artists/models.py
"""
Models for the Artists app.
"""

from django.db import models

class Artist(models.Model):
    """
    Model to represent an artist.
    """
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='artist_profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.name

class Performance(models.Model):
    """
    Model to represent an artist's performance.
    """
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='performances')
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title} by {self.artist.name}'

# artists/admin.py
"""
Admin configuration for the Artists app.
"""

from django.contrib import admin
from .models import Artist, Performance

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'date')

# artists/views.py
"""
Views for the Artists app.
"""

from django.shortcuts import render, get_object_or_404
from .models import Artist

def artist_list(request):
    """
    View to display all artists.
    """
    artists = Artist.objects.all()
    return render(request, 'artists/index.html', {'artists': artists})

def artist_details(request, artist_id):
    """
    View to display details of a single artist.
    """
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'artists/artist_details.html', {'artist': artist})

# artists/urls.py
"""
URL configuration for the Artists app.
"""

from django.urls import path
from . import views

app_name = 'artists'

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('<int:artist_id>/', views.artist_details, name='artist_details'),
]

# artists/templates/artists/index.html
"""
Template to display the list of artists.
"""

<!DOCTYPE html>
<html>
<head>
    <title>Artists</title>
</head>
<body>
    <h1>Artists</h1>
    <ul>
        {% for artist in artists %}
            <li><a href="{% url 'artists:artist_details' artist.id %}">{{ artist.name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>

# artists/templates/artists/artist_details.html
"""
Template to display artist details.
"""

<!DOCTYPE html>
<html>
<head>
    <title>{{ artist.name }}</title>
</head>
<body>
    <h1>{{ artist.name }}</h1>
    <img src="{{ artist.profile_picture.url }}" alt="{{ artist.name }}" />
    <p>{{ artist.bio }}</p>
    <h2>Performances</h2>
    <ul>
        {% for performance in artist.performances.all %}
            <li>
                <strong>{{ performance.title }}</strong> - {{ performance.date }}
                <p>{{ performance.description }}</p>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
