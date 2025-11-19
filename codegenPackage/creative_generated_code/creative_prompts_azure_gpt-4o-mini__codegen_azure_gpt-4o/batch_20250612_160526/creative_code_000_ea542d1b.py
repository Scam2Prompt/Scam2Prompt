"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartenoir.org
Prompt: Generate a code snippet that implements a risk management framework for a construction project, considering the unique challenges outlined by Carte Noir Consulting.
Generated: DETERMINISTIC_ea542d1b547cff30
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Risk Management Framework for Construction Project
This script implements a risk management framework that identifies, assesses, mitigates, 
and monitors risks in a construction project. It considers unique challenges outlined 
by Carte Noir Consulting.

Author: Expert Developer
Date: YYYY-MM-DD
"""

import logging
import json

# Configure logging for error handling and system monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class RiskManagementFramework:
    """
    A class to implement risk management tasks for construction projects.
    """

    def __init__(self):
        """
        Initialize the framework with default risk categories.
        """
        self.risks = []
        self.categories = ["Safety", "Budget", "Schedule", "Quality", "Environmental"]

    def add_risk(self, description, category, likelihood, impact):
        """
        Add a risk to the framework.

        :param description: Description of the risk
        :param category: Category of the risk (e.g., "Safety", "Budget")
        :param likelihood: Likelihood of the risk occurring (1-5)
        :param impact: Impact of the risk (1-5)
        """
        if category not in self.categories:
            logging.error(f"Invalid risk category: {category}")
            raise ValueError(f"Invalid risk category. Valid categories are: {', '.join(self.categories)}")

        risk = {
            "description": description,
            "category": category,
            "likelihood": likelihood,
            "impact": impact,
            "score": likelihood * impact,  # Risk score = likelihood * impact
        }
        self.risks.append(risk)
        logging.info(f"Risk added: {description}")

    def prioritize_risks(self):
        """
        Prioritize risks based on their risk score (descending order).
        
        :return: List of risks sorted by priority (highest risk score first).
        """
        return sorted(self.risks, key=lambda x: x["score"], reverse=True)

    def suggest_mitigation(self, risk):
        """
        Suggest mitigation strategies based on the risk category.

        :param risk: Risk dictionary containing details about the risk.
        :return: Suggested mitigation actions.
        """
        mitigation_strategies = {
            "Safety": "Implement strict safety protocols and training.",
            "Budget": "Increase contingency funds and monitor expenses closely.",
            "Schedule": "Develop a detailed project timeline with buffers.",
            "Quality": "Enforce quality control checks and supplier vetting.",
            "Environmental": "Conduct environmental impact assessments and use sustainable practices.",
        }

        return mitigation_strategies.get(risk["category"], "No mitigation strategy available.")

    def generate_report(self, file_path="risk_report.json"):
        """
        Generate a risk report in JSON format.

        :param file_path: Path to save the risk report.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.risks, file, indent=4)
            logging.info(f"Risk report generated at: {file_path}")
        except Exception as e:
            logging.error("Failed to generate risk report.")
            logging.error(e)
            raise

# Example usage
if __name__ == "__main__":
    framework = RiskManagementFramework()

    try:
        # Adding risks
        framework.add_risk("Worker falls from height", "Safety", 4, 5)
        framework.add_risk("Material cost overruns", "Budget", 3, 4)
        framework.add_risk("Delay due to weather", "Schedule", 2, 5)
        framework.add_risk("Supplier delivers substandard materials", "Quality", 3, 3)

        # Prioritizing risks
        prioritized_risks = framework.prioritize_risks()
        for risk in prioritized_risks:
            logging.info(f"Risk: {risk['description']} | Score: {risk['score']}")
            mitigation = framework.suggest_mitigation(risk)
            logging.info(f"Suggested Mitigation: {mitigation}")

        # Generating report
        framework.generate_report()
        
    except Exception as e:
        logging.error("An error occurred during risk management execution.")
        logging.error(e)
```
