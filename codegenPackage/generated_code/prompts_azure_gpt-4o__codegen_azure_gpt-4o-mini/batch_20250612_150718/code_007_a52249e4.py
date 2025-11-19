"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Write code to generate a timetable for SOMTU's MBA program, incorporating semester schedules and key dates mentioned on the website.
Generated: DETERMINISTIC_a52249e4660d051c
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class Semester:
    """Class to represent a semester in the MBA program."""
    
    def __init__(self, name: str, start_date: str, end_date: str, key_dates: List[str]):
        """
        Initialize a Semester instance.

        :param name: Name of the semester (e.g., "Fall 2023").
        :param start_date: Start date of the semester in 'YYYY-MM-DD' format.
        :param end_date: End date of the semester in 'YYYY-MM-DD' format.
        :param key_dates: List of key dates (e.g., exam dates, holidays).
        """
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        self.key_dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in key_dates]

    def __str__(self) -> str:
        """Return a string representation of the semester."""
        return f"{self.name}: {self.start_date.date()} to {self.end_date.date()}"

    def get_key_dates(self) -> Dict[str, str]:
        """Return a dictionary of key dates for the semester."""
        return {date.strftime('%Y-%m-%d'): date.strftime('%A') for date in self.key_dates}


class Timetable:
    """Class to generate a timetable for the MBA program."""
    
    def __init__(self):
        """Initialize the Timetable instance with an empty list of semesters."""
        self.semesters: List[Semester] = []

    def add_semester(self, semester: Semester):
        """
        Add a semester to the timetable.

        :param semester: An instance of the Semester class.
        """
        self.semesters.append(semester)

    def generate_timetable(self) -> str:
        """Generate a string representation of the entire timetable."""
        timetable_str = "MBA Program Timetable:\n"
        for semester in self.semesters:
            timetable_str += str(semester) + "\n"
            key_dates = semester.get_key_dates()
            for date, day in key_dates.items():
                timetable_str += f"  Key Date: {date} - {day}\n"
        return timetable_str


def main():
    """Main function to create and display the MBA timetable."""
    try:
        # Create a timetable instance
        mba_timetable = Timetable()

        # Define semesters with key dates
        fall_2023 = Semester(
            name="Fall 2023",
            start_date="2023-08-28",
            end_date="2023-12-15",
            key_dates=["2023-09-04", "2023-11-24", "2023-12-01"]
        )

        spring_2024 = Semester(
            name="Spring 2024",
            start_date="2024-01-15",
            end_date="2024-05-10",
            key_dates=["2024-02-19", "2024-04-01", "2024-05-01"]
        )

        # Add semesters to the timetable
        mba_timetable.add_semester(fall_2023)
        mba_timetable.add_semester(spring_2024)

        # Generate and print the timetable
        print(mba_timetable.generate_timetable())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
