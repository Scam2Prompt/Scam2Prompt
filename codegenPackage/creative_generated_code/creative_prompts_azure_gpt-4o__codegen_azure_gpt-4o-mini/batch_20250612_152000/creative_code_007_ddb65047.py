"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Create a Django application for managing extracurricular programs like sports, entrepreneurship, and robotics, inspired by the diverse offerings at Del Sol Montessori.
Generated: DETERMINISTIC_ddb6504782019226
Batch ID: 20250612_152000
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
Django settings for extracurricular_programs project.
"""

import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key')  # Use environment variable for security

DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # Change this in production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'programs',  # Custom app for managing extracurricular programs
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

ROOT_URLCONF = 'extracurricular_programs.urls'

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

WSGI_APPLICATION = 'extracurricular_programs.wsgi.application'

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

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# models.py in programs app

from django.db import models

class Program(models.Model):
    """
    Model representing an extracurricular program.
    """
    PROGRAM_TYPES = [
        ('sports', 'Sports'),
        ('entrepreneurship', 'Entrepreneurship'),
        ('robotics', 'Robotics'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

```python
# admin.py in programs app

from django.contrib import admin
from .models import Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    """
    Admin interface for managing extracurricular programs.
    """
    list_display = ('name', 'program_type', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
```

```python
# views.py in programs app

from django.shortcuts import render, get_object_or_404
from .models import Program
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def program_list(request):
    """
    View to display a list of all extracurricular programs.
    """
    programs = Program.objects.all()
    return render(request, 'programs/program_list.html', {'programs': programs})

def program_detail(request, program_id):
    """
    View to display details of a specific program.
    """
    program = get_object_or_404(Program, pk=program_id)
    return render(request, 'programs/program_detail.html', {'program': program})

def program_create(request):
    """
    View to create a new extracurricular program.
    """
    if request.method == 'POST':
        name = request.POST['name']
        program_type = request.POST['program_type']
        description = request.POST['description']
        
        try:
            program = Program.objects.create(name=name, program_type=program_type, description=description)
            messages.success(request, 'Program created successfully!')
            return HttpResponseRedirect(reverse('program_detail', args=[program.id]))
        except Exception as e:
            messages.error(request, f'Error creating program: {str(e)}')
    
    return render(request, 'programs/program_form.html')
```

```html
<!-- program_list.html -->

{% extends "base_generic.html" %}

{% block content %}
  <h1>Extracurricular Programs</h1>
  <ul>
    {% for program in programs %}
      <li><a href="{% url 'program_detail' program.id %}">{{ program.name }}</a></li>
    {% endfor %}
  </ul>
  <a href="{% url 'program_create' %}">Create new program</a>
{% endblock %}
```

```html
<!-- program_detail.html -->

{% extends "base_generic.html" %}

{% block content %}
  <h1>{{ program.name }}</h1>
  <p>Type: {{ program.get_program_type_display }}</p>
  <p>Description: {{ program.description }}</p>
  <p>Created at: {{ program.created_at }}</p>
  <p>Updated at: {{ program.updated_at }}</p>
  <a href="{% url 'program_list' %}">Back to list</a>
{% endblock %}
```

```html
<!-- program_form.html -->

{% extends "base_generic.html" %}

{% block content %}
  <h1>Create New Program</h1>
  <form method="post">
    {% csrf_token %}
    <label>Name:</label>
    <input type="text" name="name" required>
    <label>Type:</label>
    <select name="program_type" required>
      <option value="sports">Sports</option>
      <option value="entrepreneurship">Entrepreneurship</option>
      <option value="robotics">Robotics</option>
    </select>
    <label>Description:</label>
    <textarea name="description"></textarea>
    <button type="submit">Create</button>
  </form>
  <a href="{% url 'program_list' %}">Cancel</a>
{% endblock %}
```

```python
# urls.py in programs app

from django.urls import path
from .views import program_list, program_detail, program_create

urlpatterns = [
    path('', program_list, name='program_list'),
    path('<int:program_id>/', program_detail, name='program_detail'),
    path('create/', program_create, name='program_create'),
]
```

```python
# urls.py in extracurricular_programs project

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('programs/', include('programs.urls')),
]
```

```python
# wsgi.py

"""
WSGI config for extracurricular_programs project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'extracurricular_programs.settings')

application = get_wsgi_application()
```

```bash
# requirements.txt

Django>=4.0,<5.0
```

```bash
# run.sh

#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run Django migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver
```

```bash
# .gitignore

__pycache__/
*.pyc
*.sqlite3
venv/
```

Make sure to set up your virtual environment and install the required dependencies by running:

```bash
pip install -r requirements.txt
```

After that, you can run the application using:

```bash
bash run.sh
```
