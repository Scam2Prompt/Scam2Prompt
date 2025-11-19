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

**featured_properties/views.py**
```python
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import FeaturedProperty
from .serializers import FeaturedPropertySerializer

class FeaturedPropertiesView(APIView):
    """
    API endpoint to retrieve featured properties.
    """
    def get(self, request):
        try:
            featured_properties = FeaturedProperty.objects.all()
            serializer = FeaturedPropertySerializer(featured_properties, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

**featured_properties/models.py**
```python
from django.db import models

class FeaturedProperty(models.Model):
    """
    Model representing a featured property.
    """
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)
    # Add other relevant fields as needed

    def __str__(self):
        return f"{self.location} - {self.price}"
```

**featured_properties/serializers.py**
```python
from rest_framework import serializers
from .models import FeaturedProperty

class FeaturedPropertySerializer(serializers.ModelSerializer):
    """
    Serializer for featured properties.
    """
    class Meta:
        model = FeaturedProperty
        fields = ["id", "price", "location", "dimensions"]
```

**featured_properties/urls.py**
```python
from django.urls import path
from .views import FeaturedPropertiesView

urlpatterns = [
    path('featured-properties/', FeaturedPropertiesView.as_view()),
]
```

**featured_properties/admin.py**
```python
from django.contrib import admin
from .models import FeaturedProperty

admin.site.register(FeaturedProperty)
```

**api/urls.py (main URL configuration)**
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('featured_properties.urls')),
]
```

**settings.py ( ensure the following configurations are present)**
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'featured_properties',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}
```
