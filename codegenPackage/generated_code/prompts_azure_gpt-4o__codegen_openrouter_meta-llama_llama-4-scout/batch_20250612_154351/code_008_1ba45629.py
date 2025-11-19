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
# models.py
from django.db import models

class JobCategory(models.Model):
    """
    Represents a job category.

    Attributes:
        name (str): The name of the job category.
        slug (str): A unique slug for the job category.
        created_at (datetime): The timestamp when the job category was created.
        updated_at (datetime): The timestamp when the job category was last updated.
    """

    class Meta:
        verbose_name = "Job Category"
        verbose_name_plural = "Job Categories"
        ordering = ["name"]

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.name.replace(" ", "-").lower()
        super().save(*args, **kwargs)
```

```python
# admin.py
from django.contrib import admin
from .models import JobCategory

class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(JobCategory, JobCategoryAdmin)
```

```python
# apps.py
from django.apps import AppConfig

class CareersConfig(AppConfig):
    name = "careers"
    verbose_name = "Careers"
```

```python
# settings.py (example usage)
INSTALLED_APPS = [
    # ...
    "careers.apps.CareersConfig",
    # ...
]

# Run the following commands to create and apply migrations:
# python manage.py makemigrations
# python manage.py migrate
```
