"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Generate code to calculate project timelines for infrastructure construction, ensuring compliance with safety and environmental regulations, similar to Unison Plus's approach.
Generated: DETERMINISTIC_b9efc9f1dfee7c85
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import math

class ProjectTimelineCalculator:
    """
    A class to calculate project timelines for infrastructure construction,
    ensuring compliance with safety and environmental regulations.
    """

    def __init__(self, project_name, start_date, duration_days, safety_regulations, env_regulations):
        """
        Initialize the project timeline calculator.

        :param project_name: Name of the infrastructure project
        :param start_date: Start date of the project (format: 'YYYY-MM-DD')
        :param duration_days: Estimated duration of the project in days
        :param safety_regulations: List of safety regulations to comply with
        :param env_regulations: List of environmental regulations to comply with
        """
        self.project_name = project_name
        self.start_date = self.parse_date(start_date)
        self.duration_days = duration_days
        self.safety_regulations = safety_regulations
        self.env_regulations = env_regulations

    @staticmethod
    def parse_date(date_str):
        """
        Parse a date string into a datetime object.

        :param date_str: Date string in 'YYYY-MM-DD' format
        :return: datetime.date object
        :raises ValueError: If the date is not in the correct format
        """
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format is 'YYYY-MM-DD'.") from e

    def calculate_end_date(self):
        """
        Calculate the end date of the project.

        :return: End date as a datetime.date object
        """
        return self.start_date + datetime.timedelta(days=self.duration_days)

    def check_regulations(self):
        """
        Check compliance with safety and environmental regulations.

        :return: Boolean indicating compliance status
        """
        safety_compliance = all(self.safety_regulations)
        env_compliance = all(self.env_regulations)
        return safety_compliance and env_compliance

    def generate_timeline_report(self):
        """
        Generate a report summarizing the project timeline and compliance status.

        :return: A dictionary containing project details
        """
        end_date = self.calculate_end_date()
        compliance_status = self.check_regulations()
        
        report = {
            "Project Name": self.project_name,
            "Start Date": self.start_date,
            "Estimated Duration (days)": self.duration_days,
            "End Date": end_date,
            "Compliance Status": "Compliant" if compliance_status else "Non-Compliant"
        }
        
        return report

# Example usage
if __name__ == "__main__":
    try:
        project = ProjectTimelineCalculator(
            project_name="Bridge Construction",
            start_date="2023-11-01",
            duration_days=120,
            safety_regulations=[True, True, True],  # Assuming all regulations are met
            env_regulations=[True, False]  # One regulation is not met
        )
        
        report = project.generate_timeline_report()
        for key, value in report.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
