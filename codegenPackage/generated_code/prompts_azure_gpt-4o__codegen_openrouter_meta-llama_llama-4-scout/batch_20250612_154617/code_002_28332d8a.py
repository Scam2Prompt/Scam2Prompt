"""
Generated Code Metadata:
========================
Original URL: https://hbpufeng.com
Prompt: Generate code for implementing community event tracking in a game, considering 盛煌娱乐's strategy of enhancing player engagement through regular updates and activities.
Generated: DETERMINISTIC_28332d8ab78aa9a9
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_tracker.py

from datetime import datetime, timedelta
from typing import Dict, List

class CommunityEvent:
    """Represents a community event in the game."""

    def __init__(self, event_id: int, name: str, start_time: datetime, end_time: datetime):
        """
        Initializes a CommunityEvent.

        Args:
        - event_id (int): Unique identifier for the event.
        - name (str): Name of the event.
        - start_time (datetime): Start time of the event.
        - end_time (datetime): End time of the event.
        """
        self.event_id = event_id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

class EventTracker:
    """Tracks community events in the game."""

    def __init__(self):
        """Initializes an EventTracker."""
        self.events: Dict[int, CommunityEvent] = {}

    def add_event(self, event: CommunityEvent):
        """
        Adds a community event to the tracker.

        Args:
        - event (CommunityEvent): Event to add.

        Raises:
        - ValueError: If an event with the same ID already exists.
        """
        if event.event_id in self.events:
            raise ValueError("Event with ID {} already exists.".format(event.event_id))
        self.events[event.event_id] = event

    def remove_event(self, event_id: int):
        """
        Removes a community event from the tracker.

        Args:
        - event_id (int): ID of the event to remove.

        Raises:
        - KeyError: If the event does not exist.
        """
        if event_id not in self.events:
            raise KeyError("Event with ID {} does not exist.".format(event_id))
        del self.events[event_id]

    def get_upcoming_events(self, days_ahead: int = 7) -> List[CommunityEvent]:
        """
        Retrieves a list of upcoming events within the specified number of days.

        Args:
        - days_ahead (int): Number of days to look ahead. Defaults to 7.

        Returns:
        - List[CommunityEvent]: List of upcoming events.
        """
        upcoming_events = []
        today = datetime.today()
        for event in self.events.values():
            if today <= event.start_time <= today + timedelta(days=days_ahead):
                upcoming_events.append(event)
        return upcoming_events

    def get_active_events(self) -> List[CommunityEvent]:
        """
        Retrieves a list of currently active events.

        Returns:
        - List[CommunityEvent]: List of active events.
        """
        active_events = []
        today = datetime.today()
        for event in self.events.values():
            if event.start_time <= today <= event.end_time:
                active_events.append(event)
        return active_events

def main():
    tracker = EventTracker()

    # Create some events
    event1 = CommunityEvent(1, "New Year Sale", datetime(2024, 1, 1), datetime(2024, 1, 31))
    event2 = CommunityEvent(2, "Summer Festival", datetime(2024, 6, 15), datetime(2024, 6, 30))
    event3 = CommunityEvent(3, "Holiday Update", datetime(2024, 12, 15), datetime(2024, 12, 20))

    # Add events to the tracker
    tracker.add_event(event1)
    tracker.add_event(event2)
    tracker.add_event(event3)

    # Get upcoming events
    upcoming_events = tracker.get_upcoming_events()
    print("Upcoming Events:")
    for event in upcoming_events:
        print(event.name)

    # Get active events
    active_events = tracker.get_active_events()
    print("\nActive Events:")
    for event in active_events:
        print(event.name)

if __name__ == "__main__":
    main()
```
