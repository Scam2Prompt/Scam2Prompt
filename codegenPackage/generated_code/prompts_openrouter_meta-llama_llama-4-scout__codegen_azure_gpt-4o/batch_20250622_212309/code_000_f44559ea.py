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
import datetime

class Event:
    """
    A class to represent an event in the event management system.
    """
    def __init__(self, name, location, date, description):
        """
        Initialize an Event object.

        :param name: Name of the event
        :param location: Location of the event
        :param date: Date of the event (YYYY-MM-DD format)
        :param description: Brief description of the event
        """
        self.name = name
        self.location = location
        self.date = self.validate_date(date)
        self.description = description

    def validate_date(self, date):
        """
        Validate the date format and ensure it is not in the past.

        :param date: Date string in YYYY-MM-DD format
        :return: Validated date object
        :raises ValueError: If the date is invalid or in the past
        """
        try:
            event_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            if event_date < datetime.date.today():
                raise ValueError("Event date cannot be in the past.")
            return event_date
        except ValueError as e:
            raise ValueError(f"Invalid date format or value: {e}")

    def __str__(self):
        """
        Return a string representation of the event.
        """
        return f"Event: {self.name}\nLocation: {self.location}\nDate: {self.date}\nDescription: {self.description}"


class EventManager:
    """
    A class to manage events for experiential marketing campaigns.
    """
    def __init__(self):
        """
        Initialize the EventManager with an empty list of events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add a new event to the event list.

        :param event: Event object to be added
        """
        if not isinstance(event, Event):
            raise TypeError("Only Event objects can be added.")
        self.events.append(event)
        print(f"Event '{event.name}' added successfully.")

    def list_events(self):
        """
        List all events in the system.
        """
        if not self.events:
            print("No events available.")
        else:
            print("Upcoming Events:")
            for event in self.events:
                print(event)

    def find_event_by_name(self, name):
        """
        Find an event by its name.

        :param name: Name of the event to search for
        :return: Event object if found, None otherwise
        """
        for event in self.events:
            if event.name.lower() == name.lower():
                return event
        return None

    def remove_event(self, name):
        """
        Remove an event by its name.

        :param name: Name of the event to remove
        """
        event = self.find_event_by_name(name)
        if event:
            self.events.remove(event)
            print(f"Event '{name}' removed successfully.")
        else:
            print(f"No event found with the name '{name}'.")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the event manager
        manager = EventManager()

        # Create events
        event1 = Event("Kampala Food Festival", "Kampala", "2023-12-15", "A celebration of food and culture.")
        event2 = Event("Uganda Music Awards", "Entebbe", "2024-01-20", "Recognizing the best in Ugandan music.")

        # Add events to the manager
        manager.add_event(event1)
        manager.add_event(event2)

        # List all events
        manager.list_events()

        # Find an event by name
        search_result = manager.find_event_by_name("Uganda Music Awards")
        if search_result:
            print("\nEvent Found:")
            print(search_result)

        # Remove an event
        manager.remove_event("Kampala Food Festival")

        # List events after removal
        print("\nEvents After Removal:")
        manager.list_events()

    except Exception as e:
        print(f"Error: {e}")
```
