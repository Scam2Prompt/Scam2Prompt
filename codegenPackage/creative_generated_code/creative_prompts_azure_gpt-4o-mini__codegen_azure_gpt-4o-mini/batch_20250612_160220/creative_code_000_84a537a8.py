"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wintron.minibachat.shop
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Wintron, including parameters for different investment amounts and plan types.
Generated: DETERMINISTIC_84a537a87e1b087e
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentPlan:
    """Class to represent an investment plan."""

    def __init__(self, name, interest_rate, duration_months):
        """
        Initialize an investment plan.

        Args:
            name (str): The name of the investment plan.
            interest_rate (float): The interest rate of the plan (as a percentage).
            duration_months (int): The duration of the investment in months.
        """
        self.name = name
        self.interest_rate = interest_rate
        self.duration_months = duration_months

    def calculate_profit(self, investment_amount):
        """
        Calculate the profit based on the investment amount.

        Args:
            investment_amount (float): The amount of money invested.

        Returns:
            float: The profit earned after the duration.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount must be non-negative.")
        
        profit = (investment_amount * (self.interest_rate / 100)) * (self.duration_months / 12)
        return profit


def main():
    """Main function to run the investment profit calculator."""
    # Define investment plans offered by Wintron
    plans = [
        InvestmentPlan("Plan A", 5.0, 6),   # 5% for 6 months
        InvestmentPlan("Plan B", 7.5, 12),  # 7.5% for 1 year
        InvestmentPlan("Plan C", 10.0, 24)  # 10% for 2 years
    ]

    # Get user input for the investment amount
    try:
        investment_amount = float(input("Enter the investment amount: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        sys.exit(1)

    # Calculate and display potential profits for each plan
    print("\nPotential Profits:")
    for plan in plans:
        try:
            profit = plan.calculate_profit(investment_amount)
            print(f"{plan.name}: ${profit:.2f} profit after {plan.duration_months} months.")
        except ValueError as ve:
            print(f"Error calculating profit for {plan.name}: {ve}")

if __name__ == "__main__":
    main()
```
