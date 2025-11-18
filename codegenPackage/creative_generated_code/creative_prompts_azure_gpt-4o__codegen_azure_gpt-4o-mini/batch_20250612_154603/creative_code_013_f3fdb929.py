"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accesslinklimited.com
Prompt: Write code to simulate the investment process, including plan selection, deposit tracking, and interest accumulation, as described on Access Link Limited's platform.
Generated: DETERMINISTIC_f3fdb92911974a4e
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Class to represent an investment plan with a name and interest rate."""
    
    def __init__(self, name: str, interest_rate: float):
        """
        Initialize an investment plan.

        :param name: Name of the investment plan.
        :param interest_rate: Annual interest rate as a percentage (e.g., 5 for 5%).
        """
        self.name = name
        self.interest_rate = interest_rate / 100  # Convert to decimal

    def calculate_interest(self, principal: float, years: int) -> float:
        """
        Calculate accumulated interest over a specified number of years.

        :param principal: Initial investment amount.
        :param years: Number of years the money is invested.
        :return: Total amount after interest.
        """
        return principal * ((1 + self.interest_rate) ** years)


class InvestmentAccount:
    """Class to represent an investment account."""
    
    def __init__(self):
        self.plans = []  # List of available investment plans
        self.selected_plan = None  # Currently selected investment plan
        self.balance = 0.0  # Current account balance

    def add_plan(self, plan: InvestmentPlan):
        """Add an investment plan to the account."""
        self.plans.append(plan)

    def select_plan(self, plan_name: str):
        """
        Select an investment plan by name.

        :param plan_name: Name of the plan to select.
        :raises ValueError: If the plan is not found.
        """
        for plan in self.plans:
            if plan.name == plan_name:
                self.selected_plan = plan
                return
        raise ValueError(f"Investment plan '{plan_name}' not found.")

    def deposit(self, amount: float):
        """
        Deposit money into the investment account.

        :param amount: Amount to deposit.
        :raises ValueError: If the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def calculate_total_after_years(self, years: int) -> float:
        """
        Calculate the total balance after a specified number of years 
        with the selected investment plan.

        :param years: Number of years to calculate.
        :raises ValueError: If no plan is selected.
        :return: Total amount after interest.
        """
        if self.selected_plan is None:
            raise ValueError("No investment plan selected.")
        return self.selected_plan.calculate_interest(self.balance, years)


def main():
    """Main function to simulate the investment process."""
    try:
        # Create investment plans
        plan_a = InvestmentPlan("Plan A", 5.0)  # 5% interest
        plan_b = InvestmentPlan("Plan B", 7.0)  # 7% interest

        # Create an investment account
        account = InvestmentAccount()

        # Add plans to the account
        account.add_plan(plan_a)
        account.add_plan(plan_b)

        # Select a plan
        account.select_plan("Plan A")

        # Deposit money
        account.deposit(1000.0)  # Deposit $1000

        # Calculate total after 5 years
        total_after_5_years = account.calculate_total_after_years(5)
        print(f"Total after 5 years: ${total_after_5_years:.2f}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
