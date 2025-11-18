"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Write a Python script to automate the generation of a school timetable for classes Nursery to XII based on the structure provided on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_5680f5cc2dcdbde3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

# Constants for the timetable generation
CLASSES = ["Nursery", "LKG", "UKG"] + [f"Class {i}" for i in range(1, 13)]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
PERIODS_PER_DAY = 7 # Number of periods in a school day
DEFAULT_SUBJECTS = {
    "Nursery": ["Rhymes", "Drawing", "Playtime"],
    "LKG": ["English", "Maths", "Drawing", "Storytelling"],
    "UKG": ["English", "Maths", "Science", "Storytelling"],
    "Class 1": ["English", "Maths", "Science", "Social Studies", "Drawing"],
    "Class 2": ["English", "Maths", "Science", "Social Studies", "Art"],
    "Class 3": ["English", "Maths", "Science", "Social Studies", "Art"],
    "Class 4": ["English", "Maths", "Science", "Social Studies", "Computer"],
    "Class 5": ["English", "Maths", "Science", "Social Studies", "Computer"],
    "Class 6": ["English", "Maths", "Science", "Social Studies", "Hindi"],
    "Class 7": ["English", "Maths", "Science", "Social Studies", "Hindi"],
    "Class 8": ["English", "Maths", "Science", "Social Studies", "Hindi"],
    "Class 9": ["English", "Maths", "Physics", "Chemistry", "Biology"],
    "Class 10": ["English", "Maths", "Physics", "Chemistry", "Biology"],
    "Class 11": ["English", "Maths", "Physics", "Chemistry", "Biology"],
    "Class 12": ["English", "Maths", "Physics", "Chemistry", "Biology"]
}

# Error handling for invalid inputs
def validate_inputs():
    if PERIODS_PER_DAY < 1 or PERIODS_PER_DAY > 10:
        raise ValueError("PERIODS_PER_DAY must be between 1 and 10.")

    if not CLASSES or not isinstance(CLASSES, list):
        raise ValueError("CLASSES must be a non-empty list.")

# Generate timetable for a single class
def generate_timetable_for_class(class_name, subjects):
    timetable = {}
    for day in DAYS:
        timetable[day] = []
        for period in range(PERIODS_PER_DAY):
            # Assign subjects to periods cyclically
            subject = subjects[period % len(subjects)]
            timetable[day].append(subject)
    return timetable

# Generate timetable for all classes
def generate_school_timetable():
    validate_inputs()
    school_timetable = {}
    for class_name in CLASSES:
        subjects = DEFAULT_SUBJECTS.get(class_name, ["English", "Maths"])
        school_timetable[class_name] = generate_timetable_for_class(class_name, subjects)
    return school_timetable

# Save timetable to a JSON file
def save_timetable_to_file(timetable, filename="school_timetable.json"):
    try:
        with open(filename, "w") as file:
            json.dump(timetable, file, indent=4)
        print(f"Timetable successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving timetable to file: {str(e)}")

# Main function to build and save the timetable
def main():
    print("Generating school timetable...")
    timetable = generate_school_timetable()
    save_timetable_to_file(timetable)

if __name__ == "__main__":
    main()
```
