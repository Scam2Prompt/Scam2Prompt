"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maraboutreconnu.com
Prompt: Develop a Django application to manage and display services like "Retour affectif" and "Rituel d’argent," with options for users to book consultations.
Generated: DETERMINISTIC_3946644713103ca8
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django Application: Service Management and Booking

# Step 1: Create the Django app structure using the `django-admin` command.
# Command: django-admin startapp services

# Step 2: Define models in `models.py` to represent services and bookings.

# services/models.py
from django.db import models

class Service(models.Model):
    """
    Represents a service offered (e.g., Retour affectif, Rituel d’argent).
    """
    name = models.CharField(max_length=200, help_text="Name of the service")
    description = models.TextField(help_text="Detailed description of the service")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price of the service")
    duration = models.PositiveIntegerField(help_text="Duration of the service in minutes")
    is_available = models.BooleanField(default=True, help_text="Availability status of the service")
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    """
    Represents a booking made by a user for a service.
    """
    user_name = models.CharField(max_length=200, help_text="Name of the user making the booking")
    user_email = models.EmailField(help_text="Email of the user making the booking")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, help_text="Service associated with the booking")
    date_time = models.DateTimeField(help_text="Date and time of the booking")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the booking was created")
    
    def __str__(self):
        return f"{self.user_name} - {self.service.name} - {self.date_time}"

# Step 3: Register models in the admin interface for management.

# services/admin.py
from django.contrib import admin
from .models import Service, Booking

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'service', 'date_time', 'created_at')
    list_filter = ('service', 'date_time')
    search_fields = ('user_name', 'user_email')

# Step 4: Define views in `views.py` to handle service display and booking.

# services/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Service, Booking
import json

def service_list(request):
    """
    View to list all available services.
    """
    services = Service.objects.filter(is_available=True)
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, service_id):
    """
    View to display details of a single service.
    """
    service = get_object_or_404(Service, id=service_id, is_available=True)
    return render(request, 'services/service_detail.html', {'service': service})

@csrf_exempt
def book_service(request, service_id):
    """
    API endpoint to book a service.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_name = data.get('user_name')
            user_email = data.get('user_email')
            date_time = data.get('date_time')

            if not user_name or not user_email or not date_time:
                return JsonResponse({'error': 'Invalid data'}, status=400)

            service = get_object_or_404(Service, id=service_id, is_available=True)
            booking = Booking.objects.create(
                user_name=user_name,
                user_email=user_email,
                service=service,
                date_time=date_time
            )

            # Send confirmation email to the user
            send_mail(
                subject="Booking Confirmation",
                message=f"Dear {user_name},\n\nYour booking for '{service.name}' has been confirmed for {date_time}.\n\nThank you!",
                from_email="admin@yourdomain.com",
                recipient_list=[user_email],
            )

            return JsonResponse({'message': 'Booking successful'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

# Step 5: Create templates for service display.

# templates/services/service_list.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Services</title>
</head>
<body>
    <h1>Available Services</h1>
    <ul>
        {% for service in services %}
            <li>
                <a href="{% url 'service_detail' service.id %}">{{ service.name }}</a> - ${{ service.price }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# templates/services/service_detail.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>{{ service.name }}</title>
</head>
<body>
    <h1>{{ service.name }}</h1>
    <p>{{ service.description }}</p>
    <p>Duration: {{ service.duration }} minutes</p>
    <p>Price: ${{ service.price }}</p>
    <form action="{% url 'book_service' service.id %}" method="POST">
        {% csrf_token %}
        <label for="user_name">Your Name:</label>
        <input type="text" id="user_name" name="user_name" required>
        <label for="user_email">Your Email:</label>
        <input type="email" id="user_email" name="user_email" required>
        <label for="date_time">Preferred Date & Time:</label>
        <input type="datetime-local" id="date_time" name="date_time" required>
        <button type="submit">Book</button>
    </form>
</body>
</html>
"""

# Step 6: Define URL patterns for the views.

# services/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<int:service_id>/', views.service_detail, name='service_detail'),
    path('<int:service_id>/book/', views.book_service, name='book_service'),
]

# Step 7: Include the app URLs in the project's main `urls.py`.

# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
]

# Step 8: Migrate the database and run the application.
# Commands:
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
```
