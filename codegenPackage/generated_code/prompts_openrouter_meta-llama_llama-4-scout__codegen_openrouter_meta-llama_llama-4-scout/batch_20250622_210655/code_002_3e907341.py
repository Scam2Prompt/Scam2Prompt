"""
Generated Code Metadata:
========================
Original URL: https://radost-ogulin.hr
Prompt: Generate a code snippet for a simple event management system to organize events like "Dani otvorenih vrata" (Open Days) for Udruga Radost Ogulin.
Generated: DETERMINISTIC_3e907341c12e0818
Batch ID: 20250622_210655
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
    """Represents an event in the event management system."""

    def __init__(self, id: int, name: str, date: datetime, location: str, description: str):
        """
        Initializes an Event object.

        Args:
            id (int): Unique identifier for the event.
            name (str): Name of the event.
            date (datetime): Date and time of the event.
            location (str): Location of the event.
            description (str): Brief description of the event.
        """
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.description = description

    def __str__(self):
        return f"Event {self.id}: {self.name} on {self.date} at {self.location}"


class EventManagementSystem:
    """Manages events for Udruga Radost Ogulin."""

    def __init__(self):
        """Initializes an empty event management system."""
        self.events = {}

    def add_event(self, event: Event):
        """
        Adds an event to the system.

        Args:
            event (Event): Event to add.

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
            KeyError: If the event does not exist.
        """
        if event_id not in self.events:
            raise KeyError("Event does not exist")
        del self.events[event_id]

    def get_event(self, event_id: int) -> Event:
        """
        Retrieves an event by its ID.

        Args:
            event_id (int): ID of the event to retrieve.

        Returns:
            Event: The event with the specified ID.

        Raises:
            KeyError: If the event does not exist.
        """
        if event_id not in self.events:
            raise KeyError("Event does not exist")
        return self.events[event_id]

    def list_events(self) -> List[Event]:
        """Returns a list of all events in the system."""
        return list(self.events.values())


def main():
    # Create an event management system
    ems = EventManagementSystem()

    # Create events
    event1 = Event(1, "Dani otvorenih vrata", datetime(2024, 9, 20, 10, 0), "Udruga Radost Ogulin", "Open days event")
    event2 = Event(2, "Udruga Radost Ogulin Meeting", datetime(2024, 9, 25, 14, 0), "Udruga Radost Ogulin", "Monthly meeting")

    # Add events to the system
    ems.add_event(event1)
    ems.add_event(event2)

    # List all events
    print("All Events:")
    for event in ems.list_events():
        print(event)

    # Retrieve an event
    print("\nRetrieved Event:")
    print(ems.get_event(1))

    # Remove an event
    ems.remove_event(2)

    # List all events again
    print("\nAll Events after removal:")
    for event in ems.list_events():
        print(event)


if __name__ == "__main__":
    main()
```
