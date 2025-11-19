"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: What code can I write to automate the generation of academic calendars for pharmacy programs, inspired by the DBCOP academic structure?
Generated: DETERMINISTIC_3d6ff4aadc957173
Batch ID: 20250612_164010
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

class AcademicCalendar:
    def __init__(self, year: int):
        """
        Initializes the AcademicCalendar with the specified year.
        
        :param year: The academic year for which the calendar is generated.
        """
        self.year = year
        self.semesters = []

    def add_semester(self, name: str, start_date: str, end_date: str, holidays: List[str]):
        """
        Adds a semester to the academic calendar.
        
        :param name: The name of the semester (e.g., "Fall", "Spring").
        :param start_date: The start date of the semester in 'YYYY-MM-DD' format.
        :param end_date: The end date of the semester in 'YYYY-MM-DD' format.
        :param holidays: A list of holidays during the semester in 'YYYY-MM-DD' format.
        """
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            self.semesters.append({
                'name': name,
                'start_date': start,
                'end_date': end,
                'holidays': [datetime.datetime.strptime(holiday, '%Y-%m-%d') for holiday in holidays]
            })
        except ValueError as e:
            print(f"Error adding semester '{name}': {e}")

    def generate_calendar(self) -> Dict[str, List[Dict]]:
        """
        Generates the academic calendar as a dictionary.
        
        :return: A dictionary representation of the academic calendar.
        """
        calendar = {
            'year': self.year,
            'semesters': self.semesters
        }
        return calendar

    def display_calendar(self):
        """
        Displays the academic calendar in a readable format.
        """
        print(f"Academic Calendar for Year: {self.year}")
        for semester in self.semesters:
            print(f"Semester: {semester['name']}")
            print(f"  Start Date: {semester['start_date'].date()}")
            print(f"  End Date: {semester['end_date'].date()}")
            print(f"  Holidays: {', '.join(holiday.date().isoformat() for holiday in semester['holidays'])}")
            print()

# Example usage
if __name__ == "__main__":
    # Create an instance of AcademicCalendar for the year 2024
    academic_calendar = AcademicCalendar(year=2024)

    # Add semesters to the academic calendar
    academic_calendar.add_semester(
        name="Fall",
        start_date="2024-08-25",
        end_date="2024-12-15",
        holidays=["2024-09-02", "2024-11-28", "2024-11-29"]
    )
    
    academic_calendar.add_semester(
        name="Spring",
        start_date="2025-01-10",
        end_date="2025-05-15",
        holidays=["2025-01-20", "2025-04-21"]
    )

    # Generate and display the academic calendar
    calendar = academic_calendar.generate_calendar()
    academic_calendar.display_calendar()
```
