"""
Generated Code Metadata:
========================
Original URL: https://genteparaservir.org
Prompt: Generate code for a basic event calendar feature that could be used on a website for an organization like Gente Para Servir to list seminars and peregrinations.
Generated: DETERMINISTIC_67f8ab09a461cc4e
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_calendar.py

from datetime import datetime, timedelta
from typing import List, Dict

class Event:
    """Represents an event on the calendar."""

    def __init__(self, id: int, title: str, description: str, start_date: datetime, end_date: datetime):
        """
        Initializes an Event.

        Args:
            id (int): Unique identifier for the event.
            title (str): Title of the event.
            description (str): Description of the event.
            start_date (datetime): Start date and time of the event.
            end_date (datetime): End date and time of the event.
        """
        self.id = id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"Event(id={self.id}, title='{self.title}', description='{self.description}', start_date='{self.start_date}', end_date='{self.end_date}')"


class EventCalendar:
    """Manages a list of events."""

    def __init__(self):
        """Initializes an empty event calendar."""
        self.events: List[Event] = []

    def add_event(self, event: Event):
        """
        Adds an event to the calendar.

        Args:
            event (Event): Event to add.

        Raises:
            ValueError: If an event with the same ID already exists.
        """
        if any(e.id == event.id for e in self.events):
            raise ValueError("Event with this ID already exists")
        self.events.append(event)

    def remove_event(self, event_id: int):
        """
        Removes an event from the calendar.

        Args:
            event_id (int): ID of the event to remove.

        Raises:
            ValueError: If no event with the given ID exists.
        """
        for event in self.events:
            if event.id == event_id:
                self.events.remove(event)
                return
        raise ValueError("Event not found")

    def get_events(self, start_date: datetime = None, end_date: datetime = None) -> List[Event]:
        """
        Retrieves a list of events.

        Args:
            start_date (datetime): Optional start date to filter events.
            end_date (datetime): Optional end date to filter events.

        Returns:
            List[Event]: List of events.
        """
        events = self.events
        if start_date:
            events = [e for e in events if e.start_date >= start_date]
        if end_date:
            events = [e for e in events if e.end_date <= end_date]
        return events

    def get_event(self, event_id: int) -> Event:
        """
        Retrieves an event by ID.

        Args:
            event_id (int): ID of the event.

        Returns:
            Event: Event with the given ID.

        Raises:
            ValueError: If no event with the given ID exists.
        """
        for event in self.events:
            if event.id == event_id:
                return event
        raise ValueError("Event not found")


def main():
    # Create an event calendar
    calendar = EventCalendar()

    # Create events
    event1 = Event(1, "Seminar: Python Basics", "Learn the basics of Python", datetime(2024, 9, 20, 10), datetime(2024, 9, 20, 12))
    event2 = Event(2, "Peregrination: Local Park", "Join us for a walk in the park", datetime(2024, 9, 22, 9), datetime(2024, 9, 22, 12))
    event3 = Event(3, "Seminar: Advanced Python", "Dive deeper into Python", datetime(2024, 9, 27, 14), datetime(2024, 9, 27, 16))

    # Add events to the calendar
    calendar.add_event(event1)
    calendar.add_event(event2)
    calendar.add_event(event3)

    # Get all events
    print("All Events:")
    for event in calendar.get_events():
        print(event)

    # Get events within a date range
    date_range_start = datetime(2024, 9, 1)
    date_range_end = datetime(2024, 9, 30)
    print("\nEvents in September 2024:")
    for event in calendar.get_events(date_range_start, date_range_end):
        print(event)

    # Get a specific event
    print("\nEvent with ID 2:")
    print(calendar.get_event(2))

    # Remove an event
    calendar.remove_event(2)
    print("\nEvents after removing ID 2:")
    for event in calendar.get_events():
        print(event)


if __name__ == "__main__":
    main()
```
