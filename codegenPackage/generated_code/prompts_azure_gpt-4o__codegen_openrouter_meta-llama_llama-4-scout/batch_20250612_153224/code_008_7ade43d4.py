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

**models.py**
```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Patient(models.Model):
    """
    Patient model to store patient information.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FootAnkleCondition(models.Model):
    """
    Model to store foot and ankle conditions.
    """
    CONDITION_CHOICES = [
        ("TOE_DEFORMITY", "Toe Deformity"),
        ("ANKLE_FRACTURE", "Ankle Fracture"),
        ("FOOT_ULCER", "Foot Ulcer"),
        # Add more conditions as needed
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient} - {self.condition}"

class Surgery(models.Model):
    """
    Model to store surgery history.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    surgery_date = models.DateField()
    surgery_description = models.TextField()
    surgeon = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.patient} - {self.surgery_date}"

class FollowUpSchedule(models.Model):
    """
    Model to store follow-up schedules.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    schedule_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient} - {self.schedule_date}"

class TreatmentPlan(models.Model):
    """
    Model to store treatment plans.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    plan_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient} - {self.plan_description}"

class Medication(models.Model):
    """
    Model to store medications.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.patient} - {self.medication_name}"
```

**admin.py**
```python
from django.contrib import admin
from .models import Patient, FootAnkleCondition, Surgery, FollowUpSchedule, TreatmentPlan, Medication

admin.site.register(Patient)
admin.site.register(FootAnkleCondition)
admin.site.register(Surgery)
admin.site.register(FollowUpSchedule)
admin.site.register(TreatmentPlan)
admin.site.register(Medication)
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Patient, FootAnkleCondition, Surgery, FollowUpSchedule, TreatmentPlan, Medication
from .forms import PatientForm, FootAnkleConditionForm, SurgeryForm, FollowUpScheduleForm, TreatmentPlanForm, MedicationForm

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = Patient.objects.get(pk=pk)
    return render(request, 'patient_detail.html', {'patient': patient})

def patient_new(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient_new.html', {'form': form})

def foot_ankle_condition_list(request, patient_pk):
    conditions = FootAnkleCondition.objects.filter(patient=patient_pk)
    return render(request, 'foot_ankle_condition_list.html', {'conditions': conditions})

def surgery_list(request, patient_pk):
    surgeries = Surgery.objects.filter(patient=patient_pk)
    return render(request, 'surgery_list.html', {'surgeries': surgeries})

def follow_up_schedule_list(request, patient_pk):
    schedules = FollowUpSchedule.objects.filter(patient=patient_pk)
    return render(request, 'follow_up_schedule_list.html', {'schedules': schedules})

def treatment_plan_list(request, patient_pk):
    plans = TreatmentPlan.objects.filter(patient=patient_pk)
    return render(request, 'treatment_plan_list.html', {'plans': plans})

def medication_list(request, patient_pk):
    medications = Medication.objects.filter(patient=patient_pk)
    return render(request, 'medication_list.html', {'medications': medications})
```

**forms.py**
```python
from django import forms
from .models import Patient, FootAnkleCondition, Surgery, FollowUpSchedule, TreatmentPlan, Medication

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'date_of_birth', 'medical_history')

class FootAnkleConditionForm(forms.ModelForm):
    class Meta:
        model = FootAnkleCondition
        fields = ('condition', 'description')

class SurgeryForm(forms.ModelForm):
    class Meta:
        model = Surgery
        fields = ('surgery_date', 'surgery_description', 'surgeon')

class FollowUpScheduleForm(forms.ModelForm):
    class Meta:
        model = FollowUpSchedule
        fields = ('schedule_date', 'description')

class TreatmentPlanForm(forms.ModelForm):
    class Meta:
        model = TreatmentPlan
        fields = ('plan_description', 'start_date', 'end_date')

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ('medication_name', 'dosage', 'frequency')
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<pk>/', views.patient_detail, name='patient_detail'),
    path('patients/new/', views.patient_new, name='patient_new'),
    path('patients/<pk>/conditions/', views.foot_ankle_condition_list, name='foot_ankle_condition_list'),
    path('patients/<pk>/surgeries/', views.surgery_list, name='surgery_list'),
    path('patients/<pk>/follow-up-schedules/', views.follow_up_schedule_list, name='follow_up_schedule_list'),
    path('patients/<pk>/treatment-plans/', views.treatment_plan_list, name='treatment_plan_list'),
    path('patients/<pk>/medications/', views.medication_list, name='medication_list'),
]
```

**templates**

Create the following templates in a directory named `templates` in your app directory:

- `patient_list.html`
- `patient_detail.html`
- `patient_new.html`
- `foot_ankle_condition_list.html`
- `surgery_list.html`
- `follow_up_schedule_list.html`
- `treatment_plan_list.html`
- `medication_list.html`

**Run Migrations**

Run the following commands in your terminal:

```bash
python manage.py makemigrations
python manage.py migrate
```

**Run Server**

Run the following command to start the server:

```bash
python manage.py runserver
```
