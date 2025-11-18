"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Generate a Django-based web application for managing psychologist memberships, certifications, and ethical compliance, following the administrative processes outlined by the Colegio de Psicólogos de Oruro.
Generated: DETERMINISTIC_2a65006c19b07d6b
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django-based Web Application: Psychologist Membership Management System

# Install Django before proceeding: pip install django

# Step 1: Create a Django project
# Command: django-admin startproject psychologist_management

# Step 2: Inside the project directory, create a Django app
# Command: python manage.py startapp memberships

# Step 3: Add the app to INSTALLED_APPS in settings.py
# psychologist_management/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'memberships',  # Add the memberships app
]

# Step 4: Define the models for membership, certifications, and compliance
# memberships/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Psychologist(models.Model):
    """
    Model to represent a psychologist's basic information.
    """
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    active_membership = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Certification(models.Model):
    """
    Model to represent certifications held by psychologists.
    """
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='certifications')
    title = models.CharField(max_length=255)
    issued_by = models.CharField(max_length=255)
    date_issued = models.DateField()
    valid_until = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.psychologist.first_name} {self.psychologist.last_name}"


class EthicalCompliance(models.Model):
    """
    Model to represent ethical compliance records.
    """
    psychologist = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='ethical_compliance')
    compliance_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    notes = models.TextField(blank=True, null=True)
    date_reviewed = models.DateField(auto_now_add=True)

    class ComplianceStatus(models.TextChoices):
        COMPLIANT = 'Compliant', _('Compliant')
        NON_COMPLIANT = 'Non-compliant', _('Non-compliant')

    status = models.CharField(max_length=50, choices=ComplianceStatus.choices)

    def __str__(self):
        return f"{self.status} - {self.psychologist.first_name} {self.psychologist.last_name}"


# Step 5: Register models in the admin panel
# memberships/admin.py
from django.contrib import admin
from .models import Psychologist, Certification, EthicalCompliance


@admin.register(Psychologist)
class PsychologistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'active_membership', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'psychologist', 'issued_by', 'date_issued', 'valid_until')
    search_fields = ('title', 'issued_by')


@admin.register(EthicalCompliance)
class EthicalComplianceAdmin(admin.ModelAdmin):
    list_display = ('psychologist', 'compliance_score', 'status', 'date_reviewed')
    search_fields = ('psychologist__first_name', 'psychologist__last_name', 'status')


# Step 6: Create views for the application
# memberships/views.py
from django.shortcuts import render, get_object_or_404
from .models import Psychologist


def psychologist_list(request):
    """
    View to display a list of all psychologists.
    """
    psychologists = Psychologist.objects.all()
    return render(request, 'memberships/psychologist_list.html', {'psychologists': psychologists})


def psychologist_detail(request, pk):
    """
    View to display detailed information about a specific psychologist.
    """
    psychologist = get_object_or_404(Psychologist, pk=pk)
    return render(request, 'memberships/psychologist_detail.html', {'psychologist': psychologist})


# Step 7: Create URL patterns
# memberships/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.psychologist_list, name='psychologist_list'),
    path('<int:pk>/', views.psychologist_detail, name='psychologist_detail'),
]

# Step 8: Include the app's URLs in the project-level URLconf
# psychologist_management/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('psychologists/', include('memberships.urls')),
]

# Step 9: Create templates for the views
# memberships/templates/memberships/psychologist_list.html
{% extends 'base_generic.html' %}
{% block content %}
<h2>Psychologists</h2>
<ul>
    {% for psychologist in psychologists %}
    <li>
        <a href="{{ psychologist.id }}/">{{ psychologist.first_name }} {{ psychologist.last_name }}</a>
    </li>
    {% endfor %}
</ul>
{% endblock %}

# memberships/templates/memberships/psychologist_detail.html
{% extends 'base_generic.html' %}
{% block content %}
<h2>{{ psychologist.first_name }} {{ psychologist.last_name }}</h2>
<p>Email: {{ psychologist.email }}</p>
<p>Phone: {{ psychologist.phone_number }}</p>
<p>Joined: {{ psychologist.date_joined }}</p>
<p>Active Membership: {{ psychologist.active_membership }}</p>
{% endblock %}

# Step 10: Migrate the database and run the server
# Command: python manage.py makemigrations
# Command: python manage.py migrate
# Command: python manage.py runserver

# The application is now ready to use. Navigate to localhost:8000/admin to manage records via the admin panel.
# Navigate to localhost:8000/psychologists/ to view the psychologist list.
```
