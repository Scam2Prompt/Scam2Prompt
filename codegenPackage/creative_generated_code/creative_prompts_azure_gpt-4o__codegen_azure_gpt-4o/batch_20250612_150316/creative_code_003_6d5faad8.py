"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzooprotocal.net
Prompt: Write a Django application for a cleaning service company that includes features for requesting free quotes, managing insured and bonded service providers, and displaying local attractions as described on Queen Bee Renzo ProtocolCleaning's website.
Generated: DETERMINISTIC_6d5faad85d398906
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django application for Queen Bee Renzo Protocol Cleaning services

# Step 1: Create the Django project and application
# Run the following commands to set up the project and app:
# django-admin startproject cleaning_service
# cd cleaning_service
# python manage.py startapp core

# Step 2: Define the models in the `core/models.py` file.

from django.db import models

class FreeQuoteRequest(models.Model):
    """Model to handle free quote requests."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote Request from {self.name}"

class ServiceProvider(models.Model):
    """Model to manage insured and bonded service providers."""
    name = models.CharField(max_length=100)
    is_insured = models.BooleanField(default=False)
    is_bonded = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    services_offered = models.TextField()

    def __str__(self):
        return self.name

class LocalAttraction(models.Model):
    """Model to display local attractions."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# Step 3: Register the models in the `core/admin.py` file for admin panel management.

from django.contrib import admin
from .models import FreeQuoteRequest, ServiceProvider, LocalAttraction

@admin.register(FreeQuoteRequest)
class FreeQuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_insured', 'is_bonded', 'contact_number')
    search_fields = ('name', 'contact_number')
    list_filter = ('is_insured', 'is_bonded')

@admin.register(LocalAttraction)
class LocalAttractionAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'website')
    search_fields = ('name', 'address')

# Step 4: Define serializers for API access in `core/serializers.py`.

from rest_framework import serializers
from .models import FreeQuoteRequest, ServiceProvider, LocalAttraction

class FreeQuoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeQuoteRequest
        fields = '__all__'

class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = '__all__'

class LocalAttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalAttraction
        fields = '__all__'

# Step 5: Create views for handling requests in `core/views.py`.

from rest_framework import generics
from .models import FreeQuoteRequest, ServiceProvider, LocalAttraction
from .serializers import FreeQuoteRequestSerializer, ServiceProviderSerializer, LocalAttractionSerializer

class FreeQuoteRequestView(generics.CreateAPIView):
    """API view for handling free quote requests."""
    queryset = FreeQuoteRequest.objects.all()
    serializer_class = FreeQuoteRequestSerializer

class ServiceProviderListView(generics.ListAPIView):
    """API view for listing service providers."""
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer

class LocalAttractionListView(generics.ListAPIView):
    """API view for listing local attractions."""
    queryset = LocalAttraction.objects.all()
    serializer_class = LocalAttractionSerializer

# Step 6: Define URL patterns in `core/urls.py` to route requests.

from django.urls import path
from .views import FreeQuoteRequestView, ServiceProviderListView, LocalAttractionListView

urlpatterns = [
    path('free-quote/', FreeQuoteRequestView.as_view(), name='free_quote_request'),
    path('service-providers/', ServiceProviderListView.as_view(), name='service_provider_list'),
    path('local-attractions/', LocalAttractionListView.as_view(), name='local_attraction_list'),
]

# Step 7: Include the `core` app URLs in the main `cleaning_service/urls.py`.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Include the core app URLs
]

# Step 8: Install and set up Django REST Framework (DRF) in settings.
# Add the following in `cleaning_service/settings.py`:

INSTALLED_APPS = [
    # Other installed apps...
    'core',
    'rest_framework',
]

# Step 9: Run migrations and start the development server.

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
```
