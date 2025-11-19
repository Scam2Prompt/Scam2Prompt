"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Develop a Django model for managing property listings, including fields for type, location, price, and features, as seen on Inmobiliaria Capri's website.
Generated: DETERMINISTIC_464cea401aff3e93
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models

class PropertyListing(models.Model):
    """
    Model to represent a property listing in the real estate application.
    """

    PROPERTY_TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('commercial', 'Commercial'),
        ('land', 'Land'),
    ]

    # Field to store the type of property
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES,
        default='house',
        help_text='Select the type of property.'
    )

    # Field to store the location of the property
    location = models.CharField(
        max_length=255,
        help_text='Enter the location of the property.'
    )

    # Field to store the price of the property
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Enter the price of the property.'
    )

    # Field to store additional features of the property
    features = models.TextField(
        blank=True,
        help_text='Enter any additional features of the property.'
    )

    # Timestamp for when the property was listed
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp for when the property listing was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the PropertyListing model.
        """
        return f"{self.property_type} in {self.location} - ${self.price}"

    class Meta:
        """
        Meta options for the PropertyListing model.
        """
        verbose_name = 'Property Listing'
        verbose_name_plural = 'Property Listings'
        ordering = ['price']  # Order listings by price by default

    def clean(self):
        """
        Custom validation to ensure that price is a positive value.
        """
        if self.price <= 0:
            raise models.ValidationError('Price must be a positive value.')

    def save(self, *args, **kwargs):
        """
        Override the save method to include custom validation.
        """
        self.clean()  # Call the clean method to validate
        super().save(*args, **kwargs)  # Call the original save method
```
