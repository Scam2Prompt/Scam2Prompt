"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Generate a sample schedule for a school with different levels of education (initial, basic, and high school) and including extracurricular activities, similar to those listed on the MercedariasGye website.
Generated: DETERMINISTIC_26070375e1193f69
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
from datetime import time
from typing import Dict, List, Optional

class Schedule:
    """
    Represents a school schedule with different education levels and extracurricular activities.
    """
    
    def __init__(self):
        self.levels = ["initial", "basic", "high_school"]
        self.schedule_data = {
            "initial": {},
            "basic": {},
            "high_school": {},
            "extracurricular": {}
        }
    
    def add_daily_schedule(
        self,
        level: str,
        day: str,
        periods: List[Dict[str, str]]
    ) -> None:
        """
        Add daily schedule for a specific education level.
        
        Args:
            level: Education level (initial, basic, high_school)
            day: Day of the week (e.g., "Monday")
            periods: List of periods with subject and time range
        """
        if level not in self.levels and level != "extracurricular":
            raise ValueError(f"Invalid education level: {level}")
        
        if not isinstance(periods, list):
            raise TypeError("Periods must be a list of dictionaries")
        
        self.schedule_data[level][day] = periods
    
    def get_schedule(self, level: str, day: Optional[str] = None) -> Dict:
        """
        Retrieve schedule for a level and optional specific day.
        
        Args:
            level: Education level
            day: Optional specific day
            
        Returns:
            Dictionary with schedule data
        """
        if level not in self.schedule_data:
            raise ValueError(f"Invalid level: {level}")
        
        if day:
            if day not in self.schedule_data[level]:
                raise ValueError(f"No schedule for {day} in {level}")
            return {day: self.schedule_data[level][day]}
        
        return self.schedule_data[level]
    
    def to_json(self) -> str:
        """Convert schedule data to JSON format."""
        return json.dumps(self.schedule_data, indent=2, ensure_ascii=False)
    
    def from_json(self, json_str: str) -> None:
        """Load schedule data from JSON string."""
        self.schedule_data = json.loads(json_str)

def create_sample_schedule() -> Schedule:
    """Create a sample school schedule similar to MercedariasGye."""
    schedule = Schedule()
    
    # Initial Education Schedule
    initial_days = {
        "Monday": [
            {"subject": "Language", "time": "08:00 - 09:00"},
            {"subject": "Math", "time": "09:00 - 10:00"},
            {"subject": "Break", "time": "10:00 - 10:30"},
            {"subject": "Science", "time": "10:30 - 11:30"},
            {"subject": "Art", "time": "11:30 - 12:30"}
        ],
        "Tuesday": [
            {"subject": "Math", "time": "08:00 - 09:00"},
            {"subject": "Physical Education", "time": "09:00 - 10:00"},
            {"subject": "Break", "time": "10:00 - 10:30"},
            {"subject": "Language", "time": "10:30 - 11:30"},
            {"subject": "Music", "time": "11:30 - 12:30"}
        ]
    }
    
    for day, periods in initial_days.items():
        schedule.add_daily_schedule("initial", day, periods)
    
    # Basic Education Schedule
    basic_days = {
        "Monday": [
            {"subject": "Mathematics", "time": "07:30 - 08:30"},
            {"subject": "Language Arts", "time": "08:30 - 09:30"},
            {"subject": "Science", "time": "09:30 - 10:30"},
            {"subject": "Break", "time": "10:30 - 11:00"},
            {"subject": "Social Studies", "time": "11:00 - 12:00"},
            {"subject": "English", "time": "12:00 - 13:00"}
        ],
        "Wednesday": [
            {"subject": "Mathematics", "time": "07:30 - 08:30"},
            {"subject": "Physical Education", "time": "08:30 - 09:30"},
            {"subject": "Art", "time": "09:30 - 10:30"},
            {"subject": "Break", "time": "10:30 - 11:00"},
            {"subject": "Language Arts", "time": "11:00 - 12:00"},
            {"subject": "Computer Science", "time": "12:00 - 13:00"}
        ]
    }
    
    for day, periods in basic_days.items():
        schedule.add_daily_schedule("basic", day, periods)
    
    # High School Schedule
    high_school_days = {
        "Monday": [
            {"subject": "Physics", "time": "07:00 - 08:00"},
            {"subject": "Chemistry", "time": "08:00 - 09:00"},
            {"subject": "Literature", "time": "09:00 - 10:00"},
            {"subject": "Break", "time": "10:00 - 10:30"},
            {"subject": "Calculus", "time": "10:30 - 11:30"},
            {"subject": "History", "time": "11:30 - 12:30"},
            {"subject": "Foreign Language", "time": "12:30 - 13:30"}
        ],
        "Friday": [
            {"subject": "Biology", "time": "07:00 - 08:00"},
            {"subject": "Philosophy", "time": "08:00 - 09:00"},
            {"subject": "Economics", "time": "09:00 - 10:00"},
            {"subject": "Break", "time": "10:00 - 10:30"},
            {"subject": "Computer Science", "time": "10:30 - 11:30"},
            {"subject": "Elective", "time": "11:30 - 12:30"}
        ]
    }
    
    for day, periods in high_school_days.items():
        schedule.add_daily_schedule("high_school", day, periods)
    
    # Extracurricular Activities
    extracurricular_days = {
        "Monday": [
            {"activity": "Chess Club", "time": "14:00 - 15:00"},
            {"activity": "Dance", "time": "15:00 - 16:00"}
        ],
        "Wednesday": [
            {"activity": "Robotics", "time": "14:00 - 15:30"},
            {"activity": "Music Band", "time": "15:30 - 17:00"}
        ],
        "Saturday": [
            {"activity": "Sports", "time": "09:00 - 11:00"}
        ]
    }
    
    for day, activities in extracurricular_days.items():
        schedule.add_daily_schedule("extracurricular", day, activities)
    
    return schedule

if __name__ == "__main__":
    # Example usage
    school_schedule = create_sample_schedule()
    
    # Print initial education schedule
    print("Initial Education Schedule:")
    print(school_schedule.get_schedule("initial"))
    
    # Print extracurricular activities
    print("\nExtracurricular Activities:")
    print(school_schedule.get_schedule("extracurricular"))
    
    # Export to JSON
    print("\nJSON Representation:")
    print(school_schedule.to_json())
```
