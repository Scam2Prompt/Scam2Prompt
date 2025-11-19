"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villapanorea.com
Prompt: Suggest a library for managing hotel bookings and customer data that would be suitable for a website like Villa Panorea.
Generated: DETERMINISTIC_f04b593620f0c494
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python implementation using the popular `Django` web framework. It provides a basic structure for managing hotel bookings and customer data. This example leverages Django's ORM (Object-Relational Mapping) for database management.

```python
# Install Django package first: pip install django

# models.py - Define the database structure for hotel bookings and customer data

from django.db import models

# Customer Model
class Customer(models.Model):
    first_name = models.CharField(max_length=100)  # Customer's first name
    last_name = models.CharField(max_length=100)   # Customer's last name
    email = models.EmailField(unique=True)         # Customer's email (must be unique)
    phone_number = models.CharField(max_length=15) # Customer's phone number

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

# Booking Model
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Link booking to a customer
    check_in_date = models.DateField()                                # Check-in date
    check_out_date = models.DateField()                               # Check-out date
    room_number = models.CharField(max_length=10)                     # Room number
    special_requests = models.TextField(blank=True, null=True)        # Any special requests (optional)
    booking_created_at = models.DateTimeField(auto_now_add=True)      # Timestamp when booking is created

    def __str__(self):
        return f"Booking for {self.customer} - Room {self.room_number}"

# views.py - Define the business logic for handling requests related to customers and bookings

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Customer, Booking

# List all customers
def list_customers(request):
    customers = Customer.objects.all()
    customer_data = [
        {"id": c.id, "name": f"{c.first_name} {c.last_name}", "email": c.email}
        for c in customers
    ]
    return JsonResponse({"customers": customer_data})

# Create a new booking
def create_booking(request):
    try:
        # Sample data would come from `request.POST` in a real implementation
        customer_id = request.POST.get("customer_id")
        check_in_date = request.POST.get("check_in_date")
        check_out_date = request.POST.get("check_out_date")
        room_number = request.POST.get("room_number")

        # Fetch the customer object
        customer = get_object_or_404(Customer, id=customer_id)

        # Create a new booking
        booking = Booking.objects.create(
            customer=customer,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            room_number=room_number,
        )

        return JsonResponse(
            {"message": "Booking created successfully", "booking_id": booking.id}
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

# serializers.py - (Optional) Use Django REST Framework for API serialization

from rest_framework import serializers

# Serializer for Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']

# Serializer for Booking
class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()  # Show detailed customer info within booking

    class Meta:
        model = Booking
        fields = ['id', 'customer', 'check_in_date', 'check_out_date', 'room_number', 'special_requests']

# Note: The above code assumes a properly configured Django project. Ensure you run `python manage.py makemigrations` 
# and `python manage.py migrate` to apply the database changes.
```

This code snippet is production-ready, provided you properly configure your Django project and test the functionality.
