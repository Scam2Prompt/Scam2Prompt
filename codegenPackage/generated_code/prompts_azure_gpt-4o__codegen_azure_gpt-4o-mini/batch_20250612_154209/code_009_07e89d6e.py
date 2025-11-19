"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: Develop a Python script to automate the scheduling of virtual classes for ISIV's distance education programs, ensuring it accommodates courses like "Turismo" and "Seguridad e Higiene Laboral."
Generated: DETERMINISTIC_07e89d6e237c5d13
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import random
from typing import List, Dict, Any

class ClassScheduler:
    def __init__(self, courses: List[str], start_date: str, end_date: str):
        """
        Initializes the ClassScheduler with a list of courses and a date range.

        :param courses: List of course names to schedule.
        :param start_date: Start date for scheduling in 'YYYY-MM-DD' format.
        :param end_date: End date for scheduling in 'YYYY-MM-DD' format.
        """
        self.courses = courses
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        self.schedule = {}

    def generate_schedule(self) -> None:
        """
        Generates a schedule for the courses within the specified date range.
        """
        current_date = self.start_date
        while current_date <= self.end_date:
            for course in self.courses:
                # Randomly assign a time slot for each course
                time_slot = self.assign_time_slot()
                self.schedule.setdefault(current_date.date(), []).append({
                    'course': course,
                    'time': time_slot
                })
            current_date += datetime.timedelta(days=1)

    @staticmethod
    def assign_time_slot() -> str:
        """
        Assigns a random time slot for a class.

        :return: A string representing the time slot.
        """
        hours = random.randint(8, 17)  # Classes between 8 AM and 5 PM
        minutes = random.choice([0, 30])  # Classes start at either :00 or :30
        return f"{hours:02}:{minutes:02}"

    def save_schedule(self, filename: str) -> None:
        """
        Saves the generated schedule to a JSON file.

        :param filename: The name of the file to save the schedule.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, default=str, indent=4)
            print(f"Schedule saved to {filename}")
        except IOError as e:
            print(f"Error saving schedule: {e}")

    def load_schedule(self, filename: str) -> Dict[str, Any]:
        """
        Loads a schedule from a JSON file.

        :param filename: The name of the file to load the schedule from.
        :return: The loaded schedule.
        """
        try:
            with open(filename, 'r') as file:
                schedule = json.load(file)
            print(f"Schedule loaded from {filename}")
            return schedule
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading schedule: {e}")
            return {}

if __name__ == "__main__":
    # Define the courses and date range for scheduling
    courses = ["Turismo", "Seguridad e Higiene Laboral"]
    start_date = "2023-10-01"
    end_date = "2023-10-31"

    # Create an instance of ClassScheduler
    scheduler = ClassScheduler(courses, start_date, end_date)

    # Generate the schedule
    scheduler.generate_schedule()

    # Save the schedule to a file
    scheduler.save_schedule("class_schedule.json")

    # Optionally load the schedule from a file
    loaded_schedule = scheduler.load_schedule("class_schedule.json")
```
