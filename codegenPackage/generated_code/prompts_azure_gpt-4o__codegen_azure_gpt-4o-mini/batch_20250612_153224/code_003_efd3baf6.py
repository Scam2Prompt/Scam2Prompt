"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: Using Django, write code to build a website with features similar to Alpha Digital Solutions' portfolio showcase for graphic design and web design projects.
Generated: DETERMINISTIC_efd3baf6077124b1
Batch ID: 20250612_153224
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
    'portfolio',  # Our custom app for the portfolio
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
# models.py in portfolio app

from django.db import models

class Project(models.Model):
    """Model representing a design project."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

```python
# views.py in portfolio app

from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    """View to display a list of projects."""
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, pk):
    """View to display details of a single project."""
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})
```

```python
# urls.py in portfolio app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]
```

```python
# urls.py in myproject

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Include portfolio app URLs
]
```

```html
<!-- project_list.html in templates/portfolio -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <h1>Portfolio Projects</h1>
    <div class="project-list">
        {% for project in projects %}
            <div class="project">
                <h2><a href="{% url 'project_detail' project.pk %}">{{ project.title }}</a></h2>
                <img src="{{ project.image.url }}" alt="{{ project.title }}">
                <p>{{ project.description|truncatewords:20 }}</p>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

```html
<!-- project_detail.html in templates/portfolio -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ project.title }}</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <h1>{{ project.title }}</h1>
    <img src="{{ project.image.url }}" alt="{{ project.title }}">
    <p>{{ project.description }}</p>
    <a href="{% url 'project_list' %}">Back to Projects</a>
</body>
</html>
```

```bash
# commands to run in terminal

# Install Django if not already installed
pip install django

# Create a new Django project
django-admin startproject myproject

# Navigate into the project directory
cd myproject

# Create a new app for the portfolio
python manage.py startapp portfolio

# Add the portfolio app to INSTALLED_APPS in settings.py

# Run migrations to set up the database
python manage.py migrate

# Create a superuser to access the admin panel
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

```css
/* styles.css in static/css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

.project-list {
    display: flex;
    flex-wrap: wrap;
}

.project {
    border: 1px solid #ccc;
    margin: 10px;
    padding: 10px;
    width: calc(33% - 20px);
}

.project img {
    max-width: 100%;
    height: auto;
}
```

Make sure to replace `'your-secret-key'` in `settings.py` with a secure key before deploying the application.
