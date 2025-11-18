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
# models.py

from django.db import models

class Boat(models.Model):
    """Model representing a boat."""
    name = models.CharField(max_length=100, unique=True)
    length = models.DecimalField(max_digits=5, decimal_places=2)  # Length in meters
    capacity = models.PositiveIntegerField()  # Number of people the boat can hold
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Accessory(models.Model):
    """Model representing an accessory for boats."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)  # Rental price per day

    def __str__(self):
        return self.name

class Booking(models.Model):
    """Model representing a booking for a boat and accessories."""
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    accessory = models.ManyToManyField(Accessory, blank=True)
    user_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"Booking for {self.boat.name} by {self.user_name}"
```

```python
# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Boat, Accessory, Booking
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages

def boat_list(request):
    """View to display the list of available boats."""
    boats = Boat.objects.all()
    return render(request, 'boats/boat_list.html', {'boats': boats})

def accessory_list(request):
    """View to display the list of available accessories."""
    accessories = Accessory.objects.all()
    return render(request, 'boats/accessory_list.html', {'accessories': accessories})

def booking_create(request):
    """View to handle the booking of a boat and accessories."""
    if request.method == 'POST':
        boat_id = request.POST.get('boat_id')
        accessory_ids = request.POST.getlist('accessory_ids')
        user_name = request.POST.get('user_name')
        booking_date = request.POST.get('booking_date')
        return_date = request.POST.get('return_date')

        try:
            boat = get_object_or_404(Boat, id=boat_id)
            booking = Booking.objects.create(
                boat=boat,
                user_name=user_name,
                booking_date=booking_date,
                return_date=return_date
            )
            booking.accessory.set(accessory_ids)
            booking.save()
            messages.success(request, 'Booking created successfully!')
            return redirect('boat_list')

        except Exception as e:
            messages.error(request, f'Error creating booking: {str(e)}')

    return render(request, 'boats/booking_form.html')
```

```python
# urls.py

from django.urls import path
from .views import boat_list, accessory_list, booking_create

urlpatterns = [
    path('boats/', boat_list, name='boat_list'),
    path('accessories/', accessory_list, name='accessory_list'),
    path('book/', booking_create, name='booking_create'),
]
```

```html
<!-- boat_list.html -->

{% extends 'base.html' %}

{% block content %}
<h1>Available Boats</h1>
<ul>
    {% for boat in boats %}
        <li>{{ boat.name }} - {{ boat.length }} meters - Capacity: {{ boat.capacity }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

```html
<!-- accessory_list.html -->

{% extends 'base.html' %}

{% block content %}
<h1>Available Accessories</h1>
<ul>
    {% for accessory in accessories %}
        <li>{{ accessory.name }} - ${{ accessory.price_per_day }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

```html
<!-- booking_form.html -->

{% extends 'base.html' %}

{% block content %}
<h1>Create Booking</h1>
<form method="post">
    {% csrf_token %}
    <label for="boat_id">Select Boat:</label>
    <select name="boat_id" required>
        {% for boat in boats %}
            <option value="{{ boat.id }}">{{ boat.name }}</option>
        {% endfor %}
    </select>

    <label for="accessory_ids">Select Accessories:</label>
    <select name="accessory_ids" multiple>
        {% for accessory in accessories %}
            <option value="{{ accessory.id }}">{{ accessory.name }}</option>
        {% endfor %}
    </select>

    <label for="user_name">Your Name:</label>
    <input type="text" name="user_name" required>

    <label for="booking_date">Booking Date:</label>
    <input type="date" name="booking_date" required>

    <label for="return_date">Return Date:</label>
    <input type="date" name="return_date" required>

    <button type="submit">Book Now</button>
</form>
{% endblock %}
```

```python
# settings.py

INSTALLED_APPS = [
    # Other apps...
    'boats',  # Your app name
    'django.contrib.messages',
]

MIDDLEWARE = [
    # Other middleware...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
```

```python
# admin.py

from django.contrib import admin
from .models import Boat, Accessory, Booking

@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ('name', 'length', 'capacity')

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_day')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('boat', 'user_name', 'booking_date', 'return_date')
```

This code provides a basic Django application with models, views, and templates for managing boats and their accessories, allowing users to browse and book them. Error handling is included in the booking view, and all code is organized and follows best practices.
