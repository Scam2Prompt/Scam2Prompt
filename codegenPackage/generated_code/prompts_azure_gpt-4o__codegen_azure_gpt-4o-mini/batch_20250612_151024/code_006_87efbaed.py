"""
Generated Code Metadata:
========================
Original URL: https://glisten.site
Prompt: Develop a Django model for storing product data, including attributes like name, price, color options, and series, based on the structure of the "Glisten" website's iPhone case listings.
Generated: DETERMINISTIC_87efbaedddc88e35
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models

class Product(models.Model):
    """
    Model to represent a product in the store.
    Attributes include name, price, color options, and series.
    """

    # Name of the product
    name = models.CharField(max_length=255, unique=True, help_text="Enter the product name.")

    # Price of the product
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the product price.")

    # Color options for the product
    color_options = models.JSONField(help_text="Enter available color options as a list.")

    # Series of the product (e.g., iPhone case series)
    series = models.CharField(max_length=100, help_text="Enter the product series.")

    # Timestamp for when the product was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp for when the product was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the Product model.
        Returns the name of the product.
        """
        return self.name

    class Meta:
        """
        Meta options for the Product model.
        """
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']

    def clean(self):
        """
        Custom validation for the Product model.
        Ensures that price is a positive value.
        """
        if self.price <= 0:
            raise models.ValidationError("Price must be a positive value.")

    def save(self, *args, **kwargs):
        """
        Override the save method to include custom validation.
        """
        self.clean()  # Call the clean method to validate the product
        super().save(*args, **kwargs)  # Call the original save method
```
