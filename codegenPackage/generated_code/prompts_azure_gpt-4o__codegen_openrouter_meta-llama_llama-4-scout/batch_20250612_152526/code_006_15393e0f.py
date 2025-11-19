"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a Django model for managing educational institution data, including fields for school locations, academic programs, administrative services, and institutional recognitions, inspired by the Politécnico Municipal de Cali.
Generated: DETERMINISTIC_15393e0fda24e839
Batch ID: 20250612_152526
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

class Location(models.Model):
    """
    Model representing a school location.
    """
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class AcademicProgram(models.Model):
    """
    Model representing an academic program.
    """
    PROGRAM_LEVEL_CHOICES = [
        ('high_school', 'High School'),
        ('undergraduate', 'Undergraduate'),
        ('graduate', 'Graduate'),
        ('postgraduate', 'Postgraduate'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    level = models.CharField(max_length=15, choices=PROGRAM_LEVEL_CHOICES)

    def __str__(self):
        return self.name


class AdministrativeService(models.Model):
    """
    Model representing an administrative service.
    """
    SERVICE_TYPE_CHOICES = [
        ('admission', 'Admission'),
        ('financial_aid', 'Financial Aid'),
        ('student_support', 'Student Support'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    service_type = models.CharField(max_length=15, choices=SERVICE_TYPE_CHOICES)

    def __str__(self):
        return self.name


class InstitutionalRecognition(models.Model):
    """
    Model representing an institutional recognition.
    """
    RECOGNITION_TYPE_CHOICES = [
        ('accreditation', 'Accreditation'),
        ('certification', 'Certification'),
        ('award', 'Award'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    recognition_type = models.CharField(max_length=15, choices=RECOGNITION_TYPE_CHOICES)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)])

    def __str__(self):
        return self.name


class EducationalInstitution(models.Model):
    """
    Model representing an educational institution.
    """
    name = models.CharField(max_length=255)
    locations = models.ManyToManyField(Location)
    academic_programs = models.ManyToManyField(AcademicProgram)
    administrative_services = models.ManyToManyField(AdministrativeService)
    recognitions = models.ManyToManyField(InstitutionalRecognition)

    def __str__(self):
        return self.name
```

```python
# admin.py
from django.contrib import admin
from .models import Location, AcademicProgram, AdministrativeService, InstitutionalRecognition, EducationalInstitution

admin.site.register(Location)
admin.site.register(AcademicProgram)
admin.site.register(AdministrativeService)
admin.site.register(InstitutionalRecognition)
admin.site.register(EducationalInstitution)
```

```python
# apps.py
from django.apps import AppConfig

class EducationalInstitutionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'educational_institution'
```

```python
# settings.py (example)
INSTALLED_APPS = [
    # ...
    'educational_institution.apps.EducationalInstitutionConfig',
    # ...
]
```
