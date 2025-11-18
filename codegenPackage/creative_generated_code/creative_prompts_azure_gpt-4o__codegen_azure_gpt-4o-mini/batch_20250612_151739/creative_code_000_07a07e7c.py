"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Write Python code to generate a risk prevention plan template for "Coordination SPS" as described by AFCO Fédération, including sections for construction, exploitation, and maintenance phases.
Generated: DETERMINISTIC_07a07e7c09159d98
Batch ID: 20250612_151739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List

class RiskPreventionPlan:
    """Class to generate a risk prevention plan template."""

    def __init__(self, title: str):
        """
        Initialize the RiskPreventionPlan with a title.

        Args:
            title (str): Title of the risk prevention plan.
        """
        self.title = title
        self.sections = {
            "Construction Phase": [],
            "Exploitation Phase": [],
            "Maintenance Phase": []
        }

    def add_risk(self, phase: str, risk: str, mitigation: str):
        """
        Add a risk and its mitigation plan to the specified phase.

        Args:
            phase (str): The phase to which the risk pertains.
            risk (str): Description of the risk.
            mitigation (str): Mitigation strategy for the risk.

        Raises:
            ValueError: If the phase is not valid.
        """
        if phase not in self.sections:
            raise ValueError(f"Invalid phase: '{phase}'. Valid phases are: {list(self.sections.keys())}")

        risk_entry = {
            "risk": risk,
            "mitigation": mitigation
        }
        self.sections[phase].append(risk_entry)

    def generate_template(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Generate the risk prevention plan template.

        Returns:
            dict: A dictionary representation of the risk prevention plan.
        """
        return {
            "title": self.title,
            "sections": self.sections
        }

    def save_to_file(self, filename: str):
        """
        Save the risk prevention plan template to a JSON file.

        Args:
            filename (str): The filename to save the plan to.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_template(), file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while saving the file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        plan = RiskPreventionPlan("Coordination SPS Risk Prevention Plan")
        plan.add_risk("Construction Phase", "Site Safety Hazards", "Conduct regular safety audits.")
        plan.add_risk("Exploitation Phase", "Operational Failures", "Implement a routine maintenance schedule.")
        plan.add_risk("Maintenance Phase", "Equipment Degradation", "Use quality materials and regular inspections.")

        plan.save_to_file("risk_prevention_plan.json")
        print("Risk prevention plan successfully created and saved.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
