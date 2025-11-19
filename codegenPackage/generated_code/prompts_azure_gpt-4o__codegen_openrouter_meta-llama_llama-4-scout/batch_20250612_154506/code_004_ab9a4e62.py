"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Develop a Django model for an e-commerce platform to manage jewelry products with attributes like dual-tone finishes, gemstone types, and customizable fonts.
Generated: DETERMINISTIC_ab9a4e62ba7daaa2
Batch ID: 20250612_154506
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

class GemstoneType(models.Model):
    """Model representing a gemstone type."""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class JewelryProduct(models.Model):
    """Model representing a jewelry product."""
    class Finishes(models.TextChoices):
        GOLD = 'GOLD', 'Gold'
        SILVER = 'SILVER', 'Silver'
        ROSE_GOLD = 'ROSE_GOLD', 'Rose Gold'
        DUAL_TONE = 'DUAL_TONE', 'Dual Tone'

    class FontStyles(models.TextChoices):
        ARIAL = 'ARIAL', 'Arial'
        TIMES_NEW_ROMAN = 'TIMES_NEW_ROMAN', 'Times New Roman'
        CALIBRI = 'CALIBRI', 'Calibri'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    finish = models.CharField(max_length=10, choices=Finishes.choices, default=Finishes.GOLD)
    gemstone_type = models.ManyToManyField(GemstoneType)
    font_style = models.CharField(max_length=20, choices=FontStyles.choices, default=FontStyles.ARIAL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CustomizableJewelryProduct(JewelryProduct):
    """Model representing a customizable jewelry product."""
    engraving_text = models.CharField(max_length=255, blank=True)
    font_size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=12)

    def __str__(self):
        return f"Customizable {super().__str__()}"

class ProductImage(models.Model):
    """Model representing a product image."""
    product = models.ForeignKey(JewelryProduct, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f"Image for {self.product.name}"
```

```python
# admin.py
from django.contrib import admin
from .models import JewelryProduct, GemstoneType, CustomizableJewelryProduct, ProductImage

admin.site.register(GemstoneType)
admin.site.register(JewelryProduct)
admin.site.register(CustomizableJewelryProduct)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class JewelryProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(JewelryProduct, JewelryProductAdmin)
```

```python
# apps.py
from django.apps import AppConfig

class EcommerceConfig(AppConfig):
    name = 'ecommerce'
    verbose_name = 'E-commerce Platform'
```

```python
# settings.py (example)
INSTALLED_APPS = [
    # ...
    'ecommerce.apps.EcommerceConfig',
    # ...
]

MEDIA_ROOT = '/path/to/media/folder'
MEDIA_URL = '/media/'
```
