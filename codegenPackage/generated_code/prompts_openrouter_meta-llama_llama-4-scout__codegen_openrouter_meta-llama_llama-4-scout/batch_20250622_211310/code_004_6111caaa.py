"""
Generated Code Metadata:
========================
Original URL: https://immediate-unity-profit.com
Prompt: Design a system to match individuals with suitable investment education firms based on their preferences and budget, similar to the Juros Xyro platform, and provide a high-level architecture for the system.
Generated: DETERMINISTIC_6111caaa9b24b5f0
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_matching_system.py

from typing import Dict, List
from enum import Enum
from pydantic import BaseModel, ValidationError

class InvestmentType(str, Enum):
    """Types of investments"""
    STOCKS = "stocks"
    BONDS = "bonds"
    REAL_ESTATE = "real_estate"
    CRYPTO = "crypto"

class UserPreference(BaseModel):
    """User investment preferences"""
    investment_type: InvestmentType
    budget: float
    risk_tolerance: str

class EducationFirm(BaseModel):
    """Investment education firm details"""
    name: str
    investment_type: InvestmentType
    min_budget: float
    max_budget: float
    rating: float

class MatchingSystem:
    """Matches users with suitable investment education firms"""
    def __init__(self):
        self.firms: List[EducationFirm] = []

    def add_firm(self, firm: EducationFirm):
        """Add an education firm to the system"""
        self.firms.append(firm)

    def match(self, user_preference: UserPreference) -> List[EducationFirm]:
        """Match a user with suitable education firms"""
        suitable_firms = [
            firm for firm in self.firms 
            if firm.investment_type == user_preference.investment_type 
            and firm.min_budget <= user_preference.budget <= firm.max_budget
        ]
        return suitable_firms

def main():
    try:
        # Initialize the matching system
        system = MatchingSystem()

        # Add education firms
        firm1 = EducationFirm(
            name="Firm 1",
            investment_type=InvestmentType.STOCKS,
            min_budget=1000.0,
            max_budget=10000.0,
            rating=4.5
        )
        firm2 = EducationFirm(
            name="Firm 2",
            investment_type=InvestmentType.BONDS,
            min_budget=500.0,
            max_budget=5000.0,
            rating=4.0
        )
        firm3 = EducationFirm(
            name="Firm 3",
            investment_type=InvestmentType.STOCKS,
            min_budget=5000.0,
            max_budget=20000.0,
            rating=4.8
        )
        system.add_firm(firm1)
        system.add_firm(firm2)
        system.add_firm(firm3)

        # User preference
        user_preference = UserPreference(
            investment_type=InvestmentType.STOCKS,
            budget=5000.0,
            risk_tolerance="medium"
        )

        # Match user with suitable firms
        suitable_firms = system.match(user_preference)

        # Print suitable firms
        print("Suitable Firms:")
        for firm in suitable_firms:
            print(f"Name: {firm.name}, Rating: {firm.rating}")

    except ValidationError as e:
        print(f"Validation Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
