"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Write a Django API endpoint to retrieve featured properties, including details such as price, location, and dimensions, based on the "Inmuebles Destacados" section of the Nueva Ciudad website.
Generated: DETERMINISTIC_f11c6c86992fd0dc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db.models import Q
from .models import Property
from .serializers import PropertySerializer

class FeaturedPropertiesAPIView(APIView):
    """
    API endpoint to retrieve featured properties.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            # Get featured properties (is_featured=True) ordered by creation date
            featured_properties = Property.objects.filter(
                is_featured=True
            ).order_by('-created_at')

            # Apply optional filters from query parameters
            min_price = request.query_params.get('min_price')
            max_price = request.query_params.get('max_price')
            location = request.query_params.get('location')
            property_type = request.query_params.get('property_type')

            if min_price:
                featured_properties = featured_properties.filter(price__gte=min_price)
            if max_price:
                featured_properties = featured_properties.filter(price__lte=max_price)
            if location:
                featured_properties = featured_properties.filter(
                    Q(city__icontains=location) | 
                    Q(state__icontains=location) |
                    Q(address__icontains=location)
                )
            if property_type:
                featured_properties = featured_properties.filter(property_type=property_type)

            serializer = PropertySerializer(featured_properties, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# serializers.py
from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer for Property model including all relevant fields.
    """
    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'description',
            'price',
            'currency',
            'property_type',
            'address',
            'city',
            'state',
            'country',
            'zip_code',
            'bedrooms',
            'bathrooms',
            'area',
            'area_unit',
            'year_built',
            'features',
            'main_image',
            'is_featured',
            'created_at',
            'updated_at'
        ]


# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class Property(models.Model):
    """
    Model representing a real estate property.
    """
    class PropertyType(models.TextChoices):
        HOUSE = 'HOUSE', _('House')
        APARTMENT = 'APARTMENT', _('Apartment')
        LAND = 'LAND', _('Land')
        COMMERCIAL = 'COMMERCIAL', _('Commercial')

    class AreaUnit(models.TextChoices):
        SQFT = 'SQFT', _('Square Feet')
        SQM = 'SQM', _('Square Meters')
        ACRES = 'ACRES', _('Acres')

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    property_type = models.CharField(
        max_length=20,
        choices=PropertyType.choices,
        default=PropertyType.HOUSE
    )
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Mexico')
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    bedrooms = models.PositiveIntegerField(blank=True, null=True)
    bathrooms = models.PositiveIntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    area_unit = models.CharField(
        max_length=10,
        choices=AreaUnit.choices,
        default=AreaUnit.SQM
    )
    year_built = models.PositiveIntegerField(blank=True, null=True)
    features = models.JSONField(default=dict, blank=True)
    main_image = models.ImageField(upload_to='properties/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.city}"

    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['-created_at']


# urls.py
from django.urls import path
from .views import FeaturedPropertiesAPIView

urlpatterns = [
    path('api/properties/featured/', FeaturedPropertiesAPIView.as_view(), name='featured-properties'),
]
```
