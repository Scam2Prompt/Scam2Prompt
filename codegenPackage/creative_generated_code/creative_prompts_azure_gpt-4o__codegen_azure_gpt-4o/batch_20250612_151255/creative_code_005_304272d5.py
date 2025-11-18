"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ankarateknikservisi.com
Prompt: Develop a REST API in Django to manage service requests for appliance brands such as Bosch, Arçelik, and Beko, as described on the Ankara Teknik Servisi site.
Generated: DETERMINISTIC_304272d5b32ddd63
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django REST framework-based REST API for managing service requests for appliance brands.
# This code assumes that Django and Django REST framework are installed and configured in your environment.

# models.py
from django.db import models

class Brand(models.Model):
    """Model to represent appliance brands."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ServiceRequest(models.Model):
    """Model to represent service requests for appliances."""
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Service Request by {self.customer_name} for {self.brand.name}"


# serializers.py
from rest_framework import serializers
from .models import Brand, ServiceRequest

class BrandSerializer(serializers.ModelSerializer):
    """Serializer for Brand model."""
    class Meta:
        model = Brand
        fields = ['id', 'name']


class ServiceRequestSerializer(serializers.ModelSerializer):
    """Serializer for ServiceRequest model."""
    brand = BrandSerializer(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), source='brand', write_only=True
    )

    class Meta:
        model = ServiceRequest
        fields = [
            'id', 'customer_name', 'customer_email', 'customer_phone', 
            'brand', 'brand_id', 'description', 'request_date', 'is_resolved'
        ]


# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Brand, ServiceRequest
from .serializers import BrandSerializer, ServiceRequestSerializer

class BrandViewSet(viewsets.ModelViewSet):
    """ViewSet for managing appliance brands."""
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ServiceRequestViewSet(viewsets.ModelViewSet):
    """ViewSet for managing service requests."""
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    def create(self, request, *args, **kwargs):
        """Override create method to add custom error handling."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, ServiceRequestViewSet

router = DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'service-requests', ServiceRequestViewSet, basename='service-request')

urlpatterns = [
    path('api/', include(router.urls)),
]


# admin.py
from django.contrib import admin
from .models import Brand, ServiceRequest

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Admin configuration for Brand model."""
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    """Admin configuration for ServiceRequest model."""
    list_display = ['id', 'customer_name', 'brand', 'request_date', 'is_resolved']
    list_filter = ['brand', 'is_resolved']
    search_fields = ['customer_name', 'customer_email', 'customer_phone']


# settings.py (Add required settings for REST framework if not already present)
INSTALLED_APPS = [
    # Other apps...
    'rest_framework',
    'your_app_name',  # Replace with the name of your Django app
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```
