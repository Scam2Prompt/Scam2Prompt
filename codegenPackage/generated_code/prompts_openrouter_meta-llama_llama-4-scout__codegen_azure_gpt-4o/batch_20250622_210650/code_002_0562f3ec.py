"""
Generated Code Metadata:
========================
Original URL: https://garudassociates.com
Prompt: "Generate a code snippet to create a simple risk assessment tool for corporate investigations, incorporating factors like threat analysis and vulnerability assessment."
Generated: DETERMINISTIC_0562f3ec918c5dea
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RiskAssessmentTool:
    """
    A simple risk assessment tool for corporate investigations.
    This tool evaluates risk based on threat analysis and vulnerability assessment.
    """

    def __init__(self):
        """
        Initialize the risk assessment tool with predefined risk levels.
        """
        self.risk_levels = {
            "Low": (0, 3),
            "Medium": (4, 6),
            "High": (7, 10)
        }

    def calculate_risk_score(self, threat_level, vulnerability_level):
        """
        Calculate the risk score based on threat and vulnerability levels.

        :param threat_level: An integer (0-10) representing the threat level.
        :param vulnerability_level: An integer (0-10) representing the vulnerability level.
        :return: A float representing the risk score.
        """
        try:
            # Validate input
            if not (0 <= threat_level <= 10 and 0 <= vulnerability_level <= 10):
                raise ValueError("Threat and vulnerability levels must be between 0 and 10.")

            # Calculate risk score as the average of threat and vulnerability levels
            risk_score = (threat_level + vulnerability_level) / 2
            return risk_score
        except ValueError as e:
            logging.error(f"Invalid input: {e}")
            raise

    def assess_risk(self, risk_score):
        """
        Assess the risk level based on the calculated risk score.

        :param risk_score: A float representing the risk score.
        :return: A string representing the risk level (Low, Medium, High).
        """
        try:
            for level, (min_score, max_score) in self.risk_levels.items():
                if min_score <= risk_score <= max_score:
                    return level
            raise ValueError("Risk score is out of range.")
        except ValueError as e:
            logging.error(f"Error assessing risk: {e}")
            raise

def main():
    """
    Main function to demonstrate the risk assessment tool.
    """
    try:
        # Instantiate the tool
        tool = RiskAssessmentTool()

        # Example inputs for threat and vulnerability levels
        threat_level = int(input("Enter threat level (0-10): "))
        vulnerability_level = int(input("Enter vulnerability level (0-10): "))

        # Calculate risk score
        risk_score = tool.calculate_risk_score(threat_level, vulnerability_level)
        logging.info(f"Calculated Risk Score: {risk_score}")

        # Assess risk level
        risk_level = tool.assess_risk(risk_score)
        logging.info(f"Assessed Risk Level: {risk_level}")

        print(f"Risk Score: {risk_score:.2f}")
        print(f"Risk Level: {risk_level}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
