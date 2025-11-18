"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.findflydeals.ca
Prompt: Create a Django application that integrates flight search and booking features similar to "https://www.findflydeals.ca," including support for domestic and international flights.
Generated: DETERMINISTIC_fee130c6ecbf92fb
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# flightbooking_project/settings.py
# Django settings file for the Flight Booking application.

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "your-secret-key-here"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'flights',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.auth.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'flightbooking_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'flightbooking_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# flightbooking_project/urls.py
# URL configuration for the Flight Booking application.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('flights.urls')),  # Include URLs from the flights app
]

# flights/models.py
# Models for the flight booking application.

from django.db import models


class Flight(models.Model):
    """Model for storing flight information."""
    flight_number = models.CharField(max_length=10)
    airline = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number} - {self.airline}"


class Booking(models.Model):
    """Model for storing booking information."""
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=255)
    passenger_email = models.EmailField()
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.passenger_name} ({self.flight})"

# flights/views.py
# Views for the flight booking application.

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Flight, Booking


def search_flights(request):
    """View to search for flights."""
    origin = request.GET.get('origin', None)
    destination = request.GET.get('destination', None)

    if not origin or not destination:
        return HttpResponseBadRequest("Origin and destination are required.")

    flights = Flight.objects.filter(origin__icontains=origin, destination__icontains=destination)
    return render(request, 'flights/search_results.html', {'flights': flights})


def book_flight(request, flight_id):
    """View to book a flight."""
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == 'POST':
        passenger_name = request.POST.get('passenger_name')
        passenger_email = request.POST.get('passenger_email')

        if not passenger_name or not passenger_email:
            return HttpResponseBadRequest("Passenger name and email are required.")

        booking = Booking.objects.create(
            flight=flight,
            passenger_name=passenger_name,
            passenger_email=passenger_email,
        )
        return JsonResponse({"message": "Booking successful", "booking_id": booking.id})

    return render(request, 'flights/book_flight.html', {'flight': flight})

# flights/urls.py
# URL patterns for the flights app.

from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_flights, name='search_flights'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
]

# flights/templates/flights/search_results.html
# Template for displaying search results.

<!DOCTYPE html>
<html>
<head>
    <title>Flight Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
    <ul>
        {% for flight in flights %}
            <li>
                {{ flight.origin }} -> {{ flight.destination }}
                ({{ flight.departure_time }} - {{ flight.arrival_time }})
                <a href="{% url 'book_flight' flight.id %}">Book</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>

# flights/templates/flights/book_flight.html
# Template for booking a flight.

<!DOCTYPE html>
<html>
<head>
    <title>Book Flight</title>
</head>
<body>
    <h1>Book Flight</h1>
    <form method="post">
        {% csrf_token %}
        <label for="passenger_name">Name:</label>
        <input type="text" name="passenger_name" id="passenger_name" required>
        <br>
        <label for="passenger_email">Email:</label>
        <input type="email" name="passenger_email" id="passenger_email" required>
        <br>
        <button type="submit">Book Flight</button>
    </form>
</body>
</html>
```

To get this application running:
1. Create and activate a Django virtual environment.
2. Install Django (`pip install django`).
3. Create a project named `flightbooking_project`.
4. Create an app named `flights` and place the files accordingly.
5. Apply migrations (`python manage.py makemigrations` and `python manage.py migrate`).
6. Run the server (`python manage.py runserver`).
7. Load the templates in the `templates/flights` directory.
