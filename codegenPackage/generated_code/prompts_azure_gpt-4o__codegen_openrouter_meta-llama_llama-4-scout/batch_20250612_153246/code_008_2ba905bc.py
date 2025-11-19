"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Write code to schedule and manage events like plantation drives or food distribution programs, as highlighted in Youngistaan Foundation's blog.
Generated: DETERMINISTIC_2ba905bc681e7346
Batch ID: 20250612_153246
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

class Event:
    """Represents a scheduled event."""

    def __init__(self, id: int, name: str, date: str, time: str, location: str, description: str):
        """
        Initializes an Event object.

        Args:
        id (int): Unique event identifier.
        name (str): Event name.
        date (str): Event date in YYYY-MM-DD format.
        time (str): Event time in HH:MM format.
        location (str): Event location.
        description (str): Event description.
        """
        self.id = id
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.time = datetime.strptime(time, "%H:%M").time()
        self.location = location
        self.description = description

    def __str__(self):
        return f"Event {self.id}: {self.name} on {self.date} at {self.time} at {self.location}"


class EventManagementSystem:
    """Manages scheduled events."""

    def __init__(self):
        self.events = {}

    def add_event(self, event: Event):
        """
        Adds a new event to the system.

        Args:
        event (Event): Event object to add.

        Raises:
        ValueError: If an event with the same ID already exists.
        """
        if event.id in self.events:
            raise ValueError("Event with the same ID already exists")
        self.events[event.id] = event

    def remove_event(self, event_id: int):
        """
        Removes an event from the system.

        Args:
        event_id (int): ID of the event to remove.

        Raises:
        KeyError: If the event ID does not exist.
        """
        if event_id not in self.events:
            raise KeyError("Event ID does not exist")
        del self.events[event_id]

    def update_event(self, event_id: int, event: Event):
        """
        Updates an existing event in the system.

        Args:
        event_id (int): ID of the event to update.
        event (Event): Updated Event object.

        Raises:
        KeyError: If the event ID does not exist.
        """
        if event_id not in self.events:
            raise KeyError("Event ID does not exist")
        self.events[event_id] = event

    def get_event(self, event_id: int) -> Event:
        """
        Retrieves an event by its ID.

        Args:
        event_id (int): ID of the event to retrieve.

        Returns:
        Event: Event object if found, None otherwise.
        """
        return self.events.get(event_id)

    def list_events(self) -> List[Event]:
        """Returns a list of all scheduled events."""
        return list(self.events.values())


def main():
    # Create an event management system
    event_system = EventManagementSystem()

    # Create events
    event1 = Event(1, "Plantation Drive", "2024-09-20", "10:00", "Local Park", "Plant trees and promote sustainability")
    event2 = Event(2, "Food Distribution Program", "2024-09-25", "14:00", "Community Center", "Distribute food to those in need")

    # Add events to the system
    event_system.add_event(event1)
    event_system.add_event(event2)

    # List all events
    print("Scheduled Events:")
    for event in event_system.list_events():
        print(event)

    # Retrieve an event by ID
    retrieved_event = event_system.get_event(1)
    print("\nRetrieved Event:")
    print(retrieved_event)

    # Update an event
    updated_event = Event(1, "Plantation Drive", "2024-09-27", "10:00", "Local Park", "Plant trees and promote sustainability")
    event_system.update_event(1, updated_event)

    # List all events again
    print("\nUpdated Scheduled Events:")
    for event in event_system.list_events():
        print(event)

    # Remove an event
    event_system.remove_event(2)

    # List all events again
    print("\nScheduled Events after removal:")
    for event in event_system.list_events():
        print(event)


if __name__ == "__main__":
    main()
```
