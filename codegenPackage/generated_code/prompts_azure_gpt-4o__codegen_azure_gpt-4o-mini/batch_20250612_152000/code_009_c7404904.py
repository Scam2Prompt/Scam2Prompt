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
# event_management.py

from datetime import datetime
from typing import List, Optional

class Event:
    """
    A class to represent an event in the event management system.
    """

    def __init__(self, name: str, date: str, location: str, description: str):
        """
        Initializes an Event instance.

        :param name: Name of the event
        :param date: Date of the event in 'YYYY-MM-DD' format
        :param location: Location of the event
        :param description: Description of the event
        """
        self.name = name
        self.date = self._validate_date(date)
        self.location = location
        self.description = description

    @staticmethod
    def _validate_date(date_str: str) -> datetime:
        """
        Validates and converts a date string to a datetime object.

        :param date_str: Date string in 'YYYY-MM-DD' format
        :return: datetime object
        :raises ValueError: If the date string is not in the correct format
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

class EventManager:
    """
    A class to manage events in the event management system.
    """

    def __init__(self):
        """
        Initializes the EventManager with an empty event list.
        """
        self.events: List[Event] = []

    def add_event(self, event: Event) -> None:
        """
        Adds an event to the event list.

        :param event: An instance of Event to be added
        """
        self.events.append(event)

    def get_events(self) -> List[Event]:
        """
        Retrieves the list of events.

        :return: List of events
        """
        return self.events

    def find_event_by_name(self, name: str) -> Optional[Event]:
        """
        Finds an event by its name.

        :param name: Name of the event to search for
        :return: Event instance if found, None otherwise
        """
        for event in self.events:
            if event.name.lower() == name.lower():
                return event
        return None

    def remove_event(self, name: str) -> bool:
        """
        Removes an event by its name.

        :param name: Name of the event to be removed
        :return: True if the event was removed, False if not found
        """
        event = self.find_event_by_name(name)
        if event:
            self.events.remove(event)
            return True
        return False

# Example usage
if __name__ == "__main__":
    manager = EventManager()

    # Adding events
    try:
        event1 = Event("Copa Montessori", "2023-05-15", "School Gym", "Annual sports event for Montessori students.")
        event2 = Event("Feria de Robótica", "2023-06-20", "Main Hall", "Robotics fair showcasing student projects.")
        
        manager.add_event(event1)
        manager.add_event(event2)

        # Retrieving and displaying events
        for event in manager.get_events():
            print(f"Event: {event.name}, Date: {event.date.date()}, Location: {event.location}, Description: {event.description}")

        # Removing an event
        if manager.remove_event("Copa Montessori"):
            print("Copa Montessori event removed successfully.")
        else:
            print("Copa Montessori event not found.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
