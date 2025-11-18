"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://padmavatienterprise.org
Prompt: Write a Django model for managing inventory of industrial goods, including fields for categories such as "IT Materials," "Packing Materials," and "Gift Items," along with stock levels and pricing.
Generated: DETERMINISTIC_2d11aafc532aa3e0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models
from django.core.validators import MinValueValidator

class CategoryChoices(models.TextChoices):
    """Enum-like structure for category choices."""
    IT_MATERIALS = 'IT Materials', 'IT Materials'
    PACKING_MATERIALS = 'Packing Materials', 'Packing Materials'
    GIFT_ITEMS = 'Gift Items', 'Gift Items'

class InventoryItem(models.Model):
    """
    Model for managing inventory of industrial goods.
    """
    name = models.CharField(
        max_length=255,
        help_text="Name of the inventory item."
    )
    category = models.CharField(
        max_length=50,
        choices=CategoryChoices.choices,
        help_text="Category of the item (e.g., IT Materials, Packing Materials, Gift Items)."
    )
    stock_level = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Current stock level of the item."
    )
    price_per_unit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Price per unit of the item (in dollars)."
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp of the last update to this item's information."
    )

    def __str__(self):
        """
        Return a human-readable representation of the inventory item.
        """
        return f"{self.name} ({self.category})"

    class Meta:
        """
        Meta options for the InventoryItem model.
        """
        verbose_name = "Inventory Item"
        verbose_name_plural = "Inventory Items"
        ordering = ['category', 'name']  # Sort by category, then name for easier management.
        indexes = [
            models.Index(fields=['category']),  # Add index for quick category-based lookups.
            models.Index(fields=['name']),     # Add index for quick name-based lookups.
        ]
```
