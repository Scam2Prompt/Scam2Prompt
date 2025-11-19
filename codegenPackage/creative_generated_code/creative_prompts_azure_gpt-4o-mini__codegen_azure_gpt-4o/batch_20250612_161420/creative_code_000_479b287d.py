"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bossasopetroleum.com
Prompt: Generate code for a web application that allows users to view and manage petrol station services similar to those offered by Bosasa Petroleum in Puntland Somalia.
Generated: DETERMINISTIC_479b287d0a1bd9b7
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Django-based web application to manage petrol station services.
Assumes that Django is installed in your Python environment.
Follow the steps to set up the Django project and application before running this code.
"""

# Step 1: Create the Django project using `django-admin startproject petrol_station_app`
# Step 2: Create an app within the project using `python manage.py startapp services`

# models.py (within the `services` app)
from django.db import models

class PetrolStationService(models.Model):
    """
    Model representing a petrol station service, such as fuel types and vehicle services.
    """
    SERVICE_CATEGORIES = [
        ('Fuel', 'Fuel'),
        ('Wash', 'Car Wash'),
        ('Repair', 'Vehicle Repair'),
        ('Shop', 'Convenience Shop'),
    ]
    
    name = models.CharField(max_length=100, unique=True)  # Unique name of the service
    category = models.CharField(max_length=50, choices=SERVICE_CATEGORIES)  # Type of service
    description = models.TextField(blank=True)  # Optional description of the service
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the service
    available = models.BooleanField(default=True)  # Availability status

    def __str__(self):
        return self.name

# views.py (within the `services` app)
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import PetrolStationService

def service_list(request):
    """
    View for listing all available petrol station services.
    """
    services = PetrolStationService.objects.filter(available=True)
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, pk):
    """
    View for showing details of a specific service.
    """
    service = get_object_or_404(PetrolStationService, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})

def service_toggle_availability(request, pk):
    """
    View to toggle the availability status of a service.
    """
    try:
        service = get_object_or_404(PetrolStationService, pk=pk)
        service.available = not service.available  # Toggle availability
        service.save()
        return JsonResponse({'success': True, 'available': service.available})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

# urls.py (within the `services` app)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),  # URL for listing services
    path('<int:pk>/', views.service_detail, name='service_detail'),  # URL for service details
    path('<int:pk>/toggle/', views.service_toggle_availability, name='service_toggle'),  # URL to toggle availability
]

# templates/services/service_list.html
"""
HTML template for displaying the list of services.
"""
<!DOCTYPE html>
<html>
<head>
    <title>Petrol Station Services</title>
</head>
<body>
    <h1>Available Services</h1>
    <ul>
        {% for service in services %}
            <li>
                <strong>{{ service.name }}</strong> - {{ service.category }} - ${{ service.price }}
                <a href="{% url 'service_detail' service.pk %}">Details</a>
                <button onclick="toggleAvailability({{ service.pk }})">
                    {% if service.available %}Disable{% else %}Enable{% endif %}
                </button>
            </li>
        {% endfor %}
    </ul>

    <script>
        function toggleAvailability(serviceId) {
            fetch(`/${serviceId}/toggle/`)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        location.reload();
                    } else {
                        alert("Error: " + data.error);
                    }
                });
        }
    </script>
</body>
</html>

# templates/services/service_detail.html
"""
HTML template for displaying details of a specific service.
"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ service.name }}</title>
</head>
<body>
    <h1>{{ service.name }}</h1>
    <p>Category: {{ service.category }}</p>
    <p>Description: {{ service.description }}</p>
    <p>Price: ${{ service.price }}</p>
    <p>Available: {% if service.available %}Yes{% else %}No{% endif %}</p>
    <a href="/">Back to Services</a>
</body>
</html>

# admin.py (within the `services` app)
from django.contrib import admin
from .models import PetrolStationService

@admin.register(PetrolStationService)
class PetrolStationServiceAdmin(admin.ModelAdmin):
    """
    Admin interface for managing petrol station services.
    """
    list_display = ('name', 'category', 'price', 'available')  # Display fields
    list_filter = ('category', 'available')  # Filters for admin list view
    search_fields = ('name', 'description')  # Searchable fields

# settings.py (within the Django project)
"""
Ensure the `services` app is added to INSTALLED_APPS.
"""
INSTALLED_APPS = [
    ...
    'services',
    ...
]
```
