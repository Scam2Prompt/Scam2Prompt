"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://careeratjayamwebsolutions.com
Prompt: Create a Django model to represent job categories like "Digital Marketing" and "Web Developer" from Jayam Web Solutions' careers page.
Generated: DETERMINISTIC_1ba4562949e91a79
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

class JobCategory(models.Model):
    """
    Model representing a job category.

    Attributes:
        name (str): The name of the job category (e.g., "Digital Marketing", "Web Developer").
        description (str): A brief description of the job category.
        created_at (datetime): The timestamp when the job category was created.
        updated_at (datetime): The timestamp when the job category was last updated.
    """
    
    name = models.CharField(max_length=100, unique=True, help_text="Enter the job category name.")
    description = models.TextField(blank=True, help_text="Enter a brief description of the job category.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the job category was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the job category was last updated.")

    def __str__(self):
        """Returns a string representation of the job category."""
        return self.name

    class Meta:
        verbose_name = "Job Category"
        verbose_name_plural = "Job Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        """
        Override save method to handle any specific logic on saving the job category.

        Args:
            *args: Positional arguments to pass to the superclass save method.
            **kwargs: Keyword arguments to pass to the superclass save method.
        """
        try:
            super().save(*args, **kwargs)
        except Exception as e:
            # Handle exception and log it accordingly
            raise Exception(f"Error saving JobCategory: {str(e)}")

```
