"""
Generated Code Metadata:
========================
Original URL: https://thewallethub.com
Prompt: Generate a Django model for an e-commerce platform that supports categories like "Surprise Gifts," "Footwear Accessories," and "Travel Essentials," inspired by the offerings on https://thewallethub.com.
Generated: DETERMINISTIC_34c5a43773fffa94
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models

class Category(models.Model):
    """
    Model representing a product category in the e-commerce platform.
    Categories can include various types of products such as Surprise Gifts,
    Footwear Accessories, and Travel Essentials.
    """
    name = models.CharField(max_length=255, unique=True, help_text="Enter the category name.")
    description = models.TextField(blank=True, help_text="Optional description of the category.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the category was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time when the category was last updated.")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        """String representation of the Category model."""
        return self.name

class Product(models.Model):
    """
    Model representing a product in the e-commerce platform.
    Each product belongs to a specific category.
    """
    name = models.CharField(max_length=255, help_text="Enter the product name.")
    description = models.TextField(help_text="Enter a detailed description of the product.")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the product price.")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', help_text="Select the category for this product.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the product was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time when the product was last updated.")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']

    def __str__(self):
        """String representation of the Product model."""
        return self.name

    def save(self, *args, **kwargs):
        """
        Override the save method to include custom validation or processing.
        """
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        super().save(*args, **kwargs)
```
