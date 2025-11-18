"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.iaci.org
Prompt: Write a script to manage and display upcoming events for an organization, including filtering by industry or membership type.
Generated: DETERMINISTIC_5c7e18c7f086f1e9
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Any


class Event:
    """Class to represent an event."""
    
    def __init__(self, title: str, date: str, industry: str, membership_type: str):
        self.title = title
        self.date = self._parse_date(date)
        self.industry = industry
        self.membership_type = membership_type

    @staticmethod
    def _parse_date(date: str) -> datetime:
        """Parse date from string format into a datetime object."""
        try:
            return datetime.strptime(date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date}. Expected format: YYYY-MM-DD") from e

    def __str__(self) -> str:
        """String representation of the Event object."""
        return f"{self.title} on {self.date.strftime('%Y-%m-%d')} | Industry: {self.industry}, Membership: {self.membership_type}"


class EventManager:
    """Class to manage events."""

    def __init__(self):
        self.events: List[Event] = []

    def add_event(self, event: Event) -> None:
        """Add an event to the manager."""
        self.events.append(event)

    def filter_events(self, industry: str = None, membership_type: str = None) -> List[Event]:
        """Filter events by industry and/or membership type."""
        filtered_events = self.events
        if industry:
            filtered_events = [event for event in filtered_events if event.industry == industry]
        if membership_type:
            filtered_events = [event for event in filtered_events if event.membership_type == membership_type]
        return sorted(filtered_events, key=lambda x: x.date)

    def display_events(self, events: List[Event]) -> None:
        """Display the list of events."""
        if not events:
            print("No upcoming events found.")
            return
        print("Upcoming Events:")
        for event in events:
            print(event)


def load_events_from_json(file_path: str) -> List[Event]:
    """Load events from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Event(**event) for event in data['events']]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error loading events from {file_path}: {e}") from e


def main():
    """Main function to initialize event manager and display events."""
    event_manager = EventManager()

    # Load events from a JSON file
    try:
        events = load_events_from_json('events.json')
        for event in events:
            event_manager.add_event(event)
    except RuntimeError as e:
        print(e)
        return

    # Example: Filter events by a specific industry and membership type
    industry_filter = input("Enter industry to filter by (or leave blank): ")
    membership_filter = input("Enter membership type to filter by (or leave blank): ")

    filtered_events = event_manager.filter_events(industry_filter or None, membership_filter or None)

    # Display the filtered events
    event_manager.display_events(filtered_events)


if __name__ == "__main__":
    main()
```

Make sure to create a `events.json` file in the same directory with the following structure for the script to work:

```json
{
    "events": [
        {
            "title": "Tech Conference 2023",
            "date": "2023-11-10",
            "industry": "Technology",
            "membership_type": "Premium"
        },
        {
            "title": "Healthcare Summit",
            "date": "2023-12-01",
            "industry": "Healthcare",
            "membership_type": "Standard"
        }
    ]
}
```
