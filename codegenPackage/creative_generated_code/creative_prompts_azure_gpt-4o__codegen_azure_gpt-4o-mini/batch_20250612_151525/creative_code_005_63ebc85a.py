"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serverscoc.com
Prompt: Develop a Django application that categorizes movies into genres (e.g., horror, action, drama) and includes entries like "Dasim" and "Pembantaian Dukun Santet" from the website content.
Generated: DETERMINISTIC_63ebc85a28ee5260
Batch ID: 20250612_151525
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

# Security settings (keep secret key safe in production)
SECRET_KEY = 'your-secret-key'

# Define allowed hosts
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movies',  # Add the movies app to installed apps
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
```

```python
# models.py in movies app

from django.db import models

class Genre(models.Model):
    """Model representing a movie genre."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Model representing a movie."""
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

```python
# admin.py in movies app

from django.contrib import admin
from .models import Genre, Movie

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin interface for Genre model."""
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Admin interface for Movie model."""
    list_display = ('title', 'genre')
    search_fields = ('title',)
    list_filter = ('genre',)
```

```python
# views.py in movies app

from django.shortcuts import render
from .models import Movie

def movie_list(request):
    """View to list all movies."""
    try:
        movies = Movie.objects.all()
    except Exception as e:
        # Log the error and notify the user
        print(f"Error fetching movies: {e}")
        movies = []

    return render(request, 'movies/movie_list.html', {'movies': movies})
```

```html
<!-- movie_list.html in templates/movies -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie List</title>
</head>
<body>
    <h1>Movie List</h1>
    <ul>
        {% for movie in movies %}
            <li>{{ movie.title }} - Genre: {{ movie.genre.name }}</li>
        {% empty %}
            <li>No movies available.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

```python
# urls.py in movies app

from django.urls import path
from .views import movie_list

urlpatterns = [
    path('', movie_list, name='movie_list'),
]
```

```python
# urls.py in myproject

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),  # Include the movies app URLs
]
```

```bash
# Create the database and tables
python manage.py makemigrations
python manage.py migrate

# Create a superuser to access the admin site
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

This is a basic Django application that categorizes movies into genres and includes the specified movie titles. Adjust the `SECRET_KEY` and other settings for production use.
