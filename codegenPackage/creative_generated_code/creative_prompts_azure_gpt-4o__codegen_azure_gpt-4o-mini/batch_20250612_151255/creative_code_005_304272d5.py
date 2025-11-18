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
# settings.py

# Define the installed apps including Django REST framework
INSTALLED_APPS = [
    ...
    'rest_framework',
    'service_requests',
]

# Add any required middleware, authentication, etc.


# models.py in service_requests app
from django.db import models

class ApplianceBrand(models.Model):
    """Model to represent an appliance brand."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ServiceRequest(models.Model):
    """Model to represent a service request."""
    brand = models.ForeignKey(ApplianceBrand, related_name='service_requests', on_delete=models.CASCADE)
    description = models.TextField()
    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Request for {self.brand.name} by {self.customer_name}"


# serializers.py in service_requests app
from rest_framework import serializers
from .models import ServiceRequest, ApplianceBrand

class ApplianceBrandSerializer(serializers.ModelSerializer):
    """Serializer for ApplianceBrand model."""
    class Meta:
        model = ApplianceBrand
        fields = '__all__'


class ServiceRequestSerializer(serializers.ModelSerializer):
    """Serializer for ServiceRequest model."""
    class Meta:
        model = ServiceRequest
        fields = '__all__'


# views.py in service_requests app
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ServiceRequest, ApplianceBrand
from .serializers import ServiceRequestSerializer, ApplianceBrandSerializer

class ApplianceBrandViewSet(viewsets.ModelViewSet):
    """API endpoint to manage appliance brands."""
    queryset = ApplianceBrand.objects.all()
    serializer_class = ApplianceBrandSerializer


class ServiceRequestViewSet(viewsets.ModelViewSet):
    """API endpoint to manage service requests."""
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    def create(self, request, *args, **kwargs):
        """Handle the creation of a service request."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """Handle the update of a service request."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


# urls.py in service_requests app
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplianceBrandViewSet, ServiceRequestViewSet

router = DefaultRouter()
router.register(r'brands', ApplianceBrandViewSet)
router.register(r'requests', ServiceRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


# main urls.py in project
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('service_requests.urls')),
]
```

Make sure to run migrations to create the database tables associated with the models, and install Django and Django REST framework if not already done:

```bash
# Install Django and REST framework
pip install django djangorestframework

# Run migrations
python manage.py makemigrations
python manage.py migrate
```
