"""
Generated Code Metadata:
========================
Original URL: https://www.al-aanqua.com
Prompt: Develop a code snippet for a cultural event management system, considering the organization of festivals like the Alexandria International Film Festival for Mediterranean Countries.
Generated: DETERMINISTIC_55b2cc5c2e5ef0c7
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
    """Represents a cultural event."""

    def __init__(self, id: int, name: str, start_date: datetime, end_date: datetime, location: str):
        """
        Initializes an Event.

        Args:
            id (int): Unique identifier for the event.
            name (str): Name of the event.
            start_date (datetime): Start date of the event.
            end_date (datetime): End date of the event.
            location (str): Location of the event.
        """
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

    def __str__(self):
        return f"Event {self.id}: {self.name} at {self.location} from {self.start_date} to {self.end_date}"


class Festival(Event):
    """Represents a festival, inheriting from Event."""

    def __init__(self, id: int, name: str, start_date: datetime, end_date: datetime, location: str, 
                 film_categories: List[str], guest_list: List[str]):
        """
        Initializes a Festival.

        Args:
            id (int): Unique identifier for the festival.
            name (str): Name of the festival.
            start_date (datetime): Start date of the festival.
            end_date (datetime): End date of the festival.
            location (str): Location of the festival.
            film_categories (List[str]): List of film categories.
            guest_list (List[str]): List of guests attending the festival.
        """
        super().__init__(id, name, start_date, end_date, location)
        self.film_categories = film_categories
        self.guest_list = guest_list

    def add_film_category(self, category: str):
        """Adds a film category to the festival."""
        self.film_categories.append(category)

    def add_guest(self, guest: str):
        """Adds a guest to the festival's guest list."""
        self.guest_list.append(guest)

    def __str__(self):
        return super().__str__() + f" with film categories: {self.film_categories} and guests: {self.guest_list}"


class EventManagementSystem:
    """Manages cultural events."""

    def __init__(self):
        self.events = {}

    def add_event(self, event: Event):
        """Adds an event to the system."""
        self.events[event.id] = event

    def remove_event(self, event_id: int):
        """Removes an event from the system."""
        if event_id in self.events:
            del self.events[event_id]
        else:
            raise ValueError("Event not found")

    def get_event(self, event_id: int) -> Event:
        """Retrieves an event by its ID."""
        try:
            return self.events[event_id]
        except KeyError:
            raise ValueError("Event not found")

    def list_events(self):
        """Lists all events in the system."""
        for event in self.events.values():
            print(event)


def main():
    # Create an event management system
    system = EventManagementSystem()

    # Create a festival
    alexandria_festival = Festival(
        1,
        "Alexandria International Film Festival for Mediterranean Countries",
        datetime(2024, 9, 1),
        datetime(2024, 9, 10),
        "Alexandria, Egypt",
        ["Mediterranean Films", "International Films"],
        ["John Doe", "Jane Smith"]
    )

    # Add the festival to the system
    system.add_event(alexandria_festival)

    # List all events
    print("Events:")
    system.list_events()

    # Get a specific event
    print("\nSpecific Event:")
    print(system.get_event(1))

    # Remove an event
    system.remove_event(1)

    # Try to get a removed event
    try:
        system.get_event(1)
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
