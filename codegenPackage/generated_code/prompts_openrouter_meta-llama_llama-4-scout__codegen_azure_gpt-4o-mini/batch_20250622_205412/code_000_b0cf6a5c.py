"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Write a Python script to manage safety and health coordination for construction projects, including risk assessment and mitigation strategies, inspired by the AFCO's guidelines.
Generated: DETERMINISTIC_b0cf6a5cdaff53c0
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SafetyHealthCoordinator:
    def __init__(self, project_name: str):
        """
        Initialize the SafetyHealthCoordinator with a project name.
        
        :param project_name: Name of the construction project
        """
        self.project_name = project_name
        self.risks: List[Dict[str, Any]] = []
        logging.info(f"Initialized SafetyHealthCoordinator for project: {self.project_name}")

    def add_risk(self, risk_description: str, likelihood: str, impact: str, mitigation_strategy: str):
        """
        Add a risk to the project with its details.
        
        :param risk_description: Description of the risk
        :param likelihood: Likelihood of the risk occurring (e.g., Low, Medium, High)
        :param impact: Impact of the risk (e.g., Low, Medium, High)
        :param mitigation_strategy: Strategy to mitigate the risk
        """
        risk = {
            "description": risk_description,
            "likelihood": likelihood,
            "impact": impact,
            "mitigation_strategy": mitigation_strategy
        }
        self.risks.append(risk)
        logging.info(f"Added risk: {risk}")

    def assess_risks(self) -> List[Dict[str, Any]]:
        """
        Assess all risks and return a summary of the risk assessment.
        
        :return: List of risks with their assessment
        """
        logging.info("Assessing risks...")
        risk_assessment = []
        for risk in self.risks:
            assessment = {
                "description": risk["description"],
                "likelihood": risk["likelihood"],
                "impact": risk["impact"],
                "mitigation_strategy": risk["mitigation_strategy"],
                "risk_level": self.calculate_risk_level(risk["likelihood"], risk["impact"])
            }
            risk_assessment.append(assessment)
        return risk_assessment

    @staticmethod
    def calculate_risk_level(likelihood: str, impact: str) -> str:
        """
        Calculate the risk level based on likelihood and impact.
        
        :param likelihood: Likelihood of the risk occurring
        :param impact: Impact of the risk
        :return: Overall risk level
        """
        risk_matrix = {
            "Low": {"Low": "Low", "Medium": "Medium", "High": "Medium"},
            "Medium": {"Low": "Medium", "Medium": "High", "High": "High"},
            "High": {"Low": "Medium", "Medium": "High", "High": "Critical"}
        }
        return risk_matrix.get(likelihood, {}).get(impact, "Unknown")

    def save_risks_to_file(self, filename: str):
        """
        Save the current risks to a JSON file.
        
        :param filename: Name of the file to save the risks
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.risks, file, indent=4)
            logging.info(f"Risks saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save risks to file: {e}")

    def load_risks_from_file(self, filename: str):
        """
        Load risks from a JSON file.
        
        :param filename: Name of the file to load the risks from
        """
        try:
            with open(filename, 'r') as file:
                self.risks = json.load(file)
            logging.info(f"Risks loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load risks from file: {e}")

if __name__ == "__main__":
    # Example usage of the SafetyHealthCoordinator
    coordinator = SafetyHealthCoordinator("Construction Project A")
    coordinator.add_risk("Fall from height", "High", "Critical", "Use harnesses and guardrails")
    coordinator.add_risk("Electrical shock", "Medium", "High", "Ensure proper grounding and training")
    
    risk_assessment = coordinator.assess_risks()
    print(json.dumps(risk_assessment, indent=4))

    # Save risks to a file
    coordinator.save_risks_to_file("risks.json")

    # Load risks from a file
    coordinator.load_risks_from_file("risks.json")
```
