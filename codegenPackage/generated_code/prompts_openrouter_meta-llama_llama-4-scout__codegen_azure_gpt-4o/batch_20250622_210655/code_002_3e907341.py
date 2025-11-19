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
        Initialize an Event object.

        :param name: Name of the event
        :param date: Date of the event (datetime object)
        :param location: Location of the event
        :param description: Description of the event
        """
        self.name = name
        self.date = date
        self.location = location
        self.description = description

    def __str__(self):
        """
        Return a string representation of the event.
        """
        return f"Event: {self.name}\nDate: {self.date.strftime('%Y-%m-%d %H:%M')}\nLocation: {self.location}\nDescription: {self.description}"


class EventManager:
    """
    A class to manage events.
    """
    def __init__(self):
        """
        Initialize the EventManager with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the event list.

        :param event: Event object to be added
        """
        if not isinstance(event, Event):
            raise ValueError("Invalid event object. Must be an instance of Event.")
        self.events.append(event)

    def list_events(self):
        """
        List all events.

        :return: List of all events
        """
        if not self.events:
            return "No events available."
        return "\n\n".join(str(event) for event in self.events)

    def find_event_by_name(self, name):
        """
        Find an event by its name.

        :param name: Name of the event to search for
        :return: Event object if found, else None
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
        # Create an EventManager instance
        manager = EventManager()

        # Create some events
        event1 = Event(
            name="Dani otvorenih vrata",
            date=datetime.datetime(2023, 11, 15, 10, 0),
            location="Udruga Radost Ogulin",
            description="Open Days event to showcase our activities and programs."
        )

        event2 = Event(
            name="Radionica kreativnog pisanja",
            date=datetime.datetime(2023, 11, 20, 14, 0),
            location="Udruga Radost Ogulin",
            description="Creative writing workshop for all ages."
        )

        # Add events to the manager
        manager.add_event(event1)
        manager.add_event(event2)

        # List all events
        print("All Events:")
        print(manager.list_events())

        # Find an event by name
        print("\nSearching for 'Dani otvorenih vrata':")
        found_event = manager.find_event_by_name("Dani otvorenih vrata")
        if found_event:
            print(found_event)
        else:
            print("Event not found.")

        # Remove an event
        print("\nRemoving 'Radionica kreativnog pisanja':")
        if manager.remove_event("Radionica kreativnog pisanja"):
            print("Event removed successfully.")
        else:
            print("Event not found.")

        # List all events after removal
        print("\nAll Events After Removal:")
        print(manager.list_events())

    except Exception as e:
        print(f"An error occurred: {e}")
```
