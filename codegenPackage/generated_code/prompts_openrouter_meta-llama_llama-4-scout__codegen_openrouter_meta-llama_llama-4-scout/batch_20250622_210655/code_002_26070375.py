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
from dataclasses import dataclass
from enum import Enum
from typing import List

class EducationLevel(Enum):
    """Enum for education levels"""
    INITIAL = "Initial"
    BASIC = "Basic"
    HIGH_SCHOOL = "High School"

@dataclass
class ScheduleItem:
    """Dataclass for schedule items"""
    name: str
    start_time: str
    end_time: str

class SchoolSchedule:
    """Class for school schedule"""
    def __init__(self, education_level: EducationLevel):
        self.education_level = education_level
        self.schedule = []

    def add_schedule_item(self, item: ScheduleItem):
        """Add schedule item to the schedule"""
        self.schedule.append(item)

    def print_schedule(self):
        """Print the schedule"""
        print(f"Schedule for {self.education_level.value}:")
        for item in self.schedule:
            print(f"{item.start_time} - {item.end_time}: {item.name}")

def generate_sample_schedule(education_level: EducationLevel) -> SchoolSchedule:
    """Generate a sample schedule for a given education level"""
    schedule = SchoolSchedule(education_level)

    if education_level == EducationLevel.INITIAL:
        schedule.add_schedule_item(ScheduleItem("Welcome and morning routine", "08:00", "08:30"))
        schedule.add_schedule_item(ScheduleItem("Language and Literacy", "08:30", "09:15"))
        schedule.add_schedule_item(ScheduleItem("Math and Logic", "09:15", "10:00"))
        schedule.add_schedule_item(ScheduleItem("Recess", "10:00", "10:30"))
        schedule.add_schedule_item(ScheduleItem("Art and Music", "10:30", "11:15"))
        schedule.add_schedule_item(ScheduleItem("Lunch", "11:15", "12:00"))
        schedule.add_schedule_item(ScheduleItem("Outdoor activities", "12:00", "13:00"))
    elif education_level == EducationLevel.BASIC:
        schedule.add_schedule_item(ScheduleItem("Welcome and morning routine", "08:00", "08:30"))
        schedule.add_schedule_item(ScheduleItem("Language and Literature", "08:30", "09:15"))
        schedule.add_schedule_item(ScheduleItem("Math and Science", "09:15", "10:00"))
        schedule.add_schedule_item(ScheduleItem("Recess", "10:00", "10:30"))
        schedule.add_schedule_item(ScheduleItem("Social Studies and History", "10:30", "11:15"))
        schedule.add_schedule_item(ScheduleItem("Lunch", "11:15", "12:00"))
        schedule.add_schedule_item(ScheduleItem("Electives (Art, Music, etc.)", "12:00", "13:00"))
    elif education_level == EducationLevel.HIGH_SCHOOL:
        schedule.add_schedule_item(ScheduleItem("Welcome and morning routine", "08:00", "08:30"))
        schedule.add_schedule_item(ScheduleItem("Math and Science", "08:30", "09:15"))
        schedule.add_schedule_item(ScheduleItem("Language and Literature", "09:15", "10:00"))
        schedule.add_schedule_item(ScheduleItem("Recess", "10:00", "10:30"))
        schedule.add_schedule_item(ScheduleItem("Social Studies and History", "10:30", "11:15"))
        schedule.add_schedule_item(ScheduleItem("Electives (Art, Music, etc.)", "11:15", "12:00"))
        schedule.add_schedule_item(ScheduleItem("Lunch", "12:00", "13:00"))
        schedule.add_schedule_item(ScheduleItem("Extracurricular activities (Sports, Clubs, etc.)", "13:00", "14:00"))

    # Extracurricular activities
    schedule.add_schedule_item(ScheduleItem("Chess Club", "14:00", "15:00"))
    schedule.add_schedule_item(ScheduleItem("Drama Club", "15:00", "16:00"))
    schedule.add_schedule_item(ScheduleItem("Sports (Soccer, Basketball, etc.)", "16:00", "17:00"))

    return schedule

def main():
    try:
        initial_schedule = generate_sample_schedule(EducationLevel.INITIAL)
        basic_schedule = generate_sample_schedule(EducationLevel.BASIC)
        high_school_schedule = generate_sample_schedule(EducationLevel.HIGH_SCHOOL)

        initial_schedule.print_schedule()
        print("\n")
        basic_schedule.print_schedule()
        print("\n")
        high_school_schedule.print_schedule()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
