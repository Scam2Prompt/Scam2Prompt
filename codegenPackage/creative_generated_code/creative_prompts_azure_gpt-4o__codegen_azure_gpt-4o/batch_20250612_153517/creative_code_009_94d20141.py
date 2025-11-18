"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Develop a Django model for an online store's inventory system, including fields for categories such as "Scule electrice," "Roti si anvelope," and "Uz casnic."
Generated: DETERMINISTIC_94d20141f2946a08
Batch ID: 20250612_153517
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
    """
    Model to represent product categories in the inventory system.
    Example categories: 'Scule electrice', 'Roti si anvelope', 'Uz casnic'
    """
    name = models.CharField(max_length=255, unique=True)  # Name of the category
    description = models.TextField(blank=True, null=True)  # Optional description of the category
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the category is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the category is last updated

    def __str__(self):
        return self.name  # Display category name in admin or shell

class Product(models.Model):
    """
    Model to represent products in the inventory system.
    Each product belongs to a specific category.
    """
    name = models.CharField(max_length=255)  # Name of the product
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  
    # Category the product belongs to. Deletes all associated products when the category is deleted.
    
    description = models.TextField(blank=True, null=True)  # Optional description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product (e.g., 9999.99)
    stock = models.PositiveIntegerField(default=0)  # Quantity of the product in stock
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the product is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the product is last updated

    def __str__(self):
        return self.name  # Display product name in admin or shell

    def is_in_stock(self):
        """
        Returns True if the product is in stock, False otherwise.
        """
        return self.stock > 0

    def save(self, *args, **kwargs):
        """
        Overriding the save method to ensure price is positive before saving.
        """
        if self.price < 0:
            raise ValueError("Price cannot be negative.")
        super().save(*args, **kwargs)
```
