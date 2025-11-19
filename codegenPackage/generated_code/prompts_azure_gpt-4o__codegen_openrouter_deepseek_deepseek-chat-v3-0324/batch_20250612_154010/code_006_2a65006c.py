"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Generate a Django-based web application for managing psychologist memberships, certifications, and ethical compliance, following the administrative processes outlined by the Colegio de Psicólogos de Oruro.
Generated: DETERMINISTIC_2a65006c19b07d6b
Batch ID: 20250612_154010
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
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Psychologist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='psychologist')
    license_number = models.CharField(max_length=20, unique=True)
    specialization = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.license_number}"

class Certification(models.Model):
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    credential_id = models.CharField(max_length=50, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.psychologist}"

class EthicalCompliance(models.Model):
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='ethical_compliances')
    compliance_date = models.DateField()
    compliance_status = models.CharField(max_length=50, choices=[
        ('compliant', 'Compliant'),
        ('pending', 'Pending Review'),
        ('non_compliant', 'Non-Compliant')
    ])
    notes = models.TextField(blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.psychologist} - {self.compliance_status}"

class Membership(models.Model):
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='memberships')
    start_date = models.DateField()
    end_date = models.DateField()
    membership_type = models.CharField(max_length=50, choices=[
        ('regular', 'Regular'),
        ('student', 'Student'),
        ('honorary', 'Honorary')
    ])
    is_current = models.BooleanField(default=True)
    payment_status = models.CharField(max_length=20, choices=[
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial Payment')
    ])

    def __str__(self):
        return f"{self.psychologist} - {self.membership_type}"

class ContinuingEducation(models.Model):
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='continuing_educations')
    title = models.CharField(max_length=200)
    hours = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    completion_date = models.DateField()
    provider = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.psychologist}"

class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=50)
    record_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user} - {self.action} - {self.model_name}"

# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Psychologist, Certification, EthicalCompliance, Membership, ContinuingEducation, AuditLog

class PsychologistInline(admin.StackedInline):
    model = Psychologist
    can_delete = False
    verbose_name_plural = 'Psychologist'

class CustomUserAdmin(UserAdmin):
    inlines = (PsychologistInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'psychologist', 'issuing_organization', 'issue_date', 'is_verified')
    list_filter = ('is_verified', 'issuing_organization')
    search_fields = ('name', 'psychologist__user__first_name', 'psychologist__user__last_name')

class EthicalComplianceAdmin(admin.ModelAdmin):
    list_display = ('psychologist', 'compliance_date', 'compliance_status', 'reviewer')
    list_filter = ('compliance_status',)
    search_fields = ('psychologist__user__first_name', 'psychologist__user__last_name')

class MembershipAdmin(admin.ModelAdminAdmin):
    list_display = ('psychologist', 'membership_type', 'start_date', 'end_date', 'is_current', 'payment_status')
    list_filter = ('membership_type', 'is_current', 'payment_status')
    search_fields = ('psychologist__user__first_name', 'psychologist__user__last_name')

class ContinuingEducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'psychologist', 'hours', 'completion_date', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('title', 'psychologist__user__first_name', 'psychologist__user__last_name')

class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'model_name', 'record_id', 'timestamp')
    list_filter = ('action', 'model_name')
    search_fields = ('user__username', 'model_name')
    readonly_fields = ('timestamp',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Psychologist)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(EthicalCompliance, EthicalComplianceAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(ContinuingEducation, ContinuingEducationAdmin)
admin.site.register(AuditLog, AuditLogAdmin)

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Psychologist, Certification, EthicalCompliance, Membership, ContinuingEducation

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class PsychologistForm(forms.ModelForm):
    class Meta:
        model = Psychologist
        fields = ['license_number', 'specialization', 'years_of_experience', 'phone_number', 'address']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'issuing_organization', 'issue_date', 'expiration_date', 'credential_id']

class EthicalComplianceForm(forms.ModelForm):
    class Meta:
        model = EthicalCompliance
        fields = ['compliance_date', 'compliance_status', 'notes']

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['start_date', 'end_date', 'membership_type', 'payment_status']

class ContinuingEducationForm(forms.ModelForm):
    class Meta:
        model = ContinuingEducation
        fields = ['title', 'hours', 'completion_date', 'provider']

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Psychologist, Certification, EthicalCompliance, Membership, ContinuingEducation, AuditLog
from .forms import (UserRegistrationForm, PsychologistForm, CertificationForm, 
                   EthicalComplianceForm, MembershipForm, ContinuingEducationForm)

def is_admin(user):
    return user.is_staff

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        psychologist_form = PsychologistForm(request.POST)
        
        if user_form.is_valid() and psychologist_form.is_valid():
            user = user_form.save()
            psychologist = psychologist_form.save(commit=False)
            psychologist.user = user
            psychologist.save()
            
            messages.success(request, 'Registration successful! Please wait for admin approval.')
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        psychologist_form = PsychologistForm()
    
    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'psychologist_form': psychologist_form
    })

@login_required
def dashboard(request):
    try:
        psychologist = request.user.psychologist
    except Psych
