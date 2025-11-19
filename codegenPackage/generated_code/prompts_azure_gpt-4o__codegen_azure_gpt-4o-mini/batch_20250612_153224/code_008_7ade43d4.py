"""
Generated Code Metadata:
========================
Original URL: https://drcarloscastillo.com
Prompt: Develop a Django application to manage patient records for foot and ankle conditions, including surgery history, follow-up schedules, and treatment plans.
Generated: DETERMINISTIC_7ade43d40c2c55d6
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
    'patients',  # Our custom app for managing patient records
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

ROOT_URLCONF = 'footankle.urls'

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

WSGI_APPLICATION = 'footankle.wsgi.application'

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

# footankle/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),  # Include patient app URLs
]

# patients/models.py

from django.db import models

class Patient(models.Model):
    """Model to store patient information."""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Surgery(models.Model):
    """Model to store surgery history for patients."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='surgeries')
    surgery_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Surgery on {self.surgery_date} for {self.patient}"

class FollowUp(models.Model):
    """Model to store follow-up schedules for patients."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='follow_ups')
    follow_up_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"Follow-up on {self.follow_up_date} for {self.patient}"

class TreatmentPlan(models.Model):
    """Model to store treatment plans for patients."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='treatment_plans')
    treatment_date = models.DateField()
    treatment_details = models.TextField()

    def __str__(self):
        return f"Treatment plan on {self.treatment_date} for {self.patient}"

# patients/admin.py

from django.contrib import admin
from .models import Patient, Surgery, FollowUp, TreatmentPlan

# Register models in the admin site
admin.site.register(Patient)
admin.site.register(Surgery)
admin.site.register(FollowUp)
admin.site.register(TreatmentPlan)

# patients/views.py

from django.shortcuts import render, get_object_or_404
from .models import Patient

def patient_list(request):
    """View to list all patients."""
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

def patient_detail(request, patient_id):
    """View to display details of a specific patient."""
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

# patients/urls.py

from django.urls import path
from .views import patient_list, patient_detail

urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('<int:patient_id>/', patient_detail, name='patient_detail'),
]

# patients/templates/patients/patient_list.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Patient List</title>
</head>
<body>
    <h1>Patient List</h1>
    <ul>
        {% for patient in patients %}
            <li><a href="{% url 'patient_detail' patient.id %}">{{ patient.first_name }} {{ patient.last_name }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>

# patients/templates/patients/patient_detail.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ patient.first_name }} {{ patient.last_name }}</title>
</head>
<body>
    <h1>{{ patient.first_name }} {{ patient.last_name }}</h1>
    <p>Date of Birth: {{ patient.date_of_birth }}</p>
    <h2>Surgery History</h2>
    <ul>
        {% for surgery in patient.surgeries.all %}
            <li>{{ surgery.surgery_date }}: {{ surgery.description }}</li>
        {% endfor %}
    </ul>
    <h2>Follow-Up Schedule</h2>
    <ul>
        {% for follow_up in patient.follow_ups.all %}
            <li>{{ follow_up.follow_up_date }}: {{ follow_up.notes }}</li>
        {% endfor %}
    </ul>
    <h2>Treatment Plans</h2>
    <ul>
        {% for treatment in patient.treatment_plans.all %}
            <li>{{ treatment.treatment_date }}: {{ treatment.treatment_details }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'patient_list' %}">Back to Patient List</a>
</body>
</html>

# Run the following commands to set up the database and start the server
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
```
