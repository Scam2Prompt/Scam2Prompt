"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allorashopping.com
Prompt: Develop a Django model to store product attributes such as style (e.g., preppy, grunge, formal wear), material (e.g., lace, cotton blend), and fit (e.g., cropped fit, boxy fit).
Generated: DETERMINISTIC_abaeb012d1df7444
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.db import models

class ProductAttribute(models.Model):
    """
    Model to store product attributes such as style, material, and fit.
    """
    
    # Choices for various attributes
    STYLE_CHOICES = [
        ('preppy', 'Preppy'),
        ('grunge', 'Grunge'),
        ('formal_wear', 'Formal Wear'),
    ]
    
    MATERIAL_CHOICES = [
        ('lace', 'Lace'),
        ('cotton_blend', 'Cotton Blend'),
        ('denim', 'Denim'),
        ('wool', 'Wool'),
    ]
    
    FIT_CHOICES = [
        ('cropped_fit', 'Cropped Fit'),
        ('boxy_fit', 'Boxy Fit'),
        ('slim_fit', 'Slim Fit'),
        ('regular_fit', 'Regular Fit'),
    ]

    # Fields to store attribute data
    style = models.CharField(
        max_length=50, 
        choices=STYLE_CHOICES, 
        default='preppy',
        help_text="The style of the product (e.g., preppy, grunge, formal wear)."
    )
    material = models.CharField(
        max_length=50, 
        choices=MATERIAL_CHOICES, 
        default='cotton_blend',
        help_text="The material of the product (e.g., lace, cotton blend)."
    )
    fit = models.CharField(
        max_length=50, 
        choices=FIT_CHOICES, 
        default='regular_fit',
        help_text="The fit of the product (e.g., cropped fit, boxy fit)."
    )

    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The timestamp when the product attribute was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The timestamp when the product attribute was last updated."
    )

    def __str__(self):
        """
        String representation for the model.
        """
        return f"{self.style.capitalize()} - {self.material.capitalize()} - {self.fit.capitalize()}"

    class Meta:
        """
        Meta options for the ProductAttribute model.
        """
        verbose_name = "Product Attribute"
        verbose_name_plural = "Product Attributes"
        ordering = ['style', 'material', 'fit']

```
