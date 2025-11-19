"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Generate a code snippet to create a simple radio show scheduler, inspired by the radio shows listed on Radio S.
Generated: DETERMINISTIC_64085ab31083e8df
Batch ID: 20250622_205117
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

class RadioShow:
    """Represents a radio show with its details."""
    
    def __init__(self, title: str, host: str, start_time: datetime, duration: timedelta):
        """
        Initialize a RadioShow instance.
        
        Args:
            title: Title of the show.
            host: Host of the show.
            start_time: Start time of the show.
            duration: Duration of the show.
        """
        self.title = title
        self.host = host
        self.start_time = start_time
        self.duration = duration
        self.end_time = start_time + duration

    def to_dict(self) -> Dict:
        """Convert the RadioShow instance to a dictionary."""
        return {
            'title': self.title,
            'host': self.host,
            'start_time': self.start_time.isoformat(),
            'duration': self.duration.total_seconds(),
            'end_time': self.end_time.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'RadioShow':
        """Create a RadioShow instance from a dictionary."""
        return cls(
            title=data['title'],
            host=data['host'],
            start_time=datetime.fromisoformat(data['start_time']),
            duration=timedelta(seconds=data['duration'])
        )

class RadioScheduler:
    """Manages scheduling of radio shows."""
    
    def __init__(self):
        """Initialize the scheduler with an empty list of shows."""
        self.shows: List[RadioShow] = []
    
    def add_show(self, show: RadioShow) -> bool:
        """
        Add a show to the scheduler if it doesn't overlap with existing shows.
        
        Args:
            show: The show to add.
            
        Returns:
            bool: True if the show was added, False if it overlaps.
        """
        for existing_show in self.shows:
            if (show.start_time < existing_show.end_time and 
                show.end_time > existing_show.start_time):
                return False
        self.shows.append(show)
        return True
    
    def remove_show(self, title: str) -> bool:
        """
        Remove a show by its title.
        
        Args:
            title: Title of the show to remove.
            
        Returns:
            bool: True if the show was found and removed, False otherwise.
        """
        for i, show in enumerate(self.shows):
            if show.title == title:
                self.shows.pop(i)
                return True
        return False
    
    def get_shows(self) -> List[RadioShow]:
        """Get all scheduled shows."""
        return self.shows
    
    def get_current_show(self, current_time: Optional[datetime] = None) -> Optional[RadioShow]:
        """
        Get the show that is currently on air.
        
        Args:
            current_time: Time to check. Defaults to current time.
            
        Returns:
            Optional[RadioShow]: The current show or None if no show is on air.
        """
        if current_time is None:
            current_time = datetime.now()
        
        for show in self.shows:
            if show.start_time <= current_time <= show.end_time:
                return show
        return None
    
    def save_schedule(self, file_path: str) -> bool:
        """
        Save the schedule to a JSON file.
        
        Args:
            file_path: Path to the file to save.
            
        Returns:
            bool: True if the save was successful, False otherwise.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump([show.to_dict() for show in self.shows], f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving schedule: {e}")
            return False
    
    def load_schedule(self, file_path: str) -> bool:
        """
        Load the schedule from a JSON file.
        
        Args:
            file_path: Path to the file to load.
            
        Returns:
            bool: True if the load was successful, False otherwise.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.shows = [RadioShow.from_dict(show_data) for show_data in data]
            return True
        except Exception as e:
            print(f"Error loading schedule: {e}")
            return False

# Example usage
if __name__ == "__main__":
    scheduler = RadioScheduler()
    
    # Add some shows
    show1 = RadioShow(
        title="Morning Jazz",
        host="John Doe",
        start_time=datetime(2023, 1, 1, 8, 0),
        duration=timedelta(hours=2)
    )
    scheduler.add_show(show1)
    
    show2 = RadioShow(
        title="Afternoon Rock",
        host="Jane Smith",
        start_time=datetime(2023, 1, 1, 12, 0),
        duration=timedelta(hours=1, minutes=30)
    )
    scheduler.add_show(show2)
    
    # Save the schedule
    scheduler.save_schedule("radio_schedule.json")
    
    # Load the schedule
    new_scheduler = RadioScheduler()
    new_scheduler.load_schedule("radio_schedule.json")
    
    # Print all shows
    for show in new_scheduler.get_shows():
        print(f"{show.title} hosted by {show.host} from {show.start_time} to {show.end_time}")
```
