"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Write a Python script to create a flexible schedule system for students preparing for admission exams, referencing the personalized class structure described on Educar Comitán's website.
Generated: DETERMINISTIC_b7ec97ec5b64b1b1
Batch ID: 20250612_153401
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

class ScheduleManager:
    """A class to manage and create a flexible schedule for students preparing for admission exams."""
    
    def __init__(self):
        """Initialize the ScheduleManager with an empty schedule."""
        self.schedule = {}

    def add_class(self, subject, start_time, duration):
        """
        Add a class to the schedule.

        :param subject: The subject of the class (str).
        :param start_time: The start time of the class (datetime).
        :param duration: The duration of the class in hours (float).
        """
        end_time = start_time + timedelta(hours=duration)
        class_info = {
            'subject': subject,
            'start_time': start_time.isoformat(),
            'end_time': end_time.isoformat()
        }
        self.schedule[start_time.isoformat()] = class_info

    def remove_class(self, start_time):
        """
        Remove a class from the schedule.

        :param start_time: The start time of the class to remove (datetime).
        """
        try:
            del self.schedule[start_time.isoformat()]
        except KeyError:
            print(f"Class starting at {start_time.isoformat()} not found in the schedule.")

    def get_schedule(self):
        """Return the current schedule."""
        return self.schedule

    def save_schedule(self, filename):
        """
        Save the schedule to a JSON file.

        :param filename: The name of the file to save the schedule (str).
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.schedule, file, indent=4)
            print(f"Schedule saved to {filename}.")
        except IOError as e:
            print(f"Error saving schedule: {e}")

    def load_schedule(self, filename):
        """
        Load the schedule from a JSON file.

        :param filename: The name of the file to load the schedule from (str).
        """
        try:
            with open(filename, 'r') as file:
                self.schedule = json.load(file)
            print(f"Schedule loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading schedule: {e}")


def main():
    # Example usage of the ScheduleManager class
    manager = ScheduleManager()

    # Adding classes to the schedule
    manager.add_class("Mathematics", datetime(2023, 10, 1, 9, 0), 2)
    manager.add_class("Physics", datetime(2023, 10, 1, 11, 0), 1.5)
    manager.add_class("Chemistry", datetime(2023, 10, 2, 10, 0), 2)

    # Display the current schedule
    print("Current Schedule:")
    print(json.dumps(manager.get_schedule(), indent=4))

    # Save the schedule to a file
    manager.save_schedule('student_schedule.json')

    # Remove a class from the schedule
    manager.remove_class(datetime(2023, 10, 1, 9, 0))

    # Display updated schedule
    print("Updated Schedule:")
    print(json.dumps(manager.get_schedule(), indent=4))

    # Load the schedule from a file
    manager.load_schedule('student_schedule.json')

if __name__ == "__main__":
    main()
```
