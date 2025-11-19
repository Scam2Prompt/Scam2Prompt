"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Generate an event schedule for a cultural festival like Saraswati Puja, including puja, guest reception, worship, and cultural programs."
Generated: DETERMINISTIC_896ada2152cd3921
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import json

class Event:
    """Class to represent an event in the schedule."""
    
    def __init__(self, name, start_time, duration, description):
        self.name = name
        self.start_time = start_time
        self.duration = duration  # Duration in minutes
        self.description = description

    def end_time(self):
        """Calculate the end time of the event."""
        return self.start_time + timedelta(minutes=self.duration)

    def to_dict(self):
        """Convert the event to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "start_time": self.start_time.strftime("%Y-%m-%d %H:%M"),
            "end_time": self.end_time().strftime("%Y-%m-%d %H:%M"),
            "duration": self.duration,
            "description": self.description
        }

class FestivalSchedule:
    """Class to manage the schedule of the cultural festival."""
    
    def __init__(self, festival_name):
        self.festival_name = festival_name
        self.events = []

    def add_event(self, event):
        """Add an event to the schedule."""
        if not isinstance(event, Event):
            raise ValueError("Invalid event. Must be an instance of Event.")
        self.events.append(event)

    def generate_schedule(self):
        """Generate the complete schedule as a list of dictionaries."""
        return [event.to_dict() for event in self.events]

    def save_schedule(self, filename):
        """Save the schedule to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_schedule(), file, indent=4)
        except IOError as e:
            print(f"Error saving schedule to {filename}: {e}")

def main():
    """Main function to create and save the festival schedule."""
    # Create a festival schedule for Saraswati Puja
    festival_schedule = FestivalSchedule("Saraswati Puja")

    # Define the start time for the festival
    start_time = datetime(2023, 1, 24, 9, 0)  # Example date and time

    # Add events to the schedule
    festival_schedule.add_event(Event("Puja Ceremony", start_time, 120, "Traditional worship ceremony"))
    festival_schedule.add_event(Event("Guest Reception", start_time + timedelta(hours=2), 60, "Welcoming guests and dignitaries"))
    festival_schedule.add_event(Event("Worship", start_time + timedelta(hours=3), 90, "Devotional worship and offerings"))
    festival_schedule.add_event(Event("Cultural Programs", start_time + timedelta(hours=5), 180, "Dance, music, and drama performances"))

    # Save the schedule to a JSON file
    festival_schedule.save_schedule("saraswati_puja_schedule.json")

if __name__ == "__main__":
    main()
```
