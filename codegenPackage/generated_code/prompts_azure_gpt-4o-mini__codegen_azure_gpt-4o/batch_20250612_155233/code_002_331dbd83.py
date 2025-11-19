"""
Generated Code Metadata:
========================
Original URL: https://afco-federation.fr
Prompt: Create a Python script that simulates the evaluation of risks in construction projects, based on the guidelines provided by the AFCO for Coordination SPS.
Generated: DETERMINISTIC_331dbd83d4ca7183
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class RiskEvaluation:
    """
    A class to simulate the evaluation of risks in construction projects
    based on AFCO guidelines for Coordination SPS.
    """

    def __init__(self):
        """
        Initialize the RiskEvaluation class with predefined risk categories.
        """
        self.risk_categories = {
            "Safety": ["Falls from height", "Electrocution", "Machinery accidents"],
            "Health": ["Exposure to hazardous materials", "Noise pollution", "Vibration injuries"],
            "Environmental": ["Soil contamination", "Air pollution", "Water pollution"],
            "Economic": ["Budget overruns", "Delays", "Material shortages"]
        }

    def evaluate_risk(self, category, likelihood, impact):
        """
        Evaluate the risk based on its category, likelihood, and impact.

        Parameters:
            category (str): The risk category (e.g., "Safety", "Health").
            likelihood (int): Likelihood of the risk occurring (1-5 scale).
            impact (int): Impact of the risk if it occurs (1-5 scale).

        Returns:
            dict: A dictionary containing the risk evaluation details.
        """
        if category not in self.risk_categories:
            raise ValueError(f"Invalid risk category: {category}. Valid categories are: {list(self.risk_categories.keys())}")

        if not (1 <= likelihood <= 5):
            raise ValueError("Likelihood must be between 1 and 5.")

        if not (1 <= impact <= 5):
            raise ValueError("Impact must be between 1 and 5.")

        # Calculate risk score (likelihood * impact)
        risk_score = likelihood * impact

        # Determine risk level based on score
        if risk_score <= 6:
            risk_level = "Low"
        elif 7 <= risk_score <= 15:
            risk_level = "Medium"
        else:
            risk_level = "High"

        return {
            "Category": category,
            "Likelihood": likelihood,
            "Impact": impact,
            "Risk Score": risk_score,
            "Risk Level": risk_level
        }

    def list_risks(self):
        """
        List all predefined risks in each category.

        Returns:
            dict: A dictionary containing risk categories and their associated risks.
        """
        return self.risk_categories


def main():
    """
    Main function to simulate risk evaluation in construction projects.
    """
    logging.info("Starting risk evaluation simulation...")

    # Create an instance of RiskEvaluation
    risk_evaluator = RiskEvaluation()

    # List predefined risks
    logging.info("Listing predefined risks...")
    predefined_risks = risk_evaluator.list_risks()
    for category, risks in predefined_risks.items():
        logging.info(f"{category}: {', '.join(risks)}")

    # Simulate risk evaluation
    try:
        logging.info("Evaluating a sample risk...")
        sample_risk = risk_evaluator.evaluate_risk(category="Safety", likelihood=4, impact=5)
        logging.info(f"Risk Evaluation Result: {sample_risk}")
    except ValueError as e:
        logging.error(f"Error during risk evaluation: {e}")

    logging.info("Risk evaluation simulation completed.")


if __name__ == "__main__":
    main()
```
