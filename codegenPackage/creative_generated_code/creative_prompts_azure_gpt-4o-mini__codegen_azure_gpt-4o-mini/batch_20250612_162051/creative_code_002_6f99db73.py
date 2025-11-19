"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isbgames.isbeventteam.com
Prompt: Create a schedule for the ISB Games 2024, detailing the events for Obstacle Run, Football, Basketball, and Bowling, including dates and times for each competition.
Generated: DETERMINISTIC_6f99db739562c4e9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class Event:
    """Class to represent a single event in the schedule."""
    def __init__(self, name, date_time, duration, location):
        self.name = name
        self.date_time = date_time
        self.duration = duration
        self.location = location

    def to_dict(self):
        """Convert the event to a dictionary for easy JSON serialization."""
        return {
            'name': self.name,
            'date_time': self.date_time.strftime("%Y-%m-%d %H:%M"),
            'duration': self.duration,
            'location': self.location
        }

class Schedule:
    """Class to manage a schedule of events."""
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """Add an event to the schedule."""
        self.events.append(event)

    def to_json(self):
        """Convert the schedule to JSON format."""
        return json.dumps([event.to_dict() for event in self.events], indent=4)

def create_isb_games_schedule():
    """Create the schedule for the ISB Games 2024."""
    schedule = Schedule()

    try:
        # Define events for the ISB Games 2024
        events = [
            Event("Obstacle Run", datetime(2024, 5, 1, 9, 0), timedelta(hours=2), "Field A"),
            Event("Football", datetime(2024, 5, 1, 11, 30), timedelta(hours=2), "Field B"),
            Event("Basketball", datetime(2024, 5, 1, 14, 0), timedelta(hours=2), "Gymnasium"),
            Event("Bowling", datetime(2024, 5, 2, 10, 0), timedelta(hours=3), "Bowling Alley"),
            Event("Football Finals", datetime(2024, 5, 3, 16, 0), timedelta(hours=1, minutes=30), "Field B"),
            Event("Basketball Finals", datetime(2024, 5, 3, 18, 0), timedelta(hours=1, minutes=30), "Gymnasium"),
        ]

        for event in events:
            schedule.add_event(event)

        # Serialize the schedule to JSON format
        schedule_json = schedule.to_json()
        return schedule_json

    except Exception as e:
        print(f"An error occurred while creating the schedule: {e}")
        return None

if __name__ == "__main__":
    # Generate the ISB Games schedule and print it
    isb_games_schedule = create_isb_games_schedule()
    if isb_games_schedule:
        print(isb_games_schedule)
```
