"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Write a code snippet for a booking system that allows users to schedule mobile fuel injector cleaning services.
Generated: DETERMINISTIC_be0272316bcb3157
Batch ID: 20250612_155150
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

class Booking:
    """Class to represent a service booking for mobile fuel injector cleaning."""
    
    def __init__(self, customer_name: str, service_date: datetime, service_time: str):
        self.customer_name = customer_name
        self.service_date = service_date
        self.service_time = service_time
        self.booking_time = datetime.now()

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.service_date.strftime('%Y-%m-%d')} at {self.service_time}"

class BookingSystem:
    """Class to manage the booking system for mobile fuel injector cleaning services."""
    
    def __init__(self):
        self.bookings: List[Booking] = []
        
    def add_booking(self, customer_name: str, service_date: datetime, service_time: str) -> Optional[str]:
        """Adds a new booking to the system.
        
        Args:
            customer_name (str): The name of the customer.
            service_date (datetime): The date for the service.
            service_time (str): The time for the service in HH:MM format.
        
        Returns:
            Optional[str]: A confirmation message or an error message.
        """
        # Validate the booking time
        if not self.is_valid_time(service_time):
            return "Error: Service time is in an incorrect format. Use HH:MM."

        # Create booking object
        booking = Booking(customer_name, service_date, service_time)

        # Check for conflicts with existing bookings
        if self.is_conflict(booking):
            return "Error: Booking conflict. Please choose a different time."

        # Add to bookings list
        self.bookings.append(booking)
        return f"Booking confirmed: {booking}"

    def is_valid_time(self, time_str: str) -> bool:
        """Validates the service time format.
        
        Args:
            time_str (str): The service time as a string.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            datetime.strptime(time_str, '%H:%M')
            return True
        except ValueError:
            return False

    def is_conflict(self, new_booking: Booking) -> bool:
        """Checks if the new booking conflicts with existing bookings.
        
        Args:
            new_booking (Booking): The new booking to check against existing bookings.
        
        Returns:
            bool: True if there is a conflict, False otherwise.
        """
        for booking in self.bookings:
            if booking.service_date == new_booking.service_date and booking.service_time == new_booking.service_time:
                return True
        return False

# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Try to add a new booking
    service_date = datetime(2023, 10, 15)  # Example future date
    service_time = "14:30"  # Example time

    result = booking_system.add_booking("John Doe", service_date, service_time)
    print(result)  # Expected: Booking confirmation message
```
