"""
Generated Code Metadata:
========================
Original URL: https://samaneventos.com
Prompt: Create a code snippet for an event management system that allows users to book spaces for social and corporate events at venues like Saman Eventos.
Generated: DETERMINISTIC_67e6f85e2636b17d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_management_system.py

from datetime import datetime
from typing import List

class Venue:
    """Represents a venue for events."""

    def __init__(self, id: int, name: str, capacity: int):
        """
        Initializes a Venue object.

        Args:
        id (int): Unique identifier for the venue.
        name (str): Name of the venue.
        capacity (int): Maximum capacity of the venue.
        """
        self.id = id
        self.name = name
        self.capacity = capacity

class Event:
    """Represents an event to be booked at a venue."""

    def __init__(self, id: int, name: str, date: datetime, attendees: int):
        """
        Initializes an Event object.

        Args:
        id (int): Unique identifier for the event.
        name (str): Name of the event.
        date (datetime): Date and time of the event.
        attendees (int): Number of attendees for the event.
        """
        self.id = id
        self.name = name
        self.date = date
        self.attendees = attendees

class Booking:
    """Represents a booking for an event at a venue."""

    def __init__(self, event: Event, venue: Venue):
        """
        Initializes a Booking object.

        Args:
        event (Event): Event to be booked.
        venue (Venue): Venue where the event will be booked.
        """
        self.event = event
        self.venue = venue

class EventManagementSystem:
    """Manages bookings for events at venues."""

    def __init__(self):
        self.venues = []
        self.bookings = []

    def add_venue(self, venue: Venue):
        """
        Adds a venue to the system.

        Args:
        venue (Venue): Venue to be added.
        """
        self.venues.append(venue)

    def book_event(self, event: Event, venue_id: int) -> Booking:
        """
        Books an event at a venue.

        Args:
        event (Event): Event to be booked.
        venue_id (int): ID of the venue where the event will be booked.

        Returns:
        Booking: The booking for the event at the venue.

        Raises:
        ValueError: If the venue ID is not found.
        """
        venue = next((v for v in self.venues if v.id == venue_id), None)
        if venue is None:
            raise ValueError("Venue not found")

        if event.attendees > venue.capacity:
            raise ValueError("Event attendees exceed venue capacity")

        booking = Booking(event, venue)
        self.bookings.append(booking)
        return booking

    def get_bookings(self) -> List[Booking]:
        """
        Retrieves all bookings.

        Returns:
        List[Booking]: List of all bookings.
        """
        return self.bookings

def main():
    # Create an event management system
    ems = EventManagementSystem()

    # Create venues
    saman_eventos = Venue(1, "Saman Eventos", 1000)
    ems.add_venue(saman_eventos)

    # Create events
    event1 = Event(1, "Corporate Meeting", datetime(2024, 9, 20, 10, 0), 500)
    event2 = Event(2, "Social Party", datetime(2024, 10, 15, 18, 0), 800)

    try:
        # Book events
        booking1 = ems.book_event(event1, 1)
        booking2 = ems.book_event(event2, 1)

        # Print bookings
        for i, booking in enumerate(ems.get_bookings()):
            print(f"Booking {i+1}:")
            print(f"Event: {booking.event.name} on {booking.event.date}")
            print(f"Venue: {booking.venue.name}")
            print(f"Attendees: {booking.event.attendees}")
            print("------------------------")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
