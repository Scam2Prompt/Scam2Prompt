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

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Property   # Assuming Property is the model for properties
from .serializers import PropertySerializer  # Assuming a serializer exists for the Property model

class FeaturedPropertiesAPIView(APIView):
    """
    API endpoint to retrieve featured properties from the database
    including details such as price, location, and dimensions.
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve featured properties.
        Returns a list of featured properties with their details.
        """
        try:
            # Querying for featured properties
            featured_properties = Property.objects.filter(is_featured=True)
            serializer = PropertySerializer(featured_properties, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # Log the exception for debugging purposes (logging setup not shown)
            # logger.error(f"Error retrieving featured properties: {e}")
            return Response({"error": "Unable to retrieve featured properties."}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# urls.py

from django.urls import path
from .views import FeaturedPropertiesAPIView

urlpatterns = [
    path('api/featured-properties/', FeaturedPropertiesAPIView.as_view(), name='featured-properties'),
]

# models.py

from django.db import models

class Property(models.Model):
    """
    Model representing a property listing with relevant details.
    """
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=50)  # e.g., "2000 sqft"
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# serializers.py

from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer for the Property model to convert model instances to JSON.
    """
    class Meta:
        model = Property
        fields = ['id', 'title', 'price', 'location', 'dimensions', 'is_featured']
```

Make sure to run the migration commands after creating or modifying the models:

```bash
python manage.py makemigrations
python manage.py migrate
```

Also, ensure that you have the Django REST Framework installed and included in your `INSTALLED_APPS` within `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    ...
]
```
