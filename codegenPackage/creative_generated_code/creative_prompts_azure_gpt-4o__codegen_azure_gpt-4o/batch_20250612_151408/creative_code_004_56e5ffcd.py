"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Write a Django view to display car listings with filters for year, fuel type, and price, inspired by the Helfen Motors inventory structure.
Generated: DETERMINISTIC_56e5ffcd28dd215e
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import Car

def car_listings_view(request):
    """
    View to display car listings with filters for year, fuel type, and price.
    Filters are applied based on request GET parameters.
    """
    try:
        # Retrieve filter parameters from the GET request
        year = request.GET.get('year')  # Filter by year
        fuel_type = request.GET.get('fuel_type')  # Filter by fuel type
        max_price = request.GET.get('max_price')  # Filter by maximum price

        # Build the query set with optional filters
        filters = Q()
        if year:
            filters &= Q(year=year)
        if fuel_type:
            filters &= Q(fuel_type__iexact=fuel_type)
        if max_price:
            try:
                max_price = float(max_price)  # Ensure max_price is a valid float
                filters &= Q(price__lte=max_price)
            except ValueError:
                return JsonResponse({'error': 'Invalid max_price value.'}, status=400)

        # Query the database with the filters
        cars = Car.objects.filter(filters).order_by('price')  # Order by price for better UX

        # Prepare context data for rendering or JSON response
        context = {
            'cars': cars,
        }

        # Render the template with filtered data
        return render(request, 'car_listings.html', context)
    except Exception as e:
        # Handle unexpected errors gracefully
        return JsonResponse({'error': str(e)}, status=500)
```

```html
<!-- Template: car_listings.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Listings</title>
</head>
<body>
    <h1>Car Listings</h1>
    <ul>
        {% for car in cars %}
            <li>
                {{ car.year }} - {{ car.make }} {{ car.model }} - {{ car.fuel_type }} - ${{ car.price }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```python
# Example model: Car (models.py)
from django.db import models

class Car(models.Model):
    """
    Car model representing inventory data for Helfen Motors.
    """
    make = models.CharField(max_length=50)  # Car manufacturer (e.g., Toyota, Honda)
    model = models.CharField(max_length=50)  # Car model (e.g., Corolla, Civic)
    year = models.PositiveIntegerField()  # Manufacturing year of the car
    fuel_type = models.CharField(max_length=20)  # Fuel type (e.g., petrol, diesel, electric)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the car

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.fuel_type})"
```
