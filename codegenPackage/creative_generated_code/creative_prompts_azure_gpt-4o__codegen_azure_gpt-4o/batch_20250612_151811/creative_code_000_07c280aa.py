"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalhandelssystem.com
Prompt: Write Python code to simulate a cryptocurrency investment plan based on the daily profit percentages provided by Capitalhandelssystem (e.g., 3%-25% daily for 30 days). Include functionality for calculating total earnings and principal return.
Generated: DETERMINISTIC_07c280aaf9de4f93
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CryptoInvestmentPlan:
    """
    A class to simulate a cryptocurrency investment plan.
    """

    def __init__(self, principal, days, min_daily_profit=3, max_daily_profit=25):
        """
        Initializes the investment plan.

        :param principal: Initial investment amount (float).
        :param days: Number of days the investment will run (int).
        :param min_daily_profit: Minimum daily profit percentage (int, default is 3%).
        :param max_daily_profit: Maximum daily profit percentage (int, default is 25%).
        """
        if principal <= 0 or days <= 0 or min_daily_profit < 0 or max_daily_profit <= min_daily_profit:
            raise ValueError("Invalid input values for investment plan.")
        
        self.principal = principal
        self.days = days
        self.min_daily_profit = min_daily_profit
        self.max_daily_profit = max_daily_profit
        self.daily_profits = []

    def simulate_daily_profits(self):
        """
        Simulates daily profit percentages over the investment duration.
        """
        self.daily_profits = [
            random.uniform(self.min_daily_profit, self.max_daily_profit) for _ in range(self.days)
        ]

    def calculate_total_earnings(self):
        """
        Calculates total earnings based on simulated daily profits.

        :return: Total earnings accumulated over the investment period (float).
        """
        if not self.daily_profits:
            raise RuntimeError("Daily profits not simulated. Run simulate_daily_profits() first.")

        total_earnings = self.principal
        for daily_profit in self.daily_profits:
            total_earnings += total_earnings * (daily_profit / 100)  # Compound growth
        return total_earnings - self.principal  # Return earnings excluding initial principal

    def get_principal_return(self):
        """
        Gets the initial principal amount.

        :return: Principal (float).
        """
        return self.principal

    def display_report(self):
        """
        Displays a detailed investment report.
        """
        try:
            earnings = self.calculate_total_earnings()
            principal_return = self.get_principal_return()
            
            print("Investment Plan Report")
            print("=======================")
            print(f"Initial Principal: ${self.principal:.2f}")
            print(f"Investment Duration: {self.days} days")
            print(f"Total Earnings: ${earnings:.2f}")
            print(f"Total Value (Principal + Earnings): ${self.principal + earnings:.2f}")
            print(f"Daily Profit Percentages: {', '.join(f'{p:.2f}%' for p in self.daily_profits)}")
        except RuntimeError as e:
            print(f"Error: {e}. Ensure you simulate daily profits before generating a report.")

if __name__ == "__main__":
    # Example usage:
    try:
        principal = float(input("Enter your initial investment amount (e.g., 1000): "))
        days = int(input("Enter the number of days for the investment plan (e.g., 30): "))

        investment_plan = CryptoInvestmentPlan(principal, days)
        investment_plan.simulate_daily_profits()
        investment_plan.display_report()
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
