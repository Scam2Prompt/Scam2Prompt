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
# patient_management_app/models.py

from django.db import models

class Patient(models.Model):
    """
    Model representing a patient.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SurgeryHistory(models.Model):
    """
    Model representing a patient's surgery history.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='surgery_history')
    surgery_date = models.DateField()
    surgery_type = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Surgery on {self.surgery_date}: {self.surgery_type}"

class FollowUpSchedule(models.Model):
    """
    Model representing a patient's follow-up schedule.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='follow_up_schedules')
    follow_up_date = models.DateField()
    purpose = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Follow-up on {self.follow_up_date}"

class TreatmentPlan(models.Model):
    """
    Model representing a patient's treatment plan.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='treatment_plans')
    treatment_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Treatment: {self.treatment_name}"

# patient_management_app/admin.py

from django.contrib import admin
from .models import Patient, SurgeryHistory, FollowUpSchedule, TreatmentPlan

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """
    Admin interface for managing patient records.
    """
    list_display = ('first_name', 'last_name', 'date_of_birth', 'contact_number', 'email')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(SurgeryHistory)
class SurgeryHistoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing surgery history records.
    """
    list_display = ('patient', 'surgery_date', 'surgery_type')
    search_fields = ('surgery_type',)
    list_filter = ('surgery_date',)

@admin.register(FollowUpSchedule)
class FollowUpScheduleAdmin(admin.ModelAdmin):
    """
    Admin interface for managing follow-up schedules.
    """
    list_display = ('patient', 'follow_up_date', 'purpose')
    search_fields = ('purpose',)
    list_filter = ('follow_up_date',)

@admin.register(TreatmentPlan)
class TreatmentPlanAdmin(admin.ModelAdmin):
    """
    Admin interface for managing treatment plans.
    """
    list_display = ('patient', 'treatment_name', 'start_date', 'end_date')
    search_fields = ('treatment_name',)
    list_filter = ('start_date', 'end_date')

# patient_management_app/views.py

from django.shortcuts import render, get_object_or_404
from .models import Patient
from django.http import JsonResponse

def patient_details(request, patient_id):
    """
    View that returns details of a specific patient.
    """
    patient = get_object_or_404(Patient, pk=patient_id)
    data = {
        "first_name": patient.first_name,
        "last_name": patient.last_name,
        "date_of_birth": patient.date_of_birth,
        "contact_number": patient.contact_number,
        "email": patient.email,
        "surgery_history": list(patient.surgery_history.values()),
        "follow_up_schedules": list(patient.follow_up_schedules.values()),
        "treatment_plans": list(patient.treatment_plans.values()),
    }
    return JsonResponse(data)

# patient_management_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('patient/<int:patient_id>/', views.patient_details, name='patient_details'),
]

# patient_management_app/apps.py

from django.apps import AppConfig

class PatientManagementAppConfig(AppConfig):
    """
    Configuration for the patient management application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patient_management_app'

# settings.py (Add the app to INSTALLED_APPS)

INSTALLED_APPS = [
    # Other apps...
    'patient_management_app',
]
```
