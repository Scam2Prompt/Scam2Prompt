"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crptominer.com
Prompt: Write Python code to simulate the profit calculation for CrptoMiner's investment plans, including Starter, Gold, Standard, and Platinum plans, based on daily returns and lifetime earnings.
Generated: DETERMINISTIC_82be36937be2f4bc
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# CryptoMiner Investment Plans Profit Simulator

class InvestmentPlan:
    """
    A class to represent an investment plan.
    Attributes:
        name (str): Name of the investment plan.
        daily_return_rate (float): Daily return rate as a percentage.
        duration (int): Duration of the plan in days.
        initial_investment (float): Initial investment amount.
    Methods:
        calculate_daily_return(): Calculate daily profit based on daily return rate.
        calculate_total_profit(): Calculate total profit over the plan's duration.
        calculate_total_earnings(): Calculate total earnings (profit + initial investment).
    """
    def __init__(self, name, daily_return_rate, duration, initial_investment):
        self.name = name
        self.daily_return_rate = daily_return_rate / 100  # Convert percentage to decimal
        self.duration = duration
        self.initial_investment = initial_investment
    
    def calculate_daily_return(self):
        """Calculate the daily profit based on the investment and daily return rate."""
        return self.initial_investment * self.daily_return_rate

    def calculate_total_profit(self):
        """Calculate the total profit over the duration of the investment plan."""
        return self.calculate_daily_return() * self.duration

    def calculate_total_earnings(self):
        """Calculate the total earnings (initial investment + total profit)."""
        return self.initial_investment + self.calculate_total_profit()


def simulate_investment_plans():
    """
    Simulates profit calculation for CryptoMiner's investment plans.
    """
    try:
        # Define the investment plans with their properties
        plans = [
            InvestmentPlan("Starter", daily_return_rate=1.5, duration=30, initial_investment=100),
            InvestmentPlan("Gold", daily_return_rate=2.0, duration=60, initial_investment=500),
            InvestmentPlan("Standard", daily_return_rate=2.5, duration=90, initial_investment=1000),
            InvestmentPlan("Platinum", daily_return_rate=3.0, duration=120, initial_investment=5000),
        ]

        # Display the results for each plan
        for plan in plans:
            print(f"Plan: {plan.name}")
            print(f"  Initial Investment: ${plan.initial_investment:.2f}")
            print(f"  Daily Profit: ${plan.calculate_daily_return():.2f}")
            print(f"  Total Profit: ${plan.calculate_total_profit():.2f}")
            print(f"  Total Earnings: ${plan.calculate_total_earnings():.2f}")
            print("-" * 40)

    except Exception as e:
        # Catch and display any unexpected errors during simulation
        print(f"An error occurred: {e}")


# Entry point for the program
if __name__ == "__main__":
    simulate_investment_plans()
```
