"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jinlinghospital.com
Prompt: Develop a Django application to manage Jinling Hospital’s maternity and women’s health services, including prenatal care scheduling, postpartum support tracking, and patient feedback collection.
Generated: DETERMINISTIC_7aed6778c7e4aa52
Batch ID: 20250612_151024
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.0/ref/settings/#databases": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.0/howto/static-files/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://docs.djangoproject.com/en/4.0/topics/i18n/": {
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
"""
Django settings for Jinling Hospital Maternity Services project.
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')

DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'maternity',  # Our custom app for maternity services
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

ROOT_URLCONF = 'jinling_hospital.urls'

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

WSGI_APPLICATION = 'jinling_hospital.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

```python
# models.py
"""
Models for the Maternity app to represent prenatal care scheduling,
postpartum support tracking, and patient feedback collection.
"""
from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    """
    Model representing a patient in the maternity services.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username


class PrenatalCare(models.Model):
    """
    Model representing a prenatal care appointment.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Prenatal care for {self.patient.user.username} on {self.appointment_date}"


class PostpartumSupport(models.Model):
    """
    Model to track postpartum support for patients.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    support_date = models.DateTimeField()
    feedback = models.TextField()

    def __str__(self):
        return f"Postpartum support for {self.patient.user.username} on {self.support_date}"


class PatientFeedback(models.Model):
    """
    Model to collect feedback from patients.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    feedback_date = models.DateTimeField(auto_now_add=True)
    feedback_text = models.TextField()

    def __str__(self):
        return f"Feedback from {self.patient.user.username} on {self.feedback_date}"
```

```python
# admin.py
"""
Admin configuration for the Maternity app models.
"""
from django.contrib import admin
from .models import Patient, PrenatalCare, PostpartumSupport, PatientFeedback

class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')

class PrenatalCareAdmin(admin.ModelAdmin):
    list_display = ('patient', 'appointment_date')

class PostpartumSupportAdmin(admin.ModelAdmin):
    list_display = ('patient', 'support_date')

class PatientFeedbackAdmin(admin.ModelAdmin):
    list_display = ('patient', 'feedback_date',)

admin.site.register(Patient, PatientAdmin)
admin.site.register(PrenatalCare, PrenatalCareAdmin)
admin.site.register(PostpartumSupport, PostpartumSupportAdmin)
admin.site.register(PatientFeedback, PatientFeedbackAdmin)
```

```python
# views.py
"""
Views for handling requests related to maternity services.
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Patient, PrenatalCare, PostpartumSupport, PatientFeedback
from django.contrib.auth.decorators import login_required

@login_required
def schedule_prenatal_care(request):
    """
    View to schedule a prenatal care appointment.
    """
    if request.method == 'POST':
        appointment_date = request.POST.get('appointment_date')
        notes = request.POST.get('notes')
        patient = request.user.patient

        # Error handling for missing data
        if not appointment_date:
            return HttpResponse("Appointment date is required.", status=400)

        PrenatalCare.objects.create(patient=patient, appointment_date=appointment_date, notes=notes)
        return redirect('success_view')  # Replace with actual success URL

    return render(request, 'schedule_prenatal_care.html')


@login_required
def provide_postpartum_support(request):
    """
    View to track postpartum support.
    """
    if request.method == 'POST':
        support_date = request.POST.get('support_date')
        feedback = request.POST.get('feedback')
        patient = request.user.patient

        # Error handling for missing data
        if not support_date or not feedback:
            return HttpResponse("Support date and feedback are required.", status=400)

        PostpartumSupport.objects.create(patient=patient, support_date=support_date, feedback=feedback)
        return redirect('success_view')  # Replace with actual success URL

    return render(request, 'provide_postpartum_support.html')


@login_required
def collect_patient_feedback(request):
    """
    View to collect feedback from patients.
    """
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback_text')
        patient = request.user.patient

        # Error handling for missing feedback
        if not feedback_text:
            return HttpResponse("Feedback text is required.", status=400)

        PatientFeedback.objects.create(patient=patient, feedback_text=feedback_text)
        return redirect('success_view')  # Replace with actual success URL

    return render(request, 'collect_patient_feedback.html')
```

```python
# urls.py
"""
URL configuration for the Maternity app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('schedule-prenatal/', views.schedule_prenatal_care, name='schedule_prenatal'),
    path('postpartum-support/', views.provide_postpartum_support, name='postpartum_support'),
    path('feedback/', views.collect_patient_feedback, name='collect_feedback'),
]
```

```html
<!-- schedule_prenatal_care.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Schedule Prenatal Care</title>
</head>
<body>
    <h1>Schedule Prenatal Care</h1>
    <form method="POST">
        {% csrf_token %}
        <label for="appointment_date">Appointment Date:</label>
        <input type="datetime-local" name="appointment_date" required>
        <label for="notes">Notes:</label>
        <textarea name="notes"></textarea>
        <button type="submit">Schedule</button>
    </form>
</body>
</html>
```

```html
<!-- provide_postpartum_support.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Provide Postpartum Support</title>
</head>
<body>
    <h1>Provide Postpartum Support</h1>
    <form method="POST">
        {% csrf_token %}
        <label for="support_date">Support Date:</label>
        <input type="datetime-local" name="support_date" required>
        <label for="feedback">Feedback:</label>
        <textarea name="feedback" required></textarea>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

```html
