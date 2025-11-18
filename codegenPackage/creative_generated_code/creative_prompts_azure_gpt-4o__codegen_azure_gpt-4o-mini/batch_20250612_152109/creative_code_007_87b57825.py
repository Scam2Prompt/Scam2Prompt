"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Write a Django model for storing agricultural product data, including fields for product name, category (e.g., "Thuốc trừ sâu"), and description, referencing examples like "Seroto 224SC" and "Badang 95."
Generated: DETERMINISTIC_87b57825b68dbe8c
Batch ID: 20250612_152109
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

class AgriculturalProduct(models.Model):
    """Model representing an agricultural product."""

    # Product name as a character field with a max length of 255 characters
    name = models.CharField(max_length=255, unique=True, verbose_name="Product Name")
    
    # Category with choices, allowing only specific predefined values
    CATEGORY_CHOICES = [
        ('Pesticide', 'Pesticide'),
        ('Fertilizer', 'Fertilizer'),
        ('Seed', 'Seed'),
        ('Herbicide', 'Herbicide'),
        ('Fungicide', 'Fungicide'),
        ('Other', 'Other'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Category")
    
    # Description providing additional information about the product
    description = models.TextField(blank=True, verbose_name="Description")

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name} ({self.category})"

    def clean(self):
        """Custom validation to ensure data integrity."""
        if not self.name:
            raise ValidationError("Product name cannot be empty.")
        if self.category not in dict(self.CATEGORY_CHOICES).keys():
            raise ValidationError("Invalid category selected.")

    class Meta:
        """Meta class to define additional options for the model."""
        verbose_name = "Agricultural Product"
        verbose_name_plural = "Agricultural Products"
        ordering = ['name']  # Default ordering by product name
```
