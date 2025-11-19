"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Generate a sample school timetable for classes I to XII, including separate sections for pre-primary, KG, and mid-term schedules.
Generated: DETERMINISTIC_ec1235b6b94a6c2e
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
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Subject:
    name: str
    teacher: str
    duration: int  # in minutes

@dataclass
class TimeSlot:
    start_time: str
    end_time: str
    subject: Subject

@dataclass
class DaySchedule:
    day: str
    time_slots: List[TimeSlot]

@dataclass
class ClassTimetable:
    class_name: str
    days: List[DaySchedule]

def generate_pre_primary_timetable() -> ClassTimetable:
    subjects = [
        Subject("Story Time", "Ms. Smith", 30),
        Subject("Art & Craft", "Ms. Johnson", 45),
        Subject("Music", "Mr. Davis", 30),
        Subject("Play Time", "Ms. Wilson", 45),
        Subject("Nap Time", "Ms. Brown", 60)
    ]
    
    days = []
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        time_slots = [
            TimeSlot("09:00", "09:30", subjects[0]),
            TimeSlot("09:30", "10:15", subjects[1]),
            TimeSlot("10:15", "10:45", subjects[2]),
            TimeSlot("11:00", "11:45", subjects[3]),
            TimeSlot("12:00", "13:00", subjects[4])
        ]
        days.append(DaySchedule(day, time_slots))
    
    return ClassTimetable("Pre-Primary", days)

def generate_kg_timetable() -> ClassTimetable:
    subjects = [
        Subject("English", "Ms. Taylor", 45),
        Subject("Math", "Mr. Clark", 45),
        Subject("EVS", "Ms. Adams", 45),
        Subject("Art", "Ms. Wilson", 45),
        Subject("Music", "Mr. Davis", 30),
        Subject("Physical Education", "Mr. White", 45)
    ]
    
    days = []
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        time_slots = [
            TimeSlot("09:00", "09:45", subjects[0]),
            TimeSlot("09:45", "10:30", subjects[1]),
            TimeSlot("10:45", "11:30", subjects[2]),
            TimeSlot("11:30", "12:15", subjects[3]),
            TimeSlot("12:15", "12:45", subjects[4]),
            TimeSlot("13:00", "13:45", subjects[5])
        ]
        days.append(DaySchedule(day, time_slots))
    
    return ClassTimetable("KG", days)

def generate_primary_timetable(class_name: str) -> ClassTimetable:
    subjects = [
        Subject("English", "Ms. Taylor", 45),
        Subject("Math", "Mr. Clark", 45),
        Subject("Science", "Ms. Adams", 45),
        Subject("Social Studies", "Mr. Brown", 45),
        Subject("Second Language", "Ms. Lee", 45),
        Subject("Computer Science", "Mr. Harris", 45),
        Subject("Physical Education", "Mr. White", 45),
        Subject("Art", "Ms. Wilson", 45),
        Subject("Music", "Mr. Davis", 45)
    ]
    
    days = []
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        time_slots = [
            TimeSlot("08:00", "08:45", subjects[0]),
            TimeSlot("08:45", "09:30", subjects[1]),
            TimeSlot("09:30", "10:15", subjects[2]),
            TimeSlot("10:30", "11:15", subjects[3]),
            TimeSlot("11:15", "12:00", subjects[4]),
            TimeSlot("12:00", "12:45", subjects[5]),
            TimeSlot("12:45", "13:30", subjects[6]),
            TimeSlot("13:30", "14:15", day != "Friday" and subjects[7] or subjects[8])
        ]
        days.append(DaySchedule(day, time_slots))
    
    return ClassTimetable(class_name, days)

def generate_secondary_timetable(class_name: str) -> ClassTimetable:
    subjects = [
        Subject("English", "Ms. Taylor", 45),
        Subject("Math", "Mr. Clark", 45),
        Subject("Physics", "Dr. Green", 45),
        Subject("Chemistry", "Dr. Black", 45),
        Subject("Biology", "Dr. Gray", 45),
        Subject("History", "Mr. Brown", 45),
        Subject("Geography", "Ms. King", 45),
        Subject("Computer Science", "Mr. Harris", 45),
        Subject("Physical Education", "Mr. White", 45),
        Subject("Elective", "Varies", 45)
    ]
    
    days = []
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        time_slots = [
            TimeSlot("08:00", "08:45", subjects[0]),
            TimeSlot("08:45", "09:30", subjects[1]),
            TimeSlot("09:30", "10:15", subjects[2]),
            TimeSlot("10:30", "11:15", subjects[3]),
            TimeSlot("11:15", "12:00", subjects[4]),
            TimeSlot("12:00", "12:45", subjects[5]),
            TimeSlot("12:45", "13:30", subjects[6]),
            TimeSlot("13:30", "14:15", subjects[7]),
            TimeSlot("14:15", "15:00", day == "Wednesday" and subjects[8] or subjects[9])
        ]
        days.append(DaySchedule(day, time_slots))
    
    return ClassTimetable(class_name, days)

def generate_mid_term_schedule() -> Dict[str, List[Dict[str, str]]]:
    return {
        "Mid-Term Schedule": [
            {"Day": "Monday", "Time": "09:00-12:00", "Subject": "English"},
            {"Day": "Tuesday", "Time": "09:00-12:00", "Subject": "Math"},
            {"Day": "Wednesday", "Time": "09:00-12:00", "Subject": "Science"},
            {"Day": "Thursday", "Time": "09:00-12:00", "Subject": "Social Studies"},
            {"Day": "Friday", "Time": "09:00-12:00", "Subject": "Second Language"}
        ]
    }

def timetable_to_dict(timetable: ClassTimetable) -> Dict:
    return {
        "class": timetable.class_name,
        "schedule": [
            {
                "day": day.day,
                "time_slots": [
                    {
                        "start_time": slot.start_time,
                        "end_time": slot.end_time,
                        "subject": slot.subject.name,
                        "teacher": slot.subject.teacher,
                        "duration": slot.subject.duration
                    } for slot in day.time_slots
                ]
            } for day in timetable.days
        ]
    }

def generate_full_timetable() -> Dict:
    full_timetable = {
        "Pre-Primary": timetable_to_dict(generate_pre_primary_timetable()),
        "KG": timetable_to_dict(generate_kg_timetable()),
        "Primary": {},
        "Secondary": {},
        "Mid-Term Schedule": generate_mid_term_schedule()["Mid-Term Schedule"]
    }
    
    for i in range(1, 6):
        full_timetable["Primary"][f"Class {i}"] = timetable_to_dict(generate_primary_timetable(f"Class {i}"))
    
    for i in range(6, 13):
        full_timetable["Secondary"][f"Class {i}"] = timetable_to_dict(generate_secondary_timetable(f"Class {i}"))
    
    return full_timetable

def save_timetable_to_json(timetable: Dict, filename: str = "school_timetable.json"):
    with open(filename, "w") as f:
        json.dump(timetable, f, indent=2)

if __name__ == "__main__":
    timetable = generate_full_timetable()
    save_timetable_to_json(timetable)
    print("School timetable generated successfully!")
```
