"""
Generated Code Metadata:
========================
Original URL: https://aerotraining.com.tr
Prompt: "Create a booking system for simulator services at Aero Training Center, allowing users to schedule flights and training sessions."
Generated: DETERMINISTIC_5bf6279077b1de07
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Optional

class Booking:
    """Class representing a booking for a simulator service."""
    
    def __init__(self, user_name: str, service_type: str, start_time: datetime, duration: int):
        self.user_name = user_name
        self.service_type = service_type
        self.start_time = start_time
        self.end_time = start_time + timedelta(hours=duration)

    def __repr__(self):
        return f"Booking(user_name={self.user_name}, service_type={self.service_type}, " \
               f"start_time={self.start_time}, end_time={self.end_time})"


class BookingSystem:
    """Class to manage bookings for simulator services."""
    
    def __init__(self):
        self.bookings: List[Booking] = []

    def add_booking(self, user_name: str, service_type: str, start_time: datetime, duration: int) -> Optional[str]:
        """Add a new booking if the time slot is available."""
        if self.is_time_slot_available(start_time, duration):
            new_booking = Booking(user_name, service_type, start_time, duration)
            self.bookings.append(new_booking)
            return f"Booking confirmed: {new_booking}"
        else:
            return "Error: Time slot is not available."

    def is_time_slot_available(self, start_time: datetime, duration: int) -> bool:
        """Check if the requested time slot is available."""
        end_time = start_time + timedelta(hours=duration)
        for booking in self.bookings:
            if (start_time < booking.end_time) and (end_time > booking.start_time):
                return False
        return True

    def list_bookings(self) -> List[Booking]:
        """Return a list of all current bookings."""
        return self.bookings

    def cancel_booking(self, user_name: str, start_time: datetime) -> Optional[str]:
        """Cancel a booking for a specific user and time."""
        for booking in self.bookings:
            if booking.user_name == user_name and booking.start_time == start_time:
                self.bookings.remove(booking)
                return f"Booking cancelled: {booking}"
        return "Error: Booking not found."


# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()

    # Create some bookings
    print(booking_system.add_booking("Alice", "Flight Simulation", datetime(2023, 10, 15, 10, 0), 2))
    print(booking_system.add_booking("Bob", "Training Session", datetime(2023, 10, 15, 12, 0), 1))
    
    # List current bookings
    print("Current bookings:")
    for booking in booking_system.list_bookings():
        print(booking)

    # Attempt to book an overlapping time
    print(booking_system.add_booking("Charlie", "Flight Simulation", datetime(2023, 10, 15, 11, 0), 1))

    # Cancel a booking
    print(booking_system.cancel_booking("Alice", datetime(2023, 10, 15, 10, 0)))

    # List bookings after cancellation
    print("Bookings after cancellation:")
    for booking in booking_system.list_bookings():
        print(booking)
```
