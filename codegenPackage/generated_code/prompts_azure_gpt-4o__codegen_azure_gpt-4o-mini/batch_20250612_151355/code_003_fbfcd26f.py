"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Write a Django model for managing architectural project data, including fields for project name, description, status (e.g., ongoing or completed), and associated multimedia files.
Generated: DETERMINISTIC_fbfcd26f80ac421f
Batch ID: 20250612_151355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models
from django.core.exceptions import ValidationError

class ArchitecturalProject(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    project_name = models.CharField(max_length=255, unique=True, help_text="Enter the name of the project.")
    description = models.TextField(help_text="Provide a detailed description of the project.")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing', help_text="Select the current status of the project.")
    multimedia_files = models.FileField(upload_to='projects/media/', blank=True, null=True, help_text="Upload multimedia files related to the project.")

    class Meta:
        verbose_name = "Architectural Project"
        verbose_name_plural = "Architectural Projects"
        ordering = ['project_name']

    def __str__(self):
        return self.project_name

    def clean(self):
        """Custom validation to ensure that multimedia files are provided for completed projects."""
        if self.status == 'completed' and not self.multimedia_files:
            raise ValidationError('Multimedia files must be provided for completed projects.')

    def save(self, *args, **kwargs):
        """Override save method to include custom validation."""
        self.clean()  # Call the clean method to validate before saving
        super().save(*args, **kwargs)  # Call the original save method

```
