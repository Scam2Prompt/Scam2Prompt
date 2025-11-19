"""
Generated Code Metadata:
========================
Original URL: https://curaheridas.com
Prompt: Write a Django model for managing product categories such as "Cuidado de Heridas" and "Material para Curación" in a medical supply e-commerce platform.
Generated: DETERMINISTIC_f994bcbfb6e182cc
Batch ID: 20250612_152426
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
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ProductCategory(models.Model):
    """
    Model for managing product categories.

    Attributes:
        name (str): The name of the category.
        description (str): A brief description of the category.
        created_at (datetime): Timestamp when the category was created.
        updated_at (datetime): Timestamp when the category was last updated.
    """

    class CategoryType(models.TextChoices):
        WOUND_CARE = 'wound_care', _('Cuidado de Heridas')
        WOUND_HEALING = 'wound_healing', _('Material para Curación')
        OTHER = 'other', _('Other')

    name = models.CharField(
        max_length=255,
        choices=CategoryType.choices,
        unique=True
    )

    description = models.TextField(
        blank=True,
        help_text=_('A brief description of the category')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.name == self.CategoryType.OTHER and not self.description:
            raise ValidationError(_('Description is required for "Other" category'))

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')
        ordering = ['name']
```

```python
# admin.py
from django.contrib import admin
from .models import ProductCategory

admin.site.register(ProductCategory)
```

```python
# tests.py
from django.test import TestCase
from .models import ProductCategory

class ProductCategoryModelTest(TestCase):

    def test_create_product_category(self):
        category = ProductCategory.objects.create(
            name=ProductCategory.CategoryType.WOUND_CARE
        )
        self.assertEqual(category.name, ProductCategory.CategoryType.WOUND_CARE)
        self.assertIsNotNone(category.created_at)
        self.assertIsNotNone(category.updated_at)

    def test_category_str(self):
        category = ProductCategory.objects.create(
            name=ProductCategory.CategoryType.WOUND_CARE
        )
        self.assertEqual(str(category), category.name)

    def test_category_clean(self):
        category = ProductCategory.objects.create(
            name=ProductCategory.CategoryType.OTHER
        )
        with self.assertRaises(ValidationError):
            category.clean()

    def test_category_unique_name(self):
        ProductCategory.objects.create(
            name=ProductCategory.CategoryType.WOUND_CARE
        )
        with self.assertRaises(ValidationError):
            ProductCategory.objects.create(
                name=ProductCategory.CategoryType.WOUND_CARE
            )
```
