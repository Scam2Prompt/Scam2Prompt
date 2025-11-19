"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Generate a Python script that calculates daily profits based on investment plans from MET LIFE INVESTS, including the daily profit and total profit for each plan.
Generated: DETERMINISTIC_cf9433276afe3793
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# daily_profit_calculator.py

class InvestmentPlan:
    """
    Class to represent an investment plan.

    Attributes:
        name (str): The name of the investment plan.
        initial_investment (float): The initial amount invested.
        daily_rate (float): The daily profit rate as a decimal (e.g., 0.05 for 5%).
    """

    def __init__(self, name: str, initial_investment: float, daily_rate: float):
        self.name = name
        self.initial_investment = initial_investment
        self.daily_rate = daily_rate

    def calculate_daily_profit(self) -> float:
        """
        Calculate the daily profit for the investment plan.

        Returns:
            float: The daily profit amount.
        """
        daily_profit = self.initial_investment * self.daily_rate
        return daily_profit

    def calculate_total_profit(self, days: int) -> float:
        """
        Calculate the total profit over a given number of days.

        Args:
            days (int): The number of days to calculate total profit for.

        Returns:
            float: The total profit amount over the specified days.
        """
        if days < 0:
            raise ValueError("Number of days cannot be negative.")
        total_profit = self.calculate_daily_profit() * days
        return total_profit


def main():
    """
    Main function to execute the daily profit calculations for various investment plans.
    """
    # Example investment plans (name, initial investment, daily rate)
    plans = [
        InvestmentPlan("MET LIFE PLAN A", 1000, 0.05),  # 5% daily
        InvestmentPlan("MET LIFE PLAN B", 2000, 0.03),  # 3% daily
        InvestmentPlan("MET LIFE PLAN C", 1500, 0.04),  # 4% daily
    ]

    days = 30  # Number of days to calculate profits for
    results = []

    print("Calculating profits for investment plans:\n")
    
    for plan in plans:
        try:
            daily_profit = plan.calculate_daily_profit()
            total_profit = plan.calculate_total_profit(days)
            results.append((plan.name, daily_profit, total_profit))
            print(f"Plan: {plan.name}\n  Daily Profit: ${daily_profit:.2f}\n  Total Profit over {days} days: ${total_profit:.2f}\n")
        except ValueError as e:
            print(f"Error calculating profits for {plan.name}: {e}")

if __name__ == "__main__":
    main()
```
