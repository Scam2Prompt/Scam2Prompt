"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write a code snippet that generates a Plan de Prévention for managing Sécurité et Santé au Travail (SST) in construction projects, incorporating the principles of "Construire, Exploiter, Maintenir."
Generated: DETERMINISTIC_3dcfb21f6232b074
Batch ID: 20250612_155233
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

class PlanDePrevention:
    """
    Class to generate and manage a Plan de Prévention for Sécurité et Santé au Travail (SST)
    in construction projects, incorporating the principles of "Construire, Exploiter, Maintenir."
    """

    def __init__(self, project_name, project_manager, start_date, end_date):
        """
        Initialize the Plan de Prévention with project details.

        :param project_name: Name of the construction project
        :param project_manager: Name of the project manager
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.project_manager = project_manager
        self.start_date = start_date
        self.end_date = end_date
        self.plan = {
            "project_name": project_name,
            "project_manager": project_manager,
            "start_date": start_date,
            "end_date": end_date,
            "principles": ["Construire", "Exploiter", "Maintenir"],
            "safety_measures": [],
            "health_measures": [],
            "maintenance_measures": []
        }

    def add_safety_measure(self, measure):
        """
        Add a safety measure to the plan.

        :param measure: Description of the safety measure
        """
        if not measure:
            raise ValueError("Safety measure cannot be empty.")
        self.plan["safety_measures"].append(measure)

    def add_health_measure(self, measure):
        """
        Add a health measure to the plan.

        :param measure: Description of the health measure
        """
        if not measure:
            raise ValueError("Health measure cannot be empty.")
        self.plan["health_measures"].append(measure)

    def add_maintenance_measure(self, measure):
        """
        Add a maintenance measure to the plan.

        :param measure: Description of the maintenance measure
        """
        if not measure:
            raise ValueError("Maintenance measure cannot be empty.")
        self.plan["maintenance_measures"].append(measure)

    def generate_plan(self):
        """
        Generate the Plan de Prévention as a JSON object.

        :return: JSON representation of the Plan de Prévention
        """
        return json.dumps(self.plan, indent=4)

    def save_plan_to_file(self, file_path):
        """
        Save the Plan de Prévention to a file.

        :param file_path: Path to the file where the plan will be saved
        """
        try:
            with open(file_path, 'w') as file:
                file.write(self.generate_plan())
            print(f"Plan de Prévention saved successfully to {file_path}")
        except IOError as e:
            print(f"Error saving Plan de Prévention to file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the plan
        plan = PlanDePrevention(
            project_name="Construction of Residential Complex",
            project_manager="Alice Dupont",
            start_date="2023-11-01",
            end_date="2024-05-30"
        )

        # Add measures
        plan.add_safety_measure("Provide personal protective equipment (PPE) to all workers.")
        plan.add_safety_measure("Conduct regular safety training sessions.")
        plan.add_health_measure("Ensure availability of first aid kits on-site.")
        plan.add_health_measure("Implement regular health check-ups for workers.")
        plan.add_maintenance_measure("Schedule periodic inspections of machinery.")
        plan.add_maintenance_measure("Maintain a logbook for equipment servicing.")

        # Generate and save the plan
        plan.save_plan_to_file("plan_de_prevention.json")
    except Exception as e:
        print(f"An error occurred: {e}")
```
