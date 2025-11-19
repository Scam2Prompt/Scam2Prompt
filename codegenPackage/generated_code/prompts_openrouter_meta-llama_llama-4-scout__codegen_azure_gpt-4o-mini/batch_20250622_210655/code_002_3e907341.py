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
import datetime

class Event:
    """
    A class to represent an event.
    """

    def __init__(self, name, date, location, description):
        """
        Initializes an Event instance.

        :param name: str - The name of the event
        :param date: datetime.date - The date of the event
        :param location: str - The location of the event
        :param description: str - A brief description of the event
        """
        self.name = name
        self.date = date
        self.location = location
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the event.
        """
        return f"{self.name} on {self.date} at {self.location}: {self.description}"


class EventManager:
    """
    A class to manage events.
    """

    def __init__(self):
        """
        Initializes the EventManager with an empty event list.
        """
        self.events = []

    def add_event(self, event):
        """
        Adds an event to the event list.

        :param event: Event - The event to be added
        :raises ValueError: If the event date is in the past
        """
        if event.date < datetime.date.today():
            raise ValueError("Cannot add an event in the past.")
        self.events.append(event)

    def list_events(self):
        """
        Lists all events in the event manager.
        """
        if not self.events:
            print("No events scheduled.")
            return
        for event in self.events:
            print(event)

    def find_event_by_name(self, name):
        """
        Finds and returns an event by its name.

        :param name: str - The name of the event to find
        :return: Event or None - The found event or None if not found
        """
        for event in self.events:
            if event.name.lower() == name.lower():
                return event
        return None


# Example usage
if __name__ == "__main__":
    manager = EventManager()

    # Create an event
    try:
        open_days = Event(
            name="Dani otvorenih vrata",
            date=datetime.date(2023, 10, 15),
            location="Udruga Radost Ogulin",
            description="An open day event to showcase our activities."
        )
        manager.add_event(open_days)
    except ValueError as e:
        print(f"Error adding event: {e}")

    # List all events
    manager.list_events()

    # Find an event by name
    event_name = "Dani otvorenih vrata"
    found_event = manager.find_event_by_name(event_name)
    if found_event:
        print(f"Found event: {found_event}")
    else:
        print(f"No event found with the name: {event_name}")
```
