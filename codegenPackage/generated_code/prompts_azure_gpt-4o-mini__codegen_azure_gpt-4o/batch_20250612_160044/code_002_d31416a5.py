"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Create a Python script that manages tennis court bookings, ensuring optimal usage of facilities like those at TC Harsewinkel.
Generated: DETERMINISTIC_d31416a5297de891
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class TennisCourtBookingSystem:
    """
    A system to manage tennis court bookings, ensuring optimal usage of facilities.
    """

    def __init__(self):
        # Initialize the booking system with empty bookings
        self.bookings = {}  # Dictionary to store bookings {date: {time_slot: court_number}}

    def list_available_courts(self, date, time_slot):
        """
        List available courts for a given date and time slot.
        :param date: Date in YYYY-MM-DD format
        :param time_slot: Time slot in HH:MM-HH:MM format
        :return: List of available court numbers
        """
        all_courts = {1, 2, 3, 4}  # Example: 4 courts available
        booked_courts = set(self.bookings.get(date, {}).get(time_slot, []))
        return list(all_courts - booked_courts)

    def book_court(self, date, time_slot, court_number):
        """
        Book a tennis court for a specific date and time slot.
        :param date: Date in YYYY-MM-DD format
        :param time_slot: Time slot in HH:MM-HH:MM format
        :param court_number: Court number to book
        :return: Success message or error message
        """
        # Validate input
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return "Error: Invalid date format. Use YYYY-MM-DD."

        if not self._validate_time_slot(time_slot):
            return "Error: Invalid time slot format. Use HH:MM-HH:MM."

        if court_number not in {1, 2, 3, 4}:
            return f"Error: Court {court_number} does not exist."

        # Check availability
        if court_number in self.bookings.get(date, {}).get(time_slot, []):
            return f"Error: Court {court_number} is already booked for {date} at {time_slot}."

        # Book the court
        if date not in self.bookings:
            self.bookings[date] = {}
        if time_slot not in self.bookings[date]:
            self.bookings[date][time_slot] = []
        self.bookings[date][time_slot].append(court_number)

        return f"Success: Court {court_number} booked for {date} at {time_slot}."

    def cancel_booking(self, date, time_slot, court_number):
        """
        Cancel a booking for a specific date, time slot, and court number.
        :param date: Date in YYYY-MM-DD format
        :param time_slot: Time slot in HH:MM-HH:MM format
        :param court_number: Court number to cancel
        :return: Success message or error message
        """
        if date in self.bookings and time_slot in self.bookings[date]:
            if court_number in self.bookings[date][time_slot]:
                self.bookings[date][time_slot].remove(court_number)
                return f"Success: Booking for court {court_number} on {date} at {time_slot} has been canceled."
            else:
                return f"Error: Court {court_number} is not booked for {date} at {time_slot}."
        return f"Error: No booking found for {date} at {time_slot}."

    def view_bookings(self):
        """
        View all bookings in the system.
        :return: Dictionary of bookings
        """
        return self.bookings

    @staticmethod
    def _validate_time_slot(time_slot):
        """
        Validate the time slot format.
        :param time_slot: Time slot in HH:MM-HH:MM format
        :return: True if valid, False otherwise
        """
        try:
            start_time, end_time = time_slot.split("-")
            datetime.datetime.strptime(start_time, "%H:%M")
            datetime.datetime.strptime(end_time, "%H:%M")
            return True
        except ValueError:
            return False


# Example usage
if __name__ == "__main__":
    system = TennisCourtBookingSystem()

    # Book a court
    print(system.book_court("2023-10-15", "10:00-11:00", 1))

    # List available courts
    print(system.list_available_courts("2023-10-15", "10:00-11:00"))

    # Cancel a booking
    print(system.cancel_booking("2023-10-15", "10:00-11:00", 1))

    # View all bookings
    print(system.view_bookings())
```
