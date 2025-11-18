"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kroonation.com
Prompt: Write code for a consultation booking system that offers free 30-minute sessions, as described in Kroo Nation's consulting services.
Generated: DETERMINISTIC_5613c73bfd7018d2
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional


class Booking:
    """
    Represents a booking for a free 30-minute consultation session.
    """
    def __init__(self, name: str, email: str, date: datetime.date, time: datetime.time):
        self.name = name
        self.email = email
        self.date = date
        self.time = time

    def __str__(self):
        return f"Booking for {self.name} ({self.email}) on {self.date} at {self.time}"


class BookingSystem:
    """
    A system to manage consultation bookings for Kroo Nation.
    """
    def __init__(self):
        # Initialize an empty list of bookings
        self.bookings: List[Booking] = []

    def is_slot_available(self, date: datetime.date, time: datetime.time) -> bool:
        """
        Check if the requested slot is available.
        """
        for booking in self.bookings:
            if booking.date == date and booking.time == time:
                return False
        return True

    def add_booking(self, name: str, email: str, date: datetime.date, time: datetime.time) -> Optional[str]:
        """
        Add a new booking if the slot is available.
        """
        if not self.is_slot_available(date, time):
            return "The requested time slot is already booked. Please choose another time."

        new_booking = Booking(name, email, date, time)
        self.bookings.append(new_booking)
        return f"Booking confirmed: {new_booking}"

    def view_bookings(self) -> List[str]:
        """
        View all confirmed bookings.
        """
        if not self.bookings:
            return ["No bookings available."]
        return [str(booking) for booking in self.bookings]


def main():
    """
    Main function to demonstrate the consultation booking system functionality.
    """
    # Create an instance of the booking system
    system = BookingSystem()

    # Example of adding bookings
    try:
        print(system.add_booking("Alice", "alice@example.com", datetime.date(2023, 11, 1), datetime.time(10, 0)))
        print(system.add_booking("Bob", "bob@example.com", datetime.date(2023, 11, 1), datetime.time(10, 0)))
        print(system.add_booking("Charlie", "charlie@example.com", datetime.date(2023, 11, 1), datetime.time(11, 0)))
    except Exception as e:
        print(f"An error occurred: {e}")

    # Display all bookings
    print("\nConfirmed bookings:")
    for booking in system.view_bookings():
        print(booking)


if __name__ == "__main__":
    main()
```
