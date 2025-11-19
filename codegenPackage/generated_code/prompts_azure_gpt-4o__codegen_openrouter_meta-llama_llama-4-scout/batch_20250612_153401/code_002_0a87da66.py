"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Generate a script for automating event management and registration workflows in a CMS system tailored for cooperatives.
Generated: DETERMINISTIC_0a87da666661d58d
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_management.py

import datetime
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Event:
    def __init__(self, id: int, name: str, date: str, time: str, location: str, capacity: int):
        """
        Initialize an Event object.

        Args:
        id (int): Unique event identifier.
        name (str): Event name.
        date (str): Event date in YYYY-MM-DD format.
        time (str): Event time in HH:MM format.
        location (str): Event location.
        capacity (int): Maximum number of attendees.
        """
        self.id = id
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.capacity = capacity
        self.attendees = []

    def add_attendee(self, attendee: str):
        """
        Add an attendee to the event.

        Args:
        attendee (str): Attendee name.

        Raises:
        ValueError: If event is fully booked.
        """
        if len(self.attendees) < self.capacity:
            self.attendees.append(attendee)
        else:
            raise ValueError("Event is fully booked.")

    def __str__(self):
        return f"Event {self.id}: {self.name} on {self.date} at {self.time} in {self.location}"


class CooperativeCMS:
    def __init__(self):
        """
        Initialize a CooperativeCMS object.
        """
        self.events: Dict[int, Event] = {}
        self.next_event_id = 1

    def create_event(self, name: str, date: str, time: str, location: str, capacity: int):
        """
        Create a new event.

        Args:
        name (str): Event name.
        date (str): Event date in YYYY-MM-DD format.
        time (str): Event time in HH:MM format.
        location (str): Event location.
        capacity (int): Maximum number of attendees.

        Returns:
        int: Unique event identifier.
        """
        event = Event(self.next_event_id, name, date, time, location, capacity)
        self.events[self.next_event_id] = event
        self.next_event_id += 1
        return event.id

    def get_event(self, event_id: int):
        """
        Retrieve an event by its ID.

        Args:
        event_id (int): Unique event identifier.

        Returns:
        Event: Event object or None if not found.
        """
        return self.events.get(event_id)

    def register_attendee(self, event_id: int, attendee: str):
        """
        Register an attendee for an event.

        Args:
        event_id (int): Unique event identifier.
        attendee (str): Attendee name.

        Raises:
        ValueError: If event is not found or fully booked.
        """
        event = self.get_event(event_id)
        if event:
            event.add_attendee(attendee)
        else:
            raise ValueError("Event not found.")

    def list_events(self):
        """
        List all events.

        Returns:
        List[Event]: List of Event objects.
        """
        return list(self.events.values())


def main():
    try:
        cms = CooperativeCMS()

        # Create events
        event1_id = cms.create_event("General Meeting", "2024-09-20", "10:00", "Headquarters", 50)
        event2_id = cms.create_event("Workshop", "2024-09-22", "14:00", "Conference Room", 20)

        # Register attendees
        cms.register_attendee(event1_id, "John Doe")
        cms.register_attendee(event1_id, "Jane Smith")
        cms.register_attendee(event2_id, "Bob Johnson")

        # List events
        events = cms.list_events()
        for event in events:
            logger.info(event)
            logger.info(f"Attendees: {event.attendees}")

    except Exception as e:
        logger.error(f"Error: {e}")


if __name__ == "__main__":
    main()
```
