"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Write a Python script to generate a weekly dance class schedule based on input data for class types, instructor names, and available time slots, similar to the offerings at Sakura Dance Studio.
Generated: DETERMINISTIC_4d6381163a3356d1
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta

class DanceClassScheduler:
    def __init__(self, class_types, instructors, start_date, num_weeks=1):
        """
        Initializes the DanceClassScheduler with class types, instructors, start date, and number of weeks.

        :param class_types: List of dance class types (e.g., ['Ballet', 'Hip Hop', 'Jazz'])
        :param instructors: List of instructor names (e.g., ['Alice', 'Bob', 'Charlie'])
        :param start_date: The starting date for the schedule (datetime object)
        :param num_weeks: Number of weeks to generate the schedule for
        """
        self.class_types = class_types
        self.instructors = instructors
        self.start_date = start_date
        self.num_weeks = num_weeks
        self.schedule = {}

    def generate_schedule(self):
        """
        Generates a weekly schedule for the specified number of weeks.
        Each day will have a random selection of classes and instructors.
        """
        for week in range(self.num_weeks):
            for day in range(7):  # 0 = Monday, 6 = Sunday
                current_date = self.start_date + timedelta(weeks=week, days=day)
                self.schedule[current_date.strftime('%Y-%m-%d')] = self._generate_daily_classes()

    def _generate_daily_classes(self):
        """
        Generates a list of classes for a single day.

        :return: List of dictionaries containing class details
        """
        daily_classes = []
        num_classes = random.randint(3, 5)  # Randomly choose between 3 to 5 classes per day

        for _ in range(num_classes):
            class_info = {
                'class_type': random.choice(self.class_types),
                'instructor': random.choice(self.instructors),
                'time': self._generate_random_time()
            }
            daily_classes.append(class_info)

        return daily_classes

    def _generate_random_time(self):
        """
        Generates a random time for a class within the studio's operating hours.

        :return: Random time as a string in 'HH:MM' format
        """
        hour = random.randint(9, 21)  # Studio operates from 9 AM to 9 PM
        minute = random.choice([0, 15, 30, 45])  # Class starts at quarter-hour intervals
        return f"{hour:02}:{minute:02}"

    def display_schedule(self):
        """
        Displays the generated schedule in a readable format.
        """
        for date, classes in self.schedule.items():
            print(f"Schedule for {date}:")
            for class_info in classes:
                print(f"  {class_info['time']} - {class_info['class_type']} with {class_info['instructor']}")
            print()  # Blank line for better readability

if __name__ == "__main__":
    # Example input data
    class_types = ['Ballet', 'Hip Hop', 'Jazz', 'Contemporary', 'Tap']
    instructors = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan']
    start_date = datetime(2023, 10, 30)  # Starting from a Monday

    # Create a DanceClassScheduler instance
    scheduler = DanceClassScheduler(class_types, instructors, start_date, num_weeks=4)

    # Generate and display the schedule
    scheduler.generate_schedule()
    scheduler.display_schedule()
```
