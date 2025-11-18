"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://padmavatienterprise.org
Prompt: Write a Django model for managing inventory of industrial goods, including fields for categories such as "IT Materials," "Packing Materials," and "Gift Items," along with stock levels and pricing.
Generated: DETERMINISTIC_2d11aafc532aa3e0
Batch ID: 20250612_153225
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

class Category(models.Model):
    """Model representing a category of industrial goods."""
    
    CATEGORY_CHOICES = [
        ('IT', 'IT Materials'),
        ('PM', 'Packing Materials'),
        ('GI', 'Gift Items'),
    ]
    
    name = models.CharField(max_length=2, choices=CATEGORY_CHOICES, unique=True)
    
    def __str__(self):
        return dict(self.CATEGORY_CHOICES).get(self.name, 'Unknown Category')


class InventoryItem(models.Model):
    """Model for managing inventory of industrial goods."""
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    stock_level = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def clean(self):
        """Custom validation for the InventoryItem model."""
        if self.stock_level < 0:
            raise ValidationError('Stock level cannot be negative.')
        if self.price < 0:
            raise ValidationError('Price cannot be negative.')

    def save(self, *args, **kwargs):
        """Override save method to include validation."""
        self.clean()  # Call clean to enforce validation
        super().save(*args, **kwargs)  # Call the parent save method

    def __str__(self):
        return f"{self.name} ({self.category}) - Stock: {self.stock_level}, Price: {self.price}"
```
