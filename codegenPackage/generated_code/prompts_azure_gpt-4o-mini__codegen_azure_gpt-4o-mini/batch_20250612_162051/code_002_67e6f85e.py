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
from datetime import datetime
from typing import List, Optional

class Venue:
    """Class representing a venue for events."""
    
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.bookings: List['Booking'] = []

    def is_available(self, start_time: datetime, end_time: datetime) -> bool:
        """Check if the venue is available for the given time slot."""
        for booking in self.bookings:
            if booking.overlaps(start_time, end_time):
                return False
        return True

    def book(self, booking: 'Booking') -> None:
        """Book the venue for a specific booking."""
        if not self.is_available(booking.start_time, booking.end_time):
            raise ValueError(f"Venue {self.name} is not available for the requested time.")
        self.bookings.append(booking)

class Booking:
    """Class representing a booking for an event."""
    
    def __init__(self, event_name: str, start_time: datetime, end_time: datetime, venue: Venue):
        self.event_name = event_name
        self.start_time = start_time
        self.end_time = end_time
        self.venue = venue

    def overlaps(self, start_time: datetime, end_time: datetime) -> bool:
        """Check if this booking overlaps with another time slot."""
        return self.start_time < end_time and start_time < self.end_time

class EventManager:
    """Class to manage event bookings."""
    
    def __init__(self):
        self.venues: List[Venue] = []

    def add_venue(self, venue: Venue) -> None:
        """Add a new venue to the event manager."""
        self.venues.append(venue)

    def book_event(self, event_name: str, start_time: datetime, end_time: datetime, venue_name: str) -> Optional[Booking]:
        """Book an event at a specified venue."""
        venue = next((v for v in self.venues if v.name == venue_name), None)
        if venue is None:
            raise ValueError(f"Venue {venue_name} not found.")
        
        booking = Booking(event_name, start_time, end_time, venue)
        try:
            venue.book(booking)
            return booking
        except ValueError as e:
            print(e)
            return None

# Example usage
if __name__ == "__main__":
    # Create an event manager
    event_manager = EventManager()

    # Add venues
    venue1 = Venue("Saman Eventos", 200)
    venue2 = Venue("Grand Hall", 300)
    event_manager.add_venue(venue1)
    event_manager.add_venue(venue2)

    # Book an event
    start_time = datetime(2023, 12, 1, 10, 0)
    end_time = datetime(2023, 12, 1, 15, 0)
    booking = event_manager.book_event("Corporate Meeting", start_time, end_time, "Saman Eventos")

    if booking:
        print(f"Successfully booked {booking.event_name} at {booking.venue.name} from {booking.start_time} to {booking.end_time}.")
    else:
        print("Booking failed.")
```
