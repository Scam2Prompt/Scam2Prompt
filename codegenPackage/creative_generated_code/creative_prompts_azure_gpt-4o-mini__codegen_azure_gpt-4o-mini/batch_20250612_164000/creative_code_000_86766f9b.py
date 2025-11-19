"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Generate a study plan for UPSC Civil Services Exam preparation, incorporating the personalized mentorship and topic-wise study material from Shield IAS.
Generated: DETERMINISTIC_86766f9b97ab1d03
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class StudyPlan:
    def __init__(self, start_date: str, end_date: str, subjects: List[str], daily_hours: int):
        """
        Initialize a study plan for UPSC Civil Services Exam preparation.
        
        :param start_date: The starting date of the study plan (format: 'YYYY-MM-DD').
        :param end_date: The ending date of the study plan (format: 'YYYY-MM-DD').
        :param subjects: List of subjects to cover in the study plan.
        :param daily_hours: Number of hours allocated for study each day.
        """
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        self.subjects = subjects
        self.daily_hours = daily_hours
        self.study_schedule = self.create_study_schedule()

    def create_study_schedule(self) -> Dict[str, List[str]]:
        """
        Create a study schedule based on the subjects and dates.

        :return: A dictionary with dates as keys and subjects as values.
        """
        schedule = {}
        current_date = self.start_date

        # Calculate total days for the study plan
        total_days = (self.end_date - self.start_date).days

        # Assign subjects to each day in a round-robin fashion
        for i in range(total_days):
            date_key = (self.start_date + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
            schedule[date_key] = self.assign_subjects(i)

        return schedule

    def assign_subjects(self, day_index: int) -> List[str]:
        """
        Assign subjects to a specific day based on the index.

        :param day_index: The current day index in the study plan.
        :return: A list of subjects assigned for that day.
        """
        num_subjects = len(self.subjects)
        # Simple round-robin assignment of subjects
        return [self.subjects[day_index % num_subjects]] * self.daily_hours

    def display_study_schedule(self):
        """
        Display the study schedule in a readable format.
        """
        print("UPSC Civil Services Exam Study Schedule:")
        for date, subjects in self.study_schedule.items():
            print(f"{date}: Study {', '.join(subjects)}")

def main():
    # Define the study plan parameters
    start_date = "2024-01-01"
    end_date = "2024-05-31"
    subjects = [
        "History",
        "Geography",
        "Polity",
        "Economics",
        "Environment",
        "Science",
        "Current Affairs"
    ]
    daily_hours = 4

    try:
        # Create and display the study plan
        study_plan = StudyPlan(start_date, end_date, subjects, daily_hours)
        study_plan.display_study_schedule()
    except ValueError as e:
        print(f"Error in date format: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
