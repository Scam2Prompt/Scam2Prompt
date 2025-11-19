"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write Python code to generate a risk prevention plan template for "Coordination SPS" as described by AFCO Fédération, including sections for construction, exploitation, and maintenance phases.
Generated: DETERMINISTIC_07a07e7c09159d98
Batch ID: 20250612_151739
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

class RiskPreventionPlan:
    """
    A class to represent a Risk Prevention Plan for Coordination SPS.
    """

    def __init__(self, project_name):
        """
        Initializes the Risk Prevention Plan with a project name and current date.

        :param project_name: Name of the project for which the plan is created.
        """
        self.project_name = project_name
        self.date_created = datetime.now().strftime("%Y-%m-%d")
        self.sections = {
            "Construction Phase": [],
            "Exploitation Phase": [],
            "Maintenance Phase": []
        }

    def add_risk(self, phase, risk_description, mitigation_strategy):
        """
        Adds a risk to the specified phase of the plan.

        :param phase: The phase to which the risk is being added.
        :param risk_description: Description of the risk.
        :param mitigation_strategy: Strategy to mitigate the risk.
        """
        if phase not in self.sections:
            raise ValueError(f"Invalid phase: {phase}. Valid phases are: {list(self.sections.keys())}")

        risk_entry = {
            "risk_description": risk_description,
            "mitigation_strategy": mitigation_strategy
        }
        self.sections[phase].append(risk_entry)

    def generate_template(self):
        """
        Generates a risk prevention plan template as a dictionary.

        :return: A dictionary representation of the risk prevention plan.
        """
        template = {
            "project_name": self.project_name,
            "date_created": self.date_created,
            "sections": self.sections
        }
        return template

    def save_to_file(self, filename):
        """
        Saves the risk prevention plan template to a JSON file.

        :param filename: The name of the file to save the plan to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_template(), file, indent=4)
            print(f"Risk prevention plan saved to {filename}.")
        except IOError as e:
            print(f"Error saving file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    try:
        plan = RiskPreventionPlan("Coordination SPS Project")
        plan.add_risk("Construction Phase", "Delay in material delivery", "Establish contracts with multiple suppliers")
        plan.add_risk("Exploitation Phase", "Equipment failure", "Regular maintenance checks and immediate repairs")
        plan.add_risk("Maintenance Phase", "Inadequate staff training", "Implement a comprehensive training program")

        # Save the plan to a file
        plan.save_to_file("risk_prevention_plan.json")
    except Exception as e:
        print(f"An error occurred: {e}")
```
