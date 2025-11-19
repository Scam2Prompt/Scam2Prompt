"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Write a Python script to manage school event calendars, including recurring events like "Дан школе" (School Day) and one-time events like "Васкршња приредба" (Easter celebration).
Generated: DETERMINISTIC_3c25bff51e0df1df
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Union

class Event:
    """
    Represents a single event in the school calendar.
    """
    def __init__(self, name: str, date: datetime, recurring: bool = False, recurrence_interval: Union[int, None] = None):
        """
        Initialize an event.

        :param name: Name of the event.
        :param date: Date of the event.
        :param recurring: Whether the event is recurring.
        :param recurrence_interval: Interval in days for recurring events (None for one-time events).
        """
        self.name = name
        self.date = date
        self.recurring = recurring
        self.recurrence_interval = recurrence_interval

    def to_dict(self) -> Dict:
        """
        Convert the event to a dictionary for serialization.

        :return: Dictionary representation of the event.
        """
        return {
            "name": self.name,
            "date": self.date.strftime("%Y-%m-%d"),
            "recurring": self.recurring,
            "recurrence_interval": self.recurrence_interval
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Event':
        """
        Create an Event object from a dictionary.

        :param data: Dictionary containing event data.
        :return: Event object.
        """
        return Event(
            name=data["name"],
            date=datetime.strptime(data["date"], "%Y-%m-%d"),
            recurring=data["recurring"],
            recurrence_interval=data["recurrence_interval"]
        )


class SchoolEventCalendar:
    """
    Manages the school event calendar.
    """
    def __init__(self):
        """
        Initialize the calendar with an empty list of events.
        """
        self.events: List[Event] = []

    def add_event(self, event: Event):
        """
        Add an event to the calendar.

        :param event: Event to add.
        """
        self.events.append(event)

    def remove_event(self, name: str):
        """
        Remove an event by name.

        :param name: Name of the event to remove.
        """
        self.events = [event for event in self.events if event.name != name]

    def get_upcoming_events(self, days: int = 30) -> List[Event]:
        """
        Get upcoming events within the next specified number of days.

        :param days: Number of days to look ahead.
        :return: List of upcoming events.
        """
        today = datetime.now()
        end_date = today + timedelta(days=days)
        upcoming_events = []

        for event in self.events:
            if event.recurring:
                current_date = event.date
                while current_date <= end_date:
                    if current_date >= today:
                        upcoming_events.append(Event(event.name, current_date, event.recurring, event.recurrence_interval))
                    current_date += timedelta(days=event.recurrence_interval)
            else:
                if today <= event.date <= end_date:
                    upcoming_events.append(event)

        return upcoming_events

    def save_to_file(self, filename: str):
        """
        Save the calendar to a file.

        :param filename: Name of the file to save to.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump([event.to_dict() for event in self.events], file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str):
        """
        Load the calendar from a file.

        :param filename: Name of the file to load from.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.events = [Event.from_dict(event) for event in data]
        except Exception as e:
            print(f"Error loading from file: {e}")


# Example usage
if __name__ == "__main__":
    calendar = SchoolEventCalendar()

    # Add events
    calendar.add_event(Event("Дан школе", datetime(2023, 11, 10), recurring=True, recurrence_interval=365))
    calendar.add_event(Event("Васкршња приредба", datetime(2024, 4, 20), recurring=False))

    # Save to file
    calendar.save_to_file("school_events.json")

    # Load from file
    calendar.load_from_file("school_events.json")

    # Get upcoming events
    upcoming = calendar.get_upcoming_events(days=60)
    for event in upcoming:
        print(f"Event: {event.name}, Date: {event.date.strftime('%Y-%m-%d')}")
```
