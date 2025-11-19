"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: Write code to integrate a scheduling system for an educational institution, based on the working hours (Lun – Vie 6:00 – 18:30) mentioned on the IEBCA website.
Generated: DETERMINISTIC_20d427a756ae3c77
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, time, timedelta
import json

class Schedule:
    """A class to represent a scheduling system for an educational institution."""

    WORKING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    WORKING_HOURS_START = time(6, 0)  # 6:00 AM
    WORKING_HOURS_END = time(18, 30)   # 6:30 PM

    def __init__(self):
        """Initialize an empty schedule."""
        self.schedule = {}

    def add_class(self, day: str, start_time: str, end_time: str, class_name: str):
        """
        Add a class to the schedule.

        :param day: The day of the week (e.g., 'Monday').
        :param start_time: The start time of the class (e.g., '08:00').
        :param end_time: The end time of the class (e.g., '10:00').
        :param class_name: The name of the class.
        :raises ValueError: If the day is invalid or the times are out of working hours.
        """
        if day not in self.WORKING_DAYS:
            raise ValueError(f"Invalid day: {day}. Must be one of {self.WORKING_DAYS}.")

        start_time_obj = self._parse_time(start_time)
        end_time_obj = self._parse_time(end_time)

        if not self._is_within_working_hours(start_time_obj, end_time_obj):
            raise ValueError(f"Class times must be within working hours: {self.WORKING_HOURS_START} - {self.WORKING_HOURS_END}.")

        if day not in self.schedule:
            self.schedule[day] = []

        self.schedule[day].append({
            'class_name': class_name,
            'start_time': start_time_obj,
            'end_time': end_time_obj
        })

    def _parse_time(self, time_str: str) -> time:
        """Convert a time string to a time object."""
        try:
            return datetime.strptime(time_str, '%H:%M').time()
        except ValueError as e:
            raise ValueError(f"Invalid time format: {time_str}. Expected format is 'HH:MM'.") from e

    def _is_within_working_hours(self, start_time: time, end_time: time) -> bool:
        """Check if the given times are within the working hours."""
        return (self.WORKING_HOURS_START <= start_time <= self.WORKING_HOURS_END and
                self.WORKING_HOURS_START <= end_time <= self.WORKING_HOURS_END and
                start_time < end_time)

    def get_schedule(self) -> dict:
        """Return the current schedule."""
        return self.schedule

    def save_schedule(self, filename: str):
        """
        Save the schedule to a JSON file.

        :param filename: The name of the file to save the schedule.
        :raises IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, default=str)
        except IOError as e:
            raise IOError(f"Error saving schedule to {filename}: {e}")

    def load_schedule(self, filename: str):
        """
        Load the schedule from a JSON file.

        :param filename: The name of the file to load the schedule from.
        :raises IOError: If there is an error reading the file.
        :raises ValueError: If the file contains invalid data.
        """
        try:
            with open(filename, 'r') as file:
                self.schedule = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading schedule from {filename}: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid data in schedule file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = Schedule()
    try:
        scheduler.add_class('Monday', '08:00', '10:00', 'Math 101')
        scheduler.add_class('Tuesday', '09:00', '11:00', 'Physics 101')
        print(scheduler.get_schedule())
        scheduler.save_schedule('schedule.json')
    except Exception as e:
        print(f"An error occurred: {e}")
```
