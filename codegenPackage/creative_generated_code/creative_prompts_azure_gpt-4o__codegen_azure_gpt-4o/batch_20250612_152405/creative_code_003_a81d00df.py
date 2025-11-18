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

class Spice(models.Model):
    """
    Django model representing a spice item in an e-commerce site.
    """

    # Name of the spice
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Enter the name of the spice (e.g., 'Turmeric', 'Cumin')."
    )

    # Price of the spice in USD
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Enter the price of the spice (e.g., '4.99')."
    )

    # Availability status
    is_available = models.BooleanField(
        default=True,
        help_text="Indicates if the spice is available for purchase."
    )

    # Timestamp for when the spice was added
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the spice was added to the database."
    )

    # Timestamp for when the spice information was last updated
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when the spice information was last updated."
    )

    def __str__(self):
        """
        String representation of the Spice object for display purposes.
        """
        return f"{self.name} - ${self.price}"

    class Meta:
        """
        Meta options for the Spice model.
        """
        verbose_name = "Spice"
        verbose_name_plural = "Spices"
        ordering = ["name"]  # Order spices by name alphabetically
```
