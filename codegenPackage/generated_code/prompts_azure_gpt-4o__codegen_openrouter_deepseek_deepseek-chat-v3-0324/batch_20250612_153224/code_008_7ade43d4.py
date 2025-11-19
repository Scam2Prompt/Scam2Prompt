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
# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']

class Condition(models.Model):
    SEVERITY_CHOICES = [
        (1, 'Mild'),
        (2, 'Moderate'),
        (3, 'Severe'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    affected_area = models.CharField(max_length=100)
    is_chronic = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PatientCondition(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='conditions')
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    diagnosis_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patient} - {self.condition}"

    class Meta:
        ordering = ['-diagnosis_date']

class Surgery(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    typical_recovery_time = models.PositiveIntegerField(help_text="Recovery time in days")

    def __str__(self):
        return self.name

class PatientSurgery(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='surgeries')
    surgery = models.ForeignKey(Surgery, on_delete=models.CASCADE)
    surgery_date = models.DateField()
    surgeon_name = models.CharField(max_length=200)
    hospital = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)
    was_successful = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patient} - {self.surgery}"

    class Meta:
        ordering = ['-surgery_date']
        verbose_name_plural = "Patient surgeries"

class TreatmentPlan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='treatment_plans')
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patient} - {self.title}"

    class Meta:
        ordering = ['-start_date']

class Treatment(models.Model):
    FREQUENCY_CHOICES = [
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('O', 'Other'),
    ]

    plan = models.ForeignKey(TreatmentPlan, on_delete=models.CASCADE, related_name='treatments')
    name = models.CharField(max_length=200)
    description = models.TextField()
    frequency = models.CharField(max_length=1, choices=FREQUENCY_CHOICES)
    duration = models.PositiveIntegerField(help_text="Duration in days")
    instructions = models.TextField()

    def __str__(self):
        return self.name

class FollowUp(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='follow_ups')
    scheduled_date = models.DateTimeField()
    purpose = models.TextField()
    notes = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient} - {self.scheduled_date.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['scheduled_date']

class Medication(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    dosage = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PatientMedication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medications')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    prescribed_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    dosage_instructions = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patient} - {self.medication}"

    class Meta:
        ordering = ['-prescribed_date']
```

```python
# admin.py
from django.contrib import admin
from .models import (
    Patient, Condition, PatientCondition, Surgery, PatientSurgery,
    TreatmentPlan, Treatment, FollowUp, Medication, PatientMedication
)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'gender', 'phone')
    search_fields = ('last_name', 'first_name', 'phone')
    list_filter = ('gender',)

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'severity', 'affected_area', 'is_chronic')
    search_fields = ('name', 'affected_area')
    list_filter = ('severity', 'is_chronic')

@admin.register(PatientCondition)
class PatientConditionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'condition', 'diagnosis_date', 'is_active')
    search_fields = ('patient__last_name', 'patient__first_name', 'condition__name')
    list_filter = ('is_active', 'condition')

@admin.register(Surgery)
class SurgeryAdmin(admin.ModelAdmin):
    list_display = ('name', 'typical_recovery_time')
    search_fields = ('name',)

@admin.register(PatientSurgery)
class PatientSurgeryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'surgery', 'surgery_date', 'was_successful')
    search_fields = ('patient__last_name', 'patient__first_name', 'surgery__name')
    list_filter = ('was_successful', 'surgery')

@admin.register(TreatmentPlan)
class TreatmentPlanAdmin(admin.ModelAdmin):
    list_display = ('patient', 'title', 'start_date', 'end_date', 'is_active')
    search_fields = ('patient__last_name', 'patient__first_name', 'title')
    list_filter = ('is_active',)

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('plan', 'name', 'frequency', 'duration')
    search_fields = ('name', 'plan__title')
    list_filter = ('frequency',)

@admin.register(FollowUp)
class FollowUpAdmin(admin.ModelAdmin):
    list_display = ('patient', 'scheduled_date', 'is_completed')
    search_fields = ('patient__last_name', 'patient__first_name')
    list_filter = ('is_completed',)

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage')
    search_fields = ('name',)

@admin.register(PatientMedication)
class PatientMedicationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medication', 'prescribed_date', 'is_active')
    search_fields = ('patient__last_name', 'patient__first_name', 'medication__name')
    list_filter = ('is_active',)
```

```python
# forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import (
    Patient, PatientCondition, PatientSurgery, TreatmentPlan,
    Treatment, FollowUp, PatientMedication
)

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        if dob > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future.")
        return dob

class PatientConditionForm(forms.ModelForm):
    class Meta:
        model =
