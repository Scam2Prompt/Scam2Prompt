"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thewallethub.com
Prompt: Generate a Django model for an e-commerce platform that supports categories like "Surprise Gifts," "Footwear Accessories," and "Travel Essentials," inspired by the offerings on https://thewallethub.com.
Generated: DETERMINISTIC_34c5a43773fffa94
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models

class Category(models.Model):
    """Model representing a product category."""

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, help_text="Optional description of the category.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        """String representation of the Category model."""
        return self.name


class Product(models.Model):
    """Model representing a product in the e-commerce platform."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    stock_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']

    def __str__(self):
        """String representation of the Product model."""
        return self.name

    def is_in_stock(self):
        """Check if the product is in stock."""
        return self.stock_quantity > 0

    def reduce_stock(self, quantity):
        """Reduce the stock quantity by the specified amount.

        Args:
            quantity (int): The amount to reduce the stock by.

        Raises:
            ValueError: If the quantity to reduce is greater than the current stock.
        """
        if quantity > self.stock_quantity:
            raise ValueError("Cannot reduce stock below zero.")
        self.stock_quantity -= quantity
        self.save()
```
