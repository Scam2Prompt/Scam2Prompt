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
from django.core.exceptions import ValidationError

class ProductAttribute(models.Model):
    """
    A model to store product attributes such as style, material, and fit.
    """

    STYLES = [
        ('preppy', 'Preppy'),
        ('grunge', 'Grunge'),
        ('formal_wear', 'Formal Wear'),
        # Add more styles as needed
    ]

    MATERIALS = [
        ('lace', 'Lace'),
        ('cotton_blend', 'Cotton Blend'),
        # Add more materials as needed
    ]

    FITS = [
        ('cropped_fit', 'Cropped Fit'),
        ('boxy_fit', 'Boxy Fit'),
        # Add more fits as needed
    ]

    style = models.CharField(
        max_length=50, 
        choices=STYLES, 
        help_text="Select the style of the product."
    )
    material = models.CharField(
        max_length=50, 
        choices=MATERIALS, 
        help_text="Select the material of the product."
    )
    fit = models.CharField(
        max_length=50, 
        choices=FITS, 
        help_text="Select the fit of the product."
    )

    def clean(self):
        """
        Custom validation to ensure that the attributes are not blank.
        """
        if not self.style or not self.material or not self.fit:
            raise ValidationError("All fields must be filled out.")

    def __str__(self):
        """
        String representation of the ProductAttribute object.
        """
        return f"{self.style}, {self.material}, {self.fit}"

    class Meta:
        verbose_name = "Product Attribute"
        verbose_name_plural = "Product Attributes"
        unique_together = ('style', 'material', 'fit')

```
