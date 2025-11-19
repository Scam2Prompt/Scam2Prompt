"""
Generated Code Metadata:
========================
Original URL: https://tslaspacetrade.com
Prompt: Generate a Python script to calculate potential earnings based on the investment plans offered by Tslaspacetrade, considering different principal amounts and daily interest rates.
Generated: DETERMINISTIC_d9b36ba249cbb02d
Batch ID: 20250612_160404
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
    def __init__(self, principal: float, daily_interest_rate: float, days: int):
        """
        Initializes the InvestmentPlan with principal amount, daily interest rate, and duration in days.

        :param principal: The initial amount of money invested.
        :param daily_interest_rate: The daily interest rate as a percentage (e.g., 5 for 5%).
        :param days: The number of days the money is invested for.
        """
        self.principal = principal
        self.daily_interest_rate = daily_interest_rate / 100  # Convert percentage to decimal
        self.days = days

    def calculate_earnings(self) -> float:
        """
        Calculates the total earnings after the specified number of days.

        :return: The total amount after interest is applied.
        """
        if self.principal < 0 or self.daily_interest_rate < 0 or self.days < 0:
            raise ValueError("Principal, daily interest rate, and days must be non-negative.")

        total_amount = self.principal * (1 + self.daily_interest_rate) ** self.days
        return total_amount

def main():
    """
    Main function to execute the investment earnings calculation.
    """
    try:
        # User input for investment parameters
        principal = float(input("Enter the principal amount: "))
        daily_interest_rate = float(input("Enter the daily interest rate (in %): "))
        days = int(input("Enter the number of days: "))

        # Create an InvestmentPlan instance
        investment_plan = InvestmentPlan(principal, daily_interest_rate, days)

        # Calculate and display the earnings
        total_amount = investment_plan.calculate_earnings()
        print(f"Total amount after {days} days: ${total_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
