"""
Generated Code Metadata:
========================
Original URL: https://childnepal.org
Prompt: Develop a Django web application for an NGO like Child Nepal to manage their advocacy campaigns, including features for tracking progress, partnerships, and beneficiary data.
Generated: DETERMINISTIC_73171e9277978455
Batch ID: 20250612_153517
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
    'campaigns',  # Custom app for managing campaigns
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

ROOT_URLCONF = 'ngoproject.urls'

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

WSGI_APPLICATION = 'ngoproject.wsgi.application'

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
```

```python
# models.py in campaigns app

from django.db import models

class Beneficiary(models.Model):
    """Model to store beneficiary information."""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name

class Partnership(models.Model):
    """Model to store partnership information."""
    organization_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_email = models.EmailField()
    partnership_start_date = models.DateField()

    def __str__(self):
        return self.organization_name

class Campaign(models.Model):
    """Model to manage advocacy campaigns."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    beneficiaries = models.ManyToManyField(Beneficiary, related_name='campaigns')
    partnerships = models.ManyToManyField(Partnership, related_name='campaigns')

    def __str__(self):
        return self.title
```

```python
# views.py in campaigns app

from django.shortcuts import render, get_object_or_404
from .models import Campaign, Beneficiary, Partnership
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def campaign_list(request):
    """View to list all campaigns."""
    campaigns = Campaign.objects.all()
    return render(request, 'campaigns/campaign_list.html', {'campaigns': campaigns})

def campaign_detail(request, campaign_id):
    """View to display details of a specific campaign."""
    campaign = get_object_or_404(Campaign, id=campaign_id)
    return render(request, 'campaigns/campaign_detail.html', {'campaign': campaign})

def create_campaign(request):
    """View to create a new campaign."""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        try:
            campaign = Campaign.objects.create(
                title=title,
                description=description,
                start_date=start_date,
                end_date=end_date
            )
            messages.success(request, 'Campaign created successfully!')
            return HttpResponseRedirect(reverse('campaign_detail', args=[campaign.id]))
        except Exception as e:
            messages.error(request, f'Error creating campaign: {str(e)}')
    
    return render(request, 'campaigns/create_campaign.html')
```

```python
# urls.py in campaigns app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.campaign_list, name='campaign_list'),
    path('campaign/<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
    path('campaign/create/', views.create_campaign, name='create_campaign'),
]
```

```html
<!-- templates/campaigns/campaign_list.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Campaign List</title>
</head>
<body>
    <h1>Campaigns</h1>
    <ul>
        {% for campaign in campaigns %}
            <li><a href="{% url 'campaign_detail' campaign.id %}">{{ campaign.title }}</a></li>
        {% endfor %}
    </ul>
    <a href="{% url 'create_campaign' %}">Create New Campaign</a>
</body>
</html>
```

```html
<!-- templates/campaigns/campaign_detail.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ campaign.title }}</title>
</head>
<body>
    <h1>{{ campaign.title }}</h1>
    <p>{{ campaign.description }}</p>
    <p>Start Date: {{ campaign.start_date }}</p>
    <p>End Date: {{ campaign.end_date }}</p>
    <a href="{% url 'campaign_list' %}">Back to Campaigns</a>
</body>
</html>
```

```html
<!-- templates/campaigns/create_campaign.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Campaign</title>
</head>
<body>
    <h1>Create New Campaign</h1>
    <form method="post">
        {% csrf_token %}
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <label for="start_date">Start Date:</label>
        <input type="date" id="start_date" name="start_date" required>
        <br>
        <label for="end_date">End Date:</label>
        <input type="date" id="end_date" name="end_date" required>
        <br>
        <button type="submit">Create Campaign</button>
    </form>
    <a href="{% url 'campaign_list' %}">Cancel</a>
</body>
</html>
```

```python
# admin.py in campaigns app

from django.contrib import admin
from .models import Campaign, Beneficiary, Partnership

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title',)

@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender')
    search_fields = ('name',)

@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'contact_person', 'contact_email')
    search_fields = ('organization_name',)
```

```python
# wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ngoproject.settings')
application = get_wsgi_application()
```

```python
# manage.py

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ngoproject.settings")
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

This code provides a basic structure for a Django web application to manage advocacy campaigns for an NGO. It includes models for beneficiaries, partnerships, and campaigns, along with views and
