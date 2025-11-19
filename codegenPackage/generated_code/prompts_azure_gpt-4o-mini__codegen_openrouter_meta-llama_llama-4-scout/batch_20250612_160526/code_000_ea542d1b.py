"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: Generate a code snippet that implements a risk management framework for a construction project, considering the unique challenges outlined by Carte Noir Consulting.
Generated: DETERMINISTIC_ea542d1b547cff30
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# risk_management_framework.py

from enum import Enum
from typing import List, Dict

class RiskCategory(Enum):
    """Risk categories for construction projects."""
    FINANCIAL = 1
    OPERATIONAL = 2
    ENVIRONMENTAL = 3
    SAFETY = 4
    STRATEGIC = 5

class Risk:
    """Represents a risk in the construction project."""
    def __init__(self, name: str, category: RiskCategory, likelihood: int, impact: int):
        """
        Initializes a Risk object.

        Args:
        - name (str): Risk name.
        - category (RiskCategory): Risk category.
        - likelihood (int): Risk likelihood (1-5).
        - impact (int): Risk impact (1-5).
        """
        self.name = name
        self.category = category
        self.likelihood = likelihood
        self.impact = impact

    def calculate_risk_score(self) -> int:
        """Calculates the risk score."""
        return self.likelihood * self.impact

class RiskManagementFramework:
    """Implements a risk management framework for construction projects."""
    def __init__(self):
        self.risks: List[Risk] = []

    def add_risk(self, risk: Risk):
        """Adds a risk to the framework."""
        self.risks.append(risk)

    def remove_risk(self, risk_name: str):
        """Removes a risk from the framework."""
        self.risks = [risk for risk in self.risks if risk.name != risk_name]

    def get_risks_by_category(self) -> Dict[RiskCategory, List[Risk]]:
        """Groups risks by category."""
        risks_by_category: Dict[RiskCategory, List[Risk]] = {}
        for risk in self.risks:
            if risk.category not in risks_by_category:
                risks_by_category[risk.category] = []
            risks_by_category[risk.category].append(risk)
        return risks_by_category

    def get_top_risks(self, n: int) -> List[Risk]:
        """Gets the top n risks with the highest scores."""
        sorted_risks = sorted(self.risks, key=lambda risk: risk.calculate_risk_score(), reverse=True)
        return sorted_risks[:n]

def main():
    # Example usage
    framework = RiskManagementFramework()

    risk1 = Risk("Delay in material delivery", RiskCategory.OPERATIONAL, 3, 4)
    risk2 = Risk("Cost overrun", RiskCategory.FINANCIAL, 2, 5)
    risk3 = Risk("Workplace accident", RiskCategory.SAFETY, 4, 3)

    framework.add_risk(risk1)
    framework.add_risk(risk2)
    framework.add_risk(risk3)

    print("Risks by category:")
    for category, risks in framework.get_risks_by_category().items():
        print(f"{category.name}:")
        for risk in risks:
            print(f"- {risk.name} (Score: {risk.calculate_risk_score()})")

    print("\nTop 3 risks:")
    for risk in framework.get_top_risks(3):
        print(f"- {risk.name} (Score: {risk.calculate_risk_score()})")

if __name__ == "__main__":
    main()
```
