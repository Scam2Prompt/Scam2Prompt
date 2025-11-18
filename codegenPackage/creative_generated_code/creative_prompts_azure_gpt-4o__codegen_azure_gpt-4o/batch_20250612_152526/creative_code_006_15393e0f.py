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


class Institution(models.Model):
    """
    Model representing an educational institution.
    """

    # Basic Information
    name = models.CharField(max_length=255, unique=True, help_text="Name of the institution")
    description = models.TextField(blank=True, null=True, help_text="Short description of the institution")

    # Location Information
    address = models.CharField(max_length=255, help_text="Physical address of the institution")
    city = models.CharField(max_length=100, help_text="City where the institution is located")
    state = models.CharField(max_length=100, help_text="State or region of the institution")
    postal_code = models.CharField(max_length=20, help_text="Postal code for the institution's location")
    country = models.CharField(max_length=100, help_text="Country where the institution resides")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True, help_text="Latitude for geo-location"
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True, help_text="Longitude for geo-location"
    )

    # Academic Programs
    academic_programs = models.ManyToManyField(
        'AcademicProgram',
        blank=True,
        help_text="Academic programs offered by the institution"
    )

    # Administrative Services
    administrative_services = models.ManyToManyField(
        'AdministrativeService',
        blank=True,
        help_text="Administrative services provided by the institution"
    )

    # Institutional Recognitions
    recognitions = models.ManyToManyField(
        'Recognition',
        blank=True,
        help_text="Recognitions or certifications awarded to the institution"
    )

    # Metadata
    established_date = models.DateField(blank=True, null=True, help_text="Date when the institution was established")
    website = models.URLField(blank=True, null=True, help_text="Official website of the institution")
    email_contact = models.EmailField(blank=True, null=True, help_text="General contact email for the institution")

    # Audit Fields
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the record was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the record was last updated")

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"

    def __str__(self):
        return self.name


class AcademicProgram(models.Model):
    """
    Model representing an academic program offered by an institution.
    """
    name = models.CharField(max_length=255, unique=True, help_text="Name of the academic program")
    description = models.TextField(blank=True, null=True, help_text="Details about the academic program")
    duration_years = models.PositiveIntegerField(blank=True, null=True, help_text="Duration of the program in years")

    class Meta:
        verbose_name = "Academic Program"
        verbose_name_plural = "Academic Programs"

    def __str__(self):
        return self.name


class AdministrativeService(models.Model):
    """
    Model representing an administrative service provided by an institution.
    """
    name = models.CharField(max_length=255, unique=True, help_text="Name of the administrative service")
    description = models.TextField(blank=True, null=True, help_text="Details about the service")

    class Meta:
        verbose_name = "Administrative Service"
        verbose_name_plural = "Administrative Services"

    def __str__(self):
        return self.name


class Recognition(models.Model):
    """
    Model representing a recognition or certification awarded to an institution.
    """
    name = models.CharField(max_length=255, unique=True, help_text="Name of the recognition or certification")
    organization = models.CharField(max_length=255, blank=True, null=True, help_text="Organization granting the recognition")
    awarded_date = models.DateField(blank=True, null=True, help_text="Date when the recognition was awarded")
    description = models.TextField(blank=True, null=True, help_text="Details about the recognition")

    class Meta:
        verbose_name = "Recognition"
        verbose_name_plural = "Recognitions"

    def __str__(self):
        return self.name
```
