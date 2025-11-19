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
from dataclasses import dataclass
from enum import Enum
from typing import List

class Day(Enum):
    """Enum for days of the week"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5

@dataclass
class Period:
    """Dataclass for a period"""
    time: str
    subject: str

@dataclass
class Timetable:
    """Dataclass for a timetable"""
    day: Day
    periods: List[Period]

class SchoolTimetable:
    """Class for school timetable"""
    def __init__(self):
        self.timetable = {
            "pre_primary": {},
            "kg": {},
            "classes": {}
        }

    def add_timetable(self, section: str, class_name: str, timetable: List[Timetable]):
        """Add timetable for a section and class"""
        if section not in self.timetable:
            raise ValueError("Invalid section")

        if section in ["pre_primary", "kg"]:
            self.timetable[section] = timetable
        else:
            if class_name not in self.timetable["classes"]:
                self.timetable["classes"][class_name] = []

            self.timetable["classes"][class_name] = timetable

    def print_timetable(self, section: str = None, class_name: str = None):
        """Print timetable for a section and class"""
        if section == "pre_primary":
            print("Pre-Primary Timetable:")
            for timetable in self.timetable["pre_primary"]:
                print(f"Day: {timetable.day.name}")
                for period in timetable.periods:
                    print(f"{period.time}: {period.subject}")
                print()
        elif section == "kg":
            print("KG Timetable:")
            for timetable in self.timetable["kg"]:
                print(f"Day: {timetable.day.name}")
                for period in timetable.periods:
                    print(f"{period.time}: {period.subject}")
                print()
        elif section == "classes":
            if class_name:
                print(f"Timetable for Class {class_name}:")
                for timetable in self.timetable["classes"].get(class_name, []):
                    print(f"Day: {timetable.day.name}")
                    for period in timetable.periods:
                        print(f"{period.time}: {period.subject}")
                    print()
            else:
                for class_name, timetables in self.timetable["classes"].items():
                    print(f"Timetable for Class {class_name}:")
                    for timetable in timetables:
                        print(f"Day: {timetable.day.name}")
                        for period in timetable.periods:
                            print(f"{period.time}: {period.subject}")
                        print()

    def mid_term_schedule(self, section: str, class_name: str = None):
        """Print mid-term schedule for a section and class"""
        if section in ["pre_primary", "kg"]:
            print(f"Mid-term schedule for {section.capitalize()} Section:")
            print("Assuming mid-term schedule is the same as regular schedule")
            if section == "pre_primary":
                for timetable in self.timetable["pre_primary"]:
                    print(f"Day: {timetable.day.name}")
                    for period in timetable.periods:
                        print(f"{period.time}: {period.subject}")
                    print()
            elif section == "kg":
                for timetable in self.timetable["kg"]:
                    print(f"Day: {timetable.day.name}")
                    for period in timetable.periods:
                        print(f"{period.time}: {period.subject}")
                    print()
        elif section == "classes":
            if class_name:
                print(f"Mid-term schedule for Class {class_name}:")
                for timetable in self.timetable["classes"].get(class_name, []):
                    print(f"Day: {timetable.day.name}")
                    for period in timetable.periods:
                        print(f"{period.time}: {period.subject}")
                    print()
            else:
                for class_name, timetables in self.timetable["classes"].items():
                    print(f"Mid-term schedule for Class {class_name}:")
                    for timetable in timetables:
                        print(f"Day: {timetable.day.name}")
                        for period in timetable.periods:
                            print(f"{period.time}: {period.subject}")
                        print()

def main():
    school_timetable = SchoolTimetable()

    # Pre-primary timetable
    pre_primary_timetable = [
        Timetable(Day.MONDAY, [Period("9:00-9:30", "Playtime"), Period("9:30-10:15", "English")]),
        Timetable(Day.TUESDAY, [Period("9:00-9:30", "Playtime"), Period("9:30-10:15", "Maths")]),
        Timetable(Day.WEDNESDAY, [Period("9:00-9:30", "Playtime"), Period("9:30-10:15", "Science")]),
        Timetable(Day.THURSDAY, [Period("9:00-9:30", "Playtime"), Period("9:30-10:15", "English")]),
        Timetable(Day.FRIDAY, [Period("9:00-9:30", "Playtime"), Period("9:30-10:15", "Maths")]),
    ]
    school_timetable.add_timetable("pre_primary", None, pre_primary_timetable)

    # KG timetable
    kg_timetable = [
        Timetable(Day.MONDAY, [Period("9:00-9:30", "Playtime"), Period("9:30-10:15", "English")]),
        Timetable(Day.TUESDAY, [Period("9:00-9:30", "Playtime"), Period("9:30-10:15", "Maths")]),
        Timetable(Day.WEDNESDAY, [Period("9:00-9:30", "Playtime"), Period("9:30-10:15", "Science")]),
        Timetable(Day.THURSDAY, [Period("9:00-9:30", "Playtime"), Period("9:30-10:15", "English")]),
        Timetable(Day.FRIDAY, [Period("9:00-9:30", "Playtime"), Period("9:30-10:15", "Maths")]),
    ]
    school_timetable.add_timetable("kg", None, kg_timetable)

    # Class I to XII timetable
    class_timetable = [
        Timetable(Day.MONDAY, [Period("9:00-9:45", "English"), Period("9:45-10:30", "Maths")]),
        Timetable(Day.TUESDAY, [Period("9:00-9:45", "Science"), Period("9:45-10:30", "English")]),
        Timetable(Day.WEDNESDAY, [Period("9:00-9:45", "Maths"), Period("9:45-10:30", "Science")]),
        Timetable(Day.THURSDAY, [Period("9:00-9:45", "English"), Period("9:45-10:30", "Maths")]),
        Timetable(Day.FRIDAY, [Period("9:00-9:45", "Science"), Period("9:45-10:30", "English")]),
    ]

    for i in range(1, 13):
        school_timetable.add_timetable("classes", f"Class {i}", class_timetable)

    school_timetable.print_timetable("pre_primary")
    school_timetable.print_timetable("kg")
    school_timetable.print_timetable("classes")

    school_timetable.mid_term_schedule("pre_primary")
    school_timetable.mid_term_schedule("kg")
    school_timetable.mid_term_schedule("classes", "Class 1")

if __name__ == "__main__":
    main()
```
