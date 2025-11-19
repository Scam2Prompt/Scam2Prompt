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
from django.db import models

class EducationalInstitution(models.Model):
    """
    Model representing an educational institution.
    """
    name = models.CharField(max_length=255, unique=True, help_text="Name of the institution")
    location = models.CharField(max_length=255, help_text="Location of the institution")
    established_year = models.PositiveIntegerField(help_text="Year the institution was established")
    website = models.URLField(blank=True, null=True, help_text="Official website of the institution")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Educational Institution"
        verbose_name_plural = "Educational Institutions"


class AcademicProgram(models.Model):
    """
    Model representing an academic program offered by an educational institution.
    """
    institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, related_name='academic_programs')
    name = models.CharField(max_length=255, help_text="Name of the academic program")
    degree_type = models.CharField(max_length=50, choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Diploma', 'Diploma')], help_text="Type of degree awarded")
    duration_years = models.PositiveIntegerField(help_text="Duration of the program in years")

    def __str__(self):
        return f"{self.name} - {self.institution.name}"

    class Meta:
        unique_together = ('institution', 'name')
        verbose_name = "Academic Program"
        verbose_name_plural = "Academic Programs"


class AdministrativeService(models.Model):
    """
    Model representing an administrative service provided by an educational institution.
    """
    institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, related_name='administrative_services')
    service_name = models.CharField(max_length=255, help_text="Name of the administrative service")
    description = models.TextField(help_text="Description of the service offered")

    def __str__(self):
        return f"{self.service_name} - {self.institution.name}"

    class Meta:
        unique_together = ('institution', 'service_name')
        verbose_name = "Administrative Service"
        verbose_name_plural = "Administrative Services"


class InstitutionalRecognition(models.Model):
    """
    Model representing recognitions or accreditations received by an educational institution.
    """
    institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, related_name='recognitions')
    recognition_name = models.CharField(max_length=255, help_text="Name of the recognition or accreditation")
    awarding_body = models.CharField(max_length=255, help_text="Body that awarded the recognition")
    date_awarded = models.DateField(help_text="Date when the recognition was awarded")

    def __str__(self):
        return f"{self.recognition_name} - {self.institution.name}"

    class Meta:
        unique_together = ('institution', 'recognition_name', 'awarding_body')
        verbose_name = "Institutional Recognition"
        verbose_name_plural = "Institutional Recognitions"
```
