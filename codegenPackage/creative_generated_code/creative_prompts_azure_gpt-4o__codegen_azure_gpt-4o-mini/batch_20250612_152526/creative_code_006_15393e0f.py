"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a Django model for managing educational institution data, including fields for school locations, academic programs, administrative services, and institutional recognitions, inspired by the Politécnico Municipal de Cali.
Generated: DETERMINISTIC_15393e0fda24e839
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models

class Location(models.Model):
    """Model representing a school location."""
    address = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"


class AcademicProgram(models.Model):
    """Model representing an academic program offered by the institution."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    duration_years = models.PositiveIntegerField()
    
    class Meta:
        verbose_name = "Academic Program"
        verbose_name_plural = "Academic Programs"

    def __str__(self):
        return self.name


class AdministrativeService(models.Model):
    """Model representing an administrative service provided by the institution."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Administrative Service"
        verbose_name_plural = "Administrative Services"

    def __str__(self):
        return self.name


class InstitutionalRecognition(models.Model):
    """Model representing recognitions received by the institution."""
    name = models.CharField(max_length=100, unique=True)
    year_awarded = models.PositiveIntegerField()
    issuing_organization = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Institutional Recognition"
        verbose_name_plural = "Institutional Recognitions"

    def __str__(self):
        return f"{self.name} ({self.year_awarded})"


class EducationalInstitution(models.Model):
    """Model representing an educational institution with various attributes."""
    name = models.CharField(max_length=200, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="institutions")
    academic_programs = models.ManyToManyField(AcademicProgram, related_name="institutions")
    administrative_services = models.ManyToManyField(AdministrativeService, related_name="institutions")
    recognitions = models.ManyToManyField(InstitutionalRecognition, related_name="institutions")
    
    class Meta:
        verbose_name = "Educational Institution"
        verbose_name_plural = "Educational Institutions"

    def __str__(self):
        return self.name
```
