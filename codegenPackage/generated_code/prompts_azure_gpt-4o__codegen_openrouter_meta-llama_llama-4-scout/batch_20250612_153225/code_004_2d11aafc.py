"""
Generated Code Metadata:
========================
Original URL: https://padmavatienterprise.org
Prompt: Write a Django model for managing inventory of industrial goods, including fields for categories such as "IT Materials," "Packing Materials," and "Gift Items," along with stock levels and pricing.
Generated: DETERMINISTIC_2d11aafc532aa3e0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class InventoryCategory(models.Model):
    """
    Model representing a category of industrial goods.
    """
    CATEGORY_CHOICES = [
        ("IT Materials", "IT Materials"),
        ("Packing Materials", "Packing Materials"),
        ("Gift Items", "Gift Items"),
        # Add more categories as needed
    ]

    name = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        unique=True,
    )

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    """
    Model representing an item in the inventory.
    """
    category = models.ForeignKey(
        InventoryCategory,
        on_delete=models.CASCADE,
        related_name="items",
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    stock_level = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class InventoryTransaction(models.Model):
    """
    Model representing a transaction (stock in or out) for an inventory item.
    """
    TRANSACTION_TYPE_CHOICES = [
        ("IN", "Stock In"),
        ("OUT", "Stock Out"),
    ]

    item = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    transaction_type = models.CharField(
        max_length=3,
        choices=TRANSACTION_TYPE_CHOICES,
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)],
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} - {self.transaction_type} - {self.quantity}"


class InventoryReport(models.Model):
    """
    Model representing a snapshot of the inventory levels at a point in time.
    """
    item = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE,
        related_name="reports",
    )
    stock_level = models.IntegerField()
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inventory Report for {self.item.name} at {self.timestamp}"
```

```python
# admin.py
from django.contrib import admin
from .models import InventoryCategory, InventoryItem, InventoryTransaction, InventoryReport

admin.site.register(InventoryCategory)
admin.site.register(InventoryItem)
admin.site.register(InventoryTransaction)
admin.site.register(InventoryReport)
```

```python
# apps.py
from django.apps import AppConfig

class InventoryAppConfig(AppConfig):
    name = 'inventory'
    verbose_name = "Inventory Management"

    def ready(self):
        pass
```

```python
# settings.py (example)
INSTALLED_APPS = [
    # ...
    'inventory.apps.InventoryAppConfig',
    # ...
]
```
