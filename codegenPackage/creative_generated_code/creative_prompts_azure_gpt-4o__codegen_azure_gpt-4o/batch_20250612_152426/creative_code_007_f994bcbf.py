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

class ProductCategory(models.Model):
    """
    Model to represent product categories in a medical supply e-commerce platform.
    Examples: 'Cuidado de Heridas', 'Material para Curación'.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Name of the product category (e.g., 'Cuidado de Heridas')."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional description of the product category."
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Indicates whether this category is active and visible to users."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the category was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when the category was last updated."
    )

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"
        ordering = ['name']  # Orders categories alphabetically by name.

    def __str__(self):
        """
        String representation of the category instance.
        """
        return self.name

    def save(self, *args, **kwargs):
        """
        Override the save method to handle custom logic, if needed.
        """
        try:
            super().save(*args, **kwargs)
        except Exception as e:
            # Log the exception (logging setup not shown here)
            raise ValueError(f"Failed to save ProductCategory: {e}")

    @property
    def short_description(self):
        """
        Returns a shortened version of the description (limited to 50 characters).
        Useful for displaying in summaries or previews.
        """
        if self.description:
            return self.description[:50] + "..." if len(self.description) > 50 else self.description
        return "No description available."
```
