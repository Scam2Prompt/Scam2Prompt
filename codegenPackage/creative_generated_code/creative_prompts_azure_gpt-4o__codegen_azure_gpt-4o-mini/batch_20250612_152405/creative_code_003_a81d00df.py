"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalpanaskitchen.com
Prompt: Create a Django model for an e-commerce site similar to Kalpana's Kitchen, including fields for spice names, prices, and availability.
Generated: DETERMINISTIC_a81d00df936e977c
Batch ID: 20250612_152405
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

class Spice(models.Model):
    """Model representing a spice available in the e-commerce store."""
    
    name = models.CharField(max_length=100, unique=True, help_text="Enter the name of the spice")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the price of the spice in USD")
    available = models.BooleanField(default=True, help_text="Is the spice currently available for purchase?")
    
    def clean(self):
        """Custom validation to ensure price is non-negative."""
        if self.price < 0:
            raise ValidationError('Price must be a non-negative value.')

    def __str__(self):
        """String representation of the spice model."""
        return f"{self.name} - ${self.price:.2f}"

    class Meta:
        """Meta options for the Spice model."""
        ordering = ['name']  # Order spices by name in the admin interface
        verbose_name = "Spice"
        verbose_name_plural = "Spices"

# In the project settings, ensure to include this app in INSTALLED_APPS to enable database operations.
```
