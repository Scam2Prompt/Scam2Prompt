"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stowawaypay.com
Prompt: Write a program that integrates a savings goal feature with partner monetization options, reflecting the business model of StowAwayPay.com.
Generated: DETERMINISTIC_7d22fc1ee290324b
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class SavingsGoal:
    def __init__(self, name: str, target_amount: float, current_amount: float = 0.0):
        """Initialize a savings goal with a name, target amount, and current amount."""
        self.name = name
        self.target_amount = target_amount
        self.current_amount = current_amount

    def add_funds(self, amount: float) -> None:
        """Add funds to the current amount, ensuring it's not negative."""
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self.current_amount += amount

    def is_goal_reached(self) -> bool:
        """Check if the savings goal has been reached."""
        return self.current_amount >= self.target_amount

    def progress(self) -> Dict[str, Any]:
        """Return the progress of the savings goal as a percentage."""
        if self.target_amount <= 0:
            raise ValueError("Target amount must be greater than zero.")
        return {
            "goal": self.name,
            "current_amount": self.current_amount,
            "target_amount": self.target_amount,
            "percentage_complete": (self.current_amount / self.target_amount) * 100
        }


class PartnerMonetization:
    def __init__(self):
        """Initialize a list to store partner monetization options."""
        self.partners: List[Dict[str, Any]] = []

    def add_partner(self, name: str, revenue_share: float) -> None:
        """Add a partner's monetization option with their revenue share."""
        if revenue_share < 0 or revenue_share > 100:
            raise ValueError("Revenue share must be between 0 and 100.")
        self.partners.append({"name": name, "revenue_share": revenue_share})

    def get_partners(self) -> List[Dict[str, Any]]:
        """Get a list of all partners with their revenue shares."""
        return self.partners

    def total_revenue_shares(self) -> float:
        """Calculate the total revenue shares of all partners."""
        return sum(partner["revenue_share"] for partner in self.partners)


class SavingsApp:
    def __init__(self):
        """Initialize the Savings Application with savings goals and partners."""
        self.savings_goals: List[SavingsGoal] = []
        self.partner_monetization = PartnerMonetization()

    def create_savings_goal(self, name: str, target_amount: float) -> SavingsGoal:
        """Create and store a new savings goal."""
        goal = SavingsGoal(name, target_amount)
        self.savings_goals.append(goal)
        return goal

    def add_funds_to_goal(self, goal_name: str, amount: float) -> None:
        """Add funds to a specific savings goal by name."""
        goal = self.find_goal(goal_name)
        goal.add_funds(amount)

    def find_goal(self, goal_name: str) -> SavingsGoal:
        """Find a savings goal by name."""
        for goal in self.savings_goals:
            if goal.name == goal_name:
                return goal
        raise ValueError(f"Savings goal '{goal_name}' not found.")

    def add_partner(self, name: str, revenue_share: float) -> None:
        """Add a monetization partner to the application."""
        self.partner_monetization.add_partner(name, revenue_share)

    def get_savings_goals_progress(self) -> List[Dict[str, Any]]:
        """Get the progress of all savings goals."""
        return [goal.progress() for goal in self.savings_goals]


# Example usage:
if __name__ == "__main__":
    try:
        app = SavingsApp()
        app.create_savings_goal("Vacation Fund", 3000)
        app.add_funds_to_goal("Vacation Fund", 500)
        app.add_partner("StowAwayPay", 15)

        # Display progress of savings goals
        progress = app.get_savings_goals_progress()
        print(json.dumps(progress, indent=2))

        # Display partners
        partners = app.partner_monetization.get_partners()
        print(json.dumps(partners, indent=2))

    except ValueError as e:
        print(f"Error: {e}")
```
