"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Write a Python script to create a flexible schedule system for students preparing for admission exams, referencing the personalized class structure described on Educar Comitán's website.
Generated: DETERMINISTIC_b7ec97ec5b64b1b1
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class Schedule:
    """
    A class to represent a flexible schedule for students preparing for admission exams.
    """

    def __init__(self):
        self.schedule = {}

    def add_class(self, subject, date_time, duration_hours):
        """
        Adds a class to the schedule.

        :param subject: The subject of the class (str)
        :param date_time: The date and time of the class (datetime)
        :param duration_hours: The duration of the class in hours (float)
        :raises ValueError: If the class time overlaps with an existing class
        """
        end_time = date_time + timedelta(hours=duration_hours)
        for existing_subject, (existing_start, existing_end) in self.schedule.items():
            if (date_time < existing_end) and (end_time > existing_start):
                raise ValueError(f"Class time overlaps with existing class: {existing_subject}")

        self.schedule[subject] = (date_time, end_time)

    def remove_class(self, subject):
        """
        Removes a class from the schedule.

        :param subject: The subject of the class to remove (str)
        :raises KeyError: If the subject is not found in the schedule
        """
        if subject in self.schedule:
            del self.schedule[subject]
        else:
            raise KeyError(f"No class found for subject: {subject}")

    def get_schedule(self):
        """
        Returns the current schedule.

        :return: A dictionary of scheduled classes
        """
        return {subject: {'start': start.strftime('%Y-%m-%d %H:%M'), 'end': end.strftime('%Y-%m-%d %H:%M')}
                for subject, (start, end) in self.schedule.items()}

    def save_schedule(self, filename):
        """
        Saves the current schedule to a JSON file.

        :param filename: The name of the file to save the schedule (str)
        """
        with open(filename, 'w') as file:
            json.dump(self.get_schedule(), file, indent=4)

    def load_schedule(self, filename):
        """
        Loads a schedule from a JSON file.

        :param filename: The name of the file to load the schedule from (str)
        :raises FileNotFoundError: If the file does not exist
        :raises ValueError: If the file contains invalid data
        """
        try:
            with open(filename, 'r') as file:
                loaded_schedule = json.load(file)
                for subject, times in loaded_schedule.items():
                    start_time = datetime.strptime(times['start'], '%Y-%m-%d %H:%M')
                    end_time = datetime.strptime(times['end'], '%Y-%m-%d %H:%M')
                    self.schedule[subject] = (start_time, end_time)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filename} does not exist.")
        except json.JSONDecodeError:
            raise ValueError("The file contains invalid JSON data.")

# Example usage
if __name__ == "__main__":
    try:
        my_schedule = Schedule()
        my_schedule.add_class("Mathematics", datetime(2023, 10, 15, 10, 0), 2)
        my_schedule.add_class("Physics", datetime(2023, 10, 16, 14, 0), 1.5)
        print("Current Schedule:", my_schedule.get_schedule())

        my_schedule.save_schedule("my_schedule.json")
        print("Schedule saved to my_schedule.json")

        # Load the schedule from the file
        new_schedule = Schedule()
        new_schedule.load_schedule("my_schedule.json")
        print("Loaded Schedule:", new_schedule.get_schedule())

    except (ValueError, KeyError, FileNotFoundError) as e:
        print(f"Error: {e}")
```
