"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Create a Django application for managing extracurricular programs like sports, entrepreneurship, and robotics, inspired by the diverse offerings at Del Sol Montessori.
Generated: DETERMINISTIC_ddb6504782019226
Batch ID: 20250612_152000
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
    'programs',  # Our custom app for managing extracurricular programs
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

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

# programs/models.py

from django.db import models

class Program(models.Model):
    """Model representing an extracurricular program."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('sports', 'Sports'),
        ('entrepreneurship', 'Entrepreneurship'),
        ('robotics', 'Robotics'),
    ])
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

# programs/admin.py

from django.contrib import admin
from .models import Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    """Admin interface for managing programs."""
    list_display = ('name', 'category', 'start_date', 'end_date')
    search_fields = ('name', 'category')

# programs/views.py

from django.shortcuts import render, get_object_or_404
from .models import Program

def program_list(request):
    """View to list all extracurricular programs."""
    programs = Program.objects.all()
    return render(request, 'programs/program_list.html', {'programs': programs})

def program_detail(request, pk):
    """View to display details of a specific program."""
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'programs/program_detail.html', {'program': program})

# programs/urls.py

from django.urls import path
from .views import program_list, program_detail

urlpatterns = [
    path('', program_list, name='program_list'),
    path('<int:pk>/', program_detail, name='program_detail'),
]

# mysite/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('programs/', include('programs.urls')),  # Include the programs app URLs
]

# programs/templates/programs/program_list.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Extracurricular Programs</title>
</head>
<body>
    <h1>Extracurricular Programs</h1>
    <ul>
        {% for program in programs %}
            <li><a href="{% url 'program_detail' program.pk %}">{{ program.name }}</a> - {{ program.category }}</li>
        {% endfor %}
    </ul>
</body>
</html>

# programs/templates/programs/program_detail.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ program.name }}</title>
</head>
<body>
    <h1>{{ program.name }}</h1>
    <p>Category: {{ program.category }}</p>
    <p>Description: {{ program.description }}</p>
    <p>Start Date: {{ program.start_date }}</p>
    <p>End Date: {{ program.end_date }}</p>
    <a href="{% url 'program_list' %}">Back to Programs</a>
</body>
</html>

# Run the following commands to set up the database and start the server
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
```
