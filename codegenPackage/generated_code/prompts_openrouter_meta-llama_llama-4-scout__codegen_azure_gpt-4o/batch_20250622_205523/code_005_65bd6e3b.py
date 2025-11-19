"""
Generated Code Metadata:
========================
Original URL: https://supermining.website
Prompt: Write a script to track and calculate the profitability of a cloud mining investment using Super Mining's pricing plans, such as Micro, Mega, Giga, and Tera.
Generated: DETERMINISTIC_65bd6e3bcf9b0e2f
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class CloudMiningInvestment:
    """
    A class to track and calculate the profitability of a cloud mining investment.
    """

    def __init__(self, plan_name, investment_amount, daily_yield_percentage, maintenance_fee_percentage):
        """
        Initialize the investment details.

        :param plan_name: Name of the mining plan (e.g., Micro, Mega, Giga, Tera)
        :param investment_amount: Initial investment amount in USD
        :param daily_yield_percentage: Daily yield percentage (e.g., 1.5 for 1.5%)
        :param maintenance_fee_percentage: Daily maintenance fee percentage (e.g., 0.5 for 0.5%)
        """
        self.plan_name = plan_name
        self.investment_amount = investment_amount
        self.daily_yield_percentage = daily_yield_percentage
        self.maintenance_fee_percentage = maintenance_fee_percentage
        self.start_date = datetime.date.today()
        self.profit_history = []  # List to store daily profit history

    def calculate_daily_profit(self):
        """
        Calculate the daily profit after deducting maintenance fees.

        :return: Daily profit in USD
        """
        daily_yield = self.investment_amount * (self.daily_yield_percentage / 100)
        maintenance_fee = self.investment_amount * (self.maintenance_fee_percentage / 100)
        daily_profit = daily_yield - maintenance_fee
        return daily_profit

    def track_profit(self, days):
        """
        Track the profitability over a given number of days.

        :param days: Number of days to track
        :return: Total profit over the given period
        """
        total_profit = 0
        for day in range(1, days + 1):
            daily_profit = self.calculate_daily_profit()
            total_profit += daily_profit
            self.profit_history.append({
                "day": day,
                "date": self.start_date + datetime.timedelta(days=day),
                "daily_profit": round(daily_profit, 2)
            })
        return round(total_profit, 2)

    def display_profit_history(self):
        """
        Display the profit history in a readable format.
        """
        print(f"Profit History for Plan: {self.plan_name}")
        print(f"{'Day':<5} {'Date':<12} {'Daily Profit (USD)':<20}")
        print("-" * 40)
        for record in self.profit_history:
            print(f"{record['day']:<5} {record['date']:<12} {record['daily_profit']:<20}")
        print("-" * 40)

# Example usage
if __name__ == "__main__":
    try:
        # Define investment parameters
        plan_name = "Mega"
        investment_amount = 1000  # USD
        daily_yield_percentage = 1.5  # 1.5% daily yield
        maintenance_fee_percentage = 0.5  # 0.5% daily maintenance fee

        # Create an investment instance
        investment = CloudMiningInvestment(plan_name, investment_amount, daily_yield_percentage, maintenance_fee_percentage)

        # Track profit for 30 days
        total_profit = investment.track_profit(30)

        # Display results
        investment.display_profit_history()
        print(f"Total Profit after 30 days: ${total_profit}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
