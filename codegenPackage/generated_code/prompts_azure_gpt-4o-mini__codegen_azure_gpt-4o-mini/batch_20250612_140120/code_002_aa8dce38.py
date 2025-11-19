"""
Generated Code Metadata:
========================
Original URL: https://jamuae.com
Prompt: Write a function that automates the scheduling of entertainers for various events, inspired by the services offered by Jam UAE.
Generated: DETERMINISTIC_aa8dce38eb860a39
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Entertainer:
    """Class representing an entertainer."""
    
    def __init__(self, name: str, availability: List[datetime]):
        """
        Initialize an entertainer with a name and their available time slots.

        :param name: Name of the entertainer
        :param availability: List of datetime objects representing available time slots
        """
        self.name = name
        self.availability = availability

    def is_available(self, event_time: datetime) -> bool:
        """
        Check if the entertainer is available for a given event time.

        :param event_time: The datetime of the event
        :return: True if available, False otherwise
        """
        return event_time in self.availability


class Event:
    """Class representing an event."""
    
    def __init__(self, name: str, event_time: datetime):
        """
        Initialize an event with a name and scheduled time.

        :param name: Name of the event
        :param event_time: The datetime of the event
        """
        self.name = name
        self.event_time = event_time


class Scheduler:
    """Class to schedule entertainers for events."""
    
    def __init__(self):
        self.entertainers: List[Entertainer] = []
        self.scheduled_events: Dict[str, str] = {}  # Maps event name to entertainer name

    def add_entertainer(self, entertainer: Entertainer):
        """
        Add an entertainer to the scheduler.

        :param entertainer: An instance of Entertainer
        """
        self.entertainers.append(entertainer)

    def schedule_event(self, event: Event) -> Optional[str]:
        """
        Schedule an event with an available entertainer.

        :param event: An instance of Event
        :return: Name of the entertainer scheduled or None if no entertainer is available
        """
        for entertainer in self.entertainers:
            if entertainer.is_available(event.event_time):
                self.scheduled_events[event.name] = entertainer.name
                return entertainer.name
        return None

    def get_schedule(self) -> Dict[str, str]:
        """
        Get the current schedule of events and their assigned entertainers.

        :return: A dictionary mapping event names to entertainer names
        """
        return self.scheduled_events


# Example usage
if __name__ == "__main__":
    # Create entertainers with their availability
    entertainer1 = Entertainer("Alice", [datetime(2023, 10, 1, 18, 0), datetime(2023, 10, 1, 20, 0)])
    entertainer2 = Entertainer("Bob", [datetime(2023, 10, 1, 19, 0), datetime(2023, 10, 1, 21, 0)])

    # Create a scheduler and add entertainers
    scheduler = Scheduler()
    scheduler.add_entertainer(entertainer1)
    scheduler.add_entertainer(entertainer2)

    # Create events
    event1 = Event("Birthday Party", datetime(2023, 10, 1, 18, 0))
    event2 = Event("Corporate Event", datetime(2023, 10, 1, 19, 0))

    # Schedule events
    scheduled_entertainer1 = scheduler.schedule_event(event1)
    scheduled_entertainer2 = scheduler.schedule_event(event2)

    # Output the schedule
    print("Scheduled Events:")
    for event_name, entertainer_name in scheduler.get_schedule().items():
        print(f"{event_name} is scheduled with {entertainer_name}.")
```
