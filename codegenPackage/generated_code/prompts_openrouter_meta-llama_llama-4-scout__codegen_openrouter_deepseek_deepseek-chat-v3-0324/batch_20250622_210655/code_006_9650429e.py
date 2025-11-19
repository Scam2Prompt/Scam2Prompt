"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: "Write a code snippet in a suitable programming language to implement a time-table management system for schools, similar to Him Saral's time-table module."
Generated: DETERMINISTIC_9650429e56a9fc68
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
School Timetable Management System
"""

import json
from datetime import datetime, time
from typing import List, Dict, Optional, Union

class Subject:
    """Represents a subject taught in school"""
    def __init__(self, subject_id: str, name: str, teacher: str):
        self.subject_id = subject_id
        self.name = name
        self.teacher = teacher

    def __repr__(self):
        return f"Subject({self.subject_id}, {self.name}, {self.teacher})"

class TimeSlot:
    """Represents a time slot in the timetable"""
    def __init__(self, start_time: time, end_time: time):
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"TimeSlot({self.start_time}, {self.end_time})"

class TimetableEntry:
    """Represents a single entry in the timetable"""
    def __init__(self, day: str, time_slot: TimeSlot, subject: Subject, classroom: str):
        self.day = day
        self.time_slot = time_slot
        self.subject = subject
        self.classroom = classroom

    def __repr__(self):
        return (f"TimetableEntry({self.day}, {self.time_slot}, "
                f"{self.subject}, {self.classroom})")

class Timetable:
    """Main timetable management class"""
    def __init__(self):
        self.entries: List[TimetableEntry] = []
        self.subjects: Dict[str, Subject] = {}
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def add_subject(self, subject_id: str, name: str, teacher: str) -> None:
        """Add a new subject to the system"""
        if subject_id in self.subjects:
            raise ValueError(f"Subject with ID {subject_id} already exists")
        self.subjects[subject_id] = Subject(subject_id, name, teacher)

    def add_entry(self, day: str, start_time: time, end_time: time,
                 subject_id: str, classroom: str) -> None:
        """Add a new timetable entry"""
        if day not in self.days:
            raise ValueError(f"Invalid day: {day}")
        
        if subject_id not in self.subjects:
            raise ValueError(f"Subject with ID {subject_id} not found")
        
        time_slot = TimeSlot(start_time, end_time)
        if self._check_conflict(day, time_slot, classroom):
            raise ValueError("Time slot conflict detected")
            
        entry = TimetableEntry(day, time_slot, self.subjects[subject_id], classroom)
        self.entries.append(entry)

    def _check_conflict(self, day: str, time_slot: TimeSlot, classroom: str) -> bool:
        """Check for scheduling conflicts"""
        for entry in self.entries:
            if entry.day == day:
                if entry.classroom == classroom and self._time_overlap(entry.time_slot, time_slot):
                    return True
        return False

    @staticmethod
    def _time_overlap(slot1: TimeSlot, slot2: TimeSlot) -> bool:
        """Check if two time slots overlap"""
        return (slot1.start_time < slot2.end_time and 
                slot1.end_time > slot2.start_time)

    def get_daily_schedule(self, day: str) -> List[TimetableEntry]:
        """Get all entries for a specific day"""
        return [entry for entry in self.entries if entry.day == day]

    def get_teacher_schedule(self, teacher_name: str) -> List[TimetableEntry]:
        """Get all entries for a specific teacher"""
        return [entry for entry in self.entries 
                if entry.subject.teacher == teacher_name]

    def save_to_file(self, filename: str) -> None:
        """Save timetable to JSON file"""
        data = {
            "subjects": {sid: {"name": sub.name, "teacher": sub.teacher} 
                        for sid, sub in self.subjects.items()},
            "entries": [
                {
                    "day": entry.day,
                    "start_time": entry.time_slot.start_time.strftime("%H:%M"),
                    "end_time": entry.time_slot.end_time.strftime("%H:%M"),
                    "subject_id": entry.subject.subject_id,
                    "classroom": entry.classroom
                }
                for entry in self.entries
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str) -> None:
        """Load timetable from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.subjects = {}
        for sid, sub_data in data["subjects"].items():
            self.subjects[sid] = Subject(sid, sub_data["name"], sub_data["teacher"])
        
        self.entries = []
        for entry_data in data["entries"]:
            start_time = datetime.strptime(entry_data["start_time"], "%H:%M").time()
            end_time = datetime.strptime(entry_data["end_time"], "%H:%M").time()
            time_slot = TimeSlot(start_time, end_time)
            subject = self.subjects[entry_data["subject_id"]]
            self.entries.append(
                TimetableEntry(
                    entry_data["day"],
                    time_slot,
                    subject,
                    entry_data["classroom"]
                )
            )

# Example usage
if __name__ == "__main__":
    tt = Timetable()
    
    # Add subjects
    tt.add_subject("MATH101", "Mathematics", "Dr. Smith")
    tt.add_subject("PHY101", "Physics", "Dr. Johnson")
    tt.add_subject("CHEM101", "Chemistry", "Dr. Williams")
    
    # Add timetable entries
    try:
        tt.add_entry("Monday", time(9, 0), time(10, 0), "MATH101", "Room 101")
        tt.add_entry("Monday", time(10, 0), time(11, 0), "PHY101", "Room 102")
        tt.add_entry("Tuesday", time(9, 0), time(10, 0), "CHEM101", "Room 101")
        
        # Save to file
        tt.save_to_file("timetable.json")
        
        # Load from file
        new_tt = Timetable()
        new_tt.load_from_file("timetable.json")
        print("Monday schedule:")
        for entry in new_tt.get_daily_schedule("Monday"):
            print(f"{entry.time_slot.start_time}-{entry.time_slot.end_time}: "
                  f"{entry.subject.name} ({entry.classroom})")
    
    except ValueError as e:
        print(f"Error: {e}")
```
