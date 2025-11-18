"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Write a program to generate a school calendar with A-to-Z curricular activities, based on the structured learning environment at Happy Boarding School.
Generated: DETERMINISTIC_075b641285e2abf8
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class SchoolCalendar:
    def __init__(self, school_name):
        """
        Initialize the SchoolCalendar with the name of the school.
        :param school_name: str - The name of the school
        """
        self.school_name = school_name
        self.activities = {}

    def add_activity(self, day, activity):
        """
        Add an activity to the calendar for a specific day.
        :param day: str - The date of the activity in YYYY-MM-DD format
        :param activity: str - The name of the activity
        """
        if not self._is_valid_date(day):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        
        if day not in self.activities:
            self.activities[day] = []
        
        self.activities[day].append(activity)

    def generate_calendar(self, start_date, end_date):
        """
        Generate a school calendar with all activities between given dates.
        :param start_date: str - Start date in YYYY-MM-DD format
        :param end_date: str - End date in YYYY-MM-DD format
        :return: dict - A dictionary representing the school calendar
        """
        if not self._is_valid_date(start_date) or not self._is_valid_date(end_date):
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        
        calendar = {}
        current_date = start
        
        while current_date <= end:
            date_str = current_date.strftime('%Y-%m-%d')
            calendar[date_str] = self.activities.get(date_str, [])
            current_date += timedelta(days=1)
        
        return calendar

    def save_to_file(self, filename):
        """
        Save the activities to a JSON file.
        :param filename: str - The name of the file to save the activities
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.activities, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file: {e}")

    @staticmethod
    def _is_valid_date(date_str):
        """
        Check if the provided date string is in valid YYYY-MM-DD format.
        :param date_str: str - The date string to validate
        :return: bool - True if valid, False otherwise
        """
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

# Example usage
if __name__ == "__main__":
    calendar = SchoolCalendar("Happy Boarding School")
    
    # Adding activities
    calendar.add_activity("2023-09-01", "Start of Term")
    calendar.add_activity("2023-09-05", "Science Fair")
    calendar.add_activity("2023-09-10", "Art Exhibition")
    
    # Generate calendar for a specific date range
    school_calendar = calendar.generate_calendar("2023-09-01", "2023-09-15")
    
    # Print the generated calendar
    print(json.dumps(school_calendar, indent=4))
    
    # Optionally, save the calendar to a file
    calendar.save_to_file("happy_boarding_school_calendar.json")
```
