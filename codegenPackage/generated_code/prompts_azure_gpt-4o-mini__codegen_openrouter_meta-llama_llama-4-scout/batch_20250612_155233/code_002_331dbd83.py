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
# risk_evaluator.py

"""
Simulates the evaluation of risks in construction projects based on AFCO for Coordination SPS guidelines.

Classes:
    RiskEvaluator
    Risk

Exceptions:
    RiskEvaluationError
"""

import enum
from typing import List, Dict

class RiskLevel(enum.Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Risk:
    def __init__(self, name: str, likelihood: int, impact: int):
        """
        Initialize a Risk object.

        Args:
        - name (str): The name of the risk.
        - likelihood (int): The likelihood of the risk occurring (1-5).
        - impact (int): The potential impact of the risk (1-5).
        """
        self.name = name
        self.likelihood = likelihood
        self.impact = impact

    def calculate_risk_level(self) -> RiskLevel:
        """
        Calculate the risk level based on likelihood and impact.

        Returns:
        - RiskLevel: The calculated risk level.
        """
        risk_score = self.likelihood * self.impact
        if risk_score <= 6:
            return RiskLevel.LOW
        elif risk_score <= 12:
            return RiskLevel.MEDIUM
        else:
            return RiskLevel.HIGH

class RiskEvaluator:
    def __init__(self):
        """
        Initialize a RiskEvaluator object.
        """
        self.risks: List[Risk] = []

    def add_risk(self, risk: Risk):
        """
        Add a risk to the evaluator.

        Args:
        - risk (Risk): The risk to add.
        """
        self.risks.append(risk)

    def evaluate_risks(self) -> Dict[str, RiskLevel]:
        """
        Evaluate all risks and return a dictionary with risk names and levels.

        Returns:
        - Dict[str, RiskLevel]: A dictionary with risk names and levels.
        """
        risk_levels = {}
        for risk in self.risks:
            try:
                risk_level = risk.calculate_risk_level()
                risk_levels[risk.name] = risk_level
            except Exception as e:
                raise RiskEvaluationError(f"Error evaluating risk {risk.name}: {str(e)}")
        return risk_levels

class RiskEvaluationError(Exception):
    """
    Exception raised when there is an error evaluating risks.
    """

def main():
    # Create a risk evaluator
    evaluator = RiskEvaluator()

    # Create risks
    risk1 = Risk("Delay in material delivery", 3, 4)
    risk2 = Risk("Insufficient labor", 2, 5)
    risk3 = Risk("Weather conditions", 4, 3)

    # Add risks to evaluator
    evaluator.add_risk(risk1)
    evaluator.add_risk(risk2)
    evaluator.add_risk(risk3)

    # Evaluate risks
    try:
        risk_levels = evaluator.evaluate_risks()
        print("Risk Levels:")
        for risk, level in risk_levels.items():
            print(f"{risk}: {level.name}")
    except RiskEvaluationError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
