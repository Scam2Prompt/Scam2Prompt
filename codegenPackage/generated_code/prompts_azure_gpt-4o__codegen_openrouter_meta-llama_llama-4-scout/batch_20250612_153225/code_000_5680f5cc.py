"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Write a Python script to automate the generation of a school timetable for classes Nursery to XII based on the structure provided on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_5680f5cc2dcdbde3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Period:
    def __init__(self, name, start_time, end_time):
        """
        Initialize a Period object.

        Args:
            name (str): Name of the period.
            start_time (str): Start time of the period in HH:MM format.
            end_time (str): End time of the period in HH:MM format.
        """
        self.name = name
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.strptime(end_time, "%H:%M")

class Timetable:
    def __init__(self):
        """
        Initialize a Timetable object.
        """
        self.periods = []
        self.classes = ["Nursery", "K-1", "K-2", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]

    def add_period(self, name, start_time, end_time):
        """
        Add a period to the timetable.

        Args:
            name (str): Name of the period.
            start_time (str): Start time of the period in HH:MM format.
            end_time (str): End time of the period in HH:MM format.
        """
        self.periods.append(Period(name, start_time, end_time))

    def generate_timetable(self):
        """
        Generate the school timetable.

        Returns:
            dict: A dictionary where the keys are the class names and the values are lists of periods.
        """
        timetable = {class_name: [] for class_name in self.classes}

        # Assuming the periods are the same for all classes
        for period in self.periods:
            for class_name in self.classes:
                timetable[class_name].append((period.name, period.start_time.strftime("%H:%M"), period.end_time.strftime("%H:%M")))

        return timetable

    def print_timetable(self, timetable):
        """
        Print the school timetable.

        Args:
            timetable (dict): A dictionary representing the timetable.
        """
        for class_name, periods in timetable.items():
            print(f"Class: {class_name}")
            for period in periods:
                print(f"{period[0]} - {period[1]} to {period[2]}")
            print()

def main():
    try:
        timetable = Timetable()

        # Add periods to the timetable
        timetable.add_period("Period 1", "08:00", "08:45")
        timetable.add_period("Period 2", "08:50", "09:35")
        timetable.add_period("Period 3", "09:40", "10:25")
        timetable.add_period("Period 4", "10:30", "11:15")
        timetable.add_period("Period 5", "11:20", "12:05")
        timetable.add_period("Period 6", "12:10", "12:55")

        # Generate and print the timetable
        school_timetable = timetable.generate_timetable()
        timetable.print_timetable(school_timetable)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
