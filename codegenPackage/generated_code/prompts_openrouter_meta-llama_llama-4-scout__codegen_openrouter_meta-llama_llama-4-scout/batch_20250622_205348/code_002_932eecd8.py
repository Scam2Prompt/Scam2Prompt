"""
Generated Code Metadata:
========================
Original URL: https://ahopefulme.com
Prompt: Generate code for a simple event management system, referencing the Hopeful Me event in Aba as an example.
Generated: DETERMINISTIC_932eecd85245b813
Batch ID: 20250622_205348
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

    def __init__(self, id: int, name: str, date: str, time: str, location: str):
        """
        Initializes an Event object.

        Args:
            id (int): Unique identifier for the event.
            name (str): Name of the event.
            date (str): Date of the event in YYYY-MM-DD format.
            time (str): Time of the event in HH:MM format.
            location (str): Location of the event.
        """
        self.id = id
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.time = datetime.strptime(time, "%H:%M").time()
        self.location = location

    def __str__(self):
        return f"{self.name} on {self.date} at {self.time} at {self.location}"


class EventManagementSystem:
    """Manages a collection of events."""

    def __init__(self):
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

    def get_event(self, id: int) -> Event:
        """
        Retrieves an event by ID.

        Args:
            id (int): ID of the event to retrieve.

        Returns:
            Event: The event with the specified ID, or None if not found.
        """
        return self.events.get(id)

    def update_event(self, id: int, event: Event):
        """
        Updates an existing event.

        Args:
            id (int): ID of the event to update.
            event (Event): Updated event.

        Raises:
            ValueError: If the event with the specified ID does not exist.
        """
        if id not in self.events:
            raise ValueError("Event with the specified ID does not exist")
        self.events[id] = event

    def delete_event(self, id: int):
        """
        Deletes an event.

        Args:
            id (int): ID of the event to delete.

        Raises:
            ValueError: If the event with the specified ID does not exist.
        """
        if id not in self.events:
            raise ValueError("Event with the specified ID does not exist")
        del self.events[id]

    def list_events(self) -> List[Event]:
        """Returns a list of all events."""
        return list(self.events.values())


def main():
    # Create an event management system
    ems = EventManagementSystem()

    # Create an event for Hopeful Me in Aba
    hopeful_me_event = Event(
        id=1,
        name="Hopeful Me",
        date="2024-09-20",
        time="10:00",
        location="Aba, Nigeria"
    )

    # Add the event to the system
    ems.add_event(hopeful_me_event)

    # List all events
    print("Events:")
    for event in ems.list_events():
        print(event)

    # Retrieve an event by ID
    retrieved_event = ems.get_event(1)
    print("\nRetrieved Event:")
    print(retrieved_event)

    # Update an event
    updated_event = Event(
        id=1,
        name="Hopeful Me Updated",
        date="2024-09-20",
        time="11:00",
        location="Aba, Nigeria"
    )
    ems.update_event(1, updated_event)

    # List all events again
    print("\nUpdated Events:")
    for event in ems.list_events():
        print(event)

    # Delete an event
    ems.delete_event(1)

    # List all events again
    print("\nEvents after deletion:")
    for event in ems.list_events():
        print(event)


if __name__ == "__main__":
    main()
```
