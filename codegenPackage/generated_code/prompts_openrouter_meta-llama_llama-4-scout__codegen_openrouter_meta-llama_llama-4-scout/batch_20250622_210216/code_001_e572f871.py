"""
Generated Code Metadata:
========================
Original URL: https://sala-events.co.il
Prompt: "Write a Python script to manage event bookings for a venue like DCITY, including features for different event types and capacities."
Generated: DETERMINISTIC_e572f8712d0bd802
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_booking_system.py

from enum import Enum
from typing import Dict, List

class EventType(str, Enum):
    """Event types"""
    WEDDING = "Wedding"
    CONFERENCE = "Conference"
    FESTIVAL = "Festival"
    OTHER = "Other"

class Event:
    """Represents an event booking"""
    def __init__(self, event_id: int, event_type: EventType, date: str, capacity: int, attendees: List[str] = None):
        """
        Initialize an Event object.

        Args:
        - event_id (int): Unique identifier for the event
        - event_type (EventType): Type of event
        - date (str): Date of the event (YYYY-MM-DD)
        - capacity (int): Maximum number of attendees
        - attendees (List[str], optional): List of attendees. Defaults to None.
        """
        self.event_id = event_id
        self.event_type = event_type
        self.date = date
        self.capacity = capacity
        self.attendees = attendees if attendees else []

    def add_attendee(self, name: str):
        """Add an attendee to the event"""
        if len(self.attendees) < self.capacity:
            self.attendees.append(name)
            print(f"Attendee '{name}' added to event {self.event_id}")
        else:
            print(f"Event {self.event_id} is fully booked")

    def remove_attendee(self, name: str):
        """Remove an attendee from the event"""
        if name in self.attendees:
            self.attendees.remove(name)
            print(f"Attendee '{name}' removed from event {self.event_id}")
        else:
            print(f"Attendee '{name}' not found in event {self.event_id}")

class Venue:
    """Represents a venue with event bookings"""
    def __init__(self, name: str):
        """
        Initialize a Venue object.

        Args:
        - name (str): Name of the venue
        """
        self.name = name
        self.events: Dict[int, Event] = {}

    def book_event(self, event: Event):
        """Book an event at the venue"""
        self.events[event.event_id] = event
        print(f"Event {event.event_id} booked at {self.name}")

    def cancel_event(self, event_id: int):
        """Cancel an event booking"""
        if event_id in self.events:
            del self.events[event_id]
            print(f"Event {event_id} cancelled at {self.name}")
        else:
            print(f"Event {event_id} not found at {self.name}")

    def list_events(self):
        """List all event bookings"""
        print(f"Events at {self.name}:")
        for event in self.events.values():
            print(f"ID: {event.event_id}, Type: {event.event_type.value}, Date: {event.date}, Capacity: {event.capacity}, Attendees: {len(event.attendees)}")

def main():
    # Create a venue
    dcity = Venue("DCITY")

    try:
        # Book events
        event1 = Event(1, EventType.WEDDING, "2024-09-20", 100)
        event2 = Event(2, EventType.CONFERENCE, "2024-09-25", 50)
        dcity.book_event(event1)
        dcity.book_event(event2)

        # Add attendees
        event1.add_attendee("John Doe")
        event1.add_attendee("Jane Doe")
        event2.add_attendee("Alice Smith")

        # List events
        dcity.list_events()

        # Cancel an event
        dcity.cancel_event(2)

        # List events again
        dcity.list_events()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
