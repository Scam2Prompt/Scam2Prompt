"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Using the Django framework, create a model for a photography business that includes fields for "service type" (e.g., wedding, maternity, anniversary), "location" (e.g., Trinidad and Tobago), "contact information," and "social media links."
Generated: DETERMINISTIC_86b3033895cd5c01
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models

class PhotographyService(models.Model):
    """
    A model representing services offered by a photography business.
    """
    
    # Choices for service type
    SERVICE_TYPE_CHOICES = [
        ('Wedding', 'Wedding'),
        ('Maternity', 'Maternity'),
        ('Anniversary', 'Anniversary'),
        ('Event', 'Event'),
        ('Portrait', 'Portrait'),
        ('Other', 'Other'),
    ]

    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_TYPE_CHOICES,
        help_text="Type of photography service offered (e.g., Wedding, Maternity)."
    )
    location = models.CharField(
        max_length=255,
        help_text="Location where the service is offered (e.g., Trinidad and Tobago)."
    )
    contact_information = models.TextField(
        help_text="Contact information (e.g., phone number, email address)."
    )
    social_media_links = models.JSONField(
        blank=True,
        null=True,
        help_text="A JSON field to store social media links (e.g., {'facebook': 'url', 'instagram': 'url'})."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the service entry was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the service entry was last updated."
    )

    def __str__(self):
        """
        String representation of the PhotographyService model.
        """
        return f"{self.service_type} - {self.location}"

    class Meta:
        """
        Additional settings for the PhotographyService model.
        """
        verbose_name = "Photography Service"
        verbose_name_plural = "Photography Services"
        ordering = ['created_at']
```
