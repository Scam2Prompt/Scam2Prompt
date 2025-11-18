"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Write a Django model for managing product categories such as "Cuidado de Heridas" and "Material para Curación" in a medical supply e-commerce platform.
Generated: DETERMINISTIC_f994bcbfb6e182cc
Batch ID: 20250612_152426
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

class ProductCategory(models.Model):
    """
    Model representing a product category in the medical supply e-commerce platform.
    Each category can contain multiple products associated with it.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Category Name"),
        help_text=_("Enter the name of the product category.")
    )

    description = models.TextField(
        blank=True,
        verbose_name=_("Description"),
        help_text=_("Optional description of the product category.")
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At"),
        help_text=_("The date and time when the category was created.")
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated At"),
        help_text=_("The date and time when the category was last updated.")
    )

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")
        ordering = ['name']

    def __str__(self):
        """String representation of the ProductCategory model."""
        return self.name

    def save(self, *args, **kwargs):
        """Override the save method to include custom error handling."""
        try:
            super().save(*args, **kwargs)
        except Exception as e:
            # Log the exception or handle it as needed
            raise ValueError(_("An error occurred while saving the category: ") + str(e))
```
