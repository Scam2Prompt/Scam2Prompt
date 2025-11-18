"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secondcitysummers.com
Prompt: Suggest tools or frameworks to design a booking system for The Second City's private events and team-building workshops, ensuring seamless integration with their existing website.
Generated: DETERMINISTIC_751885075511162b
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides a suggestion for a tech stack and frameworks for designing a booking system
for The Second City's private events and team-building workshops. The example is based on Python
and Django for backend, ensuring seamless integration with an existing website.
"""

# Required Python Libraries
# To install them, run: pip install django djangorestframework
import os
from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, views, status

# Django Model for booking events
class EventBooking(models.Model):
    """
    Model to represent a booking for private events and team-building workshops.
    """
    name = models.CharField(max_length=100)  # Name of the individual or team
    email = models.EmailField()  # Contact email
    phone_number = models.CharField(max_length=15)  # Contact phone number
    event_date = models.DateField()  # Desired event date
    event_type = models.CharField(max_length=50, choices=[
        ('PRIVATE_EVENT', 'Private Event'),
        ('TEAM_BUILDING_WORKSHOP', 'Team Building Workshop')
    ])  # Type of event
    comments = models.TextField(blank=True)  # Additional comments or requests

    def clean(self):
        """
        Custom validation logic for the EventBooking model.
        """
        if self.event_date < self._get_current_date():
            raise ValidationError("Event date cannot be in the past.")

    def _get_current_date(self):
        """
        Utility method to get the current date.
        """
        from datetime import date
        return date.today()

    def __str__(self):
        return f"{self.name} - {self.event_type} on {self.event_date}"


# Serializer for EventBooking
class EventBookingSerializer(serializers.ModelSerializer):
    """
    Serializer to convert EventBooking model into JSON format for API interaction.
    """
    class Meta:
        model = EventBooking
        fields = ['id', 'name', 'email', 'phone_number', 'event_date', 'event_type', 'comments']


# Django View for handling booking requests
@csrf_exempt
def booking_view(request):
    """
    Handles booking requests.
    Supports GET to fetch bookings and POST to create a new booking.
    """
    if request.method == 'GET':
        bookings = EventBooking.objects.all()
        serializer = EventBookingSerializer(bookings, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        try:
            data = request.POST
            serializer = EventBookingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Sample Django URL Configuration
from django.urls import path

urlpatterns = [
    path('api/bookings/', booking_view, name='booking_view'),
]


# To integrate with an existing website:
# - Use Django's template system for frontend rendering or create a React/Vue component.
# - Use Django Rest Framework for more advanced APIs and authentication.
# - Use a payment gateway (Stripe, PayPal, etc.) for payments.
# - Add unit tests and logging for better reliability in production.

# Deployment Suggestion:
# - Use Docker for containerization.
# - Deploy on cloud platforms like AWS, GCP, or Azure.
# - Use a PostgreSQL database for scalability.
```
