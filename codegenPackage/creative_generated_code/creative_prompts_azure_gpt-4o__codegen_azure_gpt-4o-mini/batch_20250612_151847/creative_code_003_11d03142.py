"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytrustasset.com
Prompt: Create a script to calculate daily earnings for investors based on the fixed interest rates and investment plans provided by Sky Trust ltd.
Generated: DETERMINISTIC_11d03142b928d720
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
from typing import List, Dict, Any

class InvestmentPlan:
    """Class representing an investment plan."""

    def __init__(self, plan_name: str, interest_rate: float):
        """
        Initializes an InvestmentPlan instance.

        Args:
            plan_name (str): The name of the investment plan.
            interest_rate (float): The daily interest rate as a percentage.
        """
        self.plan_name = plan_name
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal

    def calculate_daily_earning(self, investment_amount: float) -> float:
        """
        Calculates daily earnings based on the investment amount.

        Args:
            investment_amount (float): The amount invested.

        Returns:
            float: The calculated daily earnings.
        """
        return investment_amount * self.interest_rate


class Investor:
    """Class representing an investor."""

    def __init__(self, name: str):
        """
        Initializes an Investor instance.

        Args:
            name (str): The name of the investor.
        """
        self.name = name
        self.investments: List[Dict[str, Any]] = []

    def add_investment(self, investment_plan: InvestmentPlan, amount: float):
        """
        Adds an investment to the investor's portfolio.

        Args:
            investment_plan (InvestmentPlan): The investment plan chosen.
            amount (float): The amount invested.
        """
        self.investments.append({
            'plan': investment_plan,
            'amount': amount
        })

    def calculate_total_daily_earnings(self) -> float:
        """
        Calculates total daily earnings from all investments.

        Returns:
            float: Total daily earnings from all investments.
        """
        total_earnings = 0.0
        for investment in self.investments:
            plan = investment['plan']
            amount = investment['amount']
            total_earnings += plan.calculate_daily_earning(amount)
        return total_earnings


def main():
    """Main function to run the earnings calculation."""
    try:
        # Sample investment plans provided by Sky Trust Ltd
        plans = [
            InvestmentPlan("Basic Plan", 5.0),  # 5% daily
            InvestmentPlan("Silver Plan", 7.0),  # 7% daily
            InvestmentPlan("Gold Plan", 10.0)    # 10% daily
        ]

        # Initialize an investor
        investor = Investor("John Doe")

        # Adding investments to the investor
        investor.add_investment(plans[0], 1000.0)  # Invested $1000 in Basic Plan
        investor.add_investment(plans[1], 2000.0)  # Invested $2000 in Silver Plan

        # Calculate total daily earnings
        total_daily_earnings = investor.calculate_total_daily_earnings()
        print(f"Total Daily Earnings for {investor.name}: ${total_daily_earnings:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
