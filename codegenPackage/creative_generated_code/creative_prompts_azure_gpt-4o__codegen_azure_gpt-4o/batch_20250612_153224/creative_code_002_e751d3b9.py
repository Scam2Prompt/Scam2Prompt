"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iyitixobond.com
Prompt: Create a Django model for an e-commerce site that includes product categories such as "Adhesive Joint Filler," "Epoxy Stain Remover," and "Wood Polisher," inspired by iyitixobond.com.
Generated: DETERMINISTIC_e751d3b9bcbf0373
Batch ID: 20250612_153224
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

class ProductCategory(models.Model):
    """
    Model representing product categories for an e-commerce site.
    Example categories include 'Adhesive Joint Filler', 'Epoxy Stain Remover', 'Wood Polisher', etc.
    """
    
    name = models.CharField(max_length=255, unique=True, help_text="Name of the product category.")
    description = models.TextField(blank=True, null=True, help_text="Optional description of the product category.")
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the category was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the category was last updated.")

    def __str__(self):
        """String representation of the ProductCategory model."""
        return self.name

class Product(models.Model):
    """
    Model representing individual products within the e-commerce site.
    Each product is assigned to a specific category.
    """
    
    name = models.CharField(max_length=255, help_text="Name of the product.")
    category = models.ForeignKey(
        ProductCategory, 
        on_delete=models.CASCADE, 
        related_name="products", 
        help_text="Category to which this product belongs."
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the product.")
    stock = models.PositiveIntegerField(help_text="Number of items available in stock.")
    description = models.TextField(blank=True, null=True, help_text="Optional description of the product.")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, help_text="Optional image of the product.")
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the product was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the product was last updated.")

    def __str__(self):
        """String representation of the Product model."""
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name"]  # Order products alphabetically by name
```
