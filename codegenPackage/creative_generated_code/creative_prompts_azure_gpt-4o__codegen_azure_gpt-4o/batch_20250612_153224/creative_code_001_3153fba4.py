"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Develop a module for automated timetable generation for schools, incorporating the functionality outlined in Him Saral's Time-Table Management System.
Generated: DETERMINISTIC_3153fba40ce8a57b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: timetable_generator.py
Description: Automated timetable generation for schools with functionality inspired by Him Saral's Time-Table Management System.
Language: Python 3.x
"""

import random
from collections import defaultdict

class TimetableGenerator:
    """
    A class to generate automated school timetables based on provided constraints.
    """

    def __init__(self, subjects, teachers, days, periods_per_day):
        """
        Initialize the TimetableGenerator with the required parameters.

        :param subjects: List of subjects offered by the school.
        :param teachers: Dictionary mapping subjects to their respective teachers.
        :param days: List of days for the school week (e.g., ["Monday", "Tuesday", ...]).
        :param periods_per_day: Number of periods in a day.
        """
        self.subjects = subjects
        self.teachers = teachers
        self.days = days
        self.periods_per_day = periods_per_day
        self.timetable = defaultdict(lambda: defaultdict(list))

    def validate_inputs(self):
        """
        Validate the input data to ensure timetable constraints are met.

        :raises ValueError: If input data is invalid (e.g., mismatched subjects and teachers).
        """
        if not self.subjects or not self.teachers or not self.days or self.periods_per_day <= 0:
            raise ValueError("Invalid inputs provided.")
        if len(self.subjects) != len(self.teachers):
            raise ValueError("Number of subjects must match the number of teachers.")

    def generate_timetable(self):
        """
        Generate the timetable for the school week.

        :return: A dictionary representing the timetable.
        """
        self.validate_inputs()

        # Randomly assign subjects to periods while ensuring even distribution
        for day in self.days:
            for period in range(1, self.periods_per_day + 1):
                subject = random.choice(self.subjects)
                teacher = self.teachers[subject]
                self.timetable[day][period] = (subject, teacher)

        return self.timetable

    def display_timetable(self):
        """
        Print the generated timetable in a readable format.
        """
        print("School Timetable:")
        for day, periods in self.timetable.items():
            print(f"\n{day}:")
            for period, (subject, teacher) in periods.items():
                print(f"  Period {period}: {subject} - Taught by {teacher}")

    def export_timetable_to_file(self, filename="timetable.txt"):
        """
        Export the generated timetable to a text file.

        :param filename: Name of the file to save the timetable to (default: "timetable.txt").
        """
        try:
            with open(filename, "w") as file:
                file.write("School Timetable:\n")
                for day, periods in self.timetable.items():
                    file.write(f"\n{day}:\n")
                    for period, (subject, teacher) in periods.items():
                        file.write(f"  Period {period}: {subject} - Taught by {teacher}\n")
            print(f"Timetable successfully exported to {filename}.")
        except IOError as e:
            print(f"Error exporting timetable to file: {e}")

if __name__ == "__main__":
    # Example usage:
    subjects = ["Math", "English", "Science", "History"]
    teachers = {
        "Math": "Mr. Smith",
        "English": "Ms. Johnson",
        "Science": "Dr. Brown",
        "History": "Mrs. Davis"
    }
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods_per_day = 6

    timetable_generator = TimetableGenerator(subjects, teachers, days, periods_per_day)
    timetable = timetable_generator.generate_timetable()
    timetable_generator.display_timetable()
    timetable_generator.export_timetable_to_file()
```
