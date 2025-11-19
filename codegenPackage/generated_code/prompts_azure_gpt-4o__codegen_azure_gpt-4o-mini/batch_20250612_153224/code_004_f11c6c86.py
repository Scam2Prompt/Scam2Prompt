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

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Property  # Assuming Property is the model for properties
from .serializers import PropertySerializer  # Assuming a serializer for Property exists

class FeaturedPropertiesView(generics.ListAPIView):
    """
    API endpoint to retrieve featured properties.
    This endpoint returns a list of properties marked as featured,
    including details such as price, location, and dimensions.
    """
    serializer_class = PropertySerializer

    def get_queryset(self):
        """
        Override the get_queryset method to filter for featured properties.
        """
        try:
            # Assuming 'is_featured' is a boolean field in the Property model
            return Property.objects.filter(is_featured=True)
        except Exception as e:
            # Log the exception (logging setup not shown here)
            # logger.error(f"Error retrieving featured properties: {str(e)}")
            raise NotFound("Featured properties could not be retrieved.")

    def list(self, request, *args, **kwargs):
        """
        Override the list method to provide a custom response format.
        """
        queryset = self.get_queryset()
        if not queryset:
            return Response({"message": "No featured properties found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# urls.py

from django.urls import path
from .views import FeaturedPropertiesView

urlpatterns = [
    path('api/featured-properties/', FeaturedPropertiesView.as_view(), name='featured-properties'),
]

# models.py

from django.db import models

class Property(models.Model):
    """
    Model representing a property.
    """
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# serializers.py

from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer for the Property model.
    """
    class Meta:
        model = Property
        fields = ['id', 'title', 'price', 'location', 'dimensions']
```
