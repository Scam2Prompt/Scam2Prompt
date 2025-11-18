"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Develop a Django model for an e-commerce platform to manage jewelry products with attributes like dual-tone finishes, gemstone types, and customizable fonts.
Generated: DETERMINISTIC_ab9a4e62ba7daaa2
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models

class JewelryProduct(models.Model):
    """
    A model representing a jewelry product in an e-commerce platform.
    
    Attributes:
        name (str): The name of the jewelry product.
        description (str): A detailed description of the product.
        price (Decimal): The price of the product.
        dual_tone_finish (bool): Indicates if the product has a dual-tone finish.
        gemstone_type (str): The type of gemstone used in the jewelry.
        customizable_font (str): The font customization option for engravings.
        created_at (datetime): The timestamp when the product was created.
        updated_at (datetime): The timestamp when the product was last updated.
    """
    
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dual_tone_finish = models.BooleanField(default=False)
    gemstone_type = models.CharField(max_length=100, blank=True)
    customizable_font = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Jewelry Product"
        verbose_name_plural = "Jewelry Products"
        ordering = ['name']

    def __str__(self):
        """Return the string representation of the JewelryProduct."""
        return self.name

    def clean(self):
        """
        Ensure that any necessary validations are performed before saving.
        Raise ValidationError if validations fail.
        """
        super().clean()
        if self.price < 0:
            raise ValueError("Price must be a non-negative value.")
        if self.dual_tone_finish and self.customizable_font == '':
            raise ValueError("Customizable font must be specified for dual-tone finishes.")

    def save(self, *args, **kwargs):
        """
        Override the save method to include custom validation.
        """
        self.clean()  # Call the clean method to validate before saving.
        super().save(*args, **kwargs)  # Call the superclass save method.

# To use this model, make sure to run migrations after creating it:
# python manage.py makemigrations
# python manage.py migrate
```
