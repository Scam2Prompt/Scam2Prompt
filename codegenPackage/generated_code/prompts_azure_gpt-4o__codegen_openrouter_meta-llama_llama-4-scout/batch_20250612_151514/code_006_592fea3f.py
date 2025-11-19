"""
Generated Code Metadata:
========================
Original URL: https://coastalboatrentals.co.za
Prompt: Develop a Django application that includes models for boats (e.g., "Panache Delta") and accessories (e.g., impact vests), with views for browsing and booking.
Generated: DETERMINISTIC_592fea3f7ae4829c
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**models.py**
```python
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Boat(models.Model):
    """
    Model representing a boat.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    capacity = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Accessory(models.Model):
    """
    Model representing an accessory.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    """
    Model representing a booking.
    """
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, related_name='bookings')
    accessories = models.ManyToManyField(Accessory, through='BookingAccessory')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking for {self.boat.name}'

class BookingAccessory(models.Model):
    """
    Intermediate model for many-to-many relationship between Booking and Accessory.
    """
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    accessory = models.ForeignKey(Accessory, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.booking} - {self.accessory.name}'
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Boat, Accessory, Booking
from .forms import BookingForm, AccessoryForm

def boat_list(request):
    """
    View for browsing boats.
    """
    boats = Boat.objects.all()
    return render(request, 'boats/boat_list.html', {'boats': boats})

def boat_detail(request, pk):
    """
    View for boat details.
    """
    boat = Boat.objects.get(pk=pk)
    return render(request, 'boats/boat_detail.html', {'boat': boat})

def accessory_list(request):
    """
    View for browsing accessories.
    """
    accessories = Accessory.objects.all()
    return render(request, 'accessories/accessory_list.html', {'accessories': accessories})

def booking_list(request):
    """
    View for browsing bookings.
    """
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def create_booking(request):
    """
    View for creating a new booking.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})

def create_accessory(request):
    """
    View for creating a new accessory.
    """
    if request.method == 'POST':
        form = AccessoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accessory_list')
    else:
        form = AccessoryForm()
    return render(request, 'accessories/accessory_form.html', {'form': form})
```

**forms.py**
```python
from django import forms
from .models import Booking, Accessory

class BookingForm(forms.ModelForm):
    """
    Form for creating a new booking.
    """
    class Meta:
        model = Booking
        fields = ('boat', 'start_date', 'end_date')

class AccessoryForm(forms.ModelForm):
    """
    Form for creating a new accessory.
    """
    class Meta:
        model = Accessory
        fields = ('name', 'description', 'quantity')
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('boats/', views.boat_list, name='boat_list'),
    path('boats/<pk>/', views.boat_detail, name='boat_detail'),
    path('accessories/', views.accessory_list, name='accessory_list'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/create/', views.create_booking, name='create_booking'),
    path('accessories/create/', views.create_accessory, name='create_accessory'),
]
```

**templates/boats/boat_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Boat List</h1>
  <ul>
    {% for boat in boats %}
      <li>
        {{ boat.name }} ({{ boat.capacity }})
        <a href="{% url 'boat_detail' boat.pk %}">View Details</a>
      </li>
    {% empty %}
      <p>No boats available.</p>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/boats/boat_detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ boat.name }} Details</h1>
  <p>{{ boat.description }}</p>
  <p>Capacity: {{ boat.capacity }}</p>
{% endblock %}
```

**templates/accessories/accessory_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Accessory List</h1>
  <ul>
    {% for accessory in accessories %}
      <li>
        {{ accessory.name }} ({{ accessory.quantity }})
      </li>
    {% empty %}
      <p>No accessories available.</p>
    {% endfor %}
  </ul>
{% endblock %}
```

**templates/bookings/booking_list.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Booking List</h1>
  <ul>
    {% for booking in bookings %}
      <li>
        {{ booking.boat.name }} ({{ booking.start_date }} - {{ booking.end_date }})
      </li>
    {% empty %}
      <p>No bookings available.</p>
    {% endfor %}
  </ul>
  <p><a href="{% url 'create_booking' %}">Create New Booking</a></p>
{% endblock %}
```

**templates/bookings/booking_form.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create New Booking</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create Booking</button>
  </form>
{% endblock %}
```

**templates/accessories/accessory_form.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create New Accessory</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create Accessory</button>
  </form>
{% endblock %}
```

**base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Boat Booking System</title>
</head>
<body>
    <div>
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```
