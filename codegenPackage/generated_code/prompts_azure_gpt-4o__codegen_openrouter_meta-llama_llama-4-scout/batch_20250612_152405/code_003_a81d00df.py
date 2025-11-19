"""
Generated Code Metadata:
========================
Original URL: https://kalpanaskitchen.com
Prompt: Create a Django model for an e-commerce site similar to Kalpana's Kitchen, including fields for spice names, prices, and availability.
Generated: DETERMINISTIC_a81d00df936e977c
Batch ID: 20250612_152405
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
from django.core.validators import MinValueValidator, MaxValueValidator

class Spice(models.Model):
    """
    Model representing a spice in the e-commerce database.
    """

    class SpiceCategory(models.TextChoices):
        """Enum for spice categories."""
        HERBS = 'herbs'
        SPICES = 'spices'
        BLENDS = 'blends'
        SEASONINGS = 'seasonings'

    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=10, choices=SpiceCategory.choices, default=SpiceCategory.SPICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    availability = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Spice'
        verbose_name_plural = 'Spices'
```

```python
# admin.py
from django.contrib import admin
from .models import Spice

class SpiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'availability')
    list_filter = ('category',)
    search_fields = ('name',)

admin.site.register(Spice, SpiceAdmin)
```

```python
# apps.py
from django.apps import AppConfig

class EcommerceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce'
```

```python
# settings.py (snippet)
INSTALLED_APPS = [
    # ...
    'ecommerce.apps.EcommerceAppConfig',
    # ...
]

# Run the following commands to create and apply database migrations:
# python manage.py makemigrations
# python manage.py migrate
```
