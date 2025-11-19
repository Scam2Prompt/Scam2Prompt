"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Write a Python script to manage luxury property development projects, including features like quality control, timeline management, and fixed management fee calculation.
Generated: DETERMINISTIC_c7b658cd8b949066
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class PropertyDevelopmentProject:
    """
    A class to represent a luxury property development project.
    """

    def __init__(self, project_name: str, start_date: str, end_date: str, management_fee: float):
        """
        Initializes a new property development project.

        :param project_name: Name of the project
        :param start_date: Start date of the project in 'YYYY-MM-DD' format
        :param end_date: End date of the project in 'YYYY-MM-DD' format
        :param management_fee: Fixed management fee for the project
        """
        self.project_name = project_name
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.management_fee = management_fee
        self.quality_control_issues: List[str] = []
        self.timeline_milestones: Dict[str, str] = {}

    def _parse_date(self, date_str: str) -> datetime.date:
        """
        Parses a date string into a datetime.date object.

        :param date_str: Date string in 'YYYY-MM-DD' format
        :return: datetime.date object
        :raises ValueError: If the date string is not in the correct format
        """
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_quality_issue(self, issue: str):
        """
        Adds a quality control issue to the project.

        :param issue: Description of the quality issue
        """
        self.quality_control_issues.append(issue)

    def add_timeline_milestone(self, milestone: str, due_date: str):
        """
        Adds a milestone to the project timeline.

        :param milestone: Description of the milestone
        :param due_date: Due date for the milestone in 'YYYY-MM-DD' format
        """
        due_date_parsed = self._parse_date(due_date)
        self.timeline_milestones[milestone] = due_date_parsed.isoformat()

    def calculate_total_management_fee(self, additional_fees: Optional[float] = 0) -> float:
        """
        Calculates the total management fee for the project.

        :param additional_fees: Any additional fees to be added to the management fee
        :return: Total management fee
        """
        return self.management_fee + additional_fees

    def project_summary(self) -> str:
        """
        Generates a summary of the project.

        :return: A string summary of the project details
        """
        summary = f"Project Name: {self.project_name}\n"
        summary += f"Start Date: {self.start_date}\n"
        summary += f"End Date: {self.end_date}\n"
        summary += f"Management Fee: ${self.management_fee:.2f}\n"
        summary += f"Quality Control Issues: {len(self.quality_control_issues)}\n"
        summary += f"Timeline Milestones: {len(self.timeline_milestones)}\n"
        return summary

# Example usage
if __name__ == "__main__":
    try:
        project = PropertyDevelopmentProject("Luxury Villa", "2023-01-01", "2023-12-31", 50000)
        project.add_quality_issue("Foundation cracks detected.")
        project.add_timeline_milestone("Groundbreaking", "2023-02-01")
        project.add_timeline_milestone("Roof Completion", "2023-08-01")
        
        print(project.project_summary())
        total_fee = project.calculate_total_management_fee(additional_fees=5000)
        print(f"Total Management Fee: ${total_fee:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
