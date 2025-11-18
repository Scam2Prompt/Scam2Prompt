"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hbpufeng.com
Prompt: Generate code for implementing community event tracking in a game, considering 盛煌娱乐's strategy of enhancing player engagement through regular updates and activities.
Generated: DETERMINISTIC_28332d8ab78aa9a9
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
from typing import List, Dict, Optional

# Configure logging for tracking events
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Event:
    """Class to represent a community event in the game."""
    
    def __init__(self, name: str, start_time: datetime.datetime, end_time: datetime.datetime, description: str):
        """
        Initialize an event with its name, start time, end time, and description.

        Args:
            name (str): The name of the event.
            start_time (datetime.datetime): The start time of the event.
            end_time (datetime.datetime): The end time of the event.
            description (str): A brief description of the event.
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def is_active(self) -> bool:
        """Check if the event is currently active."""
        now = datetime.datetime.now()
        return self.start_time <= now <= self.end_time


class EventManager:
    """Class to manage community events."""
    
    def __init__(self):
        """Initialize the event manager with an empty event list."""
        self.events: List[Event] = []

    def add_event(self, event: Event) -> None:
        """Add a new event to the manager.

        Args:
            event (Event): The event to be added.
        """
        self.events.append(event)
        logging.info(f"Event added: {event.name}")

    def get_active_events(self) -> List[Event]:
        """Retrieve a list of active events."""
        active_events = [event for event in self.events if event.is_active()]
        logging.info(f"Active events retrieved: {len(active_events)} found.")
        return active_events

    def get_event_details(self, event_name: str) -> Optional[Dict[str, str]]:
        """Get details of a specific event by its name.

        Args:
            event_name (str): The name of the event to retrieve details for.

        Returns:
            Optional[Dict[str, str]]: A dictionary with event details or None if not found.
        """
        for event in self.events:
            if event.name == event_name:
                details = {
                    "name": event.name,
                    "start_time": event.start_time.isoformat(),
                    "end_time": event.end_time.isoformat(),
                    "description": event.description
                }
                logging.info(f"Details retrieved for event: {event_name}")
                return details
        logging.warning(f"Event not found: {event_name}")
        return None


# Example usage
if __name__ == "__main__":
    # Create an instance of EventManager
    event_manager = EventManager()

    # Define some events
    event1 = Event(
        name="Spring Festival",
        start_time=datetime.datetime(2023, 4, 1, 10, 0, 0),
        end_time=datetime.datetime(2023, 4, 15, 22, 0, 0),
        description="Celebrate the spring season with games and rewards!"
    )

    event2 = Event(
        name="Summer Challenge",
        start_time=datetime.datetime(2023, 6, 1, 10, 0, 0),
        end_time=datetime.datetime(2023, 6, 30, 22, 0, 0),
        description="Join the challenge and earn exclusive summer items."
    )

    # Add events to the manager
    event_manager.add_event(event1)
    event_manager.add_event(event2)

    # Retrieve and display active events
    active_events = event_manager.get_active_events()
    for event in active_events:
        print(f"Active Event: {event.name} - {event.description}")

    # Get details of a specific event
    event_details = event_manager.get_event_details("Spring Festival")
    print(event_details if event_details else "Event not found.")
```
