"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alpha-digitalsolutions.com
Prompt: Using Django, write code to build a website with features similar to Alpha Digital Solutions' portfolio showcase for graphic design and web design projects.
Generated: DETERMINISTIC_efd3baf6077124b1
Batch ID: 20250612_153224
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
Django settings for myportfolio project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your_default_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',  # Custom app for portfolio
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

ROOT_URLCONF = 'myportfolio.urls'

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

WSGI_APPLICATION = 'myportfolio.wsgi.application'

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


# portfolio/models.py
"""
Models for the portfolio app.
"""

from django.db import models


class Project(models.Model):
    """
    Model to represent a design project.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# portfolio/views.py
"""
Views for the portfolio app.
"""

from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
    """
    View to display the list of projects.
    """
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})


def project_detail(request, pk):
    """
    View to display the detail of a single project.
    """
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})


# portfolio/urls.py
"""
URL configurations for the portfolio app.
"""

from django.urls import path
from .views import project_list, project_detail

urlpatterns = [
    path('', project_list, name='project_list'),
    path('project/<int:pk>/', project_detail, name='project_detail'),
]


# myportfolio/urls.py
"""
Main URL configurations for the project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Include portfolio URLs
]


# templates/portfolio/project_list.html
"""
Template for listing projects.
"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Portfolio</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
</head>
<body>
    <h1>My Portfolio</h1>
    <div class="projects">
        {% for project in projects %}
            <div class="project">
                <h2><a href="{% url 'project_detail' project.pk %}">{{ project.title }}</a></h2>
                <img src="{{ project.image.url }}" alt="{{ project.title }}">
                <p>{{ project.description }}</p>
            </div>
        {% endfor %}
    </div>
</body>
</html>


# templates/portfolio/project_detail.html
"""
Template for showing project details.
"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ project.title }}</title>
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
</head>
<body>
    <h1>{{ project.title }}</h1>
    <img src="{{ project.image.url }}" alt="{{ project.title }}">
    <p>{{ project.description }}</p>
    <a href="{% url 'project_list' %}">Back to portfolio</a>
</body>
</html>


# portfolio/admin.py
"""
Admin configurations for the portfolio app.
"""

from django.contrib import admin
from .models import Project

admin.site.register(Project)
```

### Additional Notes:
- Ensure you have `Pillow` installed for image handling: `pip install Pillow`.
- Create a directory named `templates` in your project root and another directory named `portfolio` inside `templates` to store the HTML files.
- Create a `static/css/styles.css` file for styling your templates.
- Set up your environment variables for `SECRET_KEY` and `DEBUG` in a production setting.
