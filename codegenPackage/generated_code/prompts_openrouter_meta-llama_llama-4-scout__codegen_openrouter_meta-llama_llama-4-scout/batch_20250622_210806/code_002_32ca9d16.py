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
from datetime import datetime, timedelta

class AcademicCalendar:
    def __init__(self, school_name):
        """
        Initialize the AcademicCalendar class.

        Args:
            school_name (str): The name of the school.
        """
        self.school_name = school_name
        self.calendar = []

    def add_event(self, date, event):
        """
        Add an event to the academic calendar.

        Args:
            date (datetime): The date of the event.
            event (str): The description of the event.
        """
        self.calendar.append((date, event))

    def add_holiday(self, date, holiday_name):
        """
        Add a holiday to the academic calendar.

        Args:
            date (datetime): The date of the holiday.
            holiday_name (str): The name of the holiday.
        """
        self.add_event(date, f"{holiday_name} - Holiday")

    def add_important_date(self, date, event):
        """
        Add an important date to the academic calendar.

        Args:
            date (datetime): The date of the event.
            event (str): The description of the event.
        """
        self.add_event(date, event)

    def print_calendar(self):
        """
        Print the academic calendar.
        """
        print(f"Academic Calendar for {self.school_name}:")
        self.calendar.sort(key=lambda x: x[0])
        for date, event in self.calendar:
            print(f"{date.strftime('%Y-%m-%d')}: {event}")


def main():
    try:
        # Create an academic calendar for Ideal High School
        ideal_high_school_calendar = AcademicCalendar("Ideal High School")

        # Add holidays
        ideal_high_school_calendar.add_holiday(datetime(2024, 9, 2), "Labor Day")
        ideal_high_school_calendar.add_holiday(datetime(2024, 10, 14), "Columbus Day")
        ideal_high_school_calendar.add_holiday(datetime(2024, 11, 11), "Veterans Day")
        ideal_high_school_calendar.add_holiday(datetime(2024, 11, 28), "Thanksgiving Day")
        ideal_high_school_calendar.add_holiday(datetime(2024, 12, 25), "Christmas Day")

        # Add important dates
        ideal_high_school_calendar.add_important_date(datetime(2024, 9, 1), "First Day of School")
        ideal_high_school_calendar.add_important_date(datetime(2024, 9, 15), "Parent-Teacher Conference")
        ideal_high_school_calendar.add_important_date(datetime(2024, 10, 1), "Midterm")
        ideal_high_school_calendar.add_important_date(datetime(2024, 11, 1), "College Application Deadline")
        ideal_high_school_calendar.add_important_date(datetime(2024, 12, 18), "Last Day of Semester")

        # Print the academic calendar
        ideal_high_school_calendar.print_calendar()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
