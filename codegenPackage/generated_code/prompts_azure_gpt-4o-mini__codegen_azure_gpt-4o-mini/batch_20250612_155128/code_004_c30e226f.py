"""
Generated Code Metadata:
========================
Original URL: https://kleanproutah.com
Prompt: Illustrate how to implement a booking system for residential power washing services, based on the service structure of Klean-Pro Utah.
Generated: DETERMINISTIC_c30e226f3a732adc
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import json

class BookingError(Exception):
    """Custom exception for booking errors."""
    pass

class PowerWashingService:
    """Class representing a power washing service."""
    
    def __init__(self, service_type, duration, price):
        self.service_type = service_type
        self.duration = duration  # Duration in hours
        self.price = price  # Price in USD

class Booking:
    """Class representing a booking for power washing services."""
    
    def __init__(self, customer_name, service, booking_time):
        self.customer_name = customer_name
        self.service = service
        self.booking_time = booking_time
        self.status = 'Booked'  # Initial status of the booking

    def cancel(self):
        """Cancel the booking."""
        if self.status == 'Cancelled':
            raise BookingError("Booking is already cancelled.")
        self.status = 'Cancelled'

    def reschedule(self, new_time):
        """Reschedule the booking to a new time."""
        if self.status == 'Cancelled':
            raise BookingError("Cannot reschedule a cancelled booking.")
        self.booking_time = new_time

class BookingSystem:
    """Class to manage the booking system for power washing services."""
    
    def __init__(self):
        self.bookings = []

    def add_booking(self, customer_name, service, booking_time):
        """Add a new booking to the system."""
        if not isinstance(service, PowerWashingService):
            raise BookingError("Invalid service type.")
        
        if self.is_time_slot_available(booking_time, service.duration):
            new_booking = Booking(customer_name, service, booking_time)
            self.bookings.append(new_booking)
            return new_booking
        else:
            raise BookingError("Time slot is not available.")

    def is_time_slot_available(self, booking_time, duration):
        """Check if the requested time slot is available."""
        end_time = booking_time + timedelta(hours=duration)
        for booking in self.bookings:
            if booking.status != 'Cancelled':
                if (booking.booking_time < end_time and 
                    booking.booking_time + timedelta(hours=booking.service.duration) > booking_time):
                    return False
        return True

    def get_bookings(self):
        """Return a list of all bookings."""
        return [booking.__dict__ for booking in self.bookings]

    def save_bookings_to_file(self, filename):
        """Save bookings to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_bookings(), file, default=str)
        except IOError as e:
            raise BookingError(f"Error saving bookings to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create services
        basic_wash = PowerWashingService("Basic Wash", 2, 100)
        deep_clean = PowerWashingService("Deep Clean", 4, 250)

        # Initialize booking system
        booking_system = BookingSystem()

        # Add bookings
        booking1 = booking_system.add_booking("John Doe", basic_wash, datetime(2023, 10, 15, 10, 0))
        booking2 = booking_system.add_booking("Jane Smith", deep_clean, datetime(2023, 10, 15, 14, 0))

        # Print current bookings
        print("Current Bookings:")
        print(booking_system.get_bookings())

        # Save bookings to file
        booking_system.save_bookings_to_file("bookings.json")

    except BookingError as e:
        print(f"Booking error: {e}")
```
