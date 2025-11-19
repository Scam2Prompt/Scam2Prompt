"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Write a code snippet that generates a Plan de Prévention for managing Sécurité et Santé au Travail (SST) in construction projects, incorporating the principles of "Construire, Exploiter, Maintenir."
Generated: DETERMINISTIC_3dcfb21f6232b074
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class ConstructionSafetyPlan:
    """
    A class to generate and manage a 'Plan de Prévention' for Sécurité et Santé au Travail (SST) 
    in construction projects, incorporating the principles of 'Construire, Exploiter, Maintenir'.
    """

    def __init__(self, project_name, stakeholders):
        """
        Initialize the safety plan with project details and stakeholders.

        :param project_name: Name of the construction project.
        :param stakeholders: List of stakeholders involved in the project.
        """
        self.project_name = project_name
        self.stakeholders = stakeholders
        self.created_at = datetime.now()
        self.plan = {
            "project_name": project_name,
            "stakeholders": stakeholders,
            "principles": ["Construire", "Exploiter", "Maintenir"],
            "safety_measures": [],
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

    def add_safety_measure(self, description, responsible_party):
        """
        Add a safety measure to the plan.

        :param description: Description of the safety measure.
        :param responsible_party: Party responsible for implementing the safety measure.
        """
        if not description or not responsible_party:
            raise ValueError("Description and responsible party must be provided.")

        measure = {
            "description": description,
            "responsible_party": responsible_party,
            "added_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.plan["safety_measures"].append(measure)

    def export_plan(self, file_path):
        """
        Export the 'Plan de Prévention' to a JSON file.

        :param file_path: File path to save the exported plan.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.plan, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to export plan to file: {file_path}. Error: {str(e)}")

    def display_plan(self):
        """
        Display the 'Plan de Prévention' in a readable format.
        """
        print(json.dumps(self.plan, indent=4))


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the safety plan
        project_name = "Construction of Residential Building"
        stakeholders = ["Builder", "Architect", "Safety Officer", "Workers"]
        safety_plan = ConstructionSafetyPlan(project_name, stakeholders)

        # Add safety measures
        safety_plan.add_safety_measure(
            description="Provide protective gear to all workers",
            responsible_party="Safety Officer"
        )
        safety_plan.add_safety_measure(
            description="Ensure regular safety training sessions",
            responsible_party="Builder"
        )

        # Display the plan
        print("\nGenerated 'Plan de Prévention':")
        safety_plan.display_plan()

        # Export the plan to a JSON file
        file_path = "safety_plan.json"
        safety_plan.export_plan(file_path)
        print(f"\n'Safety plan exported successfully to {file_path}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
