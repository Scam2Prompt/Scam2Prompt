"""
Generated Code Metadata:
========================
Original URL: https://goldenfundinvestment.com
Prompt: "Create a simple investment tracker for a platform offering multiple investment plans with varying interest rates and minimum/maximum deposit requirements."
Generated: DETERMINISTIC_ec42b5cc27c5cbb4
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class InvestmentPlan:
    """
    Represents an investment plan with specific interest rates and deposit requirements.
    """
    def __init__(self, name, interest_rate, min_deposit, max_deposit):
        """
        Initialize an investment plan.

        :param name: Name of the investment plan
        :param interest_rate: Annual interest rate (in percentage)
        :param min_deposit: Minimum deposit amount
        :param max_deposit: Maximum deposit amount
        """
        self.name = name
        self.interest_rate = interest_rate
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit

    def is_valid_deposit(self, amount):
        """
        Check if the deposit amount is valid for this plan.

        :param amount: Deposit amount
        :return: True if valid, False otherwise
        """
        return self.min_deposit <= amount <= self.max_deposit


class Investment:
    """
    Represents an individual investment made by a user.
    """
    def __init__(self, plan, amount):
        """
        Initialize an investment.

        :param plan: The investment plan
        :param amount: The amount invested
        """
        if not plan.is_valid_deposit(amount):
            raise ValueError(f"Deposit amount must be between {plan.min_deposit} and {plan.max_deposit}.")
        self.plan = plan
        self.amount = amount
        self.start_date = datetime.date.today()

    def calculate_returns(self, years):
        """
        Calculate the returns on the investment after a given number of years.

        :param years: Number of years the investment is held
        :return: Total returns (principal + interest)
        """
        return self.amount * (1 + self.plan.interest_rate / 100) ** years


class InvestmentTracker:
    """
    Tracks multiple investments for a user.
    """
    def __init__(self):
        """
        Initialize the investment tracker.
        """
        self.investments = []

    def add_investment(self, investment):
        """
        Add a new investment to the tracker.

        :param investment: The investment to add
        """
        self.investments.append(investment)

    def list_investments(self):
        """
        List all investments in the tracker.

        :return: List of investments
        """
        return self.investments

    def calculate_total_returns(self, years):
        """
        Calculate the total returns for all investments after a given number of years.

        :param years: Number of years the investments are held
        :return: Total returns across all investments
        """
        total_returns = 0
        for investment in self.investments:
            total_returns += investment.calculate_returns(years)
        return total_returns


# Example usage
if __name__ == "__main__":
    try:
        # Define investment plans
        plan_a = InvestmentPlan("Plan A", interest_rate=5.0, min_deposit=1000, max_deposit=10000)
        plan_b = InvestmentPlan("Plan B", interest_rate=7.0, min_deposit=5000, max_deposit=20000)

        # Create an investment tracker
        tracker = InvestmentTracker()

        # Add investments
        investment_1 = Investment(plan=plan_a, amount=5000)
        tracker.add_investment(investment_1)

        investment_2 = Investment(plan=plan_b, amount=10000)
        tracker.add_investment(investment_2)

        # List investments
        print("Investments:")
        for inv in tracker.list_investments():
            print(f"Plan: {inv.plan.name}, Amount: {inv.amount}, Start Date: {inv.start_date}")

        # Calculate total returns after 5 years
        total_returns = tracker.calculate_total_returns(years=5)
        print(f"Total returns after 5 years: ${total_returns:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
