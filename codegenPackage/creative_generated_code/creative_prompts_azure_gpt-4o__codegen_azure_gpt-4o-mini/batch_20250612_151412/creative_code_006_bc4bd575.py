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
from django.core.validators import RegexValidator

class PediatricDentist(models.Model):
    """
    Model to store information about pediatric dentists.
    """

    # Name of the dentist
    name = models.CharField(max_length=100, help_text="Enter the full name of the pediatric dentist.")

    # Qualifications of the dentist
    qualifications = models.TextField(help_text="Enter the qualifications of the dentist.")

    # Location of the dental practice
    location = models.CharField(max_length=255, help_text="Enter the practice location.")

    # Contact number with validation for format
    contact_number = models.CharField(
        max_length=15, 
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid phone number.")],
        help_text="Enter the contact number (format: +99999999999)."
    )

    # Email address with validation
    email = models.EmailField(
        max_length=254,
        help_text="Enter a valid email address for the dentist."
    )

    # Additional notes regarding the practice
    notes = models.TextField(blank=True, help_text="Any additional notes about the practice.")

    def __str__(self):
        """
        String representation of the PediatricDentist object.
        Returns the name of the dentist.
        """
        return self.name

    class Meta:
        """
        Meta options for the PediatricDentist model.
        """
        verbose_name = "Pediatric Dentist"
        verbose_name_plural = "Pediatric Dentists"
        ordering = ['name']

    def save(self, *args, **kwargs):
        """
        Override save method for additional processing before saving.
        """
        super().save(*args, **kwargs)
```
