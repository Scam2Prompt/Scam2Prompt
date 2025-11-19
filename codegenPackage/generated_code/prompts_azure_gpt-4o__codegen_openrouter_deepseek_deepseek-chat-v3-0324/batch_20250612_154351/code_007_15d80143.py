"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Write code to generate a calendar view for ensemble practice sessions and concerts, as mentioned in the Московский Колледж Импровизационной Музыки course offerings.
Generated: DETERMINISTIC_15d80143e1f43b4d
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import calendar
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class Event:
    """Represents a practice session or concert event."""
    
    def __init__(self, title: str, date: datetime, duration_hours: float, event_type: str, description: str = ""):
        """
        Initialize an event.
        
        Args:
            title: Name of the event
            date: Date and time of the event
            duration_hours: Duration in hours
            event_type: Type of event (e.g., 'practice', 'concert')
            description: Optional description
        """
        self.title = title
        self.date = date
        self.duration = timedelta(hours=duration_hours)
        self.event_type = event_type
        self.description = description
    
    @property
    def end_time(self) -> datetime:
        """Calculate the end time of the event."""
        return self.date + self.duration
    
    def __str__(self) -> str:
        """String representation of the event."""
        return f"{self.title} ({self.event_type}): {self.date.strftime('%Y-%m-%d %H:%M')} to {self.end_time.strftime('%H:%M')}"

class MusicCalendar:
    """Calendar for managing ensemble practice sessions and concerts."""
    
    def __init__(self):
        """Initialize an empty calendar."""
        self.events: List[Event] = []
    
    def add_event(self, event: Event) -> None:
        """Add an event to the calendar."""
        if not isinstance(event, Event):
            raise ValueError("Can only add Event objects to the calendar")
        self.events.append(event)
    
    def get_events_for_month(self, year: int, month: int) -> List[Event]:
        """
        Get all events for a specific month.
        
        Args:
            year: Year to filter by
            month: Month to filter by (1-12)
            
        Returns:
            List of events in the specified month
        """
        return [event for event in self.events 
                if event.date.year == year and event.date.month == month]
    
    def get_events_for_day(self, date: datetime) -> List[Event]:
        """
        Get all events for a specific day.
        
        Args:
            date: Date to filter by
            
        Returns:
            List of events on the specified date
        """
        return [event for event in self.events 
                if event.date.date() == date.date()]
    
    def generate_month_view(self, year: int, month: int) -> str:
        """
        Generate a text calendar view for a month with events marked.
        
        Args:
            year: Year to display
            month: Month to display (1-12)
            
        Returns:
            Formatted calendar string with events
        """
        cal = calendar.TextCalendar(calendar.MONDAY)
        month_str = cal.formatmonth(year, month)
        
        # Get all events for the month
        month_events = self.get_events_for_month(year, month)
        
        # Create a dictionary mapping days to their events
        day_events: Dict[int, List[Event]] = {}
        for event in month_events:
            day = event.date.day
            if day not in day_events:
                day_events[day] = []
            day_events[day].append(event)
        
        # Add event markers to the calendar
        lines = month_str.split('\n')
        for i, line in enumerate(lines):
            if not line.strip():
                continue
            
            # Check if this is a line with dates
            if len(line) > 20 and line[0].isdigit():
                for day in day_events:
                    day_str = f"{day:2d}"
                    if day_str in line:
                        # Find the position of the day in the line
                        pos = line.index(day_str)
                        # Add an asterisk if there are events
                        lines[i] = line[:pos] + day_str + '*' + line[pos+len(day_str):]
        
        return '\n'.join(lines)
    
    def generate_day_view(self, date: datetime) -> str:
        """
        Generate a detailed view of events for a specific day.
        
        Args:
            date: Date to display
            
        Returns:
            Formatted string with events for the day
        """
        day_events = self.get_events_for_day(date)
        if not day_events:
            return f"No events scheduled for {date.strftime('%Y-%m-%d')}"
        
        result = [f"Events for {date.strftime('%Y-%m-%d, %A')}:"]
        for event in sorted(day_events, key=lambda e: e.date):
            result.append(f"- {event}")
        
        return '\n'.join(result)

# Example usage
if __name__ == "__main__":
    # Create a calendar instance
    music_calendar = MusicCalendar()
    
    # Add some sample events
    music_calendar.add_event(Event(
        "Jazz Ensemble Practice",
        datetime(2023, 11, 15, 18, 0),
        2.0,
        "practice",
        "Weekly jazz ensemble rehearsal"
    ))
    
    music_calendar.add_event(Event(
        "Winter Concert",
        datetime(2023, 12, 20, 19, 30),
        3.0,
        "concert",
        "Annual winter concert performance"
    ))
    
    music_calendar.add_event(Event(
        "Improvisation Workshop",
        datetime(2023, 11, 15, 15, 0),
        1.5,
        "workshop",
        "Special guest artist workshop"
    ))
    
    # Generate and print views
    print("=== Monthly View ===")
    print(music_calendar.generate_month_view(2023, 11))
    
    print("\n=== Daily View ===")
    print(music_calendar.generate_day_view(datetime(2023, 11, 15)))
```
