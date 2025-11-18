"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Write a Django model for an e-commerce platform that sells products like speakers, microphones, and headphones. Include fields for product name, category, price, and stock availability.
Generated: DETERMINISTIC_f45c3abf6fa43947
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models

class Product(models.Model):
    """
    Model representing a product in the e-commerce platform.
    """

    # Choices for product categories
    CATEGORY_CHOICES = [
        ('speakers', 'Speakers'),
        ('microphones', 'Microphones'),
        ('headphones', 'Headphones'),
    ]

    # Fields
    name = models.CharField(max_length=255, unique=True)  # Product name (unique and required)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='headphones'  # Default category if not specified
    )
    price = models.DecimalField(
        max_digits=10,  # Maximum of 10 digits in total (e.g., 99999.99)
        decimal_places=2,  # Two decimal places for cents
    )
    stock_available = models.PositiveIntegerField(default=0)  # Stock availability (non-negative integer)

    # Metadata
    class Meta:
        ordering = ['name']  # Order products alphabetically by name
        verbose_name = "Product"
        verbose_name_plural = "Products"

    # String representation
    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price}"

    # Custom save method for error handling (optional)
    def save(self, *args, **kwargs):
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        if self.stock_available < 0:
            raise ValueError("Stock availability cannot be negative.")
        super(Product, self).save(*args, **kwargs)
```
