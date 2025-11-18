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
    """
    Model representing a property listing for Inmobiliaria Capri.
    Contains details such as type, location, price, and features.
    """
    
    # Choices for property type
    PROPERTY_TYPE_CHOICES = [
        ('AP', 'Apartment'),
        ('HS', 'House'),
        ('OF', 'Office'),
        ('ST', 'Store'),
        ('OT', 'Other'),
    ]
    
    type = models.CharField(
        max_length=2,
        choices=PROPERTY_TYPE_CHOICES,
        verbose_name="Property Type",
        help_text="Select the type of property (e.g., Apartment, House)."
    )
    location = models.CharField(
        max_length=255,
        verbose_name="Location",
        help_text="Provide the address or general location of the property."
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price",
        help_text="Specify the price of the property in decimal format."
    )
    features = models.TextField(
        blank=True,
        verbose_name="Features",
        help_text="Provide details about the features or amenities of the property."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="Timestamp when the listing was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="Timestamp when the listing was last updated."
    )

    def __str__(self):
        """
        Returns a string representation of the property listing.
        Includes the type and location for better readability.
        """
        return f"{self.get_type_display()} - {self.location}"

    class Meta:
        """
        Metadata for the PropertyListing model. Includes options
        for database table name and default ordering.
        """
        verbose_name = "Property Listing"
        verbose_name_plural = "Property Listings"
        ordering = ['-created_at']
```
