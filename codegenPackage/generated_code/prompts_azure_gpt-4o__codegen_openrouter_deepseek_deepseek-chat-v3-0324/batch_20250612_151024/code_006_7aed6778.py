"""
Generated Code Metadata:
========================
Original URL: https://jinlinghospital.com
Prompt: Develop a Django application to manage Jinling Hospital’s maternity and women’s health services, including prenatal care scheduling, postpartum support tracking, and patient feedback collection.
Generated: DETERMINISTIC_7aed6778c7e4aa52
Batch ID: 20250612_151024
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
    """
    Model representing a patient in Jinling Hospital's maternity and women's health services.
    """
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)
    medical_history = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PrenatalCare(models.Model):
    """
    Model representing prenatal care appointments and information.
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    gestation_week = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(42)]
    )
    blood_pressure = models.CharField(max_length=10, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Prenatal Care for {self.patient} on {self.appointment_date}"

class PostpartumSupport(models.Model):
    """
    Model tracking postpartum support services provided to patients.
    """
    SUPPORT_TYPE_CHOICES = [
        ('PHY', 'Physical Recovery'),
        ('EMO', 'Emotional Support'),
        ('NUT', 'Nutrition Guidance'),
        ('BF', 'Breastfeeding Support'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    support_date = models.DateField()
    support_type = models.CharField(max_length=3, choices=SUPPORT_TYPE_CHOICES)
    provider_name = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.get_support_type_display()} for {self.patient} on {self.support_date}"

class PatientFeedback(models.Model):
    """
    Model for collecting and managing patient feedback.
    """
    RATING_CHOICES = [
        (1, 'Very Poor'),
        (2, 'Poor'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    service_type = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    comments = models.TextField(blank=True, null=True)
    follow_up_required = models.BooleanField(default=False)
    follow_up_notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Feedback from {self.patient} on {self.submission_date}"

# admin.py
from django.contrib import admin
from .models import Patient, PrenatalCare, PostpartumSupport, PatientFeedback

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number')
    search_fields = ('first_name', 'last_name', 'contact_number')
    list_filter = ('gender', 'registration_date')

@admin.register(PrenatalCare)
class PrenatalCareAdmin(admin.ModelAdmin):
    list_display = ('patient', 'appointment_date', 'gestation_week', 'completed')
    search_fields = ('patient__first_name', 'patient__last_name')
    list_filter = ('appointment_date', 'completed')
    date_hierarchy = 'appointment_date'

@admin.register(PostpartumSupport)
class PostpartumSupportAdmin(admin.ModelAdmin):
    list_display = ('patient', 'support_date', 'support_type', 'provider_name')
    search_fields = ('patient__first_name', 'patient__last_name', 'provider_name')
    list_filter = ('support_type', 'support_date')

@admin.register(PatientFeedback)
class PatientFeedbackAdmin(admin.ModelAdmin):
    list_display = ('patient', 'submission_date', 'service_type', 'rating', 'follow_up_required')
    search_fields = ('patient__first_name', 'patient__last_name', 'service_type')
    list_filter = ('rating', 'follow_up_required', 'submission_date')

# forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Patient, PrenatalCare, PostpartumSupport, PatientFeedback

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'medical_history': forms.Textarea(attrs={'rows': 4}),
        }

class PrenatalCareForm(forms.ModelForm):
    class Meta:
        model = PrenatalCare
        fields = '__all__'
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }
    
    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']
        if appointment_date < timezone.now():
            raise ValidationError("Appointment date cannot be in the past.")
        return appointment_date

class PostpartumSupportForm(forms.ModelForm):
    class Meta:
        model = PostpartumSupport
        fields = '__all__'
        widgets = {
            'support_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

class PatientFeedbackForm(forms.ModelForm):
    class Meta:
        model = PatientFeedback
        fields = '__all__'
        widgets = {
            'comments': forms.Textarea(attrs={'rows': 4}),
            'follow_up_notes': forms.Textarea(attrs={'rows': 4}),
        }

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Patient, PrenatalCare, PostpartumSupport, PatientFeedback
from .forms import PatientForm, PrenatalCareForm, PostpartumSupportForm, PatientFeedbackForm

class PatientListView(ListView):
    model = Patient
    template_name = 'maternity/patient_list.html'
    context_object_name = 'patients'
    paginate_by = 20

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'maternity/patient_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prenatal_cares'] = PrenatalCare.objects.filter(patient=self.object)
        context['postpartum_supports'] = PostpartumSupport.objects.filter(patient=self.object)
        context['patient_feedbacks'] = PatientFeedback.objects.filter(patient=self.object)
        return context

class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'maternity/patient_form.html'
    success_url = reverse_lazy('patient-list')

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'maternity/patient_form.html'
    success_url = reverse_lazy('patient-list')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'maternity/patient_confirm_delete.html'
    success_url = reverse_lazy('patient-list')

class PrenatalCareCreateView(CreateView):
    model = PrenatalCare
    form_class = PrenatalCareForm
    template_name = 'maternity/prenatalcare_form.html'
    
    def get_success_url(self):
        return reverse_lazy('patient-detail', kwargs={'pk': self.object.patient.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Prenatal care appointment added successfully.')
        return super().form_valid(form)

class PostpartumSupportCreateView(CreateView):
    model = PostpartumSupport
    form_class = PostpartumSupportForm
    template_name = 'maternity/postpartumsupport_form.html'
    
    def get_success_url(self):
        return reverse_lazy('patient-detail', kwargs={'pk': self.object.patient.pk})
    
    def form_valid(self, form):
        messages.success(self.request, 'Postpartum support
