"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coastalboatrentals.co.za
Prompt: Develop a Django application that includes models for boats (e.g., "Panache Delta") and accessories (e.g., impact vests), with views for browsing and booking.
Generated: DETERMINISTIC_592fea3f7ae4829c
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Django Application Code for Boats and Accessories

# models.py
from django.db import models

class Boat(models.Model):
    """
    Model representing a boat.
    """
    name = models.CharField(max_length=100, help_text="Enter the name of the boat.")
    description = models.TextField(help_text="Provide a detailed description of the boat.")
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2, help_text="Hourly rental price for the boat.")
    available = models.BooleanField(default=True, help_text="Availability status of the boat.")

    def __str__(self):
        return self.name


class Accessory(models.Model):
    """
    Model representing an accessory.
    """
    name = models.CharField(max_length=100, help_text="Enter the name of the accessory.")
    description = models.TextField(help_text="Provide a detailed description of the accessory.")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Price for the accessory.")
    stock = models.PositiveIntegerField(help_text="Available stock for the accessory.")

    def __str__(self):
        return self.name


# forms.py
from django import forms
from .models import Boat

class BookingForm(forms.Form):
    """
    Form for booking a boat.
    """
    boat = forms.ModelChoiceField(queryset=Boat.objects.filter(available=True), help_text="Select a boat to book.")
    hours = forms.IntegerField(min_value=1, help_text="Specify the number of hours you want to book the boat.")
    customer_name = forms.CharField(max_length=100, help_text="Enter your full name.")
    customer_email = forms.EmailField(help_text="Enter your email address.")


# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Boat, Accessory
from .forms import BookingForm

def browse_boats(request):
    """
    View for browsing available boats.
    """
    boats = Boat.objects.filter(available=True)
    return render(request, 'browse_boats.html', {'boats': boats})


def browse_accessories(request):
    """
    View for browsing accessories.
    """
    accessories = Accessory.objects.all()
    return render(request, 'browse_accessories.html', {'accessories': accessories})


def book_boat(request):
    """
    View for booking a boat.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            boat = form.cleaned_data['boat']
            hours = form.cleaned_data['hours']

            # Mark the boat as unavailable (assuming one booking at a time)
            boat.available = False
            boat.save()

            return JsonResponse({"message": f"Boat '{boat.name}' booked for {hours} hours successfully!"})
        else:
            return JsonResponse({"error": "Invalid form submission"}, status=400)

    form = BookingForm()
    return render(request, 'book_boat.html', {'form': form})


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('boats/', views.browse_boats, name='browse_boats'),
    path('accessories/', views.browse_accessories, name='browse_accessories'),
    path('book/', views.book_boat, name='book_boat'),
]


# templates/browse_boats.html
"""
HTML template for browsing boats.
"""
<!DOCTYPE html>
<html>
<head>
    <title>Browse Boats</title>
</head>
<body>
    <h1>Available Boats</h1>
    <ul>
        {% for boat in boats %}
            <li>
                <strong>{{ boat.name }}</strong>: {{ boat.description }} - ${{ boat.price_per_hour }}/hour
            </li>
        {% endfor %}
    </ul>
</body>
</html>


# templates/browse_accessories.html
"""
HTML template for browsing accessories.
"""
<!DOCTYPE html>
<html>
<head>
    <title>Browse Accessories</title>
</head>
<body>
    <h1>Available Accessories</h1>
    <ul>
        {% for accessory in accessories %}
            <li>
                <strong>{{ accessory.name }}</strong>: {{ accessory.description }} - ${{ accessory.price }} (Stock: {{ accessory.stock }})
            </li>
        {% endfor %}
    </ul>
</body>
</html>


# templates/book_boat.html
"""
HTML template for booking a boat.
"""
<!DOCTYPE html>
<html>
<head>
    <title>Book a Boat</title>
</head>
<body>
    <h1>Book a Boat</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Book</button>
    </form>
</body>
</html>
```
