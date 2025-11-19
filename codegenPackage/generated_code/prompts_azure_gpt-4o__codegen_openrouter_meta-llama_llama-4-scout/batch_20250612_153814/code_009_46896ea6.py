"""
Generated Code Metadata:
========================
Original URL: https://globalfxoption.com
Prompt: Create a Python program to calculate the total return for all investment plans listed on the Global FX Option website, including validation for minimum and maximum investment amounts for each plan.
Generated: DETERMINISTIC_46896ea60e9a6199
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# global_fx_option.py

class InvestmentPlan:
    """Represents an investment plan with minimum and maximum investment amounts."""

    def __init__(self, name, min_investment, max_investment, return_rate):
        """
        Initializes an InvestmentPlan.

        Args:
            name (str): The name of the investment plan.
            min_investment (float): The minimum investment amount for the plan.
            max_investment (float): The maximum investment amount for the plan.
            return_rate (float): The return rate for the plan as a decimal.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.return_rate = return_rate

    def calculate_return(self, investment_amount):
        """
        Calculates the return for the given investment amount.

        Args:
            investment_amount (float): The amount invested.

        Returns:
            float: The return on investment.

        Raises:
            ValueError: If the investment amount is less than the minimum or greater than the maximum.
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(f"Invalid investment amount. Must be between {self.min_investment} and {self.max_investment}.")

        return investment_amount * self.return_rate


class GlobalFXOption:
    """Represents the Global FX Option website with a list of investment plans."""

    def __init__(self):
        """Initializes a GlobalFXOption with an empty list of investment plans."""
        self.investment_plans = []

    def add_investment_plan(self, plan):
        """
        Adds an investment plan to the list.

        Args:
            plan (InvestmentPlan): The plan to add.
        """
        self.investment_plans.append(plan)

    def calculate_total_return(self, investments):
        """
        Calculates the total return for all investment plans.

        Args:
            investments (dict): A dictionary of investment plans to their respective investment amounts.

        Returns:
            float: The total return on investment.

        Raises:
            ValueError: If an investment plan is not found or if an investment amount is invalid.
        """
        total_return = 0

        for plan_name, investment_amount in investments.items():
            plan = next((p for p in self.investment_plans if p.name == plan_name), None)

            if plan is None:
                raise ValueError(f"Investment plan '{plan_name}' not found.")

            try:
                return_on_investment = plan.calculate_return(investment_amount)
                total_return += return_on_investment
            except ValueError as e:
                print(f"Error calculating return for {plan_name}: {e}")

        return total_return


def main():
    # Create investment plans
    plans = [
        InvestmentPlan("Plan A", 100, 1000, 0.05),
        InvestmentPlan("Plan B", 500, 5000, 0.10),
        InvestmentPlan("Plan C", 2000, 20000, 0.15),
    ]

    # Create Global FX Option website
    global_fx_option = GlobalFXOption()

    # Add investment plans to the website
    for plan in plans:
        global_fx_option.add_investment_plan(plan)

    # Define investments
    investments = {
        "Plan A": 500,
        "Plan B": 2000,
        "Plan C": 10000,
    }

    try:
        # Calculate total return
        total_return = global_fx_option.calculate_total_return(investments)
        print(f"Total return: {total_return:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
