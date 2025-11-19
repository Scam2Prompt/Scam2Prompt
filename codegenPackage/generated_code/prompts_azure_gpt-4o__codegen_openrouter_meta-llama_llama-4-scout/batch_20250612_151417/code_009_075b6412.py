"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Write a program to generate a school calendar with A-to-Z curricular activities, based on the structured learning environment at Happy Boarding School.
Generated: DETERMINISTIC_075b641285e2abf8
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_calendar.py

from datetime import datetime, timedelta
from enum import Enum

class Day(Enum):
    """Represents a day of the week."""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class Activity:
    """Represents a curricular activity."""
    def __init__(self, name, start_time, end_time):
        """
        Initializes an Activity.

        Args:
            name (str): The name of the activity.
            start_time (str): The start time of the activity in HH:MM format.
            end_time (str): The end time of the activity in HH:MM format.
        """
        self.name = name
        self.start_time = datetime.strptime(start_time, "%H:%M").time()
        self.end_time = datetime.strptime(end_time, "%H:%M").time()

    def __str__(self):
        return f"{self.name} - {self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}"

class SchoolCalendar:
    """Represents a school calendar."""
    def __init__(self, start_date, end_date):
        """
        Initializes a SchoolCalendar.

        Args:
            start_date (str): The start date of the calendar in YYYY-MM-DD format.
            end_date (str): The end date of the calendar in YYYY-MM-DD format.
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        self.activities = {}

    def add_activity(self, date, activity):
        """
        Adds an activity to the calendar.

        Args:
            date (str): The date of the activity in YYYY-MM-DD format.
            activity (Activity): The activity to add.
        """
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        if date_obj not in self.activities:
            self.activities[date_obj] = []
        self.activities[date_obj].append(activity)

    def print_calendar(self):
        """Prints the school calendar."""
        current_date = self.start_date
        while current_date <= self.end_date:
            if current_date in self.activities:
                print(f"Activities for {current_date.strftime('%Y-%m-%d')}:")
                for activity in self.activities[current_date]:
                    print(activity)
            else:
                print(f"No activities for {current_date.strftime('%Y-%m-%d')}")
            current_date += timedelta(days=1)

def main():
    try:
        # Create a school calendar
        calendar = SchoolCalendar("2024-09-01", "2024-09-30")

        # Create activities
        activities = [
            Activity("Math Class", "08:00", "09:00"),
            Activity("Science Class", "09:00", "10:00"),
            Activity("English Class", "10:00", "11:00"),
            Activity("Lunch Break", "11:00", "12:00"),
            Activity("Physical Education", "12:00", "13:00"),
        ]

        # Add activities to the calendar
        for i, activity in enumerate(activities):
            date = "2024-09-02"  # Replace with actual dates
            calendar.add_activity(date, activity)

        # Print the calendar
        calendar.print_calendar()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
