"""
Generated Code Metadata:
========================
Original URL: https://australiawidewealth.com
Prompt: Generate a financial planning roadmap for young families looking to secure their financial future while managing a tight budget, as described by Australia Wide Wealth Services.
Generated: DETERMINISTIC_572c57bde1387715
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Planning Roadmap for Young Families
Author: Australia Wide Wealth Services
Description: A financial planning tool to help young families manage budgets and secure their financial future.
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum, auto
import datetime

class PriorityLevel(Enum):
    """Priority levels for financial goals"""
    CRITICAL = auto()
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

@dataclass
class FinancialGoal:
    """Represents a financial goal with priority and timeline"""
    name: str
    priority: PriorityLevel
    target_amount: float
    target_year: int
    monthly_contribution: Optional[float] = None

@dataclass
class FamilyMember:
    """Represents a family member with income and expenses"""
    name: str
    age: int
    income: float  # Monthly income
    expenses: float  # Monthly expenses

@dataclass
class FinancialRoadmap:
    """Main class representing the financial roadmap"""
    family_members: List[FamilyMember]
    goals: List[FinancialGoal]
    emergency_fund: float
    current_savings: float

    def total_monthly_income(self) -> float:
        """Calculate total monthly income for the family"""
        return sum(member.income for member in self.family_members)

    def total_monthly_expenses(self) -> float:
        """Calculate total monthly expenses for the family"""
        return sum(member.expenses for member in self.family_members)

    def monthly_savings(self) -> float:
        """Calculate monthly savings after expenses"""
        return self.total_monthly_income() - self.total_monthly_expenses()

    def calculate_goal_contributions(self) -> Dict[str, float]:
        """
        Calculate recommended monthly contributions for each goal
        based on priority and available savings
        """
        available_savings = self.monthly_savings()
        if available_savings <= 0:
            raise ValueError("Monthly expenses exceed income. Cannot allocate savings.")

        # Sort goals by priority (critical first)
        sorted_goals = sorted(self.goals, key=lambda g: g.priority.value)

        allocations = {}
        remaining_savings = available_savings

        # Emergency fund gets first priority
        if self.emergency_fund > self.current_savings:
            emergency_needed = self.emergency_fund - self.current_savings
            emergency_contribution = min(emergency_needed, remaining_savings * 0.3)
            allocations["Emergency Fund"] = emergency_contribution
            remaining_savings -= emergency_contribution

        # Allocate to other goals
        for goal in sorted_goals:
            if remaining_savings <= 0:
                break

            years_to_goal = goal.target_year - datetime.datetime.now().year
            if years_to_goal <= 0:
                continue  # Skip past-due goals

            months_to_goal = years_to_goal * 12
            required_monthly = goal.target_amount / months_to_goal

            # Allocate based on priority
            if goal.priority == PriorityLevel.CRITICAL:
                allocation = min(required_monthly, remaining_savings * 0.5)
            elif goal.priority == PriorityLevel.HIGH:
                allocation = min(required_monthly, remaining_savings * 0.3)
            else:
                allocation = min(required_monthly, remaining_savings * 0.2)

            allocations[goal.name] = allocation
            remaining_savings -= allocation

        return allocations

    def to_json(self) -> str:
        """Serialize the roadmap to JSON"""
        data = {
            "family_members": [asdict(member) for member in self.family_members],
            "goals": [{
                **asdict(goal),
                "priority": goal.priority.name
            } for goal in self.goals],
            "emergency_fund": self.emergency_fund,
            "current_savings": self.current_savings,
            "monthly_summary": {
                "income": self.total_monthly_income(),
                "expenses": self.total_monthly_expenses(),
                "savings": self.monthly_savings()
            }
        }
        return json.dumps(data, indent=2)

def create_sample_roadmap() -> FinancialRoadmap:
    """Create a sample financial roadmap for demonstration"""
    family = [
        FamilyMember("Parent 1", 30, 5000, 3000),
        FamilyMember("Parent 2", 28, 4500, 2500),
        FamilyMember("Child", 3, 0, 500)
    ]

    goals = [
        FinancialGoal("House Deposit", PriorityLevel.CRITICAL, 80000, 2028),
        FinancialGoal("Education Fund", PriorityLevel.HIGH, 50000, 2035),
        FinancialGoal("Family Vacation", PriorityLevel.MEDIUM, 10000, 2025)
    ]

    return FinancialRoadmap(
        family_members=family,
        goals=goals,
        emergency_fund=20000,
        current_savings=5000
    )

if __name__ == "__main__":
    try:
        roadmap = create_sample_roadmap()
        print("=== Financial Roadmap ===")
        print(f"Monthly Income: ${roadmap.total_monthly_income():,.2f}")
        print(f"Monthly Expenses: ${roadmap.total_monthly_expenses():,.2f}")
        print(f"Monthly Savings: ${roadmap.monthly_savings():,.2f}")
        
        print("\n=== Recommended Goal Contributions ===")
        contributions = roadmap.calculate_goal_contributions()
        for goal, amount in contributions.items():
            print(f"{goal}: ${amount:,.2f}")

        print("\n=== JSON Representation ===")
        print(roadmap.to_json())

    except ValueError as e:
        print(f"Error in financial planning: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
