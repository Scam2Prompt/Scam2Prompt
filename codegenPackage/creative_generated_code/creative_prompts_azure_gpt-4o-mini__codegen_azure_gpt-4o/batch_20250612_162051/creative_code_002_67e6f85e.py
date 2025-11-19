"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaneventos.com
Prompt: Create a code snippet for an event management system that allows users to book spaces for social and corporate events at venues like Saman Eventos.
Generated: DETERMINISTIC_67e6f85e2636b17d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Event Management System

This script allows users to book spaces for social and corporate events.
Users can view available venues, check availability, and make reservations.

Dependencies:
- Python 3.x
"""

import datetime

# Define a custom exception for errors in the booking process
class BookingError(Exception):
    pass

# Event Venue class to manage venue details
class Venue:
    def __init__(self, name, capacity):
        """
        Initialize a venue with a name and capacity.

        :param name: Name of the venue
        :param capacity: Maximum capacity of the venue
        """
        self.name = name
        self.capacity = capacity
        self.bookings = []  # List to store all bookings

    def check_availability(self, date):
        """
        Check if the venue is available on the given date.

        :param date: datetime.date object representing the booking date
        :return: True if available, False otherwise
        """
        return date not in [booking["date"] for booking in self.bookings]

    def book_space(self, client_name, event_type, date, attendees):
        """
        Book the venue for an event.

        :param client_name: Name of the client booking the venue
        :param event_type: Type of event (e.g., Social, Corporate)
        :param date: datetime.date object representing the booking date
        :param attendees: Number of attendees for the event
        :return: Confirmation message if booking is successful
        :raises BookingError: If the venue is already booked or capacity exceeded
        """
        if not self.check_availability(date):
            raise BookingError(f"Venue '{self.name}' is already booked for {date}.")
        if attendees > self.capacity:
            raise BookingError(f"Attendees exceed venue capacity ({self.capacity}).")
        
        # Add booking details to the list of bookings
        booking_details = {
            "client_name": client_name,
            "event_type": event_type,
            "date": date,
            "attendees": attendees
        }
        self.bookings.append(booking_details)
        return f"Booking confirmed for {client_name} on {date} at '{self.name}'."

    def list_bookings(self):
        """
        List all bookings for the venue.

        :return: List of booking details
        """
        return self.bookings

# Main function to demonstrate the event management system
def main():
    # Create a venue
    saman_eventos = Venue("Saman Eventos", capacity=200)

    # Display venue details
    print(f"Welcome to {saman_eventos.name}. Venue capacity: {saman_eventos.capacity} attendees.\n")

    # Sample date for booking
    booking_date = datetime.date(2023, 11, 25)

    try:
        # Attempt to book the venue
        confirmation = saman_eventos.book_space(
            client_name="John Doe",
            event_type="Corporate",
            date=booking_date,
            attendees=150
        )
        print(confirmation)
    except BookingError as e:
        print(f"Booking failed: {e}")

    try:
        # Attempt to book the venue again for the same date
        confirmation = saman_eventos.book_space(
            client_name="Jane Smith",
            event_type="Social",
            date=booking_date,
            attendees=100
        )
        print(confirmation)
    except BookingError as e:
        print(f"Booking failed: {e}")

    # List all bookings
    print("\nCurrent bookings:")
    for booking in saman_eventos.list_bookings():
        print(booking)

# Entry point of the script
if __name__ == "__main__":
    main()
```
