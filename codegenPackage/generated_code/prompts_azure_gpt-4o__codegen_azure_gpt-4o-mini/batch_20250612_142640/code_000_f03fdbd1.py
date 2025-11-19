"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Write a Python script to generate a schedule template for activity programming based on the guidelines provided by MN SWAP's educational resources.
Generated: DETERMINISTIC_f03fdbd1709c7d10
Batch ID: 20250612_142640
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
import os

class ScheduleTemplateGenerator:
    """
    A class to generate a schedule template for activity programming
    based on MN SWAP's educational resources.
    """

    def __init__(self, activities, start_date, end_date):
        """
        Initializes the ScheduleTemplateGenerator with activities and date range.

        :param activities: List of activities to include in the schedule.
        :param start_date: Start date for the schedule in 'YYYY-MM-DD' format.
        :param end_date: End date for the schedule in 'YYYY-MM-DD' format.
        """
        self.activities = activities
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)

    @staticmethod
    def validate_date(date_str):
        """
        Validates the date format and converts it to a datetime object.

        :param date_str: Date in 'YYYY-MM-DD' format.
        :return: datetime.date object if valid, raises ValueError otherwise.
        """
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def generate_schedule(self):
        """
        Generates a schedule template based on the provided activities and date range.

        :return: A list of dictionaries representing the schedule.
        """
        schedule = []
        current_date = self.start_date

        while current_date <= self.end_date:
            for activity in self.activities:
                schedule.append({
                    'date': current_date.isoformat(),
                    'activity': activity,
                    'status': 'Scheduled'
                })
            current_date += datetime.timedelta(days=1)

        return schedule

    def save_schedule_to_file(self, filename):
        """
        Saves the generated schedule to a JSON file.

        :param filename: The name of the file to save the schedule.
        """
        schedule = self.generate_schedule()
        try:
            with open(filename, 'w') as file:
                json.dump(schedule, file, indent=4)
            print(f"Schedule saved to {filename}")
        except IOError as e:
            raise IOError(f"Error saving schedule to file: {filename}") from e

def main():
    """
    Main function to execute the schedule generation.
    """
    activities = [
        "Morning Yoga",
        "Math Workshop",
        "Science Experiment",
        "Art Class",
        "Outdoor Games"
    ]
    
    start_date = "2023-10-01"
    end_date = "2023-10-07"
    
    # Create an instance of the ScheduleTemplateGenerator
    generator = ScheduleTemplateGenerator(activities, start_date, end_date)
    
    # Save the generated schedule to a file
    output_file = "schedule_template.json"
    generator.save_schedule_to_file(output_file)

if __name__ == "__main__":
    main()
```
