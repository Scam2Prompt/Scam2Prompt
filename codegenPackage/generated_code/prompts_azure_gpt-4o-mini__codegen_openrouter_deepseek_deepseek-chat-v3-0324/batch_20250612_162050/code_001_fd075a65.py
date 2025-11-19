"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Write a Python script that lists activities and seminars for a wine festival, similar to those offered at FestiVin Caraquet.
Generated: DETERMINISTIC_fd075a65a7e0c46f
Batch ID: 20250612_162050
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
from typing import List, Dict, Optional

class WineFestivalEvent:
    """Represents an event at the wine festival."""
    
    def __init__(self, name: str, description: str, start_time: datetime, 
                 duration: timedelta, location: str, presenter: Optional[str] = None):
        """
        Initialize a wine festival event.
        
        Args:
            name: Name of the event
            description: Description of what the event entails
            start_time: When the event starts
            duration: How long the event lasts
            location: Where the event takes place
            presenter: Optional presenter/host of the event
        """
        self.name = name
        self.description = description
        self.start_time = start_time
        self.duration = duration
        self.end_time = start_time + duration
        self.location = location
        self.presenter = presenter
    
    def to_dict(self) -> Dict:
        """Convert event to dictionary for serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'duration_hours': self.duration.total_seconds() / 3600,
            'location': self.location,
            'presenter': self.presenter
        }
    
    def __str__(self) -> str:
        """User-friendly string representation."""
        presenter_str = f" with {self.presenter}" if self.presenter else ""
        return (f"{self.name}{presenter_str}\n"
                f"  {self.description}\n"
                f"  {self.start_time.strftime('%A, %B %d at %I:%M %p')} to "
                f"{self.end_time.strftime('%I:%M %p')}\n"
                f"  Location: {self.location}\n")

class WineFestivalSchedule:
    """Manages the schedule of events for the wine festival."""
    
    def __init__(self):
        """Initialize an empty schedule."""
        self.events: List[WineFestivalEvent] = []
    
    def add_event(self, event: WineFestivalEvent) -> None:
        """Add an event to the schedule."""
        self.events.append(event)
    
    def get_events_by_date(self, date: datetime) -> List[WineFestivalEvent]:
        """Get all events occurring on a specific date."""
        return [event for event in self.events 
                if event.start_time.date() == date.date()]
    
    def get_events_by_presenter(self, presenter: str) -> List[WineFestivalEvent]:
        """Get all events presented by a specific person."""
        return [event for event in self.events 
                if event.presenter and presenter.lower() in event.presenter.lower()]
    
    def save_to_file(self, filename: str) -> None:
        """Save the schedule to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([event.to_dict() for event in self.events], f, indent=2)
        except IOError as e:
            print(f"Error saving schedule: {e}")
    
    def load_from_file(self, filename: str) -> None:
        """Load the schedule from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.events = []
                for event_data in data:
                    start_time = datetime.fromisoformat(event_data['start_time'])
                    duration = timedelta(hours=event_data['duration_hours'])
                    self.add_event(WineFestivalEvent(
                        name=event_data['name'],
                        description=event_data['description'],
                        start_time=start_time,
                        duration=duration,
                        location=event_data['location'],
                        presenter=event_data.get('presenter')
                    ))
        except (IOError, json.JSONDecodeError, KeyError) as e:
            print(f"Error loading schedule: {e}")
    
    def print_schedule(self, events: Optional[List[WineFestivalEvent]] = None) -> None:
        """Print a list of events to the console."""
        events_to_print = events if events is not None else self.events
        if not events_to_print:
            print("No events scheduled.")
            return
        
        for event in sorted(events_to_print, key=lambda e: e.start_time):
            print(event)

def create_sample_schedule() -> WineFestivalSchedule:
    """Create a sample schedule with demo events."""
    schedule = WineFestivalSchedule()
    
    # Add sample events
    start_time = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
    
    schedule.add_event(WineFestivalEvent(
        name="Wine Tasting 101",
        description="Introduction to wine tasting techniques",
        start_time=start_time,
        duration=timedelta(hours=1.5),
        location="Main Tent",
        presenter="Jean Dupont"
    ))
    
    schedule.add_event(WineFestivalEvent(
        name="Local Vineyards Showcase",
        description="Meet local winemakers and sample regional wines",
        start_time=start_time + timedelta(hours=2),
        duration=timedelta(hours=2),
        location="Vineyard Pavilion"
    ))
    
    schedule.add_event(WineFestivalEvent(
        name="Food and Wine Pairing",
        description="Learn how to pair wines with local cuisine",
        start_time=start_time + timedelta(days=1, hours=11),
        duration=timedelta(hours=1),
        location="Gourmet Tent",
        presenter="Marie Leclerc"
    ))
    
    schedule.add_event(WineFestivalEvent(
        name="Organic Winemaking Seminar",
        description="Discussion on sustainable winemaking practices",
        start_time=start_time + timedelta(days=1, hours=14),
        duration=timedelta(hours=1.5),
        location="Eco Pavilion",
        presenter="Pierre Lambert"
    ))
    
    return schedule

def main():
    """Main function to demonstrate the wine festival schedule."""
    schedule = create_sample_schedule()
    
    print("=== Full Wine Festival Schedule ===")
    schedule.print_schedule()
    
    print("\n=== Today's Events ===")
    today_events = schedule.get_events_by_date(datetime.now())
    schedule.print_schedule(today_events)
    
    # Save and load demonstration
    schedule.save_to_file("wine_festival_schedule.json")
    
    new_schedule = WineFestivalSchedule()
    new_schedule.load_from_file("wine_festival_schedule.json")
    
    print("\n=== Loaded Schedule ===")
    new_schedule.print_schedule()

if __name__ == "__main__":
    main()
```
