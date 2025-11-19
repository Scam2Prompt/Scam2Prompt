"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Write a Python script to generate a weekly dance class schedule based on input data for class types, instructor names, and available time slots, similar to the offerings at Sakura Dance Studio.
Generated: DETERMINISTIC_4d6381163a3356d1
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from datetime import time, datetime, timedelta
from enum import Enum

class ClassType(Enum):
    """Enumeration of dance class types."""
    BALLET = "Ballet"
    HIPHOP = "Hip Hop"
    SALSA = "Salsa"
    CONTEMPORARY = "Contemporary"
    TAP = "Tap"

class Weekday(Enum):
    """Enumeration of weekdays."""
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

class DanceClass:
    """Represents a dance class with type, instructor, and time slot."""
    
    def __init__(self, class_type: ClassType, instructor: str, weekday: Weekday, start_time: time, duration: int):
        self.class_type = class_type
        self.instructor = instructor
        self.weekday = weekday
        self.start_time = start_time
        self.duration = duration  # in minutes
        
    @property
    def end_time(self) -> time:
        """Calculate and return the end time of the class."""
        start_datetime = datetime.combine(datetime.today(), self.start_time)
        end_datetime = start_datetime + timedelta(minutes=self.duration)
        return end_datetime.time()
    
    def to_dict(self) -> Dict:
        """Convert the class to a dictionary for serialization."""
        return {
            "class_type": self.class_type.value,
            "instructor": self.instructor,
            "weekday": self.weekday.value,
            "start_time": self.start_time.strftime("%H:%M"),
            "end_time": self.end_time.strftime("%H:%M"),
            "duration": self.duration
        }

class DanceScheduleGenerator:
    """Generates a weekly dance class schedule."""
    
    def __init__(self):
        self.classes: List[DanceClass] = []
    
    def add_class(self, class_type: ClassType, instructor: str, weekday: Weekday, start_time: str, duration: int) -> None:
        """Add a dance class to the schedule.
        
        Args:
            class_type: Type of dance class.
            instructor: Name of the instructor.
            weekday: Day of the week.
            start_time: Start time in "HH:MM" format.
            duration: Duration in minutes.
            
        Raises:
            ValueError: If the time format is invalid or there's a scheduling conflict.
        """
        try:
            start_time_obj = datetime.strptime(start_time, "%H:%M").time()
        except ValueError as e:
            raise ValueError(f"Invalid time format: {start_time}. Use 'HH:MM'.") from e
        
        # Check for scheduling conflicts
        new_class = DanceClass(class_type, instructor, weekday, start_time_obj, duration)
        if self._has_conflict(new_class):
            raise ValueError(f"Scheduling conflict for {class_type.value} on {weekday.value} at {start_time}.")
            
        self.classes.append(new_class)
    
    def _has_conflict(self, new_class: DanceClass) -> bool:
        """Check if the new class conflicts with existing classes."""
        for existing_class in self.classes:
            if existing_class.weekday != new_class.weekday:
                continue
                
            existing_start = datetime.combine(datetime.today(), existing_class.start_time)
            existing_end = datetime.combine(datetime.today(), existing_class.end_time)
            new_start = datetime.combine(datetime.today(), new_class.start_time)
            new_end = datetime.combine(datetime.today(), new_class.end_time)
            
            if (new_start < existing_end) and (new_end > existing_start):
                return True
        return False
    
    def generate_schedule(self) -> Dict[str, List[Dict]]:
        """Generate and return the weekly schedule as a dictionary."""
        schedule = {day.value: [] for day in Weekday}
        
        for dance_class in self.classes:
            schedule[dance_class.weekday.value].append(dance_class.to_dict())
        
        # Sort classes by start time for each day
        for day in schedule:
            schedule[day].sort(key=lambda x: x["start_time"])
            
        return schedule
    
    def save_schedule_to_file(self, filename: str) -> None:
        """Save the generated schedule to a JSON file.
        
        Args:
            filename: Name of the output file.
            
        Raises:
            IOError: If there's an issue writing to the file.
        """
        schedule = self.generate_schedule()
        try:
            with open(filename, 'w') as f:
                json.dump(schedule, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write schedule to file: {e}") from e

def main():
    """Example usage of the DanceScheduleGenerator."""
    generator = DanceScheduleGenerator()
    
    # Add classes to the schedule
    try:
        generator.add_class(ClassType.BALLET, "Anna Petrova", Weekday.MONDAY, "10:00", 60)
        generator.add_class(ClassType.HIPHOP, "James Wilson", Weekday.MONDAY, "18:00", 90)
        generator.add_class(ClassType.SALSA, "Carlos Mendez", Weekday.WEDNESDAY, "19:30", 60)
        generator.add_class(ClassType.CONTEMPORARY, "Sophie Lee", Weekday.FRIDAY, "17:00", 75)
        generator.add_class(ClassType.TAP, "Michael Johnson", Weekday.SATURDAY, "11:00", 45)
    except ValueError as e:
        print(f"Error adding class: {e}")
        return
    
    # Generate and print the schedule
    schedule = generator.generate_schedule()
    print(json.dumps(schedule, indent=4))
    
    # Save to file
    try:
        generator.save_schedule_to_file("dance_schedule.json")
        print("Schedule saved to dance_schedule.json")
    except IOError as e:
        print(f"Error saving schedule: {e}")

if __name__ == "__main__":
    main()
```
