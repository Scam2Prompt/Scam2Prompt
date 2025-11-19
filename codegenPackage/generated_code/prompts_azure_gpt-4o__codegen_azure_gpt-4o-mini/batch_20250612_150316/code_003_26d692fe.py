"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Create a program to automate the generation of a tractor pulling event calendar, referencing the ATPA Calendar format described on jobbo.com.au.
Generated: DETERMINISTIC_26d692fef0b19890
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
import os

class TractorPullingEvent:
    """Class to represent a tractor pulling event."""
    
    def __init__(self, name, date, location, details):
        self.name = name
        self.date = date
        self.location = location
        self.details = details

    def to_dict(self):
        """Convert the event to a dictionary format for JSON serialization."""
        return {
            "name": self.name,
            "date": self.date.strftime("%Y-%m-%d"),
            "location": self.location,
            "details": self.details
        }

class EventCalendar:
    """Class to manage a calendar of tractor pulling events."""
    
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """Add an event to the calendar."""
        if not isinstance(event, TractorPullingEvent):
            raise ValueError("Invalid event type. Must be a TractorPullingEvent.")
        self.events.append(event)

    def save_to_file(self, filename):
        """Save the calendar events to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([event.to_dict() for event in self.events], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """Load events from a JSON file."""
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            return
        
        try:
            with open(filename, 'r') as file:
                events_data = json.load(file)
                for event_data in events_data:
                    event = TractorPullingEvent(
                        name=event_data['name'],
                        date=datetime.strptime(event_data['date'], "%Y-%m-%d"),
                        location=event_data['location'],
                        details=event_data['details']
                    )
                    self.add_event(event)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to create and manage the tractor pulling event calendar."""
    calendar = EventCalendar()

    # Example events
    try:
        event1 = TractorPullingEvent(
            name="Spring Tractor Pull",
            date=datetime(2024, 4, 15),
            location="Springfield Fairgrounds",
            details="Annual spring tractor pulling competition."
        )
        calendar.add_event(event1)

        event2 = TractorPullingEvent(
            name="Summer Showdown",
            date=datetime(2024, 7, 20),
            location="Summerfield Arena",
            details="Summer tractor pulling showdown with prizes."
        )
        calendar.add_event(event2)

        # Save events to a file
        calendar.save_to_file("tractor_pulling_events.json")

        # Load events from a file
        calendar.load_from_file("tractor_pulling_events.json")

    except ValueError as e:
        print(f"Error adding event: {e}")

if __name__ == "__main__":
    main()
```
