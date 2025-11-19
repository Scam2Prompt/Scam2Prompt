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
from typing import List, Dict

class PreventionPlan:
    def __init__(self, project_name: str, location: str, start_date: str):
        """
        Initializes a new Prevention Plan for a construction project.

        :param project_name: Name of the construction project
        :param location: Location of the construction site
        :param start_date: Start date of the project in the format 'YYYY-MM-DD'
        """
        self.project_name = project_name
        self.location = location
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.risks: List[Dict[str, str]] = []
        self.measures: List[Dict[str, str]] = []

    def add_risk(self, risk_description: str, severity: str):
        """
        Adds a risk to the prevention plan.

        :param risk_description: Description of the risk
        :param severity: Severity of the risk
        """
        self.risks.append({
            'description': risk_description,
            'severity': severity
        })

    def add_measures(self, measure_description: str, responsible: str):
        """
        Adds a safety measure to mitigate risks.

        :param measure_description: Description of the safety measure
        :param responsible: Person or role responsible for the measure
        """
        self.measures.append({
            'description': measure_description,
            'responsible': responsible
        })

    def generate_plan(self) -> Dict:
        """
        Generates the prevention plan as a dictionary.

        :return: A dictionary representation of the prevention plan
        """
        return {
            'project_name': self.project_name,
            'location': self.location,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'risks': self.risks,
            'measures': self.measures,
            'principles': {
                'Construire': self._add_construire_principles(),
                'Exploiter': self._add_exploiter_principles(),
                'Maintenir': self._add_maintenir_principles()
            }
        }

    def _add_construire_principles(self) -> str:
        return "Ensure that construction techniques and materials meet safety standards."

    def _add_exploiter_principles(self) -> str:
        return "Establish protocols for operating equipment safely to prevent accidents."

    def _add_maintenir_principles(self) -> str:
        return "Regular maintenance checks must be performed to uphold safety standards."

    def save_to_file(self, filename: str):
        """
        Saves the prevention plan to a JSON file.

        :param filename: The name of the file to save the plan to
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_plan(), file, indent=4)
            print(f"Prevention plan saved to {filename}")
        except IOError as e:
            print(f"Error saving the prevention plan: {e}")

# Example usage
if __name__ == "__main__":
    plan = PreventionPlan("Build Project A", "Location X", "2023-10-01")
    plan.add_risk("Fall from height", "High")
    plan.add_measures("Use safety harnesses", "Site Supervisor")
    
    plan.save_to_file("prevention_plan.json")
```
