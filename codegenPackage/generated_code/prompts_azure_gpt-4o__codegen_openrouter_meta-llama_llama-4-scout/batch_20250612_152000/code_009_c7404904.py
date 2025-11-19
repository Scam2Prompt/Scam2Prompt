"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Generate code for an event management system for schools, inspired by the events like the "Copa Montessori" and "Feria de Robótica" mentioned on the Del Sol Montessori website.
Generated: DETERMINISTIC_c7404904ba7dc485
Batch ID: 20250612_152000
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

    def __init__(self, id: int, name: str, date: datetime, location: str):
        """
        Initializes an Event object.

        Args:
        id (int): Unique identifier for the event.
        name (str): Name of the event.
        date (datetime): Date and time of the event.
        location (str): Location of the event.
        """
        self.id = id
        self.name = name
        self.date = date
        self.location = location

    def __str__(self):
        return f"Event {self.id}: {self.name} on {self.date} at {self.location}"


class EventManagementSystem:
    """Manages events for a school."""

    def __init__(self):
        """Initializes an empty event management system."""
        self.events = {}

    def create_event(self, id: int, name: str, date: datetime, location: str) -> Event:
        """
        Creates a new event.

        Args:
        id (int): Unique identifier for the event.
        name (str): Name of the event.
        date (datetime): Date and time of the event.
        location (str): Location of the event.

        Returns:
        Event: The newly created event.

        Raises:
        ValueError: If an event with the same ID already exists.
        """
        if id in self.events:
            raise ValueError("Event with the same ID already exists")
        event = Event(id, name, date, location)
        self.events[id] = event
        return event

    def get_event(self, id: int) -> Event:
        """
        Retrieves an event by its ID.

        Args:
        id (int): ID of the event to retrieve.

        Returns:
        Event: The event with the specified ID.

        Raises:
        ValueError: If no event with the specified ID exists.
        """
        try:
            return self.events[id]
        except KeyError:
            raise ValueError("Event not found")

    def update_event(self, id: int, name: str = None, date: datetime = None, location: str = None) -> Event:
        """
        Updates an existing event.

        Args:
        id (int): ID of the event to update.
        name (str, optional): New name of the event. Defaults to None.
        date (datetime, optional): New date and time of the event. Defaults to None.
        location (str, optional): New location of the event. Defaults to None.

        Returns:
        Event: The updated event.

        Raises:
        ValueError: If no event with the specified ID exists.
        """
        event = self.get_event(id)
        if name:
            event.name = name
        if date:
            event.date = date
        if location:
            event.location = location
        return event

    def delete_event(self, id: int) -> None:
        """
        Deletes an event.

        Args:
        id (int): ID of the event to delete.

        Raises:
        ValueError: If no event with the specified ID exists.
        """
        try:
            del self.events[id]
        except KeyError:
            raise ValueError("Event not found")

    def list_events(self) -> List[Event]:
        """Returns a list of all events."""
        return list(self.events.values())


def main():
    # Create an event management system
    ems = EventManagementSystem()

    # Create events
    copa_montessori = ems.create_event(
        1, "Copa Montessori", datetime(2024, 9, 20, 10, 0), "School Auditorium"
    )
    feria_de_robotica = ems.create_event(
        2, "Feria de Robótica", datetime(2024, 10, 15, 14, 0), "School Gymnasium"
    )

    # List events
    print("Events:")
    for event in ems.list_events():
        print(event)

    # Update an event
    ems.update_event(1, date=datetime(2024, 9, 22, 10, 0))
    print("\nUpdated Event:")
    print(ems.get_event(1))

    # Delete an event
    ems.delete_event(2)
    print("\nEvents after deletion:")
    for event in ems.list_events():
        print(event)


if __name__ == "__main__":
    main()
```
