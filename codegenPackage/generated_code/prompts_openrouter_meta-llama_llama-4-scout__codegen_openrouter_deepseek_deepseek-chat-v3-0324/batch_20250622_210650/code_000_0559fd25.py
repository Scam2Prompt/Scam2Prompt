"""
Generated Code Metadata:
========================
Original URL: https://corporacionelcristal.com.co
Prompt: Write a Python script to create a simple puppetry show schedule using the Corporación El Cristal's event data.
Generated: DETERMINISTIC_0559fd2580287a9d
Batch ID: 20250622_210650
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

class PuppetryShow:
    """Represents a puppetry show event."""
    
    def __init__(self, title: str, date: str, time: str, duration: int, description: str):
        """
        Initialize a puppetry show.
        
        Args:
            title: Title of the show
            date: Date in YYYY-MM-DD format
            time: Time in HH:MM format
            duration: Duration in minutes
            description: Description of the show
        """
        self.title = title
        self.date = date
        self.time = time
        self.duration = duration
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert show details to dictionary."""
        return {
            'title': self.title,
            'date': self.date,
            'time': self.time,
            'duration': self.duration,
            'description': self.description
        }
    
    def __str__(self) -> str:
        """String representation of the show."""
        return f"{self.title} on {self.date} at {self.time} ({self.duration} mins)"


class PuppetryShowSchedule:
    """Manages a schedule of puppetry shows."""
    
    def __init__(self):
        """Initialize an empty schedule."""
        self.shows: List[PuppetryShow] = []
    
    def add_show(self, show: PuppetryShow) -> None:
        """Add a show to the schedule."""
        self.shows.append(show)
    
    def remove_show(self, title: str, date: str) -> bool:
        """
        Remove a show by title and date.
        
        Returns:
            True if show was found and removed, False otherwise
        """
        for i, show in enumerate(self.shows):
            if show.title == title and show.date == date:
                del self.shows[i]
                return True
        return False
    
    def get_shows_by_date(self, date: str) -> List[PuppetryShow]:
        """Get all shows on a specific date."""
        return [show for show in self.shows if show.date == date]
    
    def get_upcoming_shows(self, days: int = 7) -> List[PuppetryShow]:
        """
        Get shows in the next X days.
        
        Args:
            days: Number of days to look ahead (default: 7)
        
        Returns:
            List of upcoming shows
        """
        today = datetime.now().date()
        end_date = today + timedelta(days=days)
        
        upcoming = []
        for show in self.shows:
            show_date = datetime.strptime(show.date, "%Y-%m-%d").date()
            if today <= show_date <= end_date:
                upcoming.append(show)
        return upcoming
    
    def save_to_file(self, filename: str) -> bool:
        """
        Save schedule to JSON file.
        
        Returns:
            True if save was successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump([show.to_dict() for show in self.shows], f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving schedule: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """
        Load schedule from JSON file.
        
        Returns:
            True if load was successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.shows = [
                    PuppetryShow(
                        show['title'],
                        show['date'],
                        show['time'],
                        show['duration'],
                        show['description']
                    ) for show in data
                ]
            return True
        except FileNotFoundError:
            print("Schedule file not found. Starting with empty schedule.")
            return False
        except Exception as e:
            print(f"Error loading schedule: {e}")
            return False
    
    def print_schedule(self) -> None:
        """Print the current schedule."""
        if not self.shows:
            print("No shows scheduled.")
            return
        
        print("\nPuppetry Show Schedule:")
        print("----------------------")
        for show in sorted(self.shows, key=lambda x: (x.date, x.time)):
            print(show)
        print()


def main():
    """Main function to demonstrate the puppetry show schedule."""
    schedule = PuppetryShowSchedule()
    
    # Try to load existing schedule
    schedule.load_from_file("puppetry_schedule.json")
    
    # Add some sample shows if none exist
    if not schedule.shows:
        schedule.add_show(PuppetryShow(
            "The Magic Puppet",
            "2023-12-15",
            "14:00",
            60,
            "A magical adventure with puppets and illusions"
        ))
        schedule.add_show(PuppetryShow(
            "Forest Friends",
            "2023-12-16",
            "11:00",
            45,
            "Meet the animals of the enchanted forest"
        ))
        schedule.add_show(PuppetryShow(
            "Pirate Puppets",
            "2023-12-17",
            "16:30",
            50,
            "A swashbuckling puppet adventure on the high seas"
        ))
    
    # Print the schedule
    schedule.print_schedule()
    
    # Print upcoming shows
    print("\nUpcoming Shows (next 7 days):")
    for show in schedule.get_upcoming_shows():
        print(f"- {show}")
    
    # Save the schedule
    schedule.save_to_file("puppetry_schedule.json")


if __name__ == "__main__":
    main()
```
