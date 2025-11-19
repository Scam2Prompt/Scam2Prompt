"""
Generated Code Metadata:
========================
Original URL: https://yaisatangwell.com
Prompt: Using the Django framework, create a model for a photography business that includes fields for "service type" (e.g., wedding, maternity, anniversary), "location" (e.g., Trinidad and Tobago), "contact information," and "social media links."
Generated: DETERMINISTIC_86b3033895cd5c01
Batch ID: 20250612_154207
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
from django.core.validators import URLValidator, EmailValidator
from django.core.exceptions import ValidationError

class PhotographyBusiness(models.Model):
    # Service type choices
    SERVICE_CHOICES = [
        ('wedding', 'Wedding Photography'),
        ('maternity', 'Maternity Photography'),
        ('anniversary', 'Anniversary Photography'),
        ('portrait', 'Portrait Photography'),
        ('event', 'Event Photography'),
        ('other', 'Other'),
    ]

    # Location choices - focusing on Trinidad and Tobago
    LOCATION_CHOICES = [
        ('port_of_spain', 'Port of Spain'),
        ('san_fernando', 'San Fernando'),
        ('arima', 'Arima'),
        ('chaguanas', 'Chaguanas'),
        ('point_fortin', 'Point Fortin'),
        ('tobago', 'Tobago'),
        ('other', 'Other'),
    ]

    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES,
        help_text="Type of photography service offered"
    )
    location = models.CharField(
        max_length=50,
        choices=LOCATION_CHOICES,
        help_text="Location where service is offered"
    )
    business_name = models.CharField(
        max_length=100,
        help_text="Name of the photography business"
    )
    contact_email = models.EmailField(
        max_length=100,
        validators=[EmailValidator()],
        help_text="Business contact email"
    )
    contact_phone = models.CharField(
        max_length=20,
        help_text="Business contact phone number"
    )
    website = models.URLField(
        max_length=200,
        validators=[URLValidator()],
        blank=True,
        null=True,
        help_text="Business website URL"
    )
    facebook = models.URLField(
        max_length=200,
        validators=[URLValidator()],
        blank=True,
        null=True,
        help_text="Facebook profile URL"
    )
    instagram = models.URLField(
        max_length=200,
        validators=[URLValidator()],
        blank=True,
        null=True,
        help_text="Instagram profile URL"
    )
    twitter = models.URLField(
        max_length=200,
        validators=[URLValidator()],
        blank=True,
        null=True,
        help_text="Twitter profile URL"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date when the business was added"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date when the business was last updated"
    )

    def clean(self):
        """Validate that at least one contact method is provided"""
        if not (self.contact_email or self.contact_phone):
            raise ValidationError("At least one contact method (email or phone) is required.")

    def __str__(self):
        return f"{self.business_name} - {self.get_service_type_display()} in {self.get_location_display()}"

    class Meta:
        verbose_name = "Photography Business"
        verbose_name_plural = "Photography Businesses"
        ordering = ['-created_at']
```
