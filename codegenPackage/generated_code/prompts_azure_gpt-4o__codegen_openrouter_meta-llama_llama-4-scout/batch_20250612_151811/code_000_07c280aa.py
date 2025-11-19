"""
Generated Code Metadata:
========================
Original URL: https://capitalhandelssystem.com
Prompt: Write Python code to simulate a cryptocurrency investment plan based on the daily profit percentages provided by Capitalhandelssystem (e.g., 3%-25% daily for 30 days). Include functionality for calculating total earnings and principal return.
Generated: DETERMINISTIC_07c280aaf9de4f93
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class CryptoInvestmentPlan:
    """
    Simulates a cryptocurrency investment plan based on daily profit percentages.

    Attributes:
        principal (float): Initial investment amount.
        daily_profit_percentages (list): List of daily profit percentages.
        investment_days (int): Number of days for the investment plan.
    """

    def __init__(self, principal, daily_profit_percentages, investment_days):
        """
        Initializes the CryptoInvestmentPlan instance.

        Args:
            principal (float): Initial investment amount.
            daily_profit_percentages (list): List of daily profit percentages.
            investment_days (int): Number of days for the investment plan.

        Raises:
            ValueError: If principal is not a positive number.
            ValueError: If investment_days is not a positive integer.
            ValueError: If daily_profit_percentages is not a list of valid percentages.
        """
        if principal <= 0:
            raise ValueError("Principal must be a positive number.")

        if not isinstance(investment_days, int) or investment_days <= 0:
            raise ValueError("Investment days must be a positive integer.")

        if not all(isinstance(p, (int, float)) and 0 <= p <= 100 for p in daily_profit_percentages):
            raise ValueError("Daily profit percentages must be a list of valid percentages.")

        self.principal = principal
        self.daily_profit_percentages = daily_profit_percentages
        self.investment_days = investment_days

    def simulate_investment(self):
        """
        Simulates the cryptocurrency investment plan.

        Returns:
            dict: A dictionary containing the daily earnings and balance.
        """
        balance = self.principal
        daily_earnings = []

        for i in range(self.investment_days):
            # Use a random daily profit percentage if the list is exhausted
            daily_profit_percentage = self.daily_profit_percentages[i % len(self.daily_profit_percentages)] / 100
            daily_earning = balance * daily_profit_percentage
            balance += daily_earning
            daily_earnings.append((i + 1, daily_earning, balance))

        return daily_earnings

    def calculate_total_earnings(self, daily_earnings):
        """
        Calculates the total earnings.

        Args:
            daily_earnings (list): List of daily earnings.

        Returns:
            float: Total earnings.
        """
        return daily_earnings[-1][2] - self.principal

    def calculate_principal_return(self, daily_earnings):
        """
        Calculates the principal return.

        Args:
            daily_earnings (list): List of daily earnings.

        Returns:
            float: Principal return percentage.
        """
        total_earnings = self.calculate_total_earnings(daily_earnings)
        principal_return = (total_earnings / self.principal) * 100
        return principal_return


def main():
    try:
        principal = 1000  # Initial investment amount
        daily_profit_percentages = [random.uniform(0.03, 0.25) * 100 for _ in range(30)]  # Random daily profit percentages between 3% and 25%
        investment_days = 30

        plan = CryptoInvestmentPlan(principal, daily_profit_percentages, investment_days)
        daily_earnings = plan.simulate_investment()

        print("Daily Earnings:")
        for day, earning, balance in daily_earnings:
            print(f"Day {day}: Earning = {earning:.2f}, Balance = {balance:.2f}")

        total_earnings = plan.calculate_total_earnings(daily_earnings)
        principal_return = plan.calculate_principal_return(daily_earnings)

        print(f"\nTotal Earnings: {total_earnings:.2f}")
        print(f"Principal Return: {principal_return:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
