"""
Generated Code Metadata:
========================
Original URL: https://centraltraderz.com
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Centraltraderz, including the minimum deposit and expected returns for each plan.
Generated: DETERMINISTIC_22dd4c1b89175ec4
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
        name (str): The name of the investment plan.
        min_deposit (float): The minimum deposit required for the plan.
        expected_return (float): The expected return on investment as a percentage.
    """

    def __init__(self, name, min_deposit, expected_return):
        """
        Initializes an InvestmentPlan instance.

        Args:
            name (str): The name of the investment plan.
            min_deposit (float): The minimum deposit required for the plan.
            expected_return (float): The expected return on investment as a percentage.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.expected_return = expected_return

    def calculate_profit(self, deposit):
        """
        Calculates the profit based on the deposit amount.

        Args:
            deposit (float): The amount deposited.

        Returns:
            float: The profit earned from the investment.
        """
        if deposit < self.min_deposit:
            raise ValueError(f"Deposit must be at least {self.min_deposit} for the {self.name} plan.")
        return deposit * (self.expected_return / 100)


def main():
    """
    Main function to execute the investment profit calculation.
    """
    # Define investment plans
    plans = [
        InvestmentPlan("Basic Plan", 1000, 5),
        InvestmentPlan("Standard Plan", 5000, 10),
        InvestmentPlan("Premium Plan", 10000, 15)
    ]

    # User input for deposit amount
    try:
        deposit = float(input("Enter your deposit amount: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        sys.exit(1)

    # Calculate and display profits for each plan
    print("\nPotential Profits:")
    for plan in plans:
        try:
            profit = plan.calculate_profit(deposit)
            print(f"{plan.name}: Profit = ${profit:.2f} (based on a deposit of ${deposit:.2f})")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
