"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Write a Django application for scheduling hair transplant consultations online, including fields for selecting transplant types (FUE, FUT, PRP) and clinic locations (Raipur, Durg, Bilaspur, etc.) as listed on the Auqual Hair Services website.
Generated: DETERMINISTIC_84b1ef40e58a24f0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django models, views, and templates for a hair transplant consultation scheduling application.

# models.py
from django.db import models

class ClinicLocation(models.Model):
    name = models.CharField(max_length=100)  # Example: Raipur, Durg, Bilaspur

    def __str__(self):
        return self.name


class TransplantType(models.Model):
    name = models.CharField(max_length=100)  # Example: FUE, FUT, PRP

    def __str__(self):
        return self.name


class Consultation(models.Model):
    name = models.CharField(max_length=100)  # Patient's name
    email = models.EmailField()  # Patient's email
    phone_number = models.CharField(max_length=15)  # Patient's phone number
    clinic_location = models.ForeignKey(ClinicLocation, on_delete=models.CASCADE)
    transplant_type = models.ForeignKey(TransplantType, on_delete=models.CASCADE)
    preferred_date = models.DateField()  # Preferred consultation date
    additional_notes = models.TextField(blank=True, null=True)  # Optional notes

    def __str__(self):
        return f'{self.name} - {self.transplant_type.name} at {self.clinic_location.name}'


# serializers.py (if building a REST API)
from rest_framework import serializers
from .models import ClinicLocation, TransplantType, Consultation

class ClinicLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicLocation
        fields = ['id', 'name']


class TransplantTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransplantType
        fields = ['id', 'name']


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = [
            'id', 'name', 'email', 'phone_number', 
            'clinic_location', 'transplant_type', 'preferred_date', 'additional_notes'
        ]


# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import ClinicLocation, TransplantType, Consultation
from .forms import ConsultationForm

def schedule_consultation(request):
    """Handles GET and POST requests for scheduling consultations."""
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Consultation scheduled successfully!"}, status=201)
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = ConsultationForm()
        clinic_locations = ClinicLocation.objects.all()
        transplant_types = TransplantType.objects.all()
        return render(request, "schedule_consultation.html", {
            "form": form,
            "clinic_locations": clinic_locations,
            "transplant_types": transplant_types
        })


# forms.py
from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = [
            'name', 'email', 'phone_number',
            'clinic_location', 'transplant_type', 'preferred_date', 'additional_notes'
        ]
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
        }


# templates/schedule_consultation.html
{% extends "base.html" %}
{% block content %}
<h1>Schedule Consultation</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Schedule Consultation</button>
</form>
{% endblock %}


# admin.py
from django.contrib import admin
from .models import ClinicLocation, TransplantType, Consultation

@admin.register(ClinicLocation)
class ClinicLocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(TransplantType)
class TransplantTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone_number', 'clinic_location', 'transplant_type', 'preferred_date']
    list_filter = ['clinic_location', 'transplant_type']


# urls.py
from django.urls import path
from .views import schedule_consultation

urlpatterns = [
    path('schedule/', schedule_consultation, name='schedule_consultation'),
]


# settings.py (snippet for installed apps)
INSTALLED_APPS = [
    # Default Django apps...
    'myapp',  # Replace 'myapp' with the actual name of your app
    'rest_framework',  # If building a REST API
]
```
