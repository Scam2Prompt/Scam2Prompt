"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glisten.site
Prompt: Develop a Django model for storing product data, including attributes like name, price, color options, and series, based on the structure of the "Glisten" website's iPhone case listings.
Generated: DETERMINISTIC_87efbaedddc88e35
Batch ID: 20250612_151024
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
    Model to store product details like name, price, color options, and series.
    """

    # Name of the product
    name = models.CharField(max_length=255, null=False, blank=False, help_text="Name of the product")
    
    # Price of the product
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, help_text="Price of the product")
    
    # Available color options for the product
    color_options = models.JSONField(null=False, blank=False, help_text="Available color options as a JSON list")
    
    # Series/category the product belongs to
    series = models.CharField(max_length=255, null=True, blank=True, help_text="Series or category of the product")
    
    # Timestamp for when the product was added
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the product was created")
    
    # Timestamp for when the product details were last updated
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the product was last updated")

    class Meta:
        # Adding metadata for the model
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]

    def __str__(self):
        """
        String representation of the model.
        This will be displayed in the Django admin interface.
        """
        return self.name

    def clean(self):
        """
        Custom validation logic for the model.
        Checks for valid data before saving it to the database.
        """
        if self.price <= 0:
            raise ValueError("Price must be greater than zero")
        if not isinstance(self.color_options, list):
            raise ValueError("Color options must be a list")
```
