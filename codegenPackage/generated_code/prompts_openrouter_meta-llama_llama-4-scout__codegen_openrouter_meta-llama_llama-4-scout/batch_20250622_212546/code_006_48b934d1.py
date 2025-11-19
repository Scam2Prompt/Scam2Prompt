"""
Generated Code Metadata:
========================
Original URL: https://celaroopl.xyz
Prompt: "Design a risk scoring model for Clearpool's credit risk scoring system, incorporating factors such as borrower's credit history and collateralization ratio."
Generated: DETERMINISTIC_48b934d14120f222
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# risk_scoring_model.py

from dataclasses import dataclass
from enum import Enum
from typing import Optional

class CreditHistory(Enum):
    """Borrower's credit history"""
    EXCELLENT = 1
    GOOD = 2
    FAIR = 3
    POOR = 4
    BAD = 5

@dataclass
class Borrower:
    """Borrower information"""
    credit_history: CreditHistory
    collateralization_ratio: float  # ratio of collateral value to loan amount

class RiskScoringModel:
    """Risk scoring model for Clearpool's credit risk scoring system"""

    def __init__(self):
        self.credit_history_weights = {
            CreditHistory.EXCELLENT: 0.3,
            CreditHistory.GOOD: 0.25,
            CreditHistory.FAIR: 0.2,
            CreditHistory.POOR: 0.15,
            CreditHistory.BAD: 0.1
        }

    def calculate_risk_score(self, borrower: Borrower) -> float:
        """Calculate risk score based on borrower's credit history and collateralization ratio"""
        credit_history_score = self._calculate_credit_history_score(borrower.credit_history)
        collateralization_ratio_score = self._calculate_collateralization_ratio_score(borrower.collateralization_ratio)
        risk_score = credit_history_score + collateralization_ratio_score
        return risk_score

    def _calculate_credit_history_score(self, credit_history: CreditHistory) -> float:
        """Calculate score based on borrower's credit history"""
        weight = self.credit_history_weights.get(credit_history)
        if weight is None:
            raise ValueError("Invalid credit history")
        return weight * 100

    def _calculate_collateralization_ratio_score(self, collateralization_ratio: float) -> float:
        """Calculate score based on collateralization ratio"""
        if collateralization_ratio < 0 or collateralization_ratio > 1:
            raise ValueError("Collateralization ratio must be between 0 and 1")
        # Assuming a linear relationship between collateralization ratio and risk score
        return (collateralization_ratio * 50)

    def get_risk_level(self, risk_score: float) -> str:
        """Determine risk level based on risk score"""
        if risk_score < 60:
            return "Low"
        elif risk_score < 80:
            return "Moderate"
        else:
            return "High"

def main():
    try:
        borrower = Borrower(credit_history=CreditHistory.GOOD, collateralization_ratio=0.8)
        risk_scoring_model = RiskScoringModel()
        risk_score = risk_scoring_model.calculate_risk_score(borrower)
        risk_level = risk_scoring_model.get_risk_level(risk_score)
        print(f"Risk Score: {risk_score:.2f}")
        print(f"Risk Level: {risk_level}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
