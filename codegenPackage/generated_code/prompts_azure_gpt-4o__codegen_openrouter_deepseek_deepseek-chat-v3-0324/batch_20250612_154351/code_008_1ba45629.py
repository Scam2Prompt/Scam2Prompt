"""
Generated Code Metadata:
========================
Original URL: https://careeratjayamwebsolutions.com
Prompt: Create a Django model to represent job categories like "Digital Marketing" and "Web Developer" from Jayam Web Solutions' careers page.
Generated: DETERMINISTIC_1ba4562949e91a79
Batch ID: 20250612_154351
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
from django.utils.translation import gettext_lazy as _


class JobCategory(models.Model):
    """
    Represents a job category for Jayam Web Solutions' careers page.
    Example categories: "Digital Marketing", "Web Developer", etc.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="The name of the job category (e.g., 'Digital Marketing')"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text="URL-friendly version of the name (auto-generated if blank)"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional description of the job category"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this category is currently active/visible"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When this category was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="When this category was last updated"
    )

    class Meta:
        verbose_name = "Job Category"
        verbose_name_plural = "Job Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def clean(self):
        """
        Validate the model before saving.
        """
        if not self.slug:
            self.slug = self.name.lower().replace(' ', '-')
        
        if len(self.name) < 2:
            raise ValidationError(_("Category name must be at least 2 characters long."))

    def save(self, *args, **kwargs):
        """
        Override save to ensure clean() is called and slug is properly set.
        """
        self.full_clean()
        super().save(*args, **kwargs)
```
