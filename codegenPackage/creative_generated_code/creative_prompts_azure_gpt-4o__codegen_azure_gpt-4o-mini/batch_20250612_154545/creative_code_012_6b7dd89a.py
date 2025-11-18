"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Develop a program to manage bookings for airbrush nail art courses and master classes offered by AirstyleArt.
Generated: DETERMINISTIC_6b7dd89a625ffe3e
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# airbrush_nail_art_booking.py

from datetime import datetime
from typing import List, Optional

class Booking:
    """Class representing a booking for an airbrush nail art course or masterclass."""
    
    def __init__(self, name: str, email: str, course_date: str):
        """Initializes a new booking with the customer's name, email, and the date of the course."""
        self.name = name
        self.email = email
        self.course_date = self._parse_date(course_date)
    
    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        """Parses a date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Date must be in YYYY-MM-DD format") from e

    def __str__(self) -> str:
        """Returns a string representation of the booking."""
        return f"Booking(Name: {self.name}, Email: {self.email}, Date: {self.course_date.strftime('%Y-%m-%d')})"


class BookingManager:
    """Class for managing bookings for nail art courses."""
    
    def __init__(self):
        """Initializes the booking manager with an empty list of bookings."""
        self.bookings: List[Booking] = []

    def add_booking(self, name: str, email: str, course_date: str) -> None:
        """Adds a new booking to the list."""
        booking = Booking(name, email, course_date)
        self.bookings.append(booking)

    def list_bookings(self) -> List[str]:
        """Returns a list of all bookings in string format."""
        return [str(booking) for booking in self.bookings]

    def find_booking(self, email: str) -> Optional[Booking]:
        """Finds a booking by email. Returns None if not found."""
        for booking in self.bookings:
            if booking.email == email:
                return booking
        return None

    def remove_booking(self, email: str) -> bool:
        """Removes a booking by email. Returns True if removed, False if not found."""
        booking = self.find_booking(email)
        if booking:
            self.bookings.remove(booking)
            return True
        return False


def main():
    """Main function to demonstrate the booking management system."""
    manager = BookingManager()
    
    # Example usage
    try:
        # Adding bookings
        manager.add_booking("Alice Smith", "alice@example.com", "2023-11-10")
        manager.add_booking("Bob Johnson", "bob@example.com", "2023-11-15")

        # Listing bookings
        print("Current Bookings:")
        for booking in manager.list_bookings():
            print(booking)

        # Finding a specific booking
        email_to_find = "alice@example.com"
        found_booking = manager.find_booking(email_to_find)
        if found_booking:
            print(f"Found Booking: {found_booking}")
        else:
            print(f"No booking found for {email_to_find}")

        # Removing a booking
        if manager.remove_booking(email_to_find):
            print(f"Booking for {email_to_find} removed.")
        else:
            print(f"No booking found for {email_to_find} to remove.")

        # Listing bookings after removal
        print("Updated Bookings:")
        for booking in manager.list_bookings():
            print(booking)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
