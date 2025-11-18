"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oric.kinnaird.edu.pk
Prompt: Create a program to track upcoming conferences, workshops, and seminars, based on the event structure outlined by ORIC at Kinnaird College.
Generated: DETERMINISTIC_2b0b405193fc4a2c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Event:
    """A class to represent a generic event."""
    
    def __init__(self, title, event_type, date, location, description):
        """
        Initializes the event with title, type, date, location, and description.
        
        Args:
            title (str): Title of the event.
            event_type (str): Type of the event (e.g., Conference, Workshop, Seminar).
            date (datetime.date): Date of the event.
            location (str): Location of the event.
            description (str): Description of the event.
        """
        self.title = title
        self.event_type = event_type
        self.date = date
        self.location = location
        self.description = description

    def __str__(self):
        """String representation of the event."""
        return f"{self.title} ({self.event_type}) on {self.date} at {self.location}"

class EventManager:
    """A class to manage a list of events."""
    
    def __init__(self):
        """Initializes the event manager with an empty event list."""
        self.events = []
        
    def add_event(self, event):
        """
        Adds an event to the event list.
        
        Args:
            event (Event): An instance of the Event class.
        """
        if not isinstance(event, Event):
            raise ValueError("Only instances of Event can be added.")
        self.events.append(event)

    def get_upcoming_events(self):
        """Returns a list of upcoming events."""
        today = datetime.date.today()
        upcoming_events = [event for event in self.events if event.date >= today]
        return sorted(upcoming_events, key=lambda x: x.date)

    def display_events(self):
        """Displays all upcoming events."""
        upcoming_events = self.get_upcoming_events()
        if not upcoming_events:
            print("No upcoming events.")
            return
            
        print("Upcoming Events:")
        for event in upcoming_events:
            print(event)

def main():
    """Main function to run the event tracking program."""
    manager = EventManager()

    # Example: Adding events
    try:
        manager.add_event(Event("AI Conference", "Conference", datetime.date(2023, 11, 15), "Auditorium A", "A conference on Artificial Intelligence advancements."))
        manager.add_event(Event("Python Workshop", "Workshop", datetime.date(2023, 10, 20), "Room 101", "Hands-on workshop on Python programming."))
        manager.add_event(Event("Research Seminar", "Seminar", datetime.date(2023, 12, 5), "Room 204", "Seminar on recent research findings."))
    except ValueError as e:
        print(f"Error adding event: {e}")

    # Display all upcoming events
    manager.display_events()

if __name__ == "__main__":
    main()
```
