"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Develop a Django model for managing property listings, including fields for type, location, price, and features, as seen on Inmobiliaria Capri's website.
Generated: DETERMINISTIC_464cea401aff3e93
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models

class PropertyListing(models.Model):
    """Model representing a property listing in the real estate system."""

    PROPERTY_TYPE_CHOICES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('commercial', 'Commercial'),
        ('land', 'Land'),
        ('other', 'Other'),
    ]

    # Field for the type of property
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES,
        default='other',
        verbose_name='Type of Property',
    )

    # Field for the location of the property
    location = models.CharField(
        max_length=255,
        verbose_name='Location',
    )

    # Field for the price of the property
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Price',
    )

    # Field for additional features of the property
    features = models.TextField(
        blank=True,
        verbose_name='Features',
    )

    # Timestamp for when the listing was created
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date Created',
    )

    # Timestamp for when the listing was last updated
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date Updated',
    )

    class Meta:
        ordering = ['-created_at']  # Order listings by most recent first

    def __str__(self):
        """Return a string representation of the property listing."""
        return f"{self.property_type} in {self.location} - ${self.price}"

    def clean(self):
        """Custom validation for the model fields."""
        if self.price < 0:
            raise ValueError("Price cannot be negative.")

    def save(self, *args, **kwargs):
        """Override save method to include custom validation."""
        self.clean()  # Ensure clean() is called before saving
        super(PropertyListing, self).save(*args, **kwargs)  # Call the original save method
```
