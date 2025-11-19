"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tslaspacetrade.com
Prompt: Generate a Python script to calculate potential earnings based on the investment plans offered by Tslaspacetrade, considering different principal amounts and daily interest rates.
Generated: DETERMINISTIC_d9b36ba249cbb02d
Batch ID: 20250612_160404
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
    def __init__(self, principal, daily_interest_rate, days):
        """
        Initializes the InvestmentPlan with principal amount, daily interest rate, and duration.
        
        :param principal: Initial amount invested
        :param daily_interest_rate: Daily interest rate as a decimal (e.g., 0.05 for 5%)
        :param days: Number of days the money is invested
        """
        self.principal = principal
        self.daily_interest_rate = daily_interest_rate
        self.days = days

    def calculate_earnings(self):
        """
        Calculates the total earnings after the investment period.
        
        :return: Total earnings (principal + interest)
        """
        if self.principal < 0 or self.daily_interest_rate < 0 or self.days < 0:
            raise ValueError("Principal, daily interest rate, and days must be non-negative.")
        
        # Calculate total earnings using the formula: Earnings = Principal * (1 + daily_interest_rate) ** days
        total_earnings = self.principal * (1 + self.daily_interest_rate) ** self.days
        return total_earnings


def main():
    """
    Main function to execute the investment calculation.
    """
    try:
        # Input from the user
        principal = float(input("Enter the principal amount: "))
        daily_interest_rate = float(input("Enter the daily interest rate (as a percentage): ")) / 100
        days = int(input("Enter the number of days: "))
        
        # Create an instance of InvestmentPlan
        investment_plan = InvestmentPlan(principal, daily_interest_rate, days)
        
        # Calculate and display the total earnings
        total_earnings = investment_plan.calculate_earnings()
        print(f"Total earnings after {days} days: ${total_earnings:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
