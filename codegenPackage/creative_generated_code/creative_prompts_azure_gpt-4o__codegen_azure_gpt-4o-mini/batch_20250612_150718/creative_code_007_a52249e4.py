"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Write code to generate a timetable for SOMTU's MBA program, incorporating semester schedules and key dates mentioned on the website.
Generated: DETERMINISTIC_a52249e4660d051c
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class Semester:
    """Class to represent a semester in an academic program."""
    
    def __init__(self, name: str, start_date: str, end_date: str, key_dates: List[str]):
        """
        Initializes a Semester instance.

        :param name: The name of the semester (e.g., "Fall 2023").
        :param start_date: The start date of the semester in YYYY-MM-DD format.
        :param end_date: The end date of the semester in YYYY-MM-DD format.
        :param key_dates: A list of key dates relevant to the semester.
        """
        self.name = name
        self.start_date = self.parse_date(start_date)
        self.end_date = self.parse_date(end_date)
        self.key_dates = key_dates

    @staticmethod
    def parse_date(date_str: str) -> datetime.date:
        """Parses a date string into a datetime.date object."""
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Invalid date format for '{date_str}': {e}")

    def display_schedule(self) -> Dict[str, str]:
        """Displays the semester schedule including key dates."""
        schedule = {
            "Semester": self.name,
            "Start Date": str(self.start_date),
            "End Date": str(self.end_date),
            "Key Dates": ', '.join(self.key_dates)
        }
        return schedule


class MBAProgram:
    """Class to represent the MBA program timetable."""
    
    def __init__(self):
        """Initializes the MBAProgram with its semesters."""
        self.semesters: List[Semester] = []
        self.create_schedule()

    def create_schedule(self):
        """Creates the semester schedule for the MBA program."""
        # Sample key dates for illustration purposes
        fall_key_dates = [
            "Orientation: 2023-08-15",
            "Midterm Exams: 2023-10-20",
            "Final Exams: 2023-12-15"
        ]
        
        spring_key_dates = [
            "Orientation: 2024-01-10",
            "Midterm Exams: 2024-03-15",
            "Final Exams: 2024-05-10"
        ]

        # Adding semesters to the program
        self.semesters.append(Semester("Fall 2023", "2023-08-15", "2023-12-15", fall_key_dates))
        self.semesters.append(Semester("Spring 2024", "2024-01-10", "2024-05-10", spring_key_dates))

    def display_timetable(self):
        """Displays the full timetable for the MBA program."""
        for semester in self.semesters:
            schedule = semester.display_schedule()
            print(f"--- {schedule['Semester']} ---")
            print(f"Start Date: {schedule['Start Date']}")
            print(f"End Date: {schedule['End Date']}")
            print(f"Key Dates: {schedule['Key Dates']}")
            print("\n")


if __name__ == "__main__":
    try:
        mba_program = MBAProgram()
        mba_program.display_timetable()
    except Exception as e:
        print(f"An error occurred: {e}")
```
