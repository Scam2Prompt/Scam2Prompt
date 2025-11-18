"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jinlinghospital.com
Prompt: Develop a Django application to manage Jinling Hospital’s maternity and women’s health services, including prenatal care scheduling, postpartum support tracking, and patient feedback collection.
Generated: DETERMINISTIC_7aed6778c7e4aa52
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django settings.py configuration file should be set up appropriately beforehand.

# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()  # Date of birth
    contact_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PrenatalCareSchedule(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="prenatal_appointments")
    appointment_date = models.DateField()
    doctor_name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient} - {self.appointment_date}"

class PostpartumSupport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="postpartum_support")
    support_date = models.DateField()
    support_type = models.CharField(max_length=100)  # e.g., "Lactation consultation"
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient} - {self.support_type} ({self.support_date})"

class Feedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="feedback")
    feedback_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Rating scale 1-5
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Feedback by {self.patient} - {self.rating}"

# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Patient, PrenatalCareSchedule, PostpartumSupport, Feedback
from django.views.decorators.csrf import csrf_exempt
import json

# Error handling and basic CRUD operations for the models
@csrf_exempt
def create_patient(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            patient = Patient.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                dob=data['dob'],
                contact_number=data['contact_number'],
                email=data['email'],
                address=data['address']
            )
            return JsonResponse({"message": "Patient created successfully!", "patient_id": patient.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

def get_patient_details(request, patient_id):
    try:
        patient = get_object_or_404(Patient, id=patient_id)
        return JsonResponse({
            "id": patient.id,
            "first_name": patient.first_name,
            "last_name": patient.last_name,
            "dob": patient.dob,
            "contact_number": patient.contact_number,
            "email": patient.email,
            "address": patient.address
        }, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)

@csrf_exempt
def create_prenatal_appointment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            patient = get_object_or_404(Patient, id=data['patient_id'])
            appointment = PrenatalCareSchedule.objects.create(
                patient=patient,
                appointment_date=data['appointment_date'],
                doctor_name=data['doctor_name'],
                notes=data.get('notes', "")
            )
            return JsonResponse({"message": "Prenatal appointment created successfully!", "appointment_id": appointment.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

# Additional views for postpartum support and feedback can be added with similar patterns.

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.create_patient, name='create_patient'),
    path('patients/<int:patient_id>/', views.get_patient_details, name='get_patient_details'),
    path('prenatal/', views.create_prenatal_appointment, name='create_prenatal_appointment'),
    # Add more URLs for postpartum support and feedback as needed
]

# admin.py
from django.contrib import admin
from .models import Patient, PrenatalCareSchedule, PostpartumSupport, Feedback

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'contact_number', 'email')

@admin.register(PrenatalCareSchedule)
class PrenatalCareScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'appointment_date', 'doctor_name')

@admin.register(PostpartumSupport)
class PostpartumSupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'support_date', 'support_type')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'feedback_date', 'rating')
```
