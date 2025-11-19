"""
Generated Code Metadata:
========================
Original URL: https://mctsummit.org
Prompt: Write code to generate a schedule for a multi-day conference, including sessions, workshops, and networking events, based on the MCT Summit 2024 agenda.
Generated: DETERMINISTIC_57a37662ece337a9
Batch ID: 20250612_153246
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

class ConferenceEvent:
    """Base class for conference events."""
    
    def __init__(self, title: str, start_time: datetime, duration: int, 
                 location: str, description: str = "", speakers: List[str] = None):
        """
        Initialize a conference event.
        
        Args:
            title: Title of the event
            start_time: Start time as datetime object
            duration: Duration in minutes
            location: Location/room name
            description: Event description (optional)
            speakers: List of speaker names (optional)
        """
        self.title = title
        self.start_time = start_time
        self.duration = duration
        self.location = location
        self.description = description
        self.speakers = speakers if speakers else []
    
    @property
    def end_time(self) -> datetime:
        """Calculate end time based on start time and duration."""
        return self.start_time + timedelta(minutes=self.duration)
    
    def to_dict(self) -> Dict:
        """Convert event to dictionary for serialization."""
        return {
            "title": self.title,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "duration": self.duration,
            "location": self.location,
            "description": self.description,
            "speakers": self.speakers
        }

class Session(ConferenceEvent):
    """Class representing a conference session."""
    
    def __init__(self, title: str, start_time: datetime, duration: int, 
                 location: str, description: str = "", speakers: List[str] = None,
                 session_type: str = "regular", track: str = "general"):
        """
        Initialize a conference session.
        
        Args:
            session_type: Type of session (regular, keynote, panel)
            track: Track/category of the session
        """
        super().__init__(title, start_time, duration, location, description, speakers)
        self.session_type = session_type
        self.track = track
    
    def to_dict(self) -> Dict:
        """Convert session to dictionary for serialization."""
        data = super().to_dict()
        data.update({
            "type": "session",
            "session_type": self.session_type,
            "track": self.track
        })
        return data

class Workshop(ConferenceEvent):
    """Class representing a workshop."""
    
    def __init__(self, title: str, start_time: datetime, duration: int, 
                 location: str, description: str = "", speakers: List[str] = None,
                 capacity: int = 30, requirements: str = ""):
        """
        Initialize a workshop.
        
        Args:
            capacity: Maximum number of attendees
            requirements: Any special requirements
        """
        super().__init__(title, start_time, duration, location, description, speakers)
        self.capacity = capacity
        self.requirements = requirements
    
    def to_dict(self) -> Dict:
        """Convert workshop to dictionary for serialization."""
        data = super().to_dict()
        data.update({
            "type": "workshop",
            "capacity": self.capacity,
            "requirements": self.requirements
        })
        return data

class NetworkingEvent(ConferenceEvent):
    """Class representing a networking event."""
    
    def __init__(self, title: str, start_time: datetime, duration: int, 
                 location: str, description: str = "", speakers: List[str] = None,
                 event_type: str = "social"):
        """
        Initialize a networking event.
        
        Args:
            event_type: Type of networking event (social, lunch, coffee break)
        """
        super().__init__(title, start_time, duration, location, description, speakers)
        self.event_type = event_type
    
    def to_dict(self) -> Dict:
        """Convert networking event to dictionary for serialization."""
        data = super().to_dict()
        data.update({
            "type": "networking",
            "event_type": self.event_type
        })
        return data

class ConferenceDay:
    """Class representing a single day of the conference."""
    
    def __init__(self, date: datetime, events: List[ConferenceEvent] = None):
        """
        Initialize a conference day.
        
        Args:
            date: Date of the conference day
            events: List of events for this day
        """
        self.date = date
        self.events = events if events else []
    
    def add_event(self, event: ConferenceEvent) -> None:
        """Add an event to the day's schedule."""
        if event.start_time.date() != self.date.date():
            raise ValueError("Event date does not match conference day date")
        self.events.append(event)
    
    def get_events(self) -> List[ConferenceEvent]:
        """Get all events sorted by start time."""
        return sorted(self.events, key=lambda e: e.start_time)
    
    def to_dict(self) -> Dict:
        """Convert day to dictionary for serialization."""
        return {
            "date": self.date.isoformat(),
            "events": [event.to_dict() for event in self.get_events()]
        }

class ConferenceSchedule:
    """Class representing the full conference schedule."""
    
    def __init__(self, name: str, days: List[ConferenceDay] = None):
        """
        Initialize a conference schedule.
        
        Args:
            name: Name of the conference
            days: List of conference days
        """
        self.name = name
        self.days = days if days else []
    
    def add_day(self, day: ConferenceDay) -> None:
        """Add a conference day to the schedule."""
        self.days.append(day)
    
    def get_days(self) -> List[ConferenceDay]:
        """Get all days sorted by date."""
        return sorted(self.days, key=lambda d: d.date)
    
    def to_dict(self) -> Dict:
        """Convert schedule to dictionary for serialization."""
        return {
            "conference": self.name,
            "days": [day.to_dict() for day in self.get_days()]
        }
    
    def save_to_file(self, filename: str) -> None:
        """Save schedule to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'ConferenceSchedule':
        """Load schedule from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        schedule = cls(data['conference'])
        
        for day_data in data['days']:
            date = datetime.fromisoformat(day_data['date'])
            day = ConferenceDay(date)
            
            for event_data in day_data['events']:
                event_type = event_data['type']
                start_time = datetime.fromisoformat(event_data['start_time'])
                
                common_args = {
                    'title': event_data['title'],
                    'start_time': start_time,
                    'duration': event_data['duration'],
                    'location': event_data['location'],
                    'description': event_data['description'],
                    'speakers': event_data['speakers']
                }
                
                if event_type == 'session':
                    event = Session(
                        session_type=event_data['session_type'],
                        track=event_data['track'],
                        **common_args
                    )
                elif event_type == 'workshop':
                    event = Workshop(
                        capacity=event_data['capacity'],
                        requirements=event_data['requirements'],
                        **common_args
                    )
                elif event_type == 'networking':
                    event = NetworkingEvent(
                        event_type=event_data['event_type'],
                        **common_args
                    )
                else:
                    raise ValueError(f"Unknown event type: {event_type}")
                
                day.add_event(event)
            
            schedule.add_day(day)
        
        return schedule

def create_mct_summit_2024_schedule() -> ConferenceSchedule:
    """Create a sample MCT Summit 2024 schedule."""
    schedule = ConferenceSchedule("MCT Summit 2024")
    
    # Day 1 - April 15, 2024
    day1_date = datetime(2024, 4, 15)
    day1 = ConferenceDay(day1_date)
    
    day1.add_event(NetworkingEvent(
        "Registration & Breakfast",
        datetime(2024, 4, 15, 8, 0),
        60,
        "Grand Lobby",
        "Check-in and enjoy breakfast before the sessions begin",
        event_type="social"
    ))
    
    day1.add_event(Session(
        "Opening Keynote: The Future of Cloud Technology",
        datetime(2024, 4, 15, 9, 0),
        60,
        "Main Auditorium",
        "Join our keynote speaker as they discuss emerging trends in cloud technology",
        ["Satya Nadella"],
        session_type="keynote"
    ))
    
    day1.add_event(NetworkingEvent(
        "Morning Coffee Break",
        datetime(2024, 4, 15, 10, 0),
        30,
        "Exhibition Hall",
        "Network with fellow attendees and visit sponsor booths",
        event_type="coffee break"
    ))
    
    day1.add_event(Session(
        "Azure AI: From
