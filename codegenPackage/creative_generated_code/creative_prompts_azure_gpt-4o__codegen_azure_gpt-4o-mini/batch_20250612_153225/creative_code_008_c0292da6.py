"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baturjeeptour.my.id
Prompt: Using Django, build a web application that integrates with the Batur Jeep Tour website to allow users to search and book tour packages directly.
Generated: DETERMINISTIC_c0292da6c55c14ae
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from Django
from django.db import models
from django.urls import path
from django.shortcuts import render, redirect
from django.http import Http404
from django.views import View
from django import forms
import requests

# Define the TourPackage model to store tour package details
class TourPackage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Create a form for booking a tour package
class BookingForm(forms.Form):
    package_id = forms.IntegerField(widget=forms.HiddenInput())
    user_name = forms.CharField(max_length=100, required=True)
    user_email = forms.EmailField(required=True)

# Create a view to display available tour packages
class TourListView(View):
    def get(self, request):
        tours = TourPackage.objects.filter(available=True)
        return render(request, 'tours/tour_list.html', {'tours': tours})

# Create a view for booking a tour package
class BookingView(View):
    def get(self, request, tour_id):
        try:
            tour = TourPackage.objects.get(id=tour_id)
            form = BookingForm(initial={'package_id': tour.id})
            return render(request, 'tours/booking_form.html', {'form': form, 'tour': tour})
        except TourPackage.DoesNotExist:
            raise Http404("Tour package does not exist.")

    def post(self, request):
        form = BookingForm(request.POST)
        if form.is_valid():
            package_id = form.cleaned_data['package_id']
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']

            # Here you'd integrate with the Batur Jeep Tour API for booking
            # For example:
            # response = requests.post('<API_URL>', data={
            #     'package_id': package_id,
            #     'user_name': user_name,
            #     'user_email': user_email,
            # })
            # if response.status_code == 200:
            #     return redirect('booking_success')
            # else:
            #     return render(request, 'tours/booking_form.html', {'form': form, 'error': 'Booking failed.'})
            
            return redirect('booking_success')  # Placeholder redirect

        return render(request, 'tours/booking_form.html', {'form': form})

# Define URLs for the application
urlpatterns = [
    path('tours/', TourListView.as_view(), name='tour_list'),
    path('tours/book/<int:tour_id>/', BookingView.as_view(), name='booking'),
]

# Templates should contain the following basic structure

# tour_list.html
"""
{% extends "base_generic.html" %}
{% block content %}
  <h1>Available Tour Packages</h1>
  <ul>
    {% for tour in tours %}
      <li>
        <h2>{{ tour.name }}</h2>
        <p>{{ tour.description }}</p>
        <p>Price: ${{ tour.price }}</p>
        <a href="{% url 'booking' tour.id %}">Book Now</a>
      </li>
    {% endfor %}
  </ul>
{% endblock %}
"""

# booking_form.html
"""
{% extends "base_generic.html" %}
{% block content %}
  <h1>Booking for {{ tour.name }}</h1>
  <form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Confirm Booking</button>
  </form>
  {% if error %}
    <p style="color:red;">{{ error }}</p>
  {% endif %}
{% endblock %}
"""

# Ensure to include settings for the application and run migrations
# settings.py and migrations not included for brevity.

# Note: Remember to replace '<API_URL>' with the actual Batur Jeep Tour API endpoint when implementing the booking logic.
```
