"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pediatricdentistinpune.com
Prompt: Develop a Django model for storing pediatric dentist information, including name, qualifications, location, and contact details, based on the structure of the website https://pediatricdentistinpune.com.
Generated: DETERMINISTIC_bc4bd5759148afcc
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models

class PediatricDentist(models.Model):
    """
    Model to store information about pediatric dentists.
    """

    # Dentist's full name
    name = models.CharField(max_length=255, help_text="Full name of the pediatric dentist.")

    # Dentist's professional qualifications
    qualifications = models.CharField(max_length=255, help_text="Professional qualifications (e.g., BDS, MDS).")

    # Location of the dentist's clinic
    location = models.CharField(max_length=255, help_text="Clinic location (e.g., city or specific area).")

    # Contact number for reaching the dentist or clinic
    contact_number = models.CharField(
        max_length=15, 
        help_text="Primary contact number (format: +91XXXXXXXXXX).",
        validators=[
            models.validators.RegexValidator(
                regex=r'^\+?\d{10,15}$',
                message="Enter a valid phone number (e.g., +91XXXXXXXXXX)."
            )
        ]
    )

    # Optional email address for contacting the dentist
    email = models.EmailField(
        blank=True, 
        null=True, 
        help_text="Optional email address."
    )

    # Timestamp for when the record was created
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp of record creation.")

    # Timestamp for the last modification of the record
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp of the last record update.")

    class Meta:
        """
        Meta class for additional options.
        """
        verbose_name = "Pediatric Dentist"
        verbose_name_plural = "Pediatric Dentists"
        ordering = ['name']

    def __str__(self):
        """
        String representation of the model instance.
        """
        return self.name
```
