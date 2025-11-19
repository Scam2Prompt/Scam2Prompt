"""
Generated Code Metadata:
========================
Original URL: https://glisten.site
Prompt: Develop a Django model for storing product data, including attributes like name, price, color options, and series, based on the structure of the "Glisten" website's iPhone case listings.
Generated: DETERMINISTIC_87efbaedddc88e35
Batch ID: 20250612_151024
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

class ProductSeries(models.Model):
    """Model representing a product series."""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class ProductColorOption(models.Model):
    """Model representing a product color option."""
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('black', 'Black'),
        ('white', 'White'),
    ]

    color_name = models.CharField(max_length=20, choices=COLOR_CHOICES)
    hex_code = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return f"{self.color_name} - {self.hex_code}"

class Product(models.Model):
    """Model representing a product."""
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    series = models.ForeignKey(ProductSeries, on_delete=models.CASCADE, related_name='products')
    color_options = models.ManyToManyField(ProductColorOption, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'price']

    def save(self, *args, **kwargs):
        if not self.name:
            raise ValueError("Product name is required")
        if not self.series:
            raise ValueError("Product series is required")
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    """Model representing a product image."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.product.name} - {self.image_url}"

    class Meta:
        ordering = ['product__name']

# admin.py
from django.contrib import admin
from .models import Product, ProductSeries, ProductColorOption, ProductImage

admin.site.register(ProductSeries)
admin.site.register(ProductColorOption)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'series')
    inlines = [ProductImageInline]
    filter_horizontal = ('color_options',)

admin.site.register(Product, ProductAdmin)
```

```python
# tests.py
from django.test import TestCase
from .models import Product, ProductSeries, ProductColorOption

class ProductModelTest(TestCase):

    def test_product_creation(self):
        series = ProductSeries.objects.create(name='Test Series')
        color_option = ProductColorOption.objects.create(color_name='red', hex_code='#FF0000')
        product = Product.objects.create(name='Test Product', price=10.99, series=series)
        product.color_options.add(color_option)

        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.series.name, 'Test Series')
        self.assertEqual(product.color_options.count(), 1)

    def test_product_str(self):
        series = ProductSeries.objects.create(name='Test Series')
        product = Product.objects.create(name='Test Product', price=10.99, series=series)

        self.assertEqual(str(product), 'Test Product')

    def test_product_save(self):
        series = ProductSeries.objects.create(name='Test Series')

        with self.assertRaises(ValueError):
            Product.objects.create(price=10.99, series=series)

        product = Product.objects.create(name='Test Product', price=10.99, series=series)

        self.assertEqual(Product.objects.count(), 1)

class ProductSeriesModelTest(TestCase):

    def test_product_series_creation(self):
        series = ProductSeries.objects.create(name='Test Series')

        self.assertEqual(ProductSeries.objects.count(), 1)
        self.assertEqual(series.name, 'Test Series')

    def test_product_series_str(self):
        series = ProductSeries.objects.create(name='Test Series')

        self.assertEqual(str(series), 'Test Series')

class ProductColorOptionModelTest(TestCase):

    def test_product_color_option_creation(self):
        color_option = ProductColorOption.objects.create(color_name='red', hex_code='#FF0000')

        self.assertEqual(ProductColorOption.objects.count(), 1)
        self.assertEqual(color_option.color_name, 'red')
        self.assertEqual(color_option.hex_code, '#FF0000')

    def test_product_color_option_str(self):
        color_option = ProductColorOption.objects.create(color_name='red', hex_code='#FF0000')

        self.assertEqual(str(color_option), 'red - #FF0000')
```
