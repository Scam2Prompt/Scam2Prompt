"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Create a program to automate the generation of a tractor pulling event calendar, referencing the ATPA Calendar format described on jobbo.com.au.
Generated: DETERMINISTIC_26d692fef0b19890
Batch ID: 20250612_150316
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
import os

class TractorPullingEvent:
    """
    Represents a tractor pulling event with a name, date, location, and description.
    """
    def __init__(self, name, event_date, location, description):
        self.name = name
        self.event_date = event_date
        self.location = location
        self.description = description

    def to_dict(self):
        """
        Converts the event to a dictionary format for JSON serialization.
        """
        return {
            "name": self.name,
            "date": self.event_date.strftime('%Y-%m-%d'),
            "location": self.location,
            "description": self.description
        }

class EventCalendar:
    """
    Manages a collection of tractor pulling events and generates a calendar.
    """
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """
        Adds a tractor pulling event to the calendar.
        """
        if not isinstance(event, TractorPullingEvent):
            raise ValueError("Only TractorPullingEvent instances can be added.")
        self.events.append(event)

    def generate_calendar(self, file_path):
        """
        Generates a calendar JSON file from the events.
        
        Args:
            file_path (str): The path where the calendar will be saved.
        """
        calendar_data = [event.to_dict() for event in self.events]
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        try:
            with open(file_path, 'w') as f:
                json.dump(calendar_data, f, indent=4)
            print(f"Calendar successfully generated at: {file_path}")
        except IOError as e:
            print(f"Error writing calendar to file: {e}")

def main():
    """
    Main function to create an event calendar and add events.
    """
    # Create an EventCalendar instance
    event_calendar = EventCalendar()

    # Sample events (in a real application, these would be dynamically populated)
    events = [
        TractorPullingEvent("Spring Pull", datetime.date(2023, 3, 15), "Springfield", "Annual spring tractor pull."),
        TractorPullingEvent("Summer Pull", datetime.date(2023, 6, 25), "Summerfield", "Summer season tractor pull competition."),
        TractorPullingEvent("Fall Pull", datetime.date(2023, 9, 10), "Falltown", "Fall festival tractor pulling event."),
        TractorPullingEvent("Winter Pull", datetime.date(2023, 12, 5), "Winterville", "Winter tractor pulling challenge."),
    ]

    # Add events to the calendar
    for event in events:
        try:
            event_calendar.add_event(event)
        except ValueError as e:
            print(f"Error adding event: {e}")

    # Generate the calendar JSON file
    calendar_file_path = 'calendar/tractor_pulling_events.json'
    event_calendar.generate_calendar(calendar_file_path)

if __name__ == "__main__":
    main()
```
