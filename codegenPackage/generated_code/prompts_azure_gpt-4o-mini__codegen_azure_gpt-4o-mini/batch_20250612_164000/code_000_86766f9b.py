"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Generate a study plan for UPSC Civil Services Exam preparation, incorporating the personalized mentorship and topic-wise study material from Shield IAS.
Generated: DETERMINISTIC_86766f9b97ab1d03
Batch ID: 20250612_164000
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

class StudyPlan:
    def __init__(self, start_date, duration_weeks, subjects, daily_hours):
        """
        Initializes the StudyPlan with the given parameters.

        :param start_date: The date to start the study plan (YYYY-MM-DD).
        :param duration_weeks: Duration of the study plan in weeks.
        :param subjects: List of subjects to cover.
        :param daily_hours: Number of hours to study each day.
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.duration = timedelta(weeks=duration_weeks)
        self.end_date = self.start_date + self.duration
        self.subjects = subjects
        self.daily_hours = daily_hours
        self.plan = {}

    def generate_plan(self):
        """
        Generates a study plan by distributing subjects over the study duration.
        """
        current_date = self.start_date
        total_days = self.duration.days
        subjects_count = len(self.subjects)

        for day in range(total_days):
            subject = self.subjects[day % subjects_count]
            self.plan[current_date.strftime("%Y-%m-%d")] = {
                "subject": subject,
                "hours": self.daily_hours,
                "resources": self.get_study_material(subject)
            }
            current_date += timedelta(days=1)

    def get_study_material(self, subject):
        """
        Retrieves study material for a given subject from Shield IAS.

        :param subject: The subject for which to retrieve study material.
        :return: A list of study materials.
        """
        # Placeholder for actual resource fetching logic
        resources = {
            "History": ["NCERT History Book", "Spectrum Modern History"],
            "Geography": ["NCERT Geography Book", "GC Leong"],
            "Polity": ["Laxmikant's Indian Polity", "Constitution of India"],
            "Economics": ["NCERT Economics Book", "Ramesh Singh"],
            "Environment": ["Shankar IAS Environment Book", "Current Affairs"],
            "Science": ["NCERT Science Books", "Current Affairs"]
        }
        return resources.get(subject, [])

    def save_plan(self, filename):
        """
        Saves the generated study plan to a JSON file.

        :param filename: The name of the file to save the study plan.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.plan, file, indent=4)
            print(f"Study plan saved to {filename}")
        except IOError as e:
            print(f"Error saving study plan: {e}")

    def display_plan(self):
        """
        Displays the generated study plan in a readable format.
        """
        for date, details in self.plan.items():
            print(f"Date: {date}, Subject: {details['subject']}, Hours: {details['hours']}, Resources: {', '.join(details['resources'])}")

# Example usage
if __name__ == "__main__":
    subjects = ["History", "Geography", "Polity", "Economics", "Environment", "Science"]
    study_plan = StudyPlan(start_date="2023-11-01", duration_weeks=12, subjects=subjects, daily_hours=5)
    study_plan.generate_plan()
    study_plan.display_plan()
    study_plan.save_plan("upsc_study_plan.json")
```
