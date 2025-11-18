"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyboarding.edu.np
Prompt: Write a program to generate a school calendar with A-to-Z curricular activities, based on the structured learning environment at Happy Boarding School.
Generated: DETERMINISTIC_075b641285e2abf8
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import calendar
from datetime import date, timedelta

class SchoolCalendar:
    def __init__(self, year, activities):
        """
        Initialize the School Calendar.

        :param year: The year for which the calendar is to be generated.
        :param activities: A list of curricular activities (A-to-Z).
        """
        self.year = year
        self.activities = activities
        self.calendar = {}

    def generate_calendar(self):
        """
        Generate the school calendar with assigned activities for each month.
        """
        try:
            months = list(calendar.month_name)[1:]  # Get the names of all months (excluding an empty first entry)
            activity_count = len(self.activities)

            if activity_count < 12:
                raise ValueError("Insufficient activities provided. Please provide at least 12 activities.")

            for i, month in enumerate(months):
                self.calendar[month] = self.activities[i]

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_calendar(self):
        """
        Display the school calendar.
        """
        print(f"School Calendar for {self.year}:")
        print("-" * 30)
        for month, activity in self.calendar.items():
            print(f"{month}: {activity}")

def main():
    """
    Main function to drive the program.
    """
    try:
        # Define the structured learning activities (A-to-Z).
        activities = [
            "Art and Craft",
            "Basketball Training",
            "Coding Bootcamp",
            "Dance Classes",
            "Environmental Awareness",
            "Fitness Camp",
            "Gardening Workshop",
            "History Club",
            "Innovation Lab",
            "Journal Writing",
            "Karate Sessions",
            "Literature Reading"
        ]

        # Get the current year.
        current_year = date.today().year

        # Create an instance of the SchoolCalendar.
        school_calendar = SchoolCalendar(current_year, activities)

        # Generate and display the calendar.
        school_calendar.generate_calendar()
        school_calendar.display_calendar()

    except Exception as e:
        print(f"An error occurred in the program: {e}")

if __name__ == "__main__":
    main()
```
