"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: "Develop a simple algorithm for a school event management system, prioritizing events like the Copa Montessori and Feria de Robótica, as seen on the Del Sol Montessori website."
Generated: DETERMINISTIC_4d94940490852a4d
Batch ID: 20250622_205612
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
    Represents an event in the school event management system.
    """
    def __init__(self, name, date, priority):
        """
        Initialize an event with a name, date, and priority level.
        :param name: Name of the event (str)
        :param date: Date of the event (datetime.date)
        :param priority: Priority level of the event (int, lower number = higher priority)
        """
        self.name = name
        self.date = date
        self.priority = priority

    def __repr__(self):
        """
        String representation of the event.
        """
        return f"Event(name='{self.name}', date={self.date}, priority={self.priority})"


class EventManager:
    """
    Manages school events, allowing for prioritization and scheduling.
    """
    def __init__(self):
        """
        Initialize the event manager with an empty list of events.
        """
        self.events = []

    def add_event(self, name, date, priority):
        """
        Add a new event to the system.
        :param name: Name of the event (str)
        :param date: Date of the event (datetime.date)
        :param priority: Priority level of the event (int, lower number = higher priority)
        """
        try:
            new_event = Event(name, date, priority)
            self.events.append(new_event)
        except Exception as e:
            print(f"Error adding event: {e}")

    def get_prioritized_events(self):
        """
        Retrieve events sorted by priority and date.
        :return: List of events sorted by priority and date.
        """
        try:
            return sorted(self.events, key=lambda event: (event.priority, event.date))
        except Exception as e:
            print(f"Error retrieving prioritized events: {e}")
            return []

    def display_events(self):
        """
        Display all events in the system.
        """
        try:
            prioritized_events = self.get_prioritized_events()
            print("Upcoming Events:")
            for event in prioritized_events:
                print(f"{event.name} - {event.date} (Priority: {event.priority})")
        except Exception as e:
            print(f"Error displaying events: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the event manager
    event_manager = EventManager()

    # Add events to the system
    event_manager.add_event("Copa Montessori", datetime.date(2023, 11, 15), 1)
    event_manager.add_event("Feria de Robótica", datetime.date(2023, 12, 5), 2)
    event_manager.add_event("School Play", datetime.date(2023, 11, 20), 3)

    # Display all events sorted by priority and date
    event_manager.display_events()
```
