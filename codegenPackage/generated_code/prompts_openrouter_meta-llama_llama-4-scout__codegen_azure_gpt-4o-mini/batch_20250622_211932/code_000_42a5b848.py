"""
Generated Code Metadata:
========================
Original URL: https://danceanatolia.com
Prompt: Write a Python script to create a schedule for a dance school with classes in traditional Turkish folk dances, including "Zeybek" and "Folks-Fit" for women.
Generated: DETERMINISTIC_42a5b8489c7059a8
Batch ID: 20250622_211932
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

class DanceClass:
    """Class representing a dance class."""
    
    def __init__(self, name: str, day: str, start_time: str, duration: int):
        """
        Initialize a new dance class.

        :param name: Name of the dance class.
        :param day: Day of the week the class is held.
        :param start_time: Start time of the class in HH:MM format.
        :param duration: Duration of the class in minutes.
        """
        self.name = name
        self.day = day
        self.start_time = self._parse_time(start_time)
        self.duration = duration

    def _parse_time(self, time_str: str) -> datetime.time:
        """Parse a time string into a datetime.time object."""
        try:
            return datetime.datetime.strptime(time_str, "%H:%M").time()
        except ValueError as e:
            raise ValueError(f"Invalid time format: {time_str}. Expected format is HH:MM.") from e

    def end_time(self) -> datetime.time:
        """Calculate the end time of the class."""
        start_datetime = datetime.datetime.combine(datetime.date.today(), self.start_time)
        end_datetime = start_datetime + datetime.timedelta(minutes=self.duration)
        return end_datetime.time()

    def __str__(self) -> str:
        """String representation of the dance class."""
        return f"{self.name} on {self.day} from {self.start_time} to {self.end_time()}"

class DanceSchoolSchedule:
    """Class to manage the schedule of dance classes."""
    
    def __init__(self):
        """Initialize an empty schedule."""
        self.classes: List[DanceClass] = []

    def add_class(self, dance_class: DanceClass) -> None:
        """Add a dance class to the schedule."""
        self.classes.append(dance_class)

    def get_schedule(self) -> List[Dict[str, str]]:
        """Get the full schedule of dance classes."""
        return [{"name": dance_class.name, "day": dance_class.day, 
                 "start_time": str(dance_class.start_time), 
                 "end_time": str(dance_class.end_time())} for dance_class in self.classes]

    def display_schedule(self) -> None:
        """Display the schedule in a readable format."""
        print("Dance School Schedule:")
        for dance_class in self.classes:
            print(dance_class)

def main():
    """Main function to create and display the dance school schedule."""
    try:
        schedule = DanceSchoolSchedule()

        # Adding classes to the schedule
        schedule.add_class(DanceClass("Zeybek", "Monday", "18:00", 60))
        schedule.add_class(DanceClass("Folks-Fit", "Wednesday", "19:00", 45))
        schedule.add_class(DanceClass("Zeybek", "Friday", "17:00", 60))

        # Display the schedule
        schedule.display_schedule()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
