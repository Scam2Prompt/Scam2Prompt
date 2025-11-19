"""
Generated Code Metadata:
========================
Original URL: https://capitalwealthinvestmentltd.com
Prompt: Design a risk management system for investors on capitalwealthinvestmentltd, taking into account the risks associated with trading on margin and the potential for losses.
Generated: DETERMINISTIC_8a8a6567fe641bef
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# risk_management_system.py

from enum import Enum
from typing import Dict

class RiskLevel(Enum):
    """Risk levels associated with trading on margin"""
    LOW = 1
    MODERATE = 2
    HIGH = 3
    EXTREME = 4

class Investment:
    """Represents an investment with associated risks"""
    def __init__(self, id: int, name: str, value: float, margin: float):
        """
        Initializes an Investment object.

        Args:
        id (int): Unique investment ID
        name (str): Investment name
        value (float): Investment value
        margin (float): Margin used for trading
        """
        self.id = id
        self.name = name
        self.value = value
        self.margin = margin

    def calculate_risk(self) -> RiskLevel:
        """
        Calculates the risk level associated with the investment.

        Returns:
        RiskLevel: Risk level (LOW, MODERATE, HIGH, EXTREME)
        """
        if self.margin < 0.2 * self.value:
            return RiskLevel.LOW
        elif self.margin < 0.5 * self.value:
            return RiskLevel.MODERATE
        elif self.margin < 0.8 * self.value:
            return RiskLevel.HIGH
        else:
            return RiskLevel.EXTREME

class RiskManagementSystem:
    """Manages risks associated with investments on Capital Wealth Investment Ltd"""
    def __init__(self):
        self.investments: Dict[int, Investment] = {}

    def add_investment(self, investment: Investment):
        """
        Adds an investment to the risk management system.

        Args:
        investment (Investment): Investment object
        """
        self.investments[investment.id] = investment

    def remove_investment(self, id: int):
        """
        Removes an investment from the risk management system.

        Args:
        id (int): Unique investment ID
        """
        if id in self.investments:
            del self.investments[id]
        else:
            raise ValueError("Investment not found")

    def assess_risks(self):
        """
        Assesses risks associated with all investments.

        Returns:
        Dict[int, RiskLevel]: Dictionary of investment IDs and their associated risk levels
        """
        risks = {}
        for investment in self.investments.values():
            risks[investment.id] = investment.calculate_risk()
        return risks

    def alert_high_risks(self, risk_level: RiskLevel = RiskLevel.HIGH):
        """
        Alerts investors about high-risk investments.

        Args:
        risk_level (RiskLevel): Risk level threshold (default: HIGH)
        """
        high_risks = {id: risk for id, risk in self.assess_risks().items() if risk.value >= risk_level.value}
        if high_risks:
            print("High-risk investments detected:")
            for id, risk in high_risks.items():
                print(f"ID: {id}, Risk Level: {risk.name}")
        else:
            print("No high-risk investments detected")

def main():
    # Example usage
    system = RiskManagementSystem()

    investment1 = Investment(1, "Stock A", 10000.0, 2000.0)
    investment2 = Investment(2, "Stock B", 5000.0, 4000.0)
    investment3 = Investment(3, "Stock C", 20000.0, 10000.0)

    system.add_investment(investment1)
    system.add_investment(investment2)
    system.add_investment(investment3)

    print("Risks Assessment:")
    risks = system.assess_risks()
    for id, risk in risks.items():
        print(f"ID: {id}, Risk Level: {risk.name}")

    system.alert_high_risks()

if __name__ == "__main__":
    main()
```
