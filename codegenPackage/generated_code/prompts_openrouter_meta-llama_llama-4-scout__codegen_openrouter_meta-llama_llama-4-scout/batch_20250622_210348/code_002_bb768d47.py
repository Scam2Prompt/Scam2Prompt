"""
Generated Code Metadata:
========================
Original URL: https://newworldtradex.com
Prompt: Generate a sample code for a basic cryptocurrency investment plan, such as the Basic Plan offered by New World Trade with a 50% daily yield and $200-$5,000 investment capital.
Generated: DETERMINISTIC_bb768d47ad5daf75
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Basic Cryptocurrency Investment Plan

This script simulates a basic cryptocurrency investment plan with a 50% daily yield.
The investment capital ranges from $200 to $5,000.

Author: [Your Name]
Date: [Today's Date]
"""

import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentPlan:
    def __init__(self, capital):
        """
        Initialize the investment plan with the given capital.

        Args:
            capital (float): The investment capital.
        """
        if not isinstance(capital, (int, float)) or capital < 200 or capital > 5000:
            raise ValueError("Invalid capital. Capital must be a number between $200 and $5,000.")

        self.capital = capital
        self.daily_yield = 0.5  # 50% daily yield

    def calculate_daily_return(self):
        """
        Calculate the daily return based on the capital and daily yield.

        Returns:
            float: The daily return.
        """
        return self.capital * self.daily_yield

    def calculate_total_balance(self, days):
        """
        Calculate the total balance after a given number of days.

        Args:
            days (int): The number of days.

        Returns:
            float: The total balance.
        """
        if not isinstance(days, int) or days <= 0:
            raise ValueError("Invalid number of days. Days must be a positive integer.")

        total_balance = self.capital
        daily_return = self.calculate_daily_return()

        for _ in range(days):
            total_balance += daily_return
            daily_return *= 1 + self.daily_yield  # compound interest

        return total_balance

def main():
    try:
        capital = float(input("Enter your investment capital ($200-$5,000): "))
        investment_plan = InvestmentPlan(capital)

        days = int(input("Enter the number of days: "))
        total_balance = investment_plan.calculate_total_balance(days)

        logging.info(f"Initial Capital: ${investment_plan.capital:.2f}")
        logging.info(f"Daily Yield: {investment_plan.daily_yield*100}%")
        logging.info(f"Total Balance after {days} days: ${total_balance:.2f}")

    except ValueError as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
```
