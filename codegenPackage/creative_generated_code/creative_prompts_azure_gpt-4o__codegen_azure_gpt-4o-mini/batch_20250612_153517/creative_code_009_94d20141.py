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
# models.py

from django.db import models

class Category(models.Model):
    """
    Model representing a product category.
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model representing a product in the inventory.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Optional field for product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with two decimal places
    stock_quantity = models.PositiveIntegerField(default=0)  # Stock quantity must be a positive integer
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Relationship with Category

    def __str__(self):
        return self.name

    def is_in_stock(self):
        """
        Check if the product is currently in stock.
        """
        return self.stock_quantity > 0

    def update_stock(self, quantity):
        """
        Update the stock quantity for the product.
        Args:
            quantity (int): The amount to add or subtract from the stock.
        """
        if quantity < 0 and abs(quantity) > self.stock_quantity:
            raise ValueError("Cannot reduce stock below zero.")
        
        self.stock_quantity += quantity
        self.save()  # Save the updated product to the database

# Example usage:
# category1 = Category.objects.create(name='Scule electrice')
# product1 = Product.objects.create(name='Drill', price=150.00, stock_quantity=10, category=category1)
```
