"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: "Generate a project plan for a construction project in Cali, Valle del Cauca, Colombia, considering the best use of resources and teams, as described on the INARO S.A.S. website."
Generated: DETERMINISTIC_20d4c099a7b385b7
Batch ID: 20250622_210802
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

# Define a class to represent a construction project plan
class ConstructionProjectPlan:
    def __init__(self, project_name, location, start_date, duration_days, resources, teams):
        """
        Initialize the construction project plan.

        :param project_name: Name of the project
        :param location: Location of the project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param duration_days: Duration of the project in days
        :param resources: List of resources required for the project
        :param teams: List of teams involved in the project
        """
        self.project_name = project_name
        self.location = location
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.duration_days = duration_days
        self.resources = resources
        self.teams = teams
        self.end_date = self.start_date + timedelta(days=duration_days)

    def generate_plan(self):
        """
        Generate the project plan as a dictionary.

        :return: Dictionary containing the project plan details
        """
        return {
            "Project Name": self.project_name,
            "Location": self.location,
            "Start Date": self.start_date.strftime("%Y-%m-%d"),
            "End Date": self.end_date.strftime("%Y-%m-%d"),
            "Duration (days)": self.duration_days,
            "Resources": self.resources,
            "Teams": self.teams,
        }

    def save_plan_to_file(self, file_name):
        """
        Save the project plan to a JSON file.

        :param file_name: Name of the file to save the plan
        """
        try:
            plan = self.generate_plan()
            with open(file_name, "w") as file:
                json.dump(plan, file, indent=4)
            print(f"Project plan saved to {file_name}")
        except Exception as e:
            print(f"Error saving project plan to file: {e}")

# Example usage
if __name__ == "__main__":
    # Define project details
    project_name = "Cali Construction Project"
    location = "Cali, Valle del Cauca, Colombia"
    start_date = "2023-11-01"
    duration_days = 120
    resources = [
        "Concrete",
        "Steel",
        "Wood",
        "Machinery",
        "Safety Equipment",
    ]
    teams = [
        {"Team Name": "Architects", "Members": 5},
        {"Team Name": "Engineers", "Members": 8},
        {"Team Name": "Construction Workers", "Members": 20},
        {"Team Name": "Project Managers", "Members": 3},
    ]

    # Create a project plan instance
    project_plan = ConstructionProjectPlan(
        project_name, location, start_date, duration_days, resources, teams
    )

    # Generate and save the project plan
    project_plan.save_plan_to_file("cali_construction_project_plan.json")
```
