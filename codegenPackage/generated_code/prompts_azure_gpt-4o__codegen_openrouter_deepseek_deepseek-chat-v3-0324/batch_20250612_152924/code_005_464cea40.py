"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Develop a Django model for managing property listings, including fields for type, location, price, and features, as seen on Inmobiliaria Capri's website.
Generated: DETERMINISTIC_464cea401aff3e93
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class PropertyType(models.TextChoices):
    HOUSE = 'house', _('House')
    APARTMENT = 'apartment', _('Apartment')
    LAND = 'land', _('Land')
    COMMERCIAL = 'commercial', _('Commercial')
    VACATION = 'vacation', _('Vacation Home')

class PropertyStatus(models.TextChoices):
    FOR_SALE = 'for_sale', _('For Sale')
    FOR_RENT = 'for_rent', _('For Rent')
    SOLD = 'sold', _('Sold')
    RENTED = 'rented', _('Rented')

class Property(models.Model):
    title = models.CharField(_('title'), max_length=200)
    description = models.TextField(_('description'))
    property_type = models.CharField(
        _('property type'),
        max_length=20,
        choices=PropertyType.choices,
        default=PropertyType.HOUSE
    )
    status = models.CharField(
        _('status'),
        max_length=20,
        choices=PropertyStatus.choices,
        default=PropertyStatus.FOR_SALE
    )
    price = models.DecimalField(
        _('price'),
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    area = models.DecimalField(
        _('area (sqm)'),
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    bedrooms = models.PositiveIntegerField(_('bedrooms'), default=0)
    bathrooms = models.PositiveIntegerField(_('bathrooms'), default=0)
    address = models.CharField(_('address'), max_length=255)
    city = models.CharField(_('city'), max_length=100)
    state = models.CharField(_('state'), max_length=100)
    zip_code = models.CharField(_('zip code'), max_length=20)
    country = models.CharField(_('country'), max_length=100)
    latitude = models.DecimalField(
        _('latitude'),
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        _('longitude'),
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    year_built = models.PositiveIntegerField(_('year built'), null=True, blank=True)
    garage = models.PositiveIntegerField(_('garage spaces'), default=0)
    swimming_pool = models.BooleanField(_('swimming pool'), default=False)
    garden = models.BooleanField(_('garden'), default=False)
    terrace = models.BooleanField(_('terrace'), default=False)
    elevator = models.BooleanField(_('elevator'), default=False)
    energy_certificate = models.CharField(
        _('energy certificate'),
        max_length=1,
        choices=[
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('E', 'E'),
            ('F', 'F'),
            ('G', 'G'),
        ],
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    is_featured = models.BooleanField(_('is featured'), default=False)
    is_active = models.BooleanField(_('is active'), default=True)

    class Meta:
        verbose_name = _('property')
        verbose_name_plural = _('properties')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.get_property_type_display()} in {self.city}"

class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        _('image'),
        upload_to='property_images/'
    )
    is_main = models.BooleanField(_('main image'), default=False)
    caption = models.CharField(_('caption'), max_length=200, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('property image')
        verbose_name_plural = _('property images')
        ordering = ['-is_main', 'created_at']

    def __str__(self):
        return f"Image for {self.property.title}"
```
