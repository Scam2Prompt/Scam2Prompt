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
# investment_tracker.py

class InvestmentPlan:
    """Represents an investment plan with interest rate and deposit requirements."""

    def __init__(self, name, interest_rate, min_deposit, max_deposit):
        """
        Initializes an InvestmentPlan.

        Args:
            name (str): Name of the investment plan.
            interest_rate (float): Interest rate of the plan as a decimal.
            min_deposit (float): Minimum deposit required for the plan.
            max_deposit (float): Maximum deposit allowed for the plan.
        """
        self.name = name
        self.interest_rate = interest_rate
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit

    def calculate_interest(self, principal):
        """
        Calculates the interest earned on an investment.

        Args:
            principal (float): Principal amount invested.

        Returns:
            float: Interest earned.
        """
        if principal < self.min_deposit or principal > self.max_deposit:
            raise ValueError("Principal amount is outside deposit requirements")
        return principal * self.interest_rate


class InvestmentTracker:
    """Tracks investments across multiple plans."""

    def __init__(self):
        """Initializes an InvestmentTracker with an empty list of plans."""
        self.plans = []
        self.investments = {}

    def add_plan(self, plan):
        """
        Adds an investment plan to the tracker.

        Args:
            plan (InvestmentPlan): Plan to add.
        """
        self.plans.append(plan)

    def invest(self, plan_name, principal, investor):
        """
        Records an investment in a plan.

        Args:
            plan_name (str): Name of the plan to invest in.
            principal (float): Principal amount to invest.
            investor (str): Name of the investor.

        Raises:
            ValueError: If the plan does not exist or investment amount is invalid.
        """
        plan = next((p for p in self.plans if p.name == plan_name), None)
        if plan is None:
            raise ValueError("Plan does not exist")
        try:
            interest = plan.calculate_interest(principal)
            if investor not in self.investments:
                self.investments[investor] = []
            self.investments[investor].append((plan_name, principal, interest))
        except ValueError as e:
            raise ValueError(f"Invalid investment: {e}")

    def get_investor_summary(self, investor):
        """
        Generates a summary of an investor's investments.

        Args:
            investor (str): Name of the investor.

        Returns:
            list: List of investment summaries.
        """
        return self.investments.get(investor, [])

    def get_plan_summary(self, plan_name):
        """
        Generates a summary of investments in a plan.

        Args:
            plan_name (str): Name of the plan.

        Returns:
            list: List of investment summaries.
        """
        plan_investments = []
        for investor, investments in self.investments.items():
            plan_investments.extend([(investor, investment) for investment in investments if investment[0] == plan_name])
        return plan_investments


def main():
    tracker = InvestmentTracker()

    # Create investment plans
    plan1 = InvestmentPlan("Plan A", 0.05, 1000, 10000)
    plan2 = InvestmentPlan("Plan B", 0.03, 500, 5000)

    # Add plans to tracker
    tracker.add_plan(plan1)
    tracker.add_plan(plan2)

    # Record investments
    tracker.invest("Plan A", 5000, "John Doe")
    tracker.invest("Plan B", 2000, "Jane Doe")
    tracker.invest("Plan A", 15000, "John Doe")  # This should raise an error

    # Get investment summaries
    print("John Doe's investments:")
    for investment in tracker.get_investor_summary("John Doe"):
        print(f"Plan: {investment[0]}, Principal: {investment[1]}, Interest: {investment[2]}")

    print("\nPlan A investments:")
    for investor, investment in tracker.get_plan_summary("Plan A"):
        print(f"Investor: {investor}, Plan: {investment[0]}, Principal: {investment[1]}, Interest: {investment[2]}")

    try:
        tracker.invest("Plan A", 500, "John Doe")  # This should raise an error
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
