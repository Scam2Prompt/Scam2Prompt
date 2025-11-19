"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Develop a Django-based web application that integrates an online Quran learning module, inspired by Darul Raza's Hifz and Nazra services.
Generated: DETERMINISTIC_5a7063bc7431152c
Batch ID: 20250612_152018
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
    'quran_learning',  # Our custom app for Quran learning
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

WSGI_APPLICATION = 'quran_learning_project.wsgi.application'

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
# models.py in quran_learning app

from django.db import models

class Lesson(models.Model):
    """Model representing a Quran lesson."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    """Model representing a student learning the Quran."""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    lessons = models.ManyToManyField(Lesson, related_name='students')

    def __str__(self):
        return self.name
```

```python
# views.py in quran_learning app

from django.shortcuts import render, redirect
from .models import Lesson, Student
from .forms import StudentForm

def lesson_list(request):
    """View to list all Quran lessons."""
    lessons = Lesson.objects.all()
    return render(request, 'quran_learning/lesson_list.html', {'lessons': lessons})

def register_student(request):
    """View to register a new student."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = StudentForm()
    return render(request, 'quran_learning/register_student.html', {'form': form})
```

```python
# forms.py in quran_learning app

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    """Form for registering a new student."""
    class Meta:
        model = Student
        fields = ['name', 'email']
```

```html
<!-- lesson_list.html in templates/quran_learning -->

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
            <li>{{ lesson.title }}: {{ lesson.description }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'register_student' %}">Register as a Student</a>
</body>
</html>
```

```html
<!-- register_student.html in templates/quran_learning -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register Student</title>
</head>
<body>
    <h1>Register as a Student</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
    <a href="{% url 'lesson_list' %}">Back to Lessons</a>
</body>
</html>
```

```python
# urls.py in quran_learning_project

from django.contrib import admin
from django.urls import path
from quran_learning import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lesson_list, name='lesson_list'),
    path('register/', views.register_student, name='register_student'),
]
```

```python
# wsgi.py in quran_learning_project

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quran_learning_project.settings')
application = get_wsgi_application()
```

```bash
# requirements.txt

Django>=3.2,<4.0
```

```bash
# Run the following commands to set up the project
django-admin startproject quran_learning_project
cd quran_learning_project
django-admin startapp quran_learning
```

```bash
# After creating the files, run the following commands to set up the database and start the server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

This code provides a basic structure for a Django-based web application that integrates an online Quran learning module. It includes models, views, forms, templates, and URL routing, following best practices and including error handling where appropriate.
