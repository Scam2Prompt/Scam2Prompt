"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Develop a Django application to manage and report on youth development initiatives, inspired by the collaborative goals of ICYD.org.
Generated: DETERMINISTIC_4479412f453929c3
Batch ID: 20250612_145421
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.1/topics/i18n/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.1/howto/static-files/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.1/ref/settings/#databases": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**youth_development_initiatives/settings.py**
```python
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your_secret_key_here'

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
    'initiatives',
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

ROOT_URLCONF = 'youth_development_initiatives.urls'

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

WSGI_APPLICATION = 'youth_development_initiatives.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

**youth_development_initiatives/urls.py**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('initiatives.urls')),
]
```

**initiatives/models.py**
```python
from django.db import models
from django.contrib.auth.models import User

class Initiative(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='initiatives_created')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Participant(models.Model):
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='initiatives_participated')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.initiative.title}'

class Report(models.Model):
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, related_name='reports')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_created')
    report_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report for {self.initiative.title} on {self.report_date}'
```

**initiatives/admin.py**
```python
from django.contrib import admin
from .models import Initiative, Participant, Report

admin.site.register(Initiative)
admin.site.register(Participant)
admin.site.register(Report)
```

**initiatives/views.py**
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Initiative, Participant, Report
from .forms import InitiativeForm, ReportForm

def index(request):
    initiatives = Initiative.objects.all()
    return render(request, 'initiatives/index.html', {'initiatives': initiatives})

@login_required
def create_initiative(request):
    if request.method == 'POST':
        form = InitiativeForm(request.POST)
        if form.is_valid():
            initiative = form.save(commit=False)
            initiative.created_by = request.user
            initiative.save()
            return redirect('initiatives:index')
    else:
        form = InitiativeForm()
    return render(request, 'initiatives/create_initiative.html', {'form': form})

@login_required
def join_initiative(request, pk):
    initiative = Initiative.objects.get(pk=pk)
    participant = Participant.objects.filter(initiative=initiative, user=request.user)
    if not participant.exists():
        Participant.objects.create(initiative=initiative, user=request.user)
    return redirect('initiatives:index')

@login_required
def create_report(request, pk):
    initiative = Initiative.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.initiative = initiative
            report.user = request.user
            report.save()
            return redirect('initiatives:index')
    else:
        form = ReportForm()
    return render(request, 'initiatives/create_report.html', {'form': form, 'initiative': initiative})
```

**initiatives/forms.py**
```python
from django import forms
from .models import Initiative, Report

class InitiativeForm(forms.ModelForm):
    class Meta:
        model = Initiative
        fields = ('title', 'description', 'start_date', 'end_date')

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('report_date', 'description')
```

**initiatives/urls.py**
```python
from django.urls import path
from . import views

app_name = 'initiatives'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_initiative, name='create_initiative'),
    path('<pk>/join/', views.join_initiative, name='join_initiative'),
    path('<pk>/report/', views.create_report, name='create_report'),
]
```

**initiatives/templates/initiatives/index.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Initiatives</h1>
  <ul>
    {% for initiative in initiatives %}
      <li>
        {{ initiative.title }} ({{ initiative.start_date }} - {{ initiative.end_date }})
        <a href="{% url 'initiatives:join_initiative' initiative.pk %}">Join</a>
        <a href="{% url 'initiatives:create_report' initiative.pk %}">Create Report</a>
      </li>
    {% empty %}
      <li>No initiatives found.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'initiatives:create_initiative' %}">Create Initiative</a></p>
{% endblock %}
```

**initiatives/templates/initiatives/create_initiative.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create Initiative</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
{% endblock %}
```

**initiatives/templates/initiatives/create_report.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create Report for {{ initiative.title }}</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
{% endblock %}
```
