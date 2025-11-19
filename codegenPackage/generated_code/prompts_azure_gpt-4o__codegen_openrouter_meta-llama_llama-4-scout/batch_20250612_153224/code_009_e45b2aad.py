"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Implement a feature to manage school events and cultural activities, inspired by the Event Planning module in Him Saral's school management system.
Generated: DETERMINISTIC_e45b2aad45e57ffc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_manager.py

from datetime import datetime
from typing import List, Dict

class Event:
    """Represents a school event or cultural activity."""

    def __init__(self, id: int, name: str, description: str, start_date: datetime, end_date: datetime, location: str):
        """
        Initializes an Event object.

        Args:
        id (int): Unique identifier for the event.
        name (str): Name of the event.
        description (str): Brief description of the event.
        start_date (datetime): Start date and time of the event.
        end_date (datetime): End date and time of the event.
        location (str): Location where the event will take place.
        """
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

    def __str__(self):
        return f"Event {self.id}: {self.name} on {self.start_date} at {self.location}"


class EventManager:
    """Manages school events and cultural activities."""

    def __init__(self):
        self.events: Dict[int, Event] = {}
        self.next_id: int = 1

    def create_event(self, name: str, description: str, start_date: datetime, end_date: datetime, location: str) -> Event:
        """
        Creates a new event.

        Args:
        name (str): Name of the event.
        description (str): Brief description of the event.
        start_date (datetime): Start date and time of the event.
        end_date (datetime): End date and time of the event.
        location (str): Location where the event will take place.

        Returns:
        Event: The newly created event.

        Raises:
        ValueError: If start date is after end date.
        """
        if start_date > end_date:
            raise ValueError("Start date cannot be after end date")

        event = Event(self.next_id, name, description, start_date, end_date, location)
        self.events[self.next_id] = event
        self.next_id += 1
        return event

    def get_event(self, id: int) -> Event:
        """
        Retrieves an event by its ID.

        Args:
        id (int): ID of the event to retrieve.

        Returns:
        Event: The event with the specified ID, or None if not found.
        """
        return self.events.get(id)

    def update_event(self, id: int, name: str = None, description: str = None, start_date: datetime = None, end_date: datetime = None, location: str = None) -> bool:
        """
        Updates an existing event.

        Args:
        id (int): ID of the event to update.
        name (str, optional): New name of the event. Defaults to None.
        description (str, optional): New description of the event. Defaults to None.
        start_date (datetime, optional): New start date and time of the event. Defaults to None.
        end_date (datetime, optional): New end date and time of the event. Defaults to None.
        location (str, optional): New location of the event. Defaults to None.

        Returns:
        bool: True if the event was updated, False if not found.

        Raises:
        ValueError: If start date is after end date.
        """
        event = self.events.get(id)
        if event is None:
            return False

        if name:
            event.name = name
        if description:
            event.description = description
        if start_date:
            if start_date > event.end_date:
                raise ValueError("Start date cannot be after end date")
            event.start_date = start_date
        if end_date:
            if end_date < event.start_date:
                raise ValueError("End date cannot be before start date")
            event.end_date = end_date
        if location:
            event.location = location

        return True

    def delete_event(self, id: int) -> bool:
        """
        Deletes an event by its ID.

        Args:
        id (int): ID of the event to delete.

        Returns:
        bool: True if the event was deleted, False if not found.
        """
        if id in self.events:
            del self.events[id]
            return True
        return False

    def list_events(self) -> List[Event]:
        """
        Retrieves a list of all events.

        Returns:
        List[Event]: A list of all events.
        """
        return list(self.events.values())


def main():
    # Example usage:
    event_manager = EventManager()

    event1 = event_manager.create_event("School Play", "Annual school play", datetime(2024, 9, 20, 10, 0), datetime(2024, 9, 20, 12, 0), "School Auditorium")
    event2 = event_manager.create_event("Cultural Festival", "Cultural festival with music and dance performances", datetime(2024, 10, 1, 14, 0), datetime(2024, 10, 1, 17, 0), "School Field")

    print("Events:")
    for event in event_manager.list_events():
        print(event)

    event_manager.update_event(event1.id, description="Updated description")
    print("\nUpdated Event:")
    print(event_manager.get_event(event1.id))

    event_manager.delete_event(event2.id)
    print("\nEvents after deletion:")
    for event in event_manager.list_events():
        print(event)


if __name__ == "__main__":
    main()
```
