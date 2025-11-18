"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tanhungco.vn
Prompt: Write a Django model for storing agricultural product data, including fields for product name, category (e.g., "Thuốc trừ sâu"), and description, referencing examples like "Seroto 224SC" and "Badang 95."
Generated: DETERMINISTIC_87b57825b68dbe8c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models

class AgriculturalProduct(models.Model):
    """
    A model for storing agricultural product data, including name, category, and description.
    """
    
    # Name of the agricultural product (e.g., "Seroto 224SC")
    name = models.CharField(
        max_length=255, 
        null=False, 
        blank=False, 
        help_text="Name of the agricultural product (e.g., 'Seroto 224SC')."
    )
    
    # Category of the agricultural product (e.g., "Thuốc trừ sâu")
    category = models.CharField(
        max_length=255, 
        null=False, 
        blank=False, 
        help_text="Category of the product (e.g., 'Thuốc trừ sâu')."
    )
    
    # Detailed description of the agricultural product
    description = models.TextField(
        null=True, 
        blank=True, 
        help_text="Detailed description of the product (Optional)."
    )
    
    # Timestamps for tracking creation and updates
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="Timestamp indicating when the product was added."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="Timestamp indicating when the product was last updated."
    )
    
    def __str__(self):
        """
        String representation of the agricultural product.
        Returns the product's name for display purposes.
        """
        return self.name

    class Meta:
        """
        Meta options for the AgriculturalProduct model.
        """
        verbose_name = "Agricultural Product"
        verbose_name_plural = "Agricultural Products"
        ordering = ['name']  # Sort products alphabetically by name
```
