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
from datetime import datetime
from enum import Enum
from typing import List

class EventPriority(Enum):
    """Event priority levels"""
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class Event:
    """Represents a school event"""
    def __init__(self, name: str, date: datetime, priority: EventPriority):
        """
        Initializes an Event object.

        Args:
        - name (str): Event name
        - date (datetime): Event date
        - priority (EventPriority): Event priority
        """
        self.name = name
        self.date = date
        self.priority = priority

class EventManagementSystem:
    """Manages school events"""
    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        """
        Adds an event to the system.

        Args:
        - event (Event): Event to add
        """
        self.events.append(event)
        self.events.sort(key=lambda x: (x.priority.value, x.date))

    def get_upcoming_events(self, num_events: int = 5) -> List[Event]:
        """
        Retrieves a list of upcoming events.

        Args:
        - num_events (int): Number of events to retrieve (default: 5)

        Returns:
        - List[Event]: List of upcoming events
        """
        return self.events[:num_events]

    def get_events_by_priority(self, priority: EventPriority) -> List[Event]:
        """
        Retrieves a list of events with a specific priority.

        Args:
        - priority (EventPriority): Event priority

        Returns:
        - List[Event]: List of events with the specified priority
        """
        return [event for event in self.events if event.priority == priority]

def main():
    # Create an event management system
    event_system = EventManagementSystem()

    try:
        # Create events
        copa_montessori = Event("Copa Montessori", datetime(2024, 9, 20), EventPriority.HIGH)
        feria_de_robotica = Event("Feria de Robótica", datetime(2024, 10, 15), EventPriority.HIGH)
        other_event = Event("Other Event", datetime(2024, 11, 1), EventPriority.MEDIUM)

        # Add events to the system
        event_system.add_event(copa_montessori)
        event_system.add_event(feria_de_robotica)
        event_system.add_event(other_event)

        # Get upcoming events
        upcoming_events = event_system.get_upcoming_events()
        print("Upcoming Events:")
        for event in upcoming_events:
            print(f"- {event.name} ({event.date.date()}) - Priority: {event.priority.name}")

        # Get events by priority
        high_priority_events = event_system.get_events_by_priority(EventPriority.HIGH)
        print("\nHigh Priority Events:")
        for event in high_priority_events:
            print(f"- {event.name} ({event.date.date()})")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
