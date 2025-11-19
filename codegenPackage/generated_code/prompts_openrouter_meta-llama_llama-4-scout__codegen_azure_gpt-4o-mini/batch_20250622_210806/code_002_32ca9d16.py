"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Generate a sample academic calendar for a school like Ideal High School, including holidays and important dates.
Generated: DETERMINISTIC_32ca9d16bdae9818
Batch ID: 20250622_210806
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
        
        :param year: The academic year for the calendar.
        """
        self.year = year
        self.holidays: List[Dict[str, str]] = []
        self.important_dates: List[Dict[str, str]] = []

    def add_holiday(self, date: str, description: str):
        """
        Adds a holiday to the academic calendar.
        
        :param date: The date of the holiday in 'YYYY-MM-DD' format.
        :param description: A brief description of the holiday.
        """
        try:
            holiday_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            self.holidays.append({'date': holiday_date, 'description': description})
        except ValueError as e:
            print(f"Error adding holiday: {e}")

    def add_important_date(self, date: str, description: str):
        """
        Adds an important date to the academic calendar.
        
        :param date: The date of the important event in 'YYYY-MM-DD' format.
        :param description: A brief description of the important date.
        """
        try:
            important_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            self.important_dates.append({'date': important_date, 'description': description})
        except ValueError as e:
            print(f"Error adding important date: {e}")

    def display_calendar(self):
        """
        Displays the academic calendar with holidays and important dates.
        """
        print(f"Academic Calendar for {self.year}\n")
        print("Holidays:")
        for holiday in self.holidays:
            print(f"{holiday['date']}: {holiday['description']}")
        
        print("\nImportant Dates:")
        for important_date in self.important_dates:
            print(f"{important_date['date']}: {important_date['description']}")

# Example usage
if __name__ == "__main__":
    # Create an academic calendar for the year 2024
    calendar = AcademicCalendar(2024)

    # Adding holidays
    calendar.add_holiday('2024-01-01', 'New Year\'s Day')
    calendar.add_holiday('2024-05-27', 'Memorial Day')
    calendar.add_holiday('2024-07-04', 'Independence Day')
    calendar.add_holiday('2024-11-28', 'Thanksgiving Day')
    calendar.add_holiday('2024-12-25', 'Christmas Day')

    # Adding important dates
    calendar.add_important_date('2024-08-15', 'First Day of School')
    calendar.add_important_date('2024-11-01', 'Parent-Teacher Conferences')
    calendar.add_important_date('2024-06-05', 'Last Day of School')

    # Display the calendar
    calendar.display_calendar()
```
