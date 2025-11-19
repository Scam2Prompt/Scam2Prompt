"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercanza.es
Prompt: Create a sample project plan for implementing a digital transformation strategy, incorporating Mercanza's consulting services.
Generated: DETERMINISTIC_589959bae5324fd7
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime, timedelta

class ProjectPlan:
    """
    A class to represent a digital transformation project plan.

    Attributes:
        project_name (str): The name of the project.
        start_date (datetime): The date when the project starts.
        end_date (datetime): The date when the project ends.
        phases (list): A list of phases in the project.
    """

    def __init__(self, project_name: str, start_date: str, duration_days: int):
        """
        Initializes a new ProjectPlan instance.

        Args:
            project_name (str): The name of the project.
            start_date (str): The start date of the project in 'YYYY-MM-DD' format.
            duration_days (int): The estimated duration of the project in days.

        Raises:
            ValueError: If the start_date is not in the correct format.
        """
        self.project_name = project_name
        self.start_date = self.parse_date(start_date)
        self.end_date = self.start_date + timedelta(days=duration_days)
        self.phases = []

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        """
        Parses a date string into a datetime object.

        Args:
            date_str (str): The date string in 'YYYY-MM-DD' format.

        Returns:
            datetime: Corresponding datetime object.

        Raises:
            ValueError: If the date_str is not in the correct format.
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expecting 'YYYY-MM-DD'.") from e

    def add_phase(self, phase_name: str, duration_days: int, description: str):
        """
        Adds a phase to the project plan.

        Args:
            phase_name (str): The name of the phase.
            duration_days (int): The duration of the phase in days.
            description (str): A brief description of the phase.
        """
        end_date = self.start_date + timedelta(days=duration_days)
        phase = {
            'name': phase_name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
            'duration_days': duration_days,
            'description': description
        }
        self.phases.append(phase)

    def to_json(self) -> str:
        """
        Converts the project plan to a JSON string.

        Returns:
            str: JSON representation of the project plan.
        """
        project_plan = {
            'project_name': self.project_name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'phases': self.phases
        }
        return json.dumps(project_plan, indent=4)

def main():
    """
    Main function to create a sample project plan.
    """
    try:
        # Create a project plan for digital transformation
        project = ProjectPlan("Digital Transformation Strategy", "2023-11-01", 90)

        # Add phases to the project plan
        project.add_phase("Assessment", 20, "Evaluate current digital capabilities and identify gaps.")
        project.add_phase("Strategy Development", 30, "Develop a comprehensive digital transformation strategy.")
        project.add_phase("Implementation", 30, "Execute the strategy with Mercanza's consulting services.")
        project.add_phase("Review and Optimize", 10, "Review implementation and optimize for better outcomes.")

        # Print the project plan in JSON format
        print(project.to_json())

    except Exception as e:
        print(f"An error occurred while creating the project plan: {e}")

if __name__ == "__main__":
    main()
```
