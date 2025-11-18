"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Write a Python script to automate the generation of a course schedule for INESO's "Especialidad en Ortodoncia" program, including the start date, class days, and duration as described on the website.
Generated: DETERMINISTIC_6fd7f6a0be22b358
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import pandas as pd

class CourseScheduleGenerator:
    def __init__(self, start_date, class_days, duration_weeks):
        """
        Initializes the CourseScheduleGenerator with the specified parameters.
        
        :param start_date: The start date of the course in 'YYYY-MM-DD' format.
        :param class_days: A list of strings representing the days of the week classes are held.
        :param duration_weeks: The total duration of the course in weeks.
        """
        self.start_date = self._parse_start_date(start_date)
        self.class_days = class_days
        self.duration_weeks = duration_weeks
        self.schedule = []

    def _parse_start_date(self, start_date):
        """
        Parses the start date string into a datetime object.
        
        :param start_date: The start date in 'YYYY-MM-DD' format.
        :return: A datetime.date object.
        """
        try:
            return datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

    def generate_schedule(self):
        """
        Generates the course schedule based on the initialized parameters.
        """
        for week in range(self.duration_weeks):
            for day in self.class_days:
                class_date = self._get_class_date(week, day)
                self.schedule.append(class_date)

    def _get_class_date(self, week, day):
        """
        Calculates the class date for a given week and day of the week.
        
        :param week: The week number (0-indexed).
        :param day: The day of the week as a string (e.g., 'Monday').
        :return: The class date as a datetime.date object.
        """
        day_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(day)
        class_date = self.start_date + datetime.timedelta(weeks=week, days=day_index)
        return class_date

    def export_schedule(self, filename='course_schedule.xlsx'):
        """
        Exports the generated schedule to an Excel file.
        
        :param filename: The name of the Excel file to save the schedule.
        """
        df = pd.DataFrame(self.schedule, columns=["Class Date"])
        try:
            df.to_excel(filename, index=False)
            print(f"Schedule successfully exported to {filename}.")
        except Exception as e:
            print("Error exporting schedule:", e)

if __name__ == "__main__":
    # Customize these parameters as per the program's requirements
    start_date = '2024-01-08'  # Course start date
    class_days = ['Monday', 'Wednesday', 'Friday']  # Days classes are held
    duration_weeks = 12  # Total duration in weeks

    # Instantiating the CourseScheduleGenerator
    schedule_generator = CourseScheduleGenerator(start_date, class_days, duration_weeks)

    # Generate and export the course schedule
    schedule_generator.generate_schedule()
    schedule_generator.export_schedule()
```
