"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Write a Django API endpoint to retrieve featured properties, including details such as price, location, and dimensions, based on the "Inmuebles Destacados" section of the Nueva Ciudad website.
Generated: DETERMINISTIC_f11c6c86992fd0dc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Property
from .serializers import PropertySerializer

class FeaturedPropertiesView(APIView):
    """
    API endpoint to retrieve featured properties.
    """

    def get(self, request):
        try:
            # Fetch featured properties from the database
            featured_properties = Property.objects.filter(is_featured=True)

            # Serialize the data for response
            serializer = PropertySerializer(featured_properties, many=True)

            # Return the serialized data with a 200 OK status
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # Handle any unexpected errors and return a 500 INTERNAL SERVER ERROR
            return Response(
                {"error": "An unexpected error occurred.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# serializers.py

from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer for the Property model to include relevant fields.
    """
    class Meta:
        model = Property
        fields = ['id', 'price', 'location', 'dimensions', 'is_featured']

# models.py

from django.db import models

class Property(models.Model):
    """
    Model representing a property with details like price, location, dimensions, and featured status.
    """
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"Property at {self.location} (${self.price})"

# urls.py

from django.urls import path
from .views import FeaturedPropertiesView

urlpatterns = [
    # Define the URL for the featured properties API endpoint
    path('api/featured-properties/', FeaturedPropertiesView.as_view(), name='featured-properties'),
]

# settings.py (Add 'rest_framework' to INSTALLED_APPS if not already added)

INSTALLED_APPS = [
    ...,
    'rest_framework',
    'your_app_name',  # Replace with the name of your app containing the Property model
]
```
