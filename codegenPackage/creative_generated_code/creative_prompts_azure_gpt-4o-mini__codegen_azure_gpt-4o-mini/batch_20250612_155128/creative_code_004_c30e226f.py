"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kleanproutah.com
Prompt: Illustrate how to implement a booking system for residential power washing services, based on the service structure of Klean-Pro Utah.
Generated: DETERMINISTIC_c30e226f3a732adc
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Optional

class Service:
    """Represents a power washing service."""
    
    def __init__(self, name: str, duration_hours: float, price: float):
        self.name = name  # Name of the service
        self.duration_hours = duration_hours  # Duration of the service in hours
        self.price = price  # Price of the service

class Booking:
    """Represents a booking for a power washing service."""
    
    def __init__(self, service: Service, date: datetime, customer_name: str):
        self.service = service  # The service being booked
        self.date = date  # The date and time of the booking
        self.customer_name = customer_name  # Name of the customer

class BookingSystem:
    """Manages the booking of power washing services."""
    
    def __init__(self):
        self.services: List[Service] = []  # List of available services
        self.bookings: List[Booking] = []  # List of existing bookings

    def add_service(self, service: Service):
        """Adds a new service to the system."""
        self.services.append(service)

    def list_services(self) -> List[Service]:
        """Returns a list of available services."""
        return self.services

    def book_service(self, service_name: str, date: datetime, customer_name: str) -> Optional[Booking]:
        """Books a service for a given date and customer."""
        # Check if the service exists
        service = next((s for s in self.services if s.name == service_name), None)
        if not service:
            raise ValueError(f"Service '{service_name}' not found.")

        # Check for conflicts in the booking
        if any(booking.date == date for booking in self.bookings):
            raise ValueError(f"Service is already booked for {date}.")

        # Create and store the booking
        booking = Booking(service, date, customer_name)
        self.bookings.append(booking)
        return booking

    def list_bookings(self) -> List[Booking]:
        """Returns a list of all bookings."""
        return self.bookings

# Example usage
if __name__ == "__main__":
    # Initialize the booking system
    booking_system = BookingSystem()
    
    # Add services offered
    booking_system.add_service(Service("Basic Wash", 2, 100.0))
    booking_system.add_service(Service("Deep Clean", 4, 250.0))
    
    # List available services
    print("Available Services:")
    for service in booking_system.list_services():
        print(f"- {service.name}: ${service.price} (Duration: {service.duration_hours} hours)")

    # Book a service
    try:
        booking_date = datetime.now() + timedelta(days=1)  # Book for tomorrow
        booking = booking_system.book_service("Basic Wash", booking_date, "John Doe")
        print(f"Booking successful: {booking.service.name} for {booking.customer_name} on {booking.date}")
    except ValueError as e:
        print(f"Booking failed: {e}")

    # List all bookings
    print("\nCurrent Bookings:")
    for booking in booking_system.list_bookings():
        print(f"{booking.customer_name} booked {booking.service.name} on {booking.date}")
```
