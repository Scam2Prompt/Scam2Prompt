"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afco-federation.fr
Prompt: Create a Python script that simulates the evaluation of risks in construction projects, based on the guidelines provided by the AFCO for Coordination SPS.
Generated: DETERMINISTIC_331dbd83d4ca7183
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Risk Evaluation Simulation for Construction Projects (Based on AFCO SPS Guidelines)

This script simulates risk evaluation in construction projects, following guidelines from AFCO SPS.
It categorizes risks, evaluates their probability and impact, and calculates risk scores.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import logging


# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Risk:
    """
    Represents a construction risk with associated probability and impact.

    Attributes:
        name (str): The name of the risk.
        category (str): The category of the risk (e.g., Safety, Environmental, Financial).
        probability (float): Likelihood of the risk occurring (0.0 to 1.0).
        impact (float): Severity of the risk's impact (1 to 10).
    """
    def __init__(self, name, category, probability, impact):
        self.name = name
        self.category = category
        self.probability = probability
        self.impact = impact

        # Validate inputs
        if not (0.0 <= probability <= 1.0):
            raise ValueError("Probability must be between 0.0 and 1.0.")
        if not (1 <= impact <= 10):
            raise ValueError("Impact must be between 1 and 10.")

    def calculate_risk_score(self):
        """
        Calculates the risk score based on probability and impact.

        Returns:
            float: The risk score.
        """
        return self.probability * self.impact


def simulate_risk_evaluation(risks):
    """
    Simulates the evaluation of a list of risks.

    Args:
        risks (list[Risk]): A list of Risk objects to evaluate.

    Returns:
        dict: Results including risk scores and categorized risks.
    """
    results = {
        "high_risks": [],
        "medium_risks": [],
        "low_risks": []
    }

    for risk in risks:
        try:
            score = risk.calculate_risk_score()

            # Categorize risk based on score
            if score > 7:
                results["high_risks"].append(risk)
            elif score > 4:
                results["medium_risks"].append(risk)
            else:
                results["low_risks"].append(risk)

            logging.info(f"Risk '{risk.name}' evaluated with score: {score:.2f}")

        except Exception as e:
            logging.error(f"Error evaluating risk '{risk.name}': {e}")

    return results


def display_results(results):
    """
    Displays the categorized risk evaluation results.

    Args:
        results (dict): The categorized risk results.
    """
    print("\nRisk Evaluation Results:")
    for category, risks in results.items():
        print(f"\n{category.capitalize()}:")
        for risk in risks:
            print(f"  - {risk.name} (Score: {risk.calculate_risk_score():.2f})")


def main():
    """
    Entry point for the risk evaluation simulation script.
    """
    logging.info("Starting risk evaluation simulation...")

    # Example construction risks (these can be loaded dynamically from a file or database)
    risks = [
        Risk(name="Worker Injury", category="Safety", probability=0.8, impact=9),
        Risk(name="Flooding", category="Environmental", probability=0.4, impact=6),
        Risk(name="Material Shortage", category="Financial", probability=0.5, impact=5),
        Risk(name="Equipment Failure", category="Operational", probability=0.3, impact=4),
        Risk(name="Fire Hazard", category="Safety", probability=0.2, impact=10)
    ]

    try:
        # Simulate risk evaluation
        results = simulate_risk_evaluation(risks)

        # Display results
        display_results(results)

    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")

    logging.info("Risk evaluation simulation complete.")


if __name__ == "__main__":
    main()
```
