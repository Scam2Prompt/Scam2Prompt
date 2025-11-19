"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Write a script to manage and display upcoming events for an organization, including filtering by industry or membership type.
Generated: DETERMINISTIC_5c7e18c7f086f1e9
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class Event:
    """Class to represent an event."""
    
    def __init__(self, title: str, date: str, industry: str, membership_type: str):
        """
        Initialize an Event instance.

        :param title: Title of the event
        :param date: Date of the event in 'YYYY-MM-DD' format
        :param industry: Industry associated with the event
        :param membership_type: Membership type required to attend the event
        """
        self.title = title
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.industry = industry
        self.membership_type = membership_type

    def __repr__(self):
        return f"Event(title={self.title}, date={self.date.date()}, industry={self.industry}, membership_type={self.membership_type})"


class EventManager:
    """Class to manage events."""
    
    def __init__(self):
        """Initialize the EventManager with an empty event list."""
        self.events: List[Event] = []

    def load_events(self, file_path: str):
        """
        Load events from a JSON file.

        :param file_path: Path to the JSON file containing events
        """
        try:
            with open(file_path, 'r') as file:
                events_data = json.load(file)
                for event in events_data:
                    self.events.append(Event(**event))
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def filter_events(self, industry: str = None, membership_type: str = None) -> List[Event]:
        """
        Filter events by industry and/or membership type.

        :param industry: Industry to filter by
        :param membership_type: Membership type to filter by
        :return: List of filtered events
        """
        filtered_events = self.events
        
        if industry:
            filtered_events = [event for event in filtered_events if event.industry == industry]
        
        if membership_type:
            filtered_events = [event for event in filtered_events if event.membership_type == membership_type]
        
        return filtered_events

    def display_events(self, events: List[Event]):
        """
        Display a list of events.

        :param events: List of events to display
        """
        if not events:
            print("No events found.")
            return
        
        print("Upcoming Events:")
        for event in events:
            print(f"- {event.title} on {event.date.date()} (Industry: {event.industry}, Membership: {event.membership_type})")


if __name__ == "__main__":
    # Create an instance of EventManager
    event_manager = EventManager()
    
    # Load events from a JSON file
    event_manager.load_events('events.json')
    
    # Filter events by industry and membership type
    industry_filter = input("Enter industry to filter by (or leave blank): ")
    membership_filter = input("Enter membership type to filter by (or leave blank): ")
    
    # Get filtered events
    filtered_events = event_manager.filter_events(industry=industry_filter or None, membership_type=membership_filter or None)
    
    # Display the filtered events
    event_manager.display_events(filtered_events)
```

**Note:** Ensure that the `events.json` file exists in the same directory as this script and is formatted correctly as a JSON array of event objects. Each event object should have `title`, `date`, `industry`, and `membership_type` fields.
