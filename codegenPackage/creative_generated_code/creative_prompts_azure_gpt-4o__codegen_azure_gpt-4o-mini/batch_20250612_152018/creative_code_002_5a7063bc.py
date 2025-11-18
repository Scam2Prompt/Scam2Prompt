"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://darulraza.net
Prompt: Develop a Django-based web application that integrates an online Quran learning module, inspired by Darul Raza's Hifz and Nazra services.
Generated: DETERMINISTIC_5a7063bc7431152c
Batch ID: 20250612_152018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# settings.py

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

SECRET_KEY = 'your-secret-key'  # Replace with your actual secret key
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
    'quran_learning',  # Our custom application
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

ROOT_URLCONF = 'quran_learning_project.urls'

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

WSGI_APPLICATION = 'quran_learning_project.wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

# Custom user model if needed (optional)
# AUTH_USER_MODEL = 'yourapp.CustomUser'
```

```python
# models.py in quran_learning app

from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    """Model representing a Quran lesson."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    """Model representing an enrollment in a lesson."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user.username} enrolled in {self.lesson.title}"
```

```python
# views.py in quran_learning app

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lesson, Enrollment

@login_required
def lesson_list(request):
    """View to list all Quran lessons."""
    lessons = Lesson.objects.all()
    return render(request, 'quran_learning/lesson_list.html', {'lessons': lessons})

@login_required
def enroll_in_lesson(request, lesson_id):
    """View to enroll a user in a specific lesson."""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    Enrollment.objects.get_or_create(user=request.user, lesson=lesson)
    return redirect('lesson_list')
```

```python
# urls.py in quran_learning app

from django.urls import path
from .views import lesson_list, enroll_in_lesson

urlpatterns = [
    path('', lesson_list, name='lesson_list'),
    path('enroll/<int:lesson_id>/', enroll_in_lesson, name='enroll_in_lesson'),
]
```

```html
<!-- lesson_list.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quran Lessons</title>
</head>
<body>
    <h1>Available Quran Lessons</h1>
    <ul>
        {% for lesson in lessons %}
            <li>
                <strong>{{ lesson.title }}</strong>: {{ lesson.description }}
                <a href="{% url 'enroll_in_lesson' lesson.id %}">Enroll</a>
            </li>
        {% empty %}
            <li>No lessons available.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

```python
# admin.py in quran_learning app

from django.contrib import admin
from .models import Lesson, Enrollment

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'enrolled_at')
```

```python
# wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quran_learning_project.settings')
application = get_wsgi_application()
```

```python
# manage.py

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quran_learning_project.settings")
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

```bash
# instructions for commands to run in terminal

# Create the Django project
django-admin startproject quran_learning_project

# Navigate into the project directory
cd quran_learning_project

# Create a new app for Quran learning
python manage.py startapp quran_learning

# Apply migrations
python manage.py migrate

# Create a superuser for accessing the admin site
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Make sure to replace `'your-secret-key'` with a secure key and set the appropriate configurations in the `settings.py` file before deploying the application.
