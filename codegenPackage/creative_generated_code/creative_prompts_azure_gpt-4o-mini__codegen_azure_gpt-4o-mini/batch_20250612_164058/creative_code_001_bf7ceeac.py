"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Write a code snippet for a booking system that allows users to schedule windscreen repairs, inspired by the services offered at Cheap Windscreens Melbourne.
Generated: DETERMINISTIC_bf7ceeac45cde606
Batch ID: 20250612_164058
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
    """Represents a booking for windscreen repair."""
    
    def __init__(self, customer_name: str, date_time: datetime):
        self.customer_name = customer_name
        self.date_time = date_time

    def __repr__(self):
        return f"Booking(customer_name='{self.customer_name}', date_time='{self.date_time}')"


class BookingSystem:
    """Manages bookings for windscreen repairs."""

    def __init__(self):
        self.bookings: List[Booking] = []

    def add_booking(self, customer_name: str, date_time: datetime) -> None:
        """Add a new booking if the time slot is available."""
        if not self.is_time_slot_available(date_time):
            raise ValueError("The selected time slot is already booked.")
        self.bookings.append(Booking(customer_name, date_time))

    def is_time_slot_available(self, date_time: datetime) -> bool:
        """Check if a given time slot is available for booking."""
        return all(booking.date_time != date_time for booking in self.bookings)

    def get_bookings(self) -> List[Booking]:
        """Return a list of all bookings."""
        return self.bookings

    def cancel_booking(self, customer_name: str, date_time: datetime) -> None:
        """Cancel a booking for a specific customer at a specific time."""
        booking_to_cancel = next((booking for booking in self.bookings 
                                   if booking.customer_name == customer_name and booking.date_time == date_time), None)
        if booking_to_cancel:
            self.bookings.remove(booking_to_cancel)
        else:
            raise ValueError("Booking not found.")

# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Schedule a few bookings
    try:
        booking_system.add_booking("John Doe", datetime(2023, 10, 15, 14, 30))
        booking_system.add_booking("Jane Smith", datetime(2023, 10, 15, 15, 30))
        # Attempting to book an already booked slot
        booking_system.add_booking("Alice Johnson", datetime(2023, 10, 15, 14, 30))  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")

    # Print all bookings
    print("Current bookings:")
    for booking in booking_system.get_bookings():
        print(booking)

    # Cancel a booking
    try:
        booking_system.cancel_booking("John Doe", datetime(2023, 10, 15, 14, 30))
    except ValueError as e:
        print(f"Error: {e}")

    # Print all bookings after cancellation
    print("Bookings after cancellation:")
    for booking in booking_system.get_bookings():
        print(booking)
```
