"""
Generated Code Metadata:
========================
Original URL: https://newworldtradex.com
Prompt: Develop a script to manage and display investment options with varying yields and durations, as outlined in New World Trade's investment plans.
Generated: DETERMINISTIC_88907db07ade9cec
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_plans.py

class InvestmentPlan:
    """Represents an investment plan with a name, yield, and duration."""

    def __init__(self, name: str, yield_rate: float, duration: int):
        """
        Initializes an InvestmentPlan object.

        Args:
            name (str): The name of the investment plan.
            yield_rate (float): The yield rate of the investment plan as a decimal.
            duration (int): The duration of the investment plan in months.
        """
        self.name = name
        self.yield_rate = yield_rate
        self.duration = duration

    def calculate_return(self, principal: float) -> float:
        """
        Calculates the return on investment.

        Args:
            principal (float): The initial investment amount.

        Returns:
            float: The total return on investment.
        """
        return principal * (1 + self.yield_rate) ** (self.duration / 12)


class InvestmentManager:
    """Manages a collection of investment plans."""

    def __init__(self):
        self.plans = []

    def add_plan(self, plan: InvestmentPlan):
        """
        Adds an investment plan to the collection.

        Args:
            plan (InvestmentPlan): The plan to add.
        """
        self.plans.append(plan)

    def display_plans(self):
        """Displays all investment plans."""
        for i, plan in enumerate(self.plans, start=1):
            print(f"Plan {i}: {plan.name}")
            print(f"Yield: {plan.yield_rate * 100}% per annum")
            print(f"Duration: {plan.duration} months")
            print()

    def compare_plans(self, principal: float):
        """
        Compares the returns on investment for all plans.

        Args:
            principal (float): The initial investment amount.
        """
        print("Return on Investment Comparison:")
        for i, plan in enumerate(self.plans, start=1):
            return_on_investment = plan.calculate_return(principal)
            print(f"Plan {i}: {plan.name} - ${return_on_investment:.2f}")
        print()


def main():
    try:
        # Create investment plans
        plan1 = InvestmentPlan("Conservative", 0.02, 6)
        plan2 = InvestmentPlan("Moderate", 0.05, 12)
        plan3 = InvestmentPlan("Aggressive", 0.08, 24)

        # Create investment manager
        manager = InvestmentManager()
        manager.add_plan(plan1)
        manager.add_plan(plan2)
        manager.add_plan(plan3)

        # Display plans
        print("Investment Plans:")
        manager.display_plans()

        # Compare plans
        principal = 10000.0
        manager.compare_plans(principal)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
