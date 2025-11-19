"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecbc.online
Prompt: Generate a Python script to schedule a weekly radio program on ECBC Radio, including segments and song selections as described in the programming schedule.
Generated: DETERMINISTIC_e4c0f354c8d80387
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
from typing import List, Dict

class RadioProgram:
    """Class to represent a Radio Program with segments and song selections."""
    
    def __init__(self, title: str, segments: List[Dict[str, List[str]]]):
        """
        Initializes the RadioProgram with a title and a list of segments.

        Args:
            title (str): Title of the radio program.
            segments (List[Dict[str, List[str]]]): List of segments with their song selections.
        """
        self.title = title
        self.segments = segments
        self.schedule_time = None

    def schedule_program(self, day_of_week: str, time: str):
        """
        Schedules the program for a specific day and time.

        Args:
            day_of_week (str): Day of the week to schedule the program.
            time (str): Time in 'HH:MM' format when the program will air.
        """
        try:
            self.schedule_time = self._get_schedule_datetime(day_of_week, time)
        except ValueError as e:
            print(f"Error scheduling program: {e}")

    def _get_schedule_datetime(self, day_of_week: str, time: str) -> datetime.datetime:
        """
        Converts the day of the week and time to a datetime object.

        Args:
            day_of_week (str): Day of the week to schedule the program.
            time (str): Time in 'HH:MM' format.

        Returns:
            datetime.datetime: The scheduled datetime for the program.

        Raises:
            ValueError: If the day or time format is incorrect.
        """
        days = {
            "monday": 0,
            "tuesday": 1,
            "wednesday": 2,
            "thursday": 3,
            "friday": 4,
            "saturday": 5,
            "sunday": 6
        }
        
        if day_of_week.lower() not in days:
            raise ValueError(f"Invalid day of the week: {day_of_week}")
        
        try:
            hour, minute = map(int, time.split(':'))
            scheduled_time = datetime.datetime.now()
            scheduled_time = scheduled_time.replace(hour=hour, minute=minute, second=0, microsecond=0)

            # Calculate the number of days until the next scheduled day
            days_until_schedule = (days[day_of_week.lower()] - scheduled_time.weekday() + 7) % 7
            scheduled_time += datetime.timedelta(days=days_until_schedule)

            return scheduled_time

        except ValueError:
            raise ValueError("Time must be in 'HH:MM' format.")

    def to_json(self) -> str:
        """Converts the radio program to a JSON string."""
        program_data = {
            "title": self.title,
            "schedule_time": self.schedule_time.isoformat() if self.schedule_time else None,
            "segments": self.segments
        }
        return json.dumps(program_data, indent=4)

def main():
    # Example use of the RadioProgram class
    segments = [
        {
            "segment_name": "Morning Melodies",
            "songs": ["Song A - Artist 1", "Song B - Artist 2"]
        },
        {
            "segment_name": "Afternoon Hits",
            "songs": ["Song C - Artist 3", "Song D - Artist 4"]
        },
        {
            "segment_name": "Evening Classics",
            "songs": ["Song E - Artist 5", "Song F - Artist 6"]
        }
    ]

    # Create a radio program instance
    radio_program = RadioProgram("ECBC Weekly Show", segments)

    # Schedule the program for next Monday at 10:00 AM
    radio_program.schedule_program("Monday", "10:00")

    # Output the scheduled program details in JSON format
    print(radio_program.to_json())

if __name__ == "__main__":
    main()
```
