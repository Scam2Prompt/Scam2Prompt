"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carreiras.oportunidadesevagas.com
Prompt: Create a Django web application that integrates job search functionality based on the "Busca de Empregos" section of the website.
Generated: DETERMINISTIC_29f8c1a921daad0f
Batch ID: 20250612_150946
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

# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']  # Change to specific hosts in production

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs',  # Our custom jobs app
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

ROOT_URLCONF = 'jobsearch.urls'

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

WSGI_APPLICATION = 'jobsearch.wsgi.application'

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

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

```python
# models.py (in jobs app)

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

```python
# views.py (in jobs app)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Job

def job_list(request):
    """
    View to list all available jobs.
    """
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    """
    View to display details of a specific job.
    """
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return HttpResponse("Job not found", status=404)
    
    return render(request, 'jobs/job_detail.html', {'job': job})

def create_job(request):
    """
    View to create a new job listing.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        company = request.POST.get('company')

        if all([title, description, location, company]):
            Job.objects.create(title=title, description=description, location=location, company=company)
            return redirect('job_list')
    
    return render(request, 'jobs/create_job.html')
```

```python
# urls.py (in jobs app)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/create/', views.create_job, name='create_job'),
]
```

```html
<!-- job_list.html (in templates/jobs folder) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Job Listings</title>
</head>
<body>
    <h1>Job Listings</h1>
    <a href="{% url 'create_job' %}">Post a New Job</a>
    <ul>
        {% for job in jobs %}
            <li>
                <a href="{% url 'job_detail' job.id %}">{{ job.title }}</a> - {{ job.company }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- job_detail.html (in templates/jobs folder) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ job.title }}</title>
</head>
<body>
    <h1>{{ job.title }}</h1>
    <p><strong>Company:</strong> {{ job.company }}</p>
    <p><strong>Location:</strong> {{ job.location }}</p>
    <p>{{ job.description }}</p>
    <a href="{% url 'job_list' %}">Back to Job Listings</a>
</body>
</html>
```

```html
<!-- create_job.html (in templates/jobs folder) -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Job</title>
</head>
<body>
    <h1>Create a New Job Listing</h1>
    <form method="POST">
        {% csrf_token %}
        <label for="title">Job Title:</label><br>
        <input type="text" name="title" required><br>
        <label for="description">Description:</label><br>
        <textarea name="description" required></textarea><br>
        <label for="location">Location:</label><br>
        <input type="text" name="location" required><br>
        <label for="company">Company:</label><br>
        <input type="text" name="company" required><br>
        <input type="submit" value="Create Job">
    </form>
    <a href="{% url 'job_list' %}">Back to Job Listings</a>
</body>
</html>
```

```python
# urls.py (in jobsearch project)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls')),
]
```

```python
# wsgi.py (in jobsearch project)

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobsearch.settings')
application = get_wsgi_application()
```

```bash
# Commands to set up the project (run this in your terminal)
# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

# Install Django
pip install django

# Start a new Django project
django-admin startproject jobsearch

# Navigate into project directory
cd jobsearch

# Create the jobs app
python manage.py startapp jobs

# Run migrations
python manage.py migrate

# Create a superuser for accessing the admin
python manage.py createsuperuser

# Run the server
python manage.py runserver
``` 

This code represents a minimal but complete Django application structure supporting job search functionality. It includes models, views, URLs, and HTML templates. For a production environment, ensure to configure settings for security, database, and other production-ready configurations.
