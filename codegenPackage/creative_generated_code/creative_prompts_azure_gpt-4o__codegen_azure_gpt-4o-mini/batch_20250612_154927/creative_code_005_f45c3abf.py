"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cafelc.com
Prompt: Write a Django model for an e-commerce platform that sells products like speakers, microphones, and headphones. Include fields for product name, category, price, and stock availability.
Generated: DETERMINISTIC_f45c3abf6fa43947
Batch ID: 20250612_154927
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
    A model representing a product available for sale in the e-commerce platform.
    
    Attributes:
        name (str): The name of the product.
        category (str): The category to which the product belongs (e.g., Speakers, Microphones, Headphones).
        price (Decimal): The price of the product, ensuring precision for monetary values.
        stock (int): The available stock for the product, indicating how many units are in inventory.
    """
    
    CATEGORY_CHOICES = [
        ('speakers', 'Speakers'),
        ('microphones', 'Microphones'),
        ('headphones', 'Headphones'),
    ]

    name = models.CharField(max_length=255, unique=True, help_text="Enter the product name.")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, help_text="Select the product category.")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the product price.")
    stock = models.PositiveIntegerField(default=0, help_text="Enter the available stock quantity.")

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        return f"{self.name} - {self.category}"

    def is_in_stock(self):
        """
        Check if the product is in stock.

        Returns:
            bool: True if the product is in stock, otherwise False.
        """
        return self.stock > 0

    def sell(self, quantity):
        """
        Decrease the stock of the product by the specified quantity if available.

        Parameters:
            quantity (int): The number of units to sell.

        Raises:
            ValueError: If the quantity to sell exceeds available stock.
        """
        if quantity > self.stock:
            raise ValueError("Insufficient stock available to sell.")
        self.stock -= quantity
        self.save()

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Products"
```
