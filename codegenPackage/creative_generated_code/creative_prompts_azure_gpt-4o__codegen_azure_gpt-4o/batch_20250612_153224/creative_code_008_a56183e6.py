"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arpgroupcorp.com
Prompt: Create a project plan template for IT project management that ensures timelines and budgets are met, inspired by ARP Group Corporation's methodology.
Generated: DETERMINISTIC_a56183e65b95474c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that generates an IT project plan template based on ARP Group Corporation's methodology. The code follows best practices and includes error handling.

```python
import json
from datetime import datetime
from typing import List, Dict, Union


class ITProjectPlan:
    """
    A class to represent an IT Project Plan template.
    Inspired by methodologies focused on timelines and budgets.
    """

    def __init__(self, project_name: str, start_date: str, end_date: str, budget: float):
        """
        Initialize the project plan with essential details.

        Args:
            project_name (str): Name of the project.
            start_date (str): Start date of the project (format: YYYY-MM-DD).
            end_date (str): End date of the project (format: YYYY-MM-DD).
            budget (float): Project budget in USD.
        """
        self.project_name = project_name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.budget = self._validate_budget(budget)
        self.phases: List[Dict[str, Union[str, float]]] = []  # List of project phases

    @staticmethod
    def _validate_date(date_str: str) -> str:
        """
        Validate date format.

        Args:
            date_str (str): Date string in the format YYYY-MM-DD.

        Returns:
            str: Validated date string.

        Raises:
            ValueError: If the date format is invalid.
        """
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD.")

    @staticmethod
    def _validate_budget(budget: float) -> float:
        """
        Validate budget input.

        Args:
            budget (float): Budget value.

        Returns:
            float: Validated budget.

        Raises:
            ValueError: If the budget is negative.
        """
        if budget < 0:
            raise ValueError("Budget cannot be negative.")
        return budget

    def add_phase(self, phase_name: str, description: str, duration_in_days: int, phase_budget: float):
        """
        Add a phase to the project plan.

        Args:
            phase_name (str): Name of the phase.
            description (str): Description of the phase.
            duration_in_days (int): Duration of the phase in days.
            phase_budget (float): Budget allocated for the phase in USD.

        Raises:
            ValueError: If the phase budget exceeds the total project budget.
        """
        if phase_budget > self.budget:
            raise ValueError(
                f"Phase budget ({phase_budget}) exceeds total project budget ({self.budget})."
            )

        phase = {
            "phase_name": phase_name,
            "description": description,
            "duration_in_days": duration_in_days,
            "phase_budget": phase_budget,
        }
        self.phases.append(phase)

    def generate_plan(self) -> Dict[str, Union[str, float, List[Dict[str, Union[str, float]]]]]:
        """
        Generate the complete project plan.

        Returns:
            dict: Project plan.
        """
        return {
            "project_name": self.project_name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "budget": self.budget,
            "phases": self.phases,
        }

    def export_to_json(self, file_path: str):
        """
        Export the project plan to a JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, "w") as json_file:
                json.dump(self.generate_plan(), json_file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write project plan to file: {e}")


if __name__ == "__main__":
    try:
        # Create a new project plan
        project = ITProjectPlan(
            project_name="New IT Infrastructure Project",
            start_date="2023-10-01",
            end_date="2024-01-01",
            budget=50000.00,
        )

        # Add phases to the project plan
        project.add_phase(
            phase_name="Requirement Analysis",
            description="Gathering requirements from stakeholders.",
            duration_in_days=30,
            phase_budget=10000.00,
        )
        project.add_phase(
            phase_name="Design",
            description="Designing the system architecture and user interfaces.",
            duration_in_days=45,
            phase_budget=15000.00,
        )
        project.add_phase(
            phase_name="Implementation",
            description="Developing and testing the system.",
            duration_in_days=60,
            phase_budget=20000.00,
        )
        project.add_phase(
            phase_name="Deployment",
            description="Deploying the system to production and training users.",
            duration_in_days=15,
            phase_budget=5000.00,
        )

        # Generate and export the project plan to JSON
        project.export_to_json("project_plan.json")
        print("Project plan successfully exported to project_plan.json")

    except Exception as e:
        print(f"Error: {e}")
```

This code can be run directly to create a project plan template, add phases, and export the plan to a JSON file.
