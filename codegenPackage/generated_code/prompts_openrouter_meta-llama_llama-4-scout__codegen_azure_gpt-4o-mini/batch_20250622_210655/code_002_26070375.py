"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Generate a sample schedule for a school with different levels of education (initial, basic, and high school) and including extracurricular activities, similar to those listed on the MercedariasGye website.
Generated: DETERMINISTIC_26070375e1193f69
Batch ID: 20250622_210655
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

class SchoolSchedule:
    def __init__(self):
        # Initialize the schedule with empty lists for each education level
        self.schedule = {
            'Initial': [],
            'Basic': [],
            'High School': []
        }
        self.extracurricular_activities = [
            'Football', 'Basketball', 'Music Band', 'Art Club', 'Science Club', 'Drama Club'
        ]
        self.subjects = {
            'Initial': ['Playtime', 'Storytelling', 'Arts and Crafts'],
            'Basic': ['Mathematics', 'Science', 'Language Arts', 'History'],
            'High School': ['Mathematics', 'Biology', 'Chemistry', 'Physics', 'Literature', 'History']
        }

    def generate_schedule(self):
        """Generates a weekly schedule for each education level."""
        for level in self.schedule.keys():
            self.schedule[level] = self.create_weekly_schedule(level)

    def create_weekly_schedule(self, level):
        """Creates a weekly schedule for a given education level."""
        weekly_schedule = {}
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

        for day in days_of_week:
            daily_schedule = self.create_daily_schedule(level)
            weekly_schedule[day] = daily_schedule

        return weekly_schedule

    def create_daily_schedule(self, level):
        """Creates a daily schedule for a given education level."""
        daily_schedule = []
        subjects = self.subjects[level]

        # Randomly select subjects for the day
        for _ in range(5):  # Assuming 5 periods in a day
            subject = random.choice(subjects)
            daily_schedule.append(subject)

        # Add an extracurricular activity
        extracurricular = random.choice(self.extracurricular_activities)
        daily_schedule.append(f'Extracurricular: {extracurricular}')

        return daily_schedule

    def display_schedule(self):
        """Displays the generated schedule in a readable format."""
        for level, schedule in self.schedule.items():
            print(f"\nSchedule for {level}:")
            for day, subjects in schedule.items():
                print(f"{day}: {', '.join(subjects)}")

def main():
    """Main function to run the schedule generation."""
    try:
        school_schedule = SchoolSchedule()
        school_schedule.generate_schedule()
        school_schedule.display_schedule()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
