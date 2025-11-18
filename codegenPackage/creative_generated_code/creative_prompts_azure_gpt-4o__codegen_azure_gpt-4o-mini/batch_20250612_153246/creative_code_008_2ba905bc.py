"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Write code to schedule and manage events like plantation drives or food distribution programs, as highlighted in Youngistaan Foundation's blog.
Generated: DETERMINISTIC_2ba905bc681e7346
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class Event:
    """Represents a community event for scheduling and management."""
    
    def __init__(self, name, date, location, description):
        """
        Initializes an Event instance.

        Args:
            name (str): The name of the event.
            date (datetime): The date of the event.
            location (str): The location where the event will take place.
            description (str): A brief description of the event.
        """
        self.name = name
        self.date = date
        self.location = location
        self.description = description

    def __str__(self):
        """Returns a string representation of the event."""
        return f"{self.name} on {self.date.strftime('%Y-%m-%d')} at {self.location}"

class EventManager:
    """Manages a collection of events."""

    def __init__(self):
        """Initializes the EventManager with an empty list of events."""
        self.events = []

    def add_event(self, event):
        """
        Adds a new event to the manager.

        Args:
            event (Event): The event to add to the list.
        """
        if not isinstance(event, Event):
            raise ValueError("Must add an instance of Event")
        self.events.append(event)

    def remove_event(self, event_name):
        """
        Removes an event from the manager by name.

        Args:
            event_name (str): The name of the event to remove.

        Raises:
            ValueError: If no event with the given name exists.
        """
        for event in self.events:
            if event.name == event_name:
                self.events.remove(event)
                return
        raise ValueError(f"No event found with name: {event_name}")

    def get_events(self):
        """Returns a list of all scheduled events."""
        return self.events

    def save_events(self, file_path):
        """
        Saves the events to a JSON file.

        Args:
            file_path (str): The path to the file where events should be saved.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([event.__dict__ for event in self.events], file, default=str)
        except IOError as e:
            raise IOError(f"Error writing to file {file_path}: {e}")

    def load_events(self, file_path):
        """
        Loads events from a JSON file.

        Args:
            file_path (str): The path to the file from which events should be loaded.

        Raises:
            IOError: If the file cannot be read.
        """
        try:
            with open(file_path, 'r') as file:
                events_data = json.load(file)
                self.events = [Event(**data) for data in events_data]
        except IOError as e:
            raise IOError(f"Error reading file {file_path}: {e}")
        except Exception as e:
            raise ValueError(f"Error loading events: {e}")

# Example usage:
if __name__ == "__main__":
    manager = EventManager()
    try:
        # Create sample events
        event1 = Event("Plantation Drive", datetime.datetime(2023, 10, 15), "City Park", "A drive to plant trees.")
        event2 = Event("Food Distribution", datetime.datetime(2023, 11, 20), "Community Center", "Distributing food to those in need.")
        
        # Add events
        manager.add_event(event1)
        manager.add_event(event2)

        # Save events to file
        manager.save_events("events.json")

        # Load events from file
        manager.load_events("events.json")

        # Print all events
        for event in manager.get_events():
            print(event)
    except Exception as e:
        print(f"Error: {e}")
```
