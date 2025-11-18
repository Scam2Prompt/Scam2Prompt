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
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    """
    Represents a category of products in the e-commerce platform.
    Categories include Surprise Gifts, Footwear Accessories, and Travel Essentials.
    """
    name = models.CharField(
        max_length=255, 
        unique=True, 
        verbose_name=_("Category Name"),
        help_text=_("The name of the category (e.g., Surprise Gifts, Footwear Accessories, Travel Essentials).")
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name=_("Description"),
        help_text=_("Optional brief description of the category.")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_("Created At"),
        help_text=_("The timestamp when the category was created.")
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name=_("Updated At"),
        help_text=_("The timestamp when the category was last updated.")
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["name"]  # Categories will be ordered by name alphabetically.

    def __str__(self):
        """
        String representation of the Category model.
        """
        return self.name


class Product(models.Model):
    """
    Represents a product in the e-commerce platform.
    Each product belongs to a specific category.
    """
    name = models.CharField(
        max_length=255, 
        verbose_name=_("Product Name"),
        help_text=_("The name of the product.")
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name=_("Description"),
        help_text=_("Optional brief description of the product.")
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name=_("Price"),
        help_text=_("The price of the product.")
    )
    stock = models.PositiveIntegerField(
        verbose_name=_("Stock"),
        help_text=_("The number of units available in stock.")
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="products",
        verbose_name=_("Category"),
        help_text=_("The category to which the product belongs.")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name=_("Created At"),
        help_text=_("The timestamp when the product was created.")
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name=_("Updated At"),
        help_text=_("The timestamp when the product was last updated.")
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["name"]  # Products will be ordered by name alphabetically.

    def __str__(self):
        """
        String representation of the Product model.
        """
        return self.name
```
