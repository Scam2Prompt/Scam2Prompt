"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Create a program to track upcoming conferences, workshops, and seminars, based on the event structure outlined by ORIC at Kinnaird College.
Generated: DETERMINISTIC_2b0b405193fc4a2c
Batch ID: 20250612_153224
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/register": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/python-workshop": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Event:
    """
    Represents an event (conference, workshop, seminar) with relevant details.
    """
    
    def __init__(
        self,
        title: str,
        event_type: str,
        start_date: str,
        end_date: str,
        venue: str,
        organizer: str,
        description: str,
        registration_link: Optional[str] = None,
        speakers: Optional[List[str]] = None,
        topics: Optional[List[str]] = None
    ):
        """
        Initialize an Event instance.
        
        Args:
            title: Title of the event
            event_type: Type of event (conference, workshop, seminar)
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            venue: Location of the event
            organizer: Organizing body or institution
            description: Brief description of the event
            registration_link: URL for registration (optional)
            speakers: List of speakers (optional)
            topics: List of topics covered (optional)
        """
        self.title = title
        self.event_type = event_type
        self.start_date = start_date
        self.end_date = end_date
        self.venue = venue
        self.organizer = organizer
        self.description = description
        self.registration_link = registration_link
        self.speakers = speakers or []
        self.topics = topics or []
        
        # Validate dates
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Invalid date format. Use YYYY-MM-DD") from e

    def to_dict(self) -> Dict:
        """Convert Event object to dictionary for serialization."""
        return {
            "title": self.title,
            "event_type": self.event_type,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "venue": self.venue,
            "organizer": self.organizer,
            "description": self.description,
            "registration_link": self.registration_link,
            "speakers": self.speakers,
            "topics": self.topics
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Event':
        """Create Event object from dictionary."""
        return cls(
            title=data["title"],
            event_type=data["event_type"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            venue=data["venue"],
            organizer=data["organizer"],
            description=data["description"],
            registration_link=data.get("registration_link"),
            speakers=data.get("speakers", []),
            topics=data.get("topics", [])
        )

class EventTracker:
    """
    Manages a collection of events with CRUD operations and persistence.
    """
    
    def __init__(self, storage_file: str = "events.json"):
        """
        Initialize the EventTracker.
        
        Args:
            storage_file: Path to JSON file for storing events
        """
        self.storage_file = storage_file
        self.events: List[Event] = []
        self.load_events()

    def add_event(self, event: Event) -> None:
        """Add a new event to the tracker."""
        self.events.append(event)
        self.save_events()

    def remove_event(self, title: str) -> bool:
        """
        Remove an event by title.
        
        Returns:
            True if event was found and removed, False otherwise
        """
        for i, event in enumerate(self.events):
            if event.title.lower() == title.lower():
                del self.events[i]
                self.save_events()
                return True
        return False

    def get_upcoming_events(self) -> List[Event]:
        """Get events that are upcoming (end date is in the future)."""
        today = datetime.now().date()
        upcoming = []
        for event in self.events:
            event_date = datetime.strptime(event.end_date, "%Y-%m-%d").date()
            if event_date >= today:
                upcoming.append(event)
        return sorted(upcoming, key=lambda e: e.start_date)

    def get_events_by_type(self, event_type: str) -> List[Event]:
        """Get events filtered by type (conference, workshop, seminar)."""
        return [e for e in self.events if e.event_type.lower() == event_type.lower()]

    def search_events(self, keyword: str) -> List[Event]:
        """Search events by keyword in title, description, or topics."""
        keyword = keyword.lower()
        results = []
        for event in self.events:
            if (keyword in event.title.lower() or 
                keyword in event.description.lower() or 
                any(keyword in topic.lower() for topic in event.topics)):
                results.append(event)
        return results

    def save_events(self) -> None:
        """Save events to the storage file."""
        try:
            with open(self.storage_file, "w") as f:
                json.dump([e.to_dict() for e in self.events], f, indent=2)
        except IOError as e:
            print(f"Error saving events: {e}")

    def load_events(self) -> None:
        """Load events from the storage file."""
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                self.events = [Event.from_dict(item) for item in data]
        except FileNotFoundError:
            # File doesn't exist yet, start with empty list
            self.events = []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading events: {e}")
            self.events = []

def main():
    """Example usage of the EventTracker."""
    tracker = EventTracker()
    
    # Add sample events
    conference = Event(
        title="International Conference on Computer Science",
        event_type="conference",
        start_date="2023-11-15",
        end_date="2023-11-17",
        venue="Kinnaird College",
        organizer="ORIC",
        description="Annual conference on latest trends in computer science",
        registration_link="https://example.com/register",
        speakers=["Dr. Smith", "Prof. Johnson"],
        topics=["AI", "Machine Learning", "Data Science"]
    )
    
    workshop = Event(
        title="Python Programming Workshop",
        event_type="workshop",
        start_date="2023-10-10",
        end_date="2023-10-12",
        venue="Computer Lab, Kinnaird College",
        organizer="Computer Science Department",
        description="Hands-on workshop for Python programming",
        registration_link="https://example.com/python-workshop",
        topics=["Python Basics", "Web Development", "Data Analysis"]
    )
    
    tracker.add_event(conference)
    tracker.add_event(workshop)
    
    # Display upcoming events
    print("Upcoming Events:")
    for event in tracker.get_upcoming_events():
        print(f"- {event.title} ({event.start_date} to {event.end_date})")

if __name__ == "__main__":
    main()
```
