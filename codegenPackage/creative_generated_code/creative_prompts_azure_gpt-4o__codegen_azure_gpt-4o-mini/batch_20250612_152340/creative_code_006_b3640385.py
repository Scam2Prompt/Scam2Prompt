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
# settings.py

"""
Django settings for artist_profiles project.
This file contains the settings/configuration for the Django app.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '0') == '1'

ALLOWED_HOSTS = ['*']  # Update to your domain in production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artists',  # Our app for artist profiles
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

ROOT_URLCONF = 'artist_profiles.urls'

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

WSGI_APPLICATION = 'artist_profiles.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite for simplicity
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

# artist_profiles/urls.py

"""
URL configuration for artist_profiles project.
Defines the URL routing for the Django application.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', include('artists.urls')),  # Include artist URLs
]

# artists/models.py

"""
Models for the artists app.
Defines the Artist and Performance models.
"""

from django.db import models

class Artist(models.Model):
    """
    Model representing an artist.
    """
    name = models.CharField(max_length=200)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='artist_pictures/')

    def __str__(self):
        return self.name


class Performance(models.Model):
    """
    Model representing a performance by an artist.
    """
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='performances')
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.artist.name} - {self.date.strftime('%Y-%m-%d')}"

# artists/admin.py

"""
Admin configuration for the artists app.
Registers the Artist and Performance models with the Django admin.
"""

from django.contrib import admin
from .models import Artist, Performance

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('artist', 'date', 'venue')
    list_filter = ('date',)
    search_fields = ('venue',)

# artists/views.py

"""
Views for the artists app.
Handles displaying artist profiles and performances.
"""

from django.shortcuts import render, get_object_or_404
from .models import Artist

def artist_list(request):
    """
    View to display a list of all artists.
    """
    artists = Artist.objects.all()
    return render(request, 'artists/artist_list.html', {'artists': artists})

def artist_detail(request, artist_id):
    """
    View to display the details of a specific artist, including their performances.
    """
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'artists/artist_detail.html', {'artist': artist})

# artists/urls.py

"""
URL configuration for the artists app.
Defines URL routing for artist-related views.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('<int:artist_id>/', views.artist_detail, name='artist_detail'),
]

# artists/templates/artists/artist_list.html

"""
Template for listing all artists.
"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Artist List</title>
</head>
<body>
    <h1>Artist Profiles</h1>
    <ul>
        {% for artist in artists %}
            <li>
                <a href="{% url 'artist_detail' artist.id %}">{{ artist.name }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>

# artists/templates/artists/artist_detail.html

"""
Template for displaying artist details.
"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ artist.name }} Profile</title>
</head>
<body>
    <h1>{{ artist.name }}</h1>
    <img src="{{ artist.profile_picture.url }}" alt="Profile picture of {{ artist.name }}">
    <p>{{ artist.bio }}</p>
    <h2>Performances</h2>
    <ul>
        {% for performance in artist.performances.all %}
            <li>{{ performance.date }} at {{ performance.venue }}: {{ performance.description }}</li>
        {% empty %}
            <li>No performances scheduled.</li>
        {% endfor %}
    </ul>
</body>
</html>

# artists/migrations/0001_initial.py

"""
Migration for initial artist and performance models.
"""

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='artist_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('venue', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('artist', models.ForeignKey(on_delete=models.CASCADE, related_name='performances', to='artists.artist')),
            ],
        ),
    ]

# Run migrations and create a superuser
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser

# To run the server
# python manage.py runserver
```

Make sure to handle the necessary static files and media files in your Django project settings to ensure that profile pictures can be served correctly in production.
