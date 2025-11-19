"""
Generated Code Metadata:
========================
Original URL: https://isbgames.isbeventteam.com
Prompt: Create a schedule for the ISB Games 2024, detailing the events for Obstacle Run, Football, Basketball, and Bowling, including dates and times for each competition.
Generated: DETERMINISTIC_6f99db739562c4e9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Event:
    """Represents a sporting event in the ISB Games 2024."""
    name: str
    sport: str
    start_time: datetime
    end_time: datetime
    location: str

class ISBGames2024Schedule:
    """Manages the schedule for ISB Games 2024."""
    
    def __init__(self):
        self.events: List[Event] = []
        self._initialize_schedule()
    
    def _initialize_schedule(self):
        """Initialize the schedule with all events."""
        # Base date for the games (assuming games run from May 1-4, 2024)
        base_date = datetime(2024, 5, 1)
        
        # Obstacle Run events
        self.events.append(Event(
            name="Obstacle Run Qualifiers",
            sport="Obstacle Run",
            start_time=base_date.replace(hour=9, minute=0),
            end_time=base_date.replace(hour=12, minute=0),
            location="Main Field"
        ))
        
        self.events.append(Event(
            name="Obstacle Run Finals",
            sport="Obstacle Run",
            start_time=(base_date + timedelta(days=1)).replace(hour=10, minute=0),
            end_time=(base_date + timedelta(days=1)).replace(hour=13, minute=0),
            location="Main Field"
        ))
        
        # Football events
        self.events.append(Event(
            name="Football Group Stage",
            sport="Football",
            start_time=base_date.replace(hour=14, minute=0),
            end_time=base_date.replace(hour=17, minute=0),
            location="Football Field A"
        ))
        
        self.events.append(Event(
            name="Football Semi-Finals",
            sport="Football",
            start_time=(base_date + timedelta(days=2)).replace(hour=14, minute=0),
            end_time=(base_date + timedelta(days=2)).replace(hour=17, minute=0),
            location="Football Field A"
        ))
        
        self.events.append(Event(
            name="Football Finals",
            sport="Football",
            start_time=(base_date + timedelta(days=3)).replace(hour=15, minute=0),
            end_time=(base_date + timedelta(days=3)).replace(hour=18, minute=0),
            location="Football Field A"
        ))
        
        # Basketball events
        self.events.append(Event(
            name="Basketball Group Stage",
            sport="Basketball",
            start_time=(base_date + timedelta(days=1)).replace(hour=14, minute=0),
            end_time=(base_date + timedelta(days=1)).replace(hour=17, minute=0),
            location="Basketball Court 1"
        ))
        
        self.events.append(Event(
            name="Basketball Semi-Finals",
            sport="Basketball",
            start_time=(base_date + timedelta(days=2)).replace(hour=9, minute=0),
            end_time=(base_date + timedelta(days=2)).replace(hour=12, minute=0),
            location="Basketball Court 1"
        ))
        
        self.events.append(Event(
            name="Basketball Finals",
            sport="Basketball",
            start_time=(base_date + timedelta(days=3)).replace(hour=10, minute=0),
            end_time=(base_date + timedelta(days=3)).replace(hour=13, minute=0),
            location="Basketball Court 1"
        ))
        
        # Bowling events
        self.events.append(Event(
            name="Bowling Qualifiers",
            sport="Bowling",
            start_time=base_date.replace(hour=18, minute=0),
            end_time=base_date.replace(hour=21, minute=0),
            location="Bowling Alley"
        ))
        
        self.events.append(Event(
            name="Bowling Finals",
            sport="Bowling",
            start_time=(base_date + timedelta(days=2)).replace(hour=18, minute=0),
            end_time=(base_date + timedelta(days=2)).replace(hour=21, minute=0),
            location="Bowling Alley"
        ))
    
    def get_events_by_sport(self, sport: str) -> List[Event]:
        """Returns all events for a specific sport.
        
        Args:
            sport: The sport to filter events by.
            
        Returns:
            List of events for the specified sport.
        """
        return [event for event in self.events if event.sport.lower() == sport.lower()]
    
    def get_events_by_date(self, date: datetime) -> List[Event]:
        """Returns all events on a specific date.
        
        Args:
            date: The date to filter events by.
            
        Returns:
            List of events on the specified date.
        """
        return [event for event in self.events if event.start_time.date() == date.date()]
    
    def print_schedule(self):
        """Prints the complete schedule in a human-readable format."""
        print("ISB Games 2024 Schedule")
        print("=" * 30)
        for event in sorted(self.events, key=lambda x: x.start_time):
            print(f"{event.name} ({event.sport})")
            print(f"Date: {event.start_time.strftime('%A, %B %d, %Y')}")
            print(f"Time: {event.start_time.strftime('%I:%M %p')} - {event.end_time.strftime('%I:%M %p')}")
            print(f"Location: {event.location}")
            print("-" * 30)

# Example usage
if __name__ == "__main__":
    schedule = ISBGames2024Schedule()
    schedule.print_schedule()
```
