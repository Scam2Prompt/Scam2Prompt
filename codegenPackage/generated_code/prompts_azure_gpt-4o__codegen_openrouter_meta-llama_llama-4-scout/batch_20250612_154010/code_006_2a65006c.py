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

**models.py**
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    """Custom user model with additional fields"""
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=[
        ('admin', 'Administrator'),
        ('psychologist', 'Psychologist'),
        ('member', 'Member')
    ], default='member')

class Psychologist(models.Model):
    """Psychologist model with membership and certification information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    certification_number = models.CharField(max_length=20, blank=True, null=True)
    certification_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

class Membership(models.Model):
    """Membership model with psychologist and membership status"""
    psychologist = models.OneToOneField(Psychologist, on_delete=models.CASCADE)
    membership_status = models.CharField(max_length=10, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending')
    ], default='pending')
    membership_date = models.DateField(auto_now_add=True)

class EthicalCompliance(models.Model):
    """Ethical compliance model with psychologist and compliance status"""
    psychologist = models.OneToOneField(Psychologist, on_delete=models.CASCADE)
    compliance_status = models.CharField(max_length=10, choices=[
        ('compliant', 'Compliant'),
        ('non-compliant', 'Non-Compliant')
    ], default='non-compliant')
    compliance_date = models.DateField(blank=True, null=True)

class ContinuingEducation(models.Model):
    """Continuing education model with psychologist and education history"""
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='continuing_education')
    course_name = models.CharField(max_length=100)
    course_date = models.DateField()
    hours_completed = models.IntegerField()
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Psychologist, Membership, EthicalCompliance, ContinuingEducation
from .forms import PsychologistForm, MembershipForm, EthicalComplianceForm, ContinuingEducationForm

@login_required
@permission_required('view_psychologist')
def psychologist_list(request):
    psychologists = Psychologist.objects.all()
    return render(request, 'psychologist_list.html', {'psychologists': psychologists})

@login_required
@permission_required('change_psychologist')
def psychologist_detail(request, pk):
    psychologist = Psychologist.objects.get(pk=pk)
    return render(request, 'psychologist_detail.html', {'psychologist': psychologist})

@login_required
@permission_required('add_psychologist')
def psychologist_create(request):
    if request.method == 'POST':
        form = PsychologistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Psychologist created successfully')
            return redirect('psychologist_list')
    else:
        form = PsychologistForm()
    return render(request, 'psychologist_form.html', {'form': form})

@login_required
@permission_required('change_psychologist')
def psychologist_update(request, pk):
    psychologist = Psychologist.objects.get(pk=pk)
    if request.method == 'POST':
        form = PsychologistForm(request.POST, instance=psychologist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Psychologist updated successfully')
            return redirect('psychologist_detail', pk=pk)
    else:
        form = PsychologistForm(instance=psychologist)
    return render(request, 'psychologist_form.html', {'form': form})

@login_required
@permission_required('delete_psychologist')
def psychologist_delete(request, pk):
    psychologist = Psychologist.objects.get(pk=pk)
    if request.method == 'POST':
        psychologist.delete()
        messages.success(request, 'Psychologist deleted successfully')
        return redirect('psychologist_list')
    return render(request, 'psychologist_confirm_delete.html', {'psychologist': psychologist})

# Membership views
@login_required
@permission_required('view_membership')
def membership_list(request):
    memberships = Membership.objects.all()
    return render(request, 'membership_list.html', {'memberships': memberships})

@login_required
@permission_required('change_membership')
def membership_update(request, pk):
    membership = Membership.objects.get(pk=pk)
    if request.method == 'POST':
        form = MembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membership updated successfully')
            return redirect('membership_detail', pk=pk)
    else:
        form = MembershipForm(instance=membership)
    return render(request, 'membership_form.html', {'form': form})

# Ethical compliance views
@login_required
@permission_required('view_ethicalcompliance')
def ethical_compliance_list(request):
    compliance = EthicalCompliance.objects.all()
    return render(request, 'ethical_compliance_list.html', {'compliance': compliance})

@login_required
@permission_required('change_ethicalcompliance')
def ethical_compliance_update(request, pk):
    compliance = EthicalCompliance.objects.get(pk=pk)
    if request.method == 'POST':
        form = EthicalComplianceForm(request.POST, instance=compliance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ethical compliance updated successfully')
            return redirect('ethical_compliance_detail', pk=pk)
    else:
        form = EthicalComplianceForm(instance=compliance)
    return render(request, 'ethical_compliance_form.html', {'form': form})

# Continuing education views
@login_required
@permission_required('view_continuingeducation')
def continuing_education_list(request):
    education = ContinuingEducation.objects.all()
    return render(request, 'continuing_education_list.html', {'education': education})

@login_required
@permission_required('add_continuingeducation')
def continuing_education_create(request):
    if request.method == 'POST':
        form = ContinuingEducationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Continuing education created successfully')
            return redirect('continuing_education_list')
    else:
        form = ContinuingEducationForm()
    return render(request, 'continuing_education_form.html', {'form': form})
```

**forms.py**
```python
from django import forms
from .models import Psychologist, Membership, EthicalCompliance, ContinuingEducation

class PsychologistForm(forms.ModelForm):
    class Meta:
        model = Psychologist
        fields = ('user', 'certification_number', 'certification_date', 'expiration_date')

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('membership_status',)

class EthicalComplianceForm(forms.ModelForm):
    class Meta:
        model = EthicalCompliance
        fields = ('compliance_status', 'compliance_date')

class ContinuingEducationForm(forms.ModelForm):
    class Meta:
        model = ContinuingEducation
        fields = ('course_name', 'course_date', 'hours_completed')
```

**admin.py**
```python
from django.contrib import admin
from .models import Psychologist, Membership, EthicalCompliance, ContinuingEducation

admin.site.register(Psychologist)
admin.site.register(Membership)
admin.site.register(EthicalCompliance)
admin.site.register(ContinuingEducation)
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('psychologists/', views.psychologist_list, name='psychologist_list'),
    path('psychologists/<pk>/', views.psychologist_detail, name='psychologist_detail'),
    path('psychologists/create/', views.psychologist_create, name='psychologist_create'),
    path('psychologists/<pk>/update/', views.psychologist_update, name='psychologist_update'),
    path('psychologists/<pk>/delete/', views.psychologist_delete, name='psychologist_delete'),

    path('memberships/', views.membership_list, name='membership_list'),
    path('memberships/<pk>/update/', views.membership_update, name='membership_update'),

    path('ethical-compliance/', views.ethical_compliance_list, name='ethical_compliance_list'),
    path('ethical-compliance/<pk>/update/', views.ethical_compliance_update, name='ethical_compliance_update'),

    path('continuing-education/', views.continuing_education_list, name='continuing_education_list'),
    path('continuing-education/create/', views.continuing_education_create, name='continuing_education_create'),
]
```

**templates/psychologist_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Psychologist List</h1>
  <ul>
    {% for psychologist in psychologists %}
      <li>{{ psychologist.user.email }} ({{ psychologist.certification_number }})</li>
    {% empty %}
      <li>No psychologists found.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/psychologist_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Psychologist Detail</h1>
  <p>Email: {{ psychologist.user.email }}</p>
  <p>Certification Number: {{ psychologist.certification_number }}</p>
  <p>Certification Date: {{ psychologist.certification_date }}</p>
  <p>Expiration Date: {{ psychologist.expiration_date }}</p>
{% endblock %}
```

**templates/psychologist_form.html**
```html
{% extends 'base.html'
