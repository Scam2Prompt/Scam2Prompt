"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: "Write a code for a simple event management system for experiential marketing campaigns in Uganda."
Generated: DETERMINISTIC_f44559eaaf6ddeba
Batch ID: 20250622_212309
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
from typing import List, Dict

class Event:
    """Represents an event in the event management system."""

    def __init__(self, id: int, name: str, date: str, location: str, attendees: List[str] = None):
        """
        Initializes an Event object.

        Args:
        id (int): Unique identifier for the event.
        name (str): Name of the event.
        date (str): Date of the event in YYYY-MM-DD format.
        location (str): Location of the event.
        attendees (List[str], optional): List of attendees. Defaults to None.
        """
        self.id = id
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.location = location
        self.attendees = attendees if attendees else []

    def add_attendee(self, attendee: str):
        """Adds an attendee to the event."""
        self.attendees.append(attendee)

    def remove_attendee(self, attendee: str):
        """Removes an attendee from the event."""
        if attendee in self.attendees:
            self.attendees.remove(attendee)

    def __str__(self):
        return f"Event {self.id}: {self.name} on {self.date} at {self.location}"


class EventManagementSystem:
    """Manages events for experiential marketing campaigns."""

    def __init__(self):
        """Initializes the event management system."""
        self.events: Dict[int, Event] = {}
        self.next_event_id = 1

    def create_event(self, name: str, date: str, location: str) -> Event:
        """
        Creates a new event.

        Args:
        name (str): Name of the event.
        date (str): Date of the event in YYYY-MM-DD format.
        location (str): Location of the event.

        Returns:
        Event: The newly created event.
        """
        event = Event(self.next_event_id, name, date, location)
        self.events[self.next_event_id] = event
        self.next_event_id += 1
        return event

    def get_event(self, event_id: int) -> Event:
        """
        Retrieves an event by its ID.

        Args:
        event_id (int): ID of the event to retrieve.

        Returns:
        Event: The event with the specified ID, or None if not found.
        """
        return self.events.get(event_id)

    def update_event(self, event_id: int, name: str = None, date: str = None, location: str = None):
        """
        Updates an existing event.

        Args:
        event_id (int): ID of the event to update.
        name (str, optional): New name of the event. Defaults to None.
        date (str, optional): New date of the event in YYYY-MM-DD format. Defaults to None.
        location (str, optional): New location of the event. Defaults to None.

        Raises:
        ValueError: If the event ID is not found.
        """
        event = self.get_event(event_id)
        if event:
            if name:
                event.name = name
            if date:
                event.date = datetime.strptime(date, "%Y-%m-%d").date()
            if location:
                event.location = location
        else:
            raise ValueError("Event not found")

    def delete_event(self, event_id: int):
        """
        Deletes an event.

        Args:
        event_id (int): ID of the event to delete.

        Raises:
        ValueError: If the event ID is not found.
        """
        if event_id in self.events:
            del self.events[event_id]
        else:
            raise ValueError("Event not found")


def main():
    # Example usage
    ems = EventManagementSystem()

    # Create events
    event1 = ems.create_event("Launch of New Product", "2024-09-20", "Kampala")
    event2 = ems.create_event("Trade Show", "2024-09-25", "Entebbe")

    # Add attendees
    event1.add_attendee("John Doe")
    event1.add_attendee("Jane Doe")

    # Print events
    print(event1)
    print(event2)

    # Update event
    ems.update_event(event1.id, name="New Product Launch Event")

    # Print updated event
    print(ems.get_event(event1.id))

    # Delete event
    ems.delete_event(event2.id)

    try:
        ems.get_event(event2.id)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
