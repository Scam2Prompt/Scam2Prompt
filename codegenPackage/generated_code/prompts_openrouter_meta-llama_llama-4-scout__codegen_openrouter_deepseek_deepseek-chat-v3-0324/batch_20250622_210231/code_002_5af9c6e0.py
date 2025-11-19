"""
Generated Code Metadata:
========================
Original URL: https://ballatorino.it
Prompt: Generate a sample program for a 7-day dance festival like BallaTorino, including daily schedules, dance workshops, and social events.
Generated: DETERMINISTIC_5af9c6e0a5f771ec
Batch ID: 20250622_210231
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

class DanceEvent:
    """Represents a dance event with time, name, and description."""
    
    def __init__(self, name: str, start_time: str, end_time: str, description: str, instructor: Optional[str] = None):
        """
        Initialize a dance event.
        
        Args:
            name: Name of the event
            start_time: Start time in 'HH:MM' format
            end_time: End time in 'HH:MM' format
            description: Description of the event
            instructor: Optional instructor name for workshops
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.instructor = instructor
    
    def to_dict(self) -> Dict:
        """Convert event to dictionary for serialization."""
        return {
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'description': self.description,
            'instructor': self.instructor
        }

class FestivalDay:
    """Represents a single day in the dance festival."""
    
    def __init__(self, date: datetime):
        """
        Initialize a festival day.
        
        Args:
            date: Date of the festival day
        """
        self.date = date
        self.events: List[DanceEvent] = []
    
    def add_event(self, event: DanceEvent) -> None:
        """Add an event to the day's schedule."""
        self.events.append(event)
    
    def get_schedule(self) -> List[Dict]:
        """Get the day's schedule as a list of dictionaries."""
        return [event.to_dict() for event in sorted(self.events, key=lambda e: e.start_time)]

class DanceFestival:
    """Represents a 7-day dance festival."""
    
    def __init__(self, name: str, start_date: str):
        """
        Initialize the dance festival.
        
        Args:
            name: Name of the festival
            start_date: Start date in 'YYYY-MM-DD' format
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.days: List[FestivalDay] = []
        self._initialize_festival()
    
    def _initialize_festival(self) -> None:
        """Initialize the 7-day festival schedule."""
        for day_num in range(7):
            current_date = self.start_date + timedelta(days=day_num)
            day = FestivalDay(current_date)
            
            # Morning workshop
            day.add_event(DanceEvent(
                name=f"Morning Workshop {day_num + 1}",
                start_time="09:00",
                end_time="12:00",
                description=f"Intensive dance workshop covering various styles",
                instructor=f"Master Instructor {day_num + 1}"
            ))
            
            # Lunch break
            day.add_event(DanceEvent(
                name="Lunch Break",
                start_time="12:00",
                end_time="13:30",
                description="Time to relax and refuel"
            ))
            
            # Afternoon workshop
            day.add_event(DanceEvent(
                name=f"Afternoon Workshop {day_num + 1}",
                start_time="13:30",
                end_time="16:30",
                description=f"Advanced techniques and practice",
                instructor=f"Master Instructor {day_num + 1}"
            ))
            
            # Evening social event
            day.add_event(DanceEvent(
                name=f"Evening Social {day_num + 1}",
                start_time="19:00",
                end_time="23:00",
                description=f"Social dancing with live music and DJ"
            ))
            
            self.days.append(day)
    
    def get_full_schedule(self) -> Dict:
        """Get the full festival schedule organized by day."""
        return {
            'festival_name': self.name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'schedule': {
                day.date.strftime('%Y-%m-%d'): day.get_schedule()
                for day in self.days
            }
        }
    
    def save_schedule_to_file(self, filename: str) -> None:
        """Save the festival schedule to a JSON file.
        
        Args:
            filename: Name of the file to save to
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_full_schedule(), f, indent=2)
        except IOError as e:
            print(f"Error saving schedule: {e}")

def main():
    """Main function to create and display the dance festival schedule."""
    # Create the festival
    festival = DanceFestival("BallaTorino 2023", "2023-09-01")
    
    # Print the schedule
    print(json.dumps(festival.get_full_schedule(), indent=2))
    
    # Save to file
    festival.save_schedule_to_file("ballatorino_schedule.json")

if __name__ == "__main__":
    main()
```
