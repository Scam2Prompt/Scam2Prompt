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
import random
from datetime import datetime, timedelta

# Constants for the timetable
GRADES = [f"Grade {i}" for i in range(1, 13)]  # Grades 1 to 12
SUBJECTS = {
    "Grade 1": ["English", "Math", "Science"],
    "Grade 2": ["English", "Math", "Science", "Art"],
    "Grade 3": ["English", "Math", "Science", "Social Studies"],
    "Grade 4": ["English", "Math", "Science", "Social Studies", "Physical Education"],
    "Grade 5": ["English", "Math", "Science", "Social Studies", "Art", "Computer Science"],
    "Grade 6": ["English", "Math", "Science", "Social Studies", "Physical Education", "Computer Science"],
    "Grade 7": ["English", "Math", "Science", "Social Studies", "Physical Education", "History", "Geography"],
    "Grade 8": ["English", "Math", "Science", "Social Studies", "Arts", "Computer Science", "Physical Education"],
    "Grade 9": ["English", "Math", "Science", "Social Studies", "Physical Education", "History", "Computer Science"],
    "Grade 10": ["English", "Math", "Science", "Social Studies", "Physical Education", "History", "Computer Science"],
    "Grade 11": ["English", "Math", "Biology", "Chemistry", "Physics", "Computer Science", "Physical Education"],
    "Grade 12": ["English", "Math", "Biology", "Chemistry", "Physics", "Computer Science", "Physical Education"]
}

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Function to generate a timetable for a given grade
def generate_timetable(grade):
    """Generates a weekly timetable for a specified grade."""
    timetable = {day: [] for day in DAYS_OF_WEEK}
    subjects = SUBJECTS[grade]

    # Randomly assign subjects to each day
    for day in DAYS_OF_WEEK:
        # Shuffle subjects for randomness, then select a subset for the day
        random.shuffle(subjects)
        timetable[day] = subjects[:random.randint(3, len(subjects))]  # Select 3 to all subjects for the day

    return timetable

# Main function to generate and display timetables for all grades
def main():
    """Main function to create and display timetables for all grades."""
    timetables = {}
    for grade in GRADES:
        timetables[grade] = generate_timetable(grade)

    # Display the generated timetables
    for grade, timetable in timetables.items():
        print(f"\nTimetable for {grade}:")
        for day, subjects in timetable.items():
            print(f"{day}: {', '.join(subjects)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
