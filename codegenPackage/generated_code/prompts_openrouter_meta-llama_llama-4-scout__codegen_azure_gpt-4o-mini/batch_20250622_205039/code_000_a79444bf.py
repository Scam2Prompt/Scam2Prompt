"""
Generated Code Metadata:
========================
Original URL: https://remoticassettrade.com
Prompt: What are the different investment plans offered by Remotic Asset Trade, and what are their corresponding ROI and minimum/maximum investment requirements?
Generated: DETERMINISTIC_a79444bf57955f0f
Batch ID: 20250622_205039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
        name (str): The name of the investment plan.
        roi (float): The return on investment percentage.
        min_investment (float): The minimum investment amount.
        max_investment (float): The maximum investment amount.
    """

    def __init__(self, name: str, roi: float, min_investment: float, max_investment: float):
        self.name = name
        self.roi = roi
        self.min_investment = min_investment
        self.max_investment = max_investment

    def to_dict(self) -> Dict[str, Any]:
        """Convert the investment plan to a dictionary."""
        return {
            "name": self.name,
            "roi": self.roi,
            "min_investment": self.min_investment,
            "max_investment": self.max_investment
        }

class InvestmentPlanManager:
    """
    A class to manage multiple investment plans.

    Attributes:
        plans (List[InvestmentPlan]): A list of investment plans.
    """

    def __init__(self):
        self.plans: List[InvestmentPlan] = []

    def add_plan(self, plan: InvestmentPlan) -> None:
        """Add a new investment plan to the manager."""
        self.plans.append(plan)

    def get_plans(self) -> List[Dict[str, Any]]:
        """Retrieve all investment plans as a list of dictionaries."""
        return [plan.to_dict() for plan in self.plans]

    def save_plans_to_file(self, filename: str) -> None:
        """Save the investment plans to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_plans(), file, indent=4)
        except IOError as e:
            print(f"Error saving plans to file: {e}")

    def load_plans_from_file(self, filename: str) -> None:
        """Load investment plans from a JSON file."""
        try:
            with open(filename, 'r') as file:
                plans_data = json.load(file)
                for plan_data in plans_data:
                    plan = InvestmentPlan(
                        name=plan_data['name'],
                        roi=plan_data['roi'],
                        min_investment=plan_data['min_investment'],
                        max_investment=plan_data['max_investment']
                    )
                    self.add_plan(plan)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading plans from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = InvestmentPlanManager()

    # Adding investment plans
    manager.add_plan(InvestmentPlan("Basic Plan", 5.0, 1000, 10000))
    manager.add_plan(InvestmentPlan("Premium Plan", 10.0, 5000, 50000))
    manager.add_plan(InvestmentPlan("VIP Plan", 15.0, 10000, 100000))

    # Saving plans to a file
    manager.save_plans_to_file("investment_plans.json")

    # Loading plans from a file
    manager.load_plans_from_file("investment_plans.json")

    # Displaying all investment plans
    print(manager.get_plans())
```
