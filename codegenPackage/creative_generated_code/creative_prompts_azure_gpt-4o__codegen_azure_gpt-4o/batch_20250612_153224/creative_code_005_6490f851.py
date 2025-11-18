"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Develop a Python program to manage bookings for a music studio, such as the one managed by Sophia Loisirs & Vie, including features for scheduling and availability checks.
Generated: DETERMINISTIC_6490f85178326306
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class MusicStudioBooking:
    """
    A class to manage bookings for a music studio.
    Supports scheduling, availability checks, and management of bookings.
    """

    def __init__(self):
        """
        Initialize an empty booking dictionary to store bookings by date.
        Each date will have a list of booked time slots.
        """
        self.bookings = {}

    def is_slot_available(self, date, start_time, end_time):
        """
        Check if a time slot is available for a given date.
        :param date: The date for booking in 'YYYY-MM-DD' format.
        :param start_time: Start time in 'HH:MM' format.
        :param end_time: End time in 'HH:MM' format.
        :return: True if the slot is available, False otherwise.
        """
        if date not in self.bookings:
            return True  # No bookings exist for the given date

        # Check against existing bookings on the date
        for slot in self.bookings[date]:
            existing_start, existing_end = slot
            if not (end_time <= existing_start or start_time >= existing_end):
                return False  # Time slot overlaps with an existing booking

        return True

    def book_slot(self, date, start_time, end_time):
        """
        Book a slot if it's available.
        :param date: The date for booking in 'YYYY-MM-DD' format.
        :param start_time: Start time in 'HH:MM' format.
        :param end_time: End time in 'HH:MM' format.
        :return: A message indicating success or failure.
        """
        # Input validation
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            datetime.datetime.strptime(start_time, '%H:%M')
            datetime.datetime.strptime(end_time, '%H:%M')
        except ValueError:
            return "Invalid date or time format. Please use 'YYYY-MM-DD' for date and 'HH:MM' for time."

        if start_time >= end_time:
            return "Start time must be earlier than end time."

        # Check availability
        if self.is_slot_available(date, start_time, end_time):
            if date not in self.bookings:
                self.bookings[date] = []  # Initialize the date if no bookings exist
            self.bookings[date].append((start_time, end_time))
            return f"Booking successful for {date} from {start_time} to {end_time}."
        else:
            return f"Time slot unavailable for {date} from {start_time} to {end_time}."

    def view_bookings(self, date):
        """
        View all bookings for a specific date.
        :param date: The date for viewing bookings in 'YYYY-MM-DD' format.
        :return: A list of bookings for the date, or a message if no bookings exist.
        """
        if date not in self.bookings or not self.bookings[date]:
            return f"No bookings found for {date}."
        
        return [f"{start_time} - {end_time}" for start_time, end_time in self.bookings[date]]

    def cancel_booking(self, date, start_time, end_time):
        """
        Cancel a specific booking.
        :param date: The date of the booking in 'YYYY-MM-DD' format.
        :param start_time: Start time in 'HH:MM' format.
        :param end_time: End time in 'HH:MM' format.
        :return: A message indicating success or failure.
        """
        if date in self.bookings:
            for slot in self.bookings[date]:
                if slot == (start_time, end_time):
                    self.bookings[date].remove(slot)
                    return f"Booking cancelled for {date} from {start_time} to {end_time}."
        
        return f"No matching booking found for {date} from {start_time} to {end_time}."

# Example usage:
if __name__ == "__main__":
    studio = MusicStudioBooking()

    # Book a slot
    print(studio.book_slot("2023-12-01", "10:00", "12:00"))
    print(studio.book_slot("2023-12-01", "12:00", "14:00"))

    # Attempt to book an overlapping slot
    print(studio.book_slot("2023-12-01", "11:00", "13:00"))

    # View bookings
    print(studio.view_bookings("2023-12-01"))

    # Cancel a booking
    print(studio.cancel_booking("2023-12-01", "10:00", "12:00"))

    # View bookings after cancellation
    print(studio.view_bookings("2023-12-01"))
```
