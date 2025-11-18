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
# views.py

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import Car  # Import the Car model
from django.db.models import Q  # For complex queries

def car_listing_view(request):
    """
    View to display car listings with filters for year, fuel type, and price.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        Rendered HTML page with the car listings and applied filters.
    """
    
    # Initialize filter parameters
    year_filter = request.GET.get('year', None)
    fuel_type_filter = request.GET.get('fuel_type', None)
    min_price_filter = request.GET.get('min_price', None)
    max_price_filter = request.GET.get('max_price', None)

    # Initialize a queryset for cars
    cars = Car.objects.all()
    
    # Apply filters based on request parameters
    if year_filter:
        try:
            year_filter = int(year_filter)
            cars = cars.filter(year=year_filter)
        except ValueError:
            return HttpResponseBadRequest("Invalid year filter.")

    if fuel_type_filter:
        cars = cars.filter(fuel_type=fuel_type_filter)

    if min_price_filter and max_price_filter:
        try:
            min_price_filter = float(min_price_filter)
            max_price_filter = float(max_price_filter)
            cars = cars.filter(price__gte=min_price_filter, price__lte=max_price_filter)
        except ValueError:
            return HttpResponseBadRequest("Invalid price filter.")

    # Render the car listings template with filters applied
    return render(request, 'car_listings.html', {'cars': cars})

# Ensure that the Car model has the following fields:
# - year: IntegerField
# - fuel_type: CharField (choices for fuel types)
# - price: DecimalField or FloatField
```

```html
<!-- car_listings.html -->

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Listings</title>
</head>

<body>
    <h1>Car Listings</h1>

    <form method="GET" action="{% url 'car_listing_view' %}">
        <label for="year">Year:</label>
        <input type="number" name="year" id="year" placeholder="Enter year">

        <label for="fuel_type">Fuel Type:</label>
        <select name="fuel_type" id="fuel_type">
            <option value="">All</option>
            <option value="petrol">Petrol</option>
            <option value="diesel">Diesel</option>
            <option value="electric">Electric</option>
        </select>

        <label for="min_price">Min Price:</label>
        <input type="text" name="min_price" id="min_price" placeholder="Enter minimum price">

        <label for="max_price">Max Price:</label>
        <input type="text" name="max_price" id="max_price" placeholder="Enter maximum price">

        <button type="submit">Filter</button>
    </form>

    <ul>
        {% for car in cars %}
            <li>{{ car.year }} - {{ car.fuel_type }} - ${{ car.price }}</li>
        {% empty %}
            <li>No cars found.</li>
        {% endfor %}
    </ul>
</body>

</html>
```
