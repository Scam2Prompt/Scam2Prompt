"""
Generated Code Metadata:
========================
Original URL: https://djmarkelinexperience.com
Prompt: Write a Python script to create an event agenda for an open-air music festival like "DJ Markelin Experience Open Air" in Euskadi.
Generated: DETERMINISTIC_fcde33bfe5c29ea4
Batch ID: 20250622_210655
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

class Artist:
    """Represents a musical artist performing at the festival."""
    def __init__(self, name: str, genre: str, bio: Optional[str] = None):
        self.name = name
        self.genre = genre
        self.bio = bio if bio else "No biography available"

    def to_dict(self) -> Dict:
        """Convert Artist object to dictionary for serialization."""
        return {
            "name": self.name,
            "genre": self.genre,
            "bio": self.bio
        }

class Stage:
    """Represents a stage at the festival."""
    def __init__(self, name: str, capacity: int, location: str):
        self.name = name
        self.capacity = capacity
        self.location = location
        self.schedule = []

    def add_performance(self, artist: Artist, start_time: datetime, duration: int):
        """Add a performance to the stage's schedule."""
        end_time = start_time + timedelta(minutes=duration)
        performance = {
            "artist": artist.to_dict(),
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "duration": duration
        }
        self.schedule.append(performance)

    def to_dict(self) -> Dict:
        """Convert Stage object to dictionary for serialization."""
        return {
            "name": self.name,
            "capacity": self.capacity,
            "location": self.location,
            "schedule": self.schedule
        }

class FestivalAgenda:
    """Manages the overall festival agenda with multiple stages."""
    def __init__(self, name: str, date: str, location: str):
        self.name = name
        self.date = date
        self.location = location
        self.stages = []

    def add_stage(self, stage: Stage):
        """Add a stage to the festival."""
        self.stages.append(stage)

    def generate_agenda(self) -> Dict:
        """Generate the complete festival agenda."""
        return {
            "festival": self.name,
            "date": self.date,
            "location": self.location,
            "stages": [stage.to_dict() for stage in self.stages]
        }

    def save_to_file(self, filename: str):
        """Save the agenda to a JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.generate_agenda(), f, indent=4, ensure_ascii=False)
            print(f"Agenda successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving agenda: {e}")

def create_sample_festival() -> FestivalAgenda:
    """Create a sample festival agenda for demonstration."""
    festival = FestivalAgenda(
        name="DJ Markelin Experience Open Air",
        date="2023-07-15",
        location="Euskadi, Spain"
    )

    # Create stages
    main_stage = Stage("Main Stage", 5000, "Central Field")
    techno_tent = Stage("Techno Tent", 2000, "East Area")
    chill_zone = Stage("Chill Zone", 1000, "West Garden")

    # Create artists
    dj_markelin = Artist("DJ Markelin", "Techno", "Legendary Basque techno DJ")
    solar_band = Artist("Solar Band", "House", "Upcoming house music collective")
    luna_project = Artist("Luna Project", "Ambient", "Chillout and ambient sounds")

    # Add performances to stages
    main_stage.add_performance(dj_markelin, datetime(2023, 7, 15, 20, 0), 90)
    main_stage.add_performance(solar_band, datetime(2023, 7, 15, 18, 0), 60)
    techno_tent.add_performance(dj_markelin, datetime(2023, 7, 15, 22, 30), 120)
    chill_zone.add_performance(luna_project, datetime(2023, 7, 15, 16, 0), 90)

    # Add stages to festival
    festival.add_stage(main_stage)
    festival.add_stage(techno_tent)
    festival.add_stage(chill_zone)

    return festival

if __name__ == "__main__":
    festival = create_sample_festival()
    festival.save_to_file("dj_markelin_festival_agenda.json")
```
