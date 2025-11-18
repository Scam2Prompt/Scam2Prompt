"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcarloscastillo.com
Prompt: Develop a Django application to manage patient records for foot and ankle conditions, including surgery history, follow-up schedules, and treatment plans.
Generated: DETERMINISTIC_7ade43d40c2c55d6
Batch ID: 20250612_153224
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
Django settings for patient_records project.
"""

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
    'patients',  # Our custom app
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

ROOT_URLCONF = 'patient_records.urls'

# Templates configuration
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

WSGI_APPLICATION = 'patient_records.wsgi.application'

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

# Custom User Model Setting
AUTH_USER_MODEL = 'auth.User'
```

```python
# models.py

from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    """
    Model representing a patient with foot and ankle conditions.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SurgeryHistory(models.Model):
    """
    Model representing a patient's surgery history.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='surgeries')
    surgery_date = models.DateField()
    surgery_description = models.TextField()
    
    def __str__(self):
        return f"Surgery on {self.surgery_date} for {self.patient}"

class FollowUpSchedule(models.Model):
    """
    Model representing follow-up schedules for patients.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='follow_ups')
    follow_up_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Follow-up for {self.patient} on {self.follow_up_date}"

class TreatmentPlan(models.Model):
    """
    Model representing a treatment plan for a patient.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='treatment_plans')
    treatment_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Treatment plan for {self.patient} from {self.start_date} to {self.end_date}"
```

```python
# admin.py

from django.contrib import admin
from .models import Patient, SurgeryHistory, FollowUpSchedule, TreatmentPlan

class SurgeryHistoryInline(admin.TabularInline):
    model = SurgeryHistory
    extra = 1

class FollowUpScheduleInline(admin.TabularInline):
    model = FollowUpSchedule
    extra = 1

class TreatmentPlanInline(admin.TabularInline):
    model = TreatmentPlan
    extra = 1

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    inlines = [SurgeryHistoryInline, FollowUpScheduleInline, TreatmentPlanInline]

@admin.register(SurgeryHistory)
class SurgeryHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'surgery_date', 'surgery_description')

@admin.register(FollowUpSchedule)
class FollowUpScheduleAdmin(admin.ModelAdmin):
    list_display = ('patient', 'follow_up_date', 'notes')

@admin.register(TreatmentPlan)
class TreatmentPlanAdmin(admin.ModelAdmin):
    list_display = ('patient', 'treatment_description', 'start_date', 'end_date')
```

```python
# views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Patient, SurgeryHistory, FollowUpSchedule, TreatmentPlan
from .forms import PatientForm, SurgeryHistoryForm, FollowUpScheduleForm, TreatmentPlanForm

def patient_list(request):
    """
    View to list all patients.
    """
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

def patient_detail(request, patient_id):
    """
    View to display details of a specific patient.
    """
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

def add_patient(request):
    """
    View to add a new patient.
    """
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('patient_list'))
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})
```

```python
# forms.py

from django import forms
from .models import Patient, SurgeryHistory, FollowUpSchedule, TreatmentPlan

class PatientForm(forms.ModelForm):
    """
    Form for creating and updating patient records.
    """
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth']

class SurgeryHistoryForm(forms.ModelForm):
    """
    Form for creating and updating surgery history records.
    """
    class Meta:
        model = SurgeryHistory
        fields = ['surgery_date', 'surgery_description']

class FollowUpScheduleForm(forms.ModelForm):
    """
    Form for creating and updating follow-up schedules.
    """
    class Meta:
        model = FollowUpSchedule
        fields = ['follow_up_date', 'notes']

class TreatmentPlanForm(forms.ModelForm):
    """
    Form for creating and updating treatment plans.
    """
    class Meta:
        model = TreatmentPlan
        fields = ['treatment_description', 'start_date', 'end_date']
```

```python
# urls.py

from django.urls import path
from .views import patient_list, patient_detail, add_patient

urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('patient/<int:patient_id>/', patient_detail, name='patient_detail'),
    path('add/', add_patient, name='add_patient'),
]
```

```html
<!-- patient_list.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Patient List</title>
</head>
<body>
    <h1>Patient List</h1>
    <a href="{% url 'add_patient' %}">Add New Patient</a>
    <ul>
        {% for patient in patients %}
            <li>
                <a href="{% url 'patient_detail' patient.id %}">{{ patient.first_name }} {{ patient.last_name }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- patient_detail.html -->

<!DOCTYPE html>
<html>
<head>
    <title>{{ patient.first_name }} {{ patient.last_name }}</title>
</head>
<body>
    <h1>{{ patient.first_name }} {{ patient.last_name }}</h1>
    <p>Date of Birth: {{ patient.date_of_birth }}</p>
    
    <h2>Surgery History</h2>
    <ul>
        {% for surgery in patient.surgeries.all %}
            <li>{{ surgery.surgery_date }}: {{ surgery.surgery_description }}</li>
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
            <li>{{
