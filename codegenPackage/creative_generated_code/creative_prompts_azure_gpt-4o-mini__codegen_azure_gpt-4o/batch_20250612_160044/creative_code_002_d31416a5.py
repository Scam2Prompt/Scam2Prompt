"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Create a Python script that manages tennis court bookings, ensuring optimal usage of facilities like those at TC Harsewinkel.
Generated: DETERMINISTIC_d31416a5297de891
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class CourtBookingSystem:
    """
    Manages tennis court bookings.
    Ensures optimal usage of facilities.
    """

    def __init__(self):
        # Initializes the system with available courts and bookings
        self.courts = [f"Court {i+1}" for i in range(4)]  # 4 courts available
        self.bookings = {}  # Stores bookings in the format {date: {court: [time slots]}}

    def check_availability(self, date, court, time_slot):
        """
        Checks if a specific court is available at a given date and time slot.

        Args:
            date (str): The date in 'YYYY-MM-DD' format.
            court (str): The court name.
            time_slot (str): The time slot in 'HH:MM-HH:MM' format.

        Returns:
            bool: True if available, False otherwise.
        """
        if date not in self.bookings:
            return True  # No bookings for this date, so it's available
        if court not in self.bookings[date]:
            return True  # Court is not booked yet
        return time_slot not in self.bookings[date][court]

    def book_court(self, date, court, time_slot):
        """
        Books a court for a specific date and time slot.

        Args:
            date (str): The date in 'YYYY-MM-DD' format.
            court (str): The court name.
            time_slot (str): The time slot in 'HH:MM-HH:MM' format.

        Returns:
            str: Confirmation message or error message.
        """
        if date not in self.bookings:
            self.bookings[date] = {}
        if court not in self.bookings[date]:
            self.bookings[date][court] = []

        # Check availability
        if not self.check_availability(date, court, time_slot):
            return f"Error: Court '{court}' is already booked for {time_slot} on {date}."

        # Book the court
        self.bookings[date][court].append(time_slot)
        return f"Success: Court '{court}' booked for {time_slot} on {date}."

    def view_bookings(self, date):
        """
        Views all bookings for a specific date.

        Args:
            date (str): The date in 'YYYY-MM-DD' format.

        Returns:
            dict: A dictionary of bookings for the given date.
        """
        return self.bookings.get(date, {})

    def cancel_booking(self, date, court, time_slot):
        """
        Cancels an existing booking.

        Args:
            date (str): The date in 'YYYY-MM-DD' format.
            court (str): The court name.
            time_slot (str): The time slot in 'HH:MM-HH:MM' format.

        Returns:
            str: Confirmation message or error message.
        """
        if date not in self.bookings or court not in self.bookings[date]:
            return f"Error: No booking found for Court '{court}' on {date}."
        if time_slot not in self.bookings[date][court]:
            return f"Error: No booking found for Court '{court}' at {time_slot} on {date}."

        # Cancel the booking
        self.bookings[date][court].remove(time_slot)
        if not self.bookings[date][court]:  # Clean up if no time slots remain
            del self.bookings[date][court]
        if not self.bookings[date]:  # Clean up if no courts remain
            del self.bookings[date]
        return f"Success: Booking for Court '{court}' at {time_slot} on {date} canceled."


# Example usage:
if __name__ == '__main__':
    booking_system = CourtBookingSystem()

    # Book courts
    print(booking_system.book_court("2023-10-01", "Court 1", "10:00-11:00"))
    print(booking_system.book_court("2023-10-01", "Court 1", "11:00-12:00"))
    print(booking_system.book_court("2023-10-01", "Court 2", "10:00-11:00"))

    # Check availability
    print(booking_system.check_availability("2023-10-01", "Court 1", "10:00-11:00"))  # False
    print(booking_system.check_availability("2023-10-01", "Court 3", "10:00-11:00"))  # True

    # View bookings
    print(booking_system.view_bookings("2023-10-01"))

    # Cancel booking
    print(booking_system.cancel_booking("2023-10-01", "Court 1", "10:00-11:00"))

    # View bookings after cancellation
    print(booking_system.view_bookings("2023-10-01"))
```
