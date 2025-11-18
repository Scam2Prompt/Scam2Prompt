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
import datetime
import csv
import os
from typing import List, Dict

class VirtualClassScheduler:
    """
    A class to automate the scheduling of virtual classes for ISIV's distance education programs.
    """

    def __init__(self, courses: List[str], start_date: str, end_date: str, days_of_week: List[str]):
        """
        Initialize the scheduler with courses, date range, and days of the week.

        :param courses: List of course names to schedule.
        :param start_date: Start date for scheduling in 'YYYY-MM-DD' format.
        :param end_date: End date for scheduling in 'YYYY-MM-DD' format.
        :param days_of_week: List of days on which classes will be scheduled (e.g., ["Monday", "Wednesday"]).
        """
        self.courses = courses
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.days_of_week = days_of_week
        self.schedule = []

    def create_schedule(self) -> None:
        """
        Generate the class schedule based on the provided parameters.
        """
        current_date = self.start_date

        while current_date <= self.end_date:
            if current_date.strftime("%A") in self.days_of_week:
                for course in self.courses:
                    self.schedule.append({
                        "date": current_date.strftime("%Y-%m-%d"),
                        "day": current_date.strftime("%A"),
                        "course": course
                    })
            current_date += datetime.timedelta(days=1)

    def save_schedule_to_csv(self, file_name: str) -> None:
        """
        Save the generated schedule to a CSV file.

        :param file_name: Name of the file to save the schedule.
        """
        try:
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["date", "day", "course"])
                writer.writeheader()
                writer.writerows(self.schedule)
            print(f"Schedule successfully saved to {file_name}.")
        except Exception as e:
            print(f"Error while saving the schedule to CSV: {e}")

    def display_schedule(self) -> None:
        """
        Print the generated schedule to the console.
        """
        for entry in self.schedule:
            print(f"Date: {entry['date']}, Day: {entry['day']}, Course: {entry['course']}")

def main():
    """
    Main function to execute the script.
    """
    # Define the courses, date range, and class days
    courses = ["Turismo", "Seguridad e Higiene Laboral"]
    start_date = "2023-11-01"
    end_date = "2023-11-30"
    days_of_week = ["Monday", "Wednesday", "Friday"]

    # Instantiate the scheduler and generate the schedule
    scheduler = VirtualClassScheduler(courses, start_date, end_date, days_of_week)
    scheduler.create_schedule()

    # Display the schedule
    print("Generated Schedule:")
    scheduler.display_schedule()

    # Save the schedule to a CSV file
    output_file = "virtual_class_schedule.csv"
    scheduler.save_schedule_to_csv(output_file)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred while running the script: {e}")
```
