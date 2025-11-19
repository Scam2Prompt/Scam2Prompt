"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: Develop a Django model for an online store's inventory system, including fields for categories such as "Scule electrice," "Roti si anvelope," and "Uz casnic."
Generated: DETERMINISTIC_94d20141f2946a08
Batch ID: 20250612_153517
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
    Model representing a category of products in the inventory.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model representing a product in the inventory.
    """
    CATEGORY_CHOICES = [
        ('scule_electrice', 'Scule electrice'),
        ('roti_si_anvelope', 'Roti si anvelope'),
        ('uz_casnic', 'Uz casnic'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def is_in_stock(self):
        """
        Check if the product is in stock.
        """
        return self.stock_quantity > 0

    def restock(self, quantity):
        """
        Restock the product with the given quantity.
        """
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self.stock_quantity += quantity
        self.save()

    def sell(self, quantity):
        """
        Sell the product, reducing the stock quantity.
        """
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if quantity > self.stock_quantity:
            raise ValueError("Not enough stock available.")
        self.stock_quantity -= quantity
        self.save()
```
