"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Write a Python script to manage school event calendars for events like "Дан школе" and "Васкршња приредба".
Generated: DETERMINISTIC_e1280ecf30dd9a31
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_event_calendar.py

from datetime import datetime
from typing import Dict, List

class SchoolEvent:
    """Represents a school event."""

    def __init__(self, name: str, date: str, time: str, description: str = ""):
        """
        Initializes a SchoolEvent.

        Args:
            name (str): Event name.
            date (str): Event date in YYYY-MM-DD format.
            time (str): Event time in HH:MM format.
            description (str, optional): Event description. Defaults to "".
        """
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.time = datetime.strptime(time, "%H:%M").time()
        self.description = description

    def __str__(self):
        return f"{self.name} on {self.date} at {self.time}"


class SchoolEventCalendar:
    """Manages school event calendars."""

    def __init__(self):
        """Initializes an empty school event calendar."""
        self.events: Dict[str, List[SchoolEvent]] = {}

    def add_event(self, event: SchoolEvent):
        """
        Adds an event to the calendar.

        Args:
            event (SchoolEvent): Event to add.
        """
        date_str = event.date.strftime("%Y-%m-%d")
        if date_str not in self.events:
            self.events[date_str] = []
        self.events[date_str].append(event)

    def get_events(self, date: str = None) -> List[SchoolEvent]:
        """
        Retrieves events from the calendar.

        Args:
            date (str, optional): Date in YYYY-MM-DD format. Defaults to None.

        Returns:
            List[SchoolEvent]: List of events.
        """
        if date:
            date_str = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
            return self.events.get(date_str, [])
        else:
            events = []
            for date_str in self.events:
                events.extend(self.events[date_str])
            return events

    def delete_event(self, event_name: str, date: str):
        """
        Deletes an event from the calendar.

        Args:
            event_name (str): Name of the event to delete.
            date (str): Date of the event to delete in YYYY-MM-DD format.
        """
        date_str = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        if date_str in self.events:
            self.events[date_str] = [event for event in self.events[date_str] if event.name != event_name]


def main():
    calendar = SchoolEventCalendar()

    # Add events
    event1 = SchoolEvent("Дан школе", "2024-09-20", "10:00", "School day event")
    event2 = SchoolEvent("Васкршња приредба", "2024-04-15", "12:00", "Easter celebration")
    calendar.add_event(event1)
    calendar.add_event(event2)

    # Get events
    print("All events:")
    for event in calendar.get_events():
        print(event)

    print("\nEvents on 2024-09-20:")
    for event in calendar.get_events("2024-09-20"):
        print(event)

    # Delete event
    calendar.delete_event("Дан школе", "2024-09-20")

    print("\nEvents after deletion:")
    for event in calendar.get_events():
        print(event)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
