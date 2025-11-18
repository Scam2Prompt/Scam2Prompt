"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.icyd.org
Prompt: Develop a Django application to manage and report on youth development initiatives, inspired by the collaborative goals of ICYD.org.
Generated: DETERMINISTIC_4479412f453929c3
Batch ID: 20250612_145421
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

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'initiatives',  # Our app for managing youth initiatives
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

ROOT_URLCONF = 'youth_development.urls'

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

WSGI_APPLICATION = 'youth_development.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'youth_development'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# models.py (in initiatives app)

from django.db import models

class Initiative(models.Model):
    """Model to represent a youth development initiative"""
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Report(models.Model):
    """Model to represent a report associated with an initiative"""
    
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, related_name='reports')
    date = models.DateField()
    content = models.TextField()

    class Meta:
        unique_together = ('initiative', 'date')  # Prevent duplicate reports for the same initiative/date

    def __str__(self):
        return f'Report for {self.initiative.title} on {self.date}'
```

```python
# views.py (in initiatives app)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Initiative, Report
from .forms import InitiativeForm, ReportForm

def initiative_list(request):
    """View to list all initiatives"""
    initiatives = Initiative.objects.all()
    return render(request, 'initiatives/initiative_list.html', {'initiatives': initiatives})

def initiative_detail(request, pk):
    """View to detail a single initiative and its reports"""
    initiative = get_object_or_404(Initiative, pk=pk)
    reports = initiative.reports.all()
    return render(request, 'initiatives/initiative_detail.html', {'initiative': initiative, 'reports': reports})

def initiative_create(request):
    """View to create a new initiative"""
    if request.method == "POST":
        form = InitiativeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('initiative_list')
    else:
        form = InitiativeForm()
    return render(request, 'initiatives/initiative_form.html', {'form': form})

def report_create(request, initiative_pk):
    """View to create a report for a specific initiative"""
    initiative = get_object_or_404(Initiative, pk=initiative_pk)
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.initiative = initiative
            report.save()
            return redirect('initiative_detail', pk=initiative.pk)
    else:
        form = ReportForm()
    return render(request, 'initiatives/report_form.html', {'form': form, 'initiative': initiative})
```

```python
# forms.py (in initiatives app)

from django import forms
from .models import Initiative, Report

class InitiativeForm(forms.ModelForm):
    """Form for creating and updating initiatives"""
    
    class Meta:
        model = Initiative
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ReportForm(forms.ModelForm):
    """Form for creating and updating reports"""
    
    class Meta:
        model = Report
        fields = ['date', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
```

```python
# urls.py (in initiatives app)

from django.urls import path
from .views import initiative_list, initiative_detail, initiative_create, report_create

urlpatterns = [
    path('', initiative_list, name='initiative_list'),
    path('initiative/<int:pk>/', initiative_detail, name='initiative_detail'),
    path('initiative/create/', initiative_create, name='initiative_create'),
    path('initiative/<int:initiative_pk>/report/create/', report_create, name='report_create'),
]
```

```python
# urls.py (in youth_development project)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('initiatives/', include('initiatives.urls')),  # Include initiatives app URLs
]
```

```html
<!-- templates/initiatives/initiative_list.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Initiatives</title>
</head>
<body>
<h1>Youth Development Initiatives</h1>
<a href="{% url 'initiative_create' %}">Create New Initiative</a>
<ul>
    {% for initiative in initiatives %}
        <li>
            <a href="{% url 'initiative_detail' initiative.pk %}">{{ initiative.title }}</a>
        </li>
    {% endfor %}
</ul>
</body>
</html>
```

```html
<!-- templates/initiatives/initiative_detail.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ initiative.title }}</title>
</head>
<body>
<h1>{{ initiative.title }}</h1>
<p>{{ initiative.description }}</p>

<h2>Reports</h2>
<ul>
    {% for report in reports %}
        <li>{{ report.date }}: {{ report.content }}</li>
    {% endfor %}
</ul>

<a href="{% url 'report_create' initiative.pk %}">Add Report</a>
<a href="{% url 'initiative_list' %}">Back to list</a>
</body>
</html>
```

```html
<!-- templates/initiatives/initiative_form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Initiative</title>
</head>
<body>
<h1>Create Initiative</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
<a href="{% url 'initiative_list' %}">Back to list</a>
</body>
</html>
```

```html
<!-- templates/initiatives/report_form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Report</title>
</head>
<body>
<h1>Add Report for {{ initiative.title }}</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
<a href="{% url 'initiative_detail' initiative.pk %}">Back to initiative</a>
</body>
</html>
```

```bash
# Run the following commands to initialize the project
django-admin startproject youth_development
cd youth_development
python manage.py startapp initiatives
```

```bash
# After creating the application structure, run these commands to set up the database and start the server
