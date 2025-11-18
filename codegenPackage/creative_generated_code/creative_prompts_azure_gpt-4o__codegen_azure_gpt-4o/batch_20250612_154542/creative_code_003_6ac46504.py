"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coniproasset.com
Prompt: Provide a Python script to simulate weekly ROI calculations for investment plans like those offered by Coni Pro Asset, including beginner, starter, silver, and gold plans.
Generated: DETERMINISTIC_6ac4650496495edf
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to simulate weekly ROI calculations for investment plans.
Plans include Beginner, Starter, Silver, and Gold.
Each plan has a different investment range and weekly ROI percentage.
"""

# Import libraries
import sys
from typing import List, Dict

class InvestmentPlan:
    """
    A class to represent an investment plan and calculate weekly ROI.
    """
    def __init__(self, name: str, min_investment: float, max_investment: float, weekly_roi_percentage: float):
        """
        Initialize an investment plan.
        :param name: Name of the investment plan (e.g., Beginner, Starter, etc.)
        :param min_investment: Minimum investment amount for the plan
        :param max_investment: Maximum investment amount for the plan
        :param weekly_roi_percentage: Weekly ROI percentage for the plan
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.weekly_roi_percentage = weekly_roi_percentage

    def calculate_roi(self, investment_amount: float) -> float:
        """
        Calculate the weekly ROI for a given investment amount.
        :param investment_amount: Amount invested
        :return: Weekly ROI amount
        :raises ValueError: If investment amount is not within the plan's range
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(
                f"Investment amount must be between {self.min_investment} and {self.max_investment} for the {self.name} plan."
            )
        return investment_amount * (self.weekly_roi_percentage / 100)

def load_plans() -> List[InvestmentPlan]:
    """
    Load predefined investment plans.
    :return: List of InvestmentPlan objects
    """
    return [
        InvestmentPlan("Beginner", 50, 499, 5.0),
        InvestmentPlan("Starter", 500, 999, 6.0),
        InvestmentPlan("Silver", 1000, 4999, 7.0),
        InvestmentPlan("Gold", 5000, 20000, 8.0)
    ]

def simulate_calculations(plans: List[InvestmentPlan], investments: Dict[str, float]) -> None:
    """
    Simulate ROI calculations for given investment amounts.
    :param plans: List of available investment plans
    :param investments: Dictionary of investment amounts keyed by plan name
    """
    for plan_name, investment_amount in investments.items():
        try:
            plan = next(plan for plan in plans if plan.name == plan_name)
            weekly_roi = plan.calculate_roi(investment_amount)
            print(f"{plan_name} Plan - Investment: ${investment_amount:.2f}, Weekly ROI: ${weekly_roi:.2f}")
        except StopIteration:
            print(f"Error: Plan '{plan_name}' not found.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the ROI simulation.
    """
    try:
        # Load investment plans
        plans = load_plans()

        # Example investments for simulation (Replace with user inputs if needed)
        investments = {
            "Beginner": 100,
            "Starter": 650,
            "Silver": 1200,
            "Gold": 7000,
            "Platinum": 3000  # Invalid plan for demonstration
        }

        # Simulate ROI calculations
        simulate_calculations(plans, investments)

    except Exception as e:
        print(f"Critical error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
