"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Develop a Python script to automate the scheduling of virtual classes for ISIV's distance education programs, ensuring it accommodates courses like "Turismo" and "Seguridad e Higiene Laboral."
Generated: DETERMINISTIC_07e89d6e237c5d13
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import random
from datetime import datetime, timedelta

class ClassScheduler:
    def __init__(self, courses, start_date, end_date):
        """
        Initializes the ClassScheduler with course names and date range.
        
        :param courses: List of course names.
        :param start_date: Starting date for scheduling classes (YYYY-MM-DD).
        :param end_date: Ending date for scheduling classes (YYYY-MM-DD).
        """
        self.courses = courses
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.schedule = []

    def generate_schedule(self, classes_per_course=3):
        """
        Generates a schedule for each course within the date range.

        :param classes_per_course: Number of classes to schedule for each course.
        """
        for course in self.courses:
            for _ in range(classes_per_course):
                class_date = self.get_random_date()
                class_time = self.get_random_time()
                self.schedule.append((course, class_date, class_time))

    def get_random_date(self):
        """
        Generates a random date within the specified date range.

        :return: Random date as a string (YYYY-MM-DD).
        """
        delta = self.end_date - self.start_date
        random_days = random.randint(0, delta.days)
        return (self.start_date + timedelta(days=random_days)).date()

    def get_random_time(self):
        """
        Generates a random time for the class.

        :return: Random time as a string (HH:MM).
        """
        hour = random.randint(8, 18)  # Classes between 8 AM and 6 PM
        minute = random.choice([0, 30])  # Classes on the hour or half-hour
        return f"{hour:02}:{minute:02}"

    def save_schedule_to_csv(self, filename):
        """
        Saves the generated schedule to a CSV file.

        :param filename: Name of the output CSV file.
        """
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Course", "Date", "Time"])
                writer.writerows(self.schedule)
            print(f"Schedule successfully saved to {filename}.")
        except IOError as e:
            print(f"An error occurred while writing to file: {e}")

def main():
    # Define the courses and date range for scheduling
    courses = ["Turismo", "Seguridad e Higiene Laboral"]
    start_date = '2023-11-01'  # Start scheduling from November 1, 2023
    end_date = '2023-12-01'    # End scheduling by December 1, 2023

    # Create an instance of ClassScheduler
    scheduler = ClassScheduler(courses, start_date, end_date)
    
    # Generate the schedule
    scheduler.generate_schedule(classes_per_course=3)
    
    # Save the schedule to a CSV file
    scheduler.save_schedule_to_csv("class_schedule.csv")

if __name__ == "__main__":
    main()
```
