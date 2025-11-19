"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Develop a Django model for an e-commerce platform to manage jewelry products with attributes like dual-tone finishes, gemstone types, and customizable fonts.
Generated: DETERMINISTIC_ab9a4e62ba7daaa2
Batch ID: 20250612_154506
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

class JewelryProduct(models.Model):
    """
    Model to represent a jewelry product in an e-commerce platform.
    Attributes include dual-tone finishes, gemstone types, and customizable fonts.
    """

    # Choices for dual-tone finishes
    FINISH_CHOICES = [
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('rose_gold', 'Rose Gold'),
        ('platinum', 'Platinum'),
    ]

    # Choices for gemstone types
    GEMSTONE_CHOICES = [
        ('diamond', 'Diamond'),
        ('ruby', 'Ruby'),
        ('sapphire', 'Sapphire'),
        ('emerald', 'Emerald'),
        ('amethyst', 'Amethyst'),
        ('topaz', 'Topaz'),
        ('opal', 'Opal'),
    ]

    # Fields for the JewelryProduct model
    name = models.CharField(max_length=255, unique=True, help_text="Name of the jewelry product.")
    description = models.TextField(help_text="Detailed description of the jewelry product.")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the jewelry product.")
    dual_tone_finish = models.CharField(max_length=20, choices=FINISH_CHOICES, help_text="Dual-tone finish of the jewelry.")
    gemstone_type = models.CharField(max_length=20, choices=GEMSTONE_CHOICES, help_text="Type of gemstone used in the jewelry.")
    customizable_font = models.CharField(max_length=100, blank=True, help_text="Font for customization, if applicable.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the product was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the product was last updated.")

    class Meta:
        verbose_name = "Jewelry Product"
        verbose_name_plural = "Jewelry Products"
        ordering = ['name']

    def __str__(self):
        """Return a string representation of the jewelry product."""
        return self.name

    def clean(self):
        """Custom validation to ensure price is positive."""
        if self.price <= 0:
            raise ValidationError('Price must be a positive number.')

    def save(self, *args, **kwargs):
        """Override save method to include custom validation."""
        self.clean()  # Call clean method to validate before saving
        super().save(*args, **kwargs)  # Call the original save method
```
