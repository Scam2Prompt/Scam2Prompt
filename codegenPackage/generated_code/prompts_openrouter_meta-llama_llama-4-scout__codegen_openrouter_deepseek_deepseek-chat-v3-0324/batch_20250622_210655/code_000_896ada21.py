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
from typing import List, Dict, Optional
import json

class Event:
    """Represents a single event in the festival schedule."""
    def __init__(self, name: str, start_time: datetime, duration: timedelta, 
                 description: str, participants: Optional[List[str]] = None):
        self.name = name
        self.start_time = start_time
        self.duration = duration
        self.description = description
        self.participants = participants or []
    
    def to_dict(self) -> Dict:
        """Convert event to dictionary for serialization."""
        return {
            "name": self.name,
            "start_time": self.start_time.isoformat(),
            "duration": self.duration.total_seconds(),
            "description": self.description,
            "participants": self.participants
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Event':
        """Create Event from dictionary."""
        return cls(
            name=data["name"],
            start_time=datetime.fromisoformat(data["start_time"]),
            duration=timedelta(seconds=data["duration"]),
            description=data["description"],
            participants=data.get("participants", [])
        )

class FestivalSchedule:
    """Manages the schedule of events for the festival."""
    def __init__(self, festival_name: str, date: datetime):
        self.festival_name = festival_name
        self.date = date
        self.events: List[Event] = []
    
    def add_event(self, event: Event) -> None:
        """Add an event to the schedule."""
        if event.start_time.date() != self.date.date():
            raise ValueError("Event date must match festival date")
        self.events.append(event)
    
    def get_schedule(self) -> List[Dict]:
        """Return the schedule as a list of dictionaries."""
        return [event.to_dict() for event in sorted(
            self.events, key=lambda e: e.start_time)]
    
    def save_to_file(self, filename: str) -> None:
        """Save schedule to JSON file."""
        with open(filename, 'w') as f:
            json.dump({
                "festival_name": self.festival_name,
                "date": self.date.isoformat(),
                "events": self.get_schedule()
            }, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'FestivalSchedule':
        """Load schedule from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        schedule = cls(
            festival_name=data["festival_name"],
            date=datetime.fromisoformat(data["date"])
        )
        for event_data in data["events"]:
            schedule.add_event(Event.from_dict(event_data))
        return schedule

def create_saraswati_puja_schedule() -> FestivalSchedule:
    """Create a sample Saraswati Puja schedule."""
    festival_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    schedule = FestivalSchedule("Saraswati Puja", festival_date)
    
    # Morning events
    schedule.add_event(Event(
        name="Puja Preparation",
        start_time=festival_date.replace(hour=6, minute=0),
        duration=timedelta(hours=1),
        description="Preparation of the altar and decorations"
    ))
    
    schedule.add_event(Event(
        name="Morning Puja",
        start_time=festival_date.replace(hour=7, minute=0),
        duration=timedelta(hours=2),
        description="Main worship ceremony with priest",
        participants=["Priest", "Organizers"]
    ))
    
    # Midday events
    schedule.add_event(Event(
        name="Guest Reception",
        start_time=festival_date.replace(hour=10, minute=0),
        duration=timedelta(hours=1),
        description="Welcome and reception of honored guests"
    ))
    
    schedule.add_event(Event(
        name="Prasad Distribution",
        start_time=festival_date.replace(hour=11, minute=30),
        duration=timedelta(minutes=30),
        description="Distribution of blessed food offerings"
    ))
    
    # Afternoon events
    schedule.add_event(Event(
        name="Cultural Program Preparation",
        start_time=festival_date.replace(hour=13, minute=0),
        duration=timedelta(hours=1),
        description="Setup for cultural performances"
    ))
    
    schedule.add_event(Event(
        name="Cultural Performances",
        start_time=festival_date.replace(hour=14, minute=0),
        duration=timedelta(hours=3),
        description="Music, dance, and drama performances",
        participants=["Local Artists", "Students"]
    ))
    
    # Evening events
    schedule.add_event(Event(
        name="Evening Aarti",
        start_time=festival_date.replace(hour=18, minute=0),
        duration=timedelta(minutes=30),
        description="Evening lamp ceremony"
    ))
    
    schedule.add_event(Event(
        name="Closing Ceremony",
        start_time=festival_date.replace(hour=19, minute=0),
        duration=timedelta(hours=1),
        description="Final speeches and thanks"
    ))
    
    return schedule

if __name__ == "__main__":
    try:
        schedule = create_saraswati_puja_schedule()
        print(f"Schedule for {schedule.festival_name} on {schedule.date.date()}:")
        for event in schedule.get_schedule():
            print(f"{event['start_time']} - {event['name']} ({event['description']})")
        
        # Save to file
        filename = "saraswati_puja_schedule.json"
        schedule.save_to_file(filename)
        print(f"\nSchedule saved to {filename}")
        
        # Optional: Load from file to demonstrate
        # loaded_schedule = FestivalSchedule.load_from_file(filename)
        # print("\nLoaded schedule matches:", loaded_schedule.get_schedule() == schedule.get_schedule())
    except Exception as e:
        print(f"Error generating schedule: {e}")
```
