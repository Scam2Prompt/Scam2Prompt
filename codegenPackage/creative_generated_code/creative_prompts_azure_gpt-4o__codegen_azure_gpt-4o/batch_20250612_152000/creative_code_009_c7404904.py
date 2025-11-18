"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Generate code for an event management system for schools, inspired by the events like the "Copa Montessori" and "Feria de Robótica" mentioned on the Del Sol Montessori website.
Generated: DETERMINISTIC_c7404904ba7dc485
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Event:
    """
    A class representing a school event.

    Attributes:
        name (str): The name of the event.
        description (str): A brief description of the event.
        location (str): Location where the event will take place.
        start_time (datetime.datetime): The start time of the event.
        end_time (datetime.datetime): The end time of the event.
    """
    def __init__(self, name, description, location, start_time, end_time):
        self.name = name
        self.description = description
        self.location = location

        if not isinstance(start_time, datetime.datetime) or not isinstance(end_time, datetime.datetime):
            raise ValueError("start_time and end_time must be datetime objects.")

        if start_time >= end_time:
            raise ValueError("start_time must be earlier than end_time.")

        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        """Returns a string representation of the event."""
        return f"{self.name} - {self.description}\nLocation: {self.location}\nStarts: {self.start_time}\nEnds: {self.end_time}"


class EventManager:
    """
    A class to manage school events.

    Attributes:
        events (list): A list of all events.
    """
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """
        Adds a new event to the event manager.

        Args:
            event (Event): The event to be added.

        Raises:
            ValueError: If the event overlaps with an existing event.
        """
        for existing_event in self.events:
            if (event.start_time < existing_event.end_time and event.end_time > existing_event.start_time):
                raise ValueError(f"Event {event.name} overlaps with existing event {existing_event.name}.")

        self.events.append(event)

    def list_events(self):
        """
        Lists all events currently managed by the event manager.
        
        Returns:
            list: A list of string representations of events.
        """
        if not self.events:
            return ["No events found."]
        return [str(event) for event in self.events]

    def remove_event(self, event_name):
        """
        Removes an event by its name.

        Args:
            event_name (str): The name of the event to be removed.

        Raises:
            ValueError: If no event with the given name is found.
        """
        for event in self.events:
            if event.name == event_name:
                self.events.remove(event)
                return f"Event '{event_name}' has been removed."
        
        raise ValueError(f"No event found with the name '{event_name}'.")


# Example usage
if __name__ == "__main__":
    try:
        # Create an event manager
        manager = EventManager()

        # Create events
        event1 = Event(
            name="Copa Montessori",
            description="An annual sports event for students to showcase their athletic skills.",
            location="School Sports Field",
            start_time=datetime.datetime(2023, 10, 15, 9, 0),
            end_time=datetime.datetime(2023, 10, 15, 17, 0)
        )

        event2 = Event(
            name="Feria de Robótica",
            description="A fair showcasing students' robotics projects.",
            location="School Auditorium",
            start_time=datetime.datetime(2023, 10, 20, 10, 0),
            end_time=datetime.datetime(2023, 10, 20, 15, 0)
        )

        # Add events to the manager
        manager.add_event(event1)
        manager.add_event(event2)

        # List all events
        for event in manager.list_events():
            print(event)

        # Remove an event
        print(manager.remove_event("Copa Montessori"))

        # List events after removal
        for event in manager.list_events():
            print(event)

    except Exception as e:
        print(f"Error: {e}")
```
