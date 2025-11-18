"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Create a Django model for managing faculty information, including fields for instrument specialization (e.g., vocal, guitar, saxophone) and teaching schedules, based on the Московский Колледж Импровизационной Музыки website.
Generated: DETERMINISTIC_c93528029baae4da
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models
from django.core.exceptions import ValidationError

# Faculty model to represent faculty information
class Faculty(models.Model):
    # Faculty name
    name = models.CharField(max_length=255, verbose_name="Full Name", help_text="Enter the full name of the faculty member.")

    # Instrument specialization
    instrument_specialization = models.CharField(
        max_length=100,
        verbose_name="Instrument Specialization",
        help_text="Enter the faculty member's specialization (e.g., vocal, guitar, saxophone)."
    )

    # Teaching schedule (JSON field for flexibility in storing schedule data)
    teaching_schedule = models.JSONField(
        verbose_name="Teaching Schedule",
        help_text="Enter the teaching schedule in JSON format (e.g., {'Monday': '10:00-12:00'}).",
        blank=True, null=True
    )

    # Additional fields for metadata
    email = models.EmailField(
        verbose_name="Email Address",
        help_text="Enter the faculty member's email address.",
        blank=True, null=True
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Phone Number",
        help_text="Enter the faculty member's phone number (optional).",
        blank=True, null=True
    )
    bio = models.TextField(
        verbose_name="Biography",
        help_text="Enter a brief biography of the faculty member.",
        blank=True, null=True
    )

    # Timestamps for record creation and update
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"
        ordering = ["name"]

    def clean(self):
        """
        Custom validation logic for the Faculty model.
        """
        # Ensure instrument specialization is provided
        if not self.instrument_specialization:
            raise ValidationError("Instrument specialization is a required field.")
        
        # Ensure teaching schedule is provided in JSON format and is valid
        if self.teaching_schedule and not isinstance(self.teaching_schedule, dict):
            raise ValidationError("Teaching schedule must be a valid JSON object.")

    def __str__(self):
        """
        String representation of the Faculty model for admin and debugging purposes.
        """
        return f"{self.name} - {self.instrument_specialization}"
```
