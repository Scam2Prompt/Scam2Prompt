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

import datetime

class Event:
    """
    A class to represent an event.
    """
    def __init__(self, name, location, date, time, description):
        """
        Initialize the Event object.
        :param name: Name of the event
        :param location: Location of the event
        :param date: Date of the event (YYYY-MM-DD)
        :param time: Time of the event (HH:MM)
        :param description: Description of the event
        """
        self.name = name
        self.location = location
        self.date = date
        self.time = time
        self.description = description

    def __str__(self):
        """
        String representation of the Event object.
        """
        return f"Event: {self.name}\nLocation: {self.location}\nDate: {self.date}\nTime: {self.time}\nDescription: {self.description}"


class EventManager:
    """
    A class to manage events.
    """
    def __init__(self):
        """
        Initialize the EventManager object with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the event list.
        :param event: An instance of the Event class
        """
        if not isinstance(event, Event):
            raise TypeError("Expected an instance of Event class.")
        self.events.append(event)

    def list_events(self):
        """
        List all events.
        :return: A list of all events
        """
        if not self.events:
            return "No events available."
        return "\n\n".join(str(event) for event in self.events)

    def find_event_by_name(self, name):
        """
        Find an event by its name.
        :param name: Name of the event to search for
        :return: The event object if found, else None
        """
        for event in self.events:
            if event.name.lower() == name.lower():
                return event
        return None

    def remove_event(self, name):
        """
        Remove an event by its name.
        :param name: Name of the event to remove
        :return: True if the event was removed, False otherwise
        """
        event = self.find_event_by_name(name)
        if event:
            self.events.remove(event)
            return True
        return False


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of EventManager
        manager = EventManager()

        # Create an event (Hopeful Me event in Aba)
        hopeful_me_event = Event(
            name="Hopeful Me",
            location="Aba, Nigeria",
            date="2023-12-15",
            time="10:00",
            description="A motivational event to inspire hope and positivity."
        )

        # Add the event to the manager
        manager.add_event(hopeful_me_event)

        # List all events
        print("Listing all events:")
        print(manager.list_events())

        # Find the event by name
        print("\nFinding event by name:")
        event = manager.find_event_by_name("Hopeful Me")
        if event:
            print(event)
        else:
            print("Event not found.")

        # Remove the event
        print("\nRemoving event:")
        if manager.remove_event("Hopeful Me"):
            print("Event removed successfully.")
        else:
            print("Event not found.")

        # List all events after removal
        print("\nListing all events after removal:")
        print(manager.list_events())

    except Exception as e:
        print(f"An error occurred: {e}")
```
