"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Construct a detailed social practice activity report for college students, inspired by the examples listed on 账云范文网.
Generated: DETERMINISTIC_8b6c855693b1f615
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class SocialPracticeActivityReport:
    """
    A class to represent a social practice activity report for college students.
    """

    def __init__(self, student_name, activity_title, activity_date, description, participants):
        """
        Initializes the report with student name, activity title, date, description, and participants.

        :param student_name: Name of the student
        :param activity_title: Title of the activity
        :param activity_date: Date of the activity (YYYY-MM-DD)
        :param description: Description of the activity
        :param participants: List of participants in the activity
        """
        self.student_name = student_name
        self.activity_title = activity_title
        self.activity_date = self.validate_date(activity_date)
        self.description = description
        self.participants = participants

    @staticmethod
    def validate_date(date_str):
        """
        Validates the date format and returns a datetime object.

        :param date_str: Date string in YYYY-MM-DD format
        :return: datetime object
        :raises ValueError: If the date format is incorrect
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def generate_report(self):
        """
        Generates a detailed report of the social practice activity.

        :return: A dictionary containing the report details
        """
        report = {
            "student_name": self.student_name,
            "activity_title": self.activity_title,
            "activity_date": self.activity_date.strftime('%Y-%m-%d'),
            "description": self.description,
            "participants": self.participants,
            "report_generated_on": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return report

    def save_report(self, filename):
        """
        Saves the report to a JSON file.

        :param filename: The name of the file to save the report
        :raises IOError: If there is an error writing to the file
        """
        report = self.generate_report()
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=4)
        except IOError as e:
            raise IOError(f"Error saving report to {filename}: {e}") from e

# Example usage
if __name__ == "__main__":
    try:
        report = SocialPracticeActivityReport(
            student_name="John Doe",
            activity_title="Community Clean-Up",
            activity_date="2023-10-15",
            description="A community service activity focused on cleaning local parks.",
            participants=["John Doe", "Jane Smith", "Alice Johnson"]
        )
        report.save_report("social_practice_report.json")
        print("Report generated and saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
