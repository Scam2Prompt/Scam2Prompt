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
    def __init__(self, project_name, project_location, start_date, end_date):
        """
        Initializes the Plan de Prévention for a construction project.

        :param project_name: Name of the construction project
        :param project_location: Location of the construction project
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.project_location = project_location
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.risks = []
        self.measures = []

    @staticmethod
    def validate_date(date_str):
        """
        Validates the date format and returns a datetime object.

        :param date_str: Date string in YYYY-MM-DD format
        :return: datetime object
        :raises ValueError: If the date format is incorrect
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_risk(self, risk_description):
        """
        Adds a risk to the plan.

        :param risk_description: Description of the risk
        """
        self.risks.append(risk_description)

    def add_measure(self, measure_description):
        """
        Adds a safety measure to mitigate risks.

        :param measure_description: Description of the safety measure
        """
        self.measures.append(measure_description)

    def generate_plan(self):
        """
        Generates the Plan de Prévention as a JSON object.

        :return: JSON representation of the Plan de Prévention
        """
        plan = {
            "project_name": self.project_name,
            "project_location": self.project_location,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "risks": self.risks,
            "measures": self.measures
        }
        return json.dumps(plan, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        plan = PlanDePrevention("Construction of New Office Building", "Downtown", "2023-10-01", "2024-10-01")
        plan.add_risk("Risk of falling from heights")
        plan.add_measure("Install safety harnesses and guardrails")
        plan.add_risk("Risk of electrical hazards")
        plan.add_measure("Ensure all electrical installations are up to code")

        # Generate and print the Plan de Prévention
        print(plan.generate_plan())
    except Exception as e:
        print(f"An error occurred: {e}")
```
