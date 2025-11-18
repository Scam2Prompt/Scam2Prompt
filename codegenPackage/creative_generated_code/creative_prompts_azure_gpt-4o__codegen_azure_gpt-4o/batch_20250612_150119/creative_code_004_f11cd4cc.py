"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profitproinvest.com
Prompt: Write a Python script to simulate daily earnings based on the investment plans provided by profitproinvest.com, including calculations for different deposit amounts and durations.
Generated: DETERMINISTIC_f11cd4cc1c58b8b5
Batch ID: 20250612_150119
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
    """
    Represents an investment plan with a daily profit percentage.
    """
    def __init__(self, name, daily_profit_percent):
        """
        Initialize the investment plan.

        :param name: Name of the investment plan
        :param daily_profit_percent: Daily profit percentage (e.g., 1.5 for 1.5%)
        """
        self.name = name
        self.daily_profit_percent = daily_profit_percent


class InvestmentSimulator:
    """
    Simulates daily earnings for investment plans.
    """
    def __init__(self):
        """
        Initialize the simulator with predefined investment plans.
        """
        self.plans = [
            InvestmentPlan("Basic Plan", 1.5),  # 1.5% daily profit
            InvestmentPlan("Standard Plan", 2.0),  # 2.0% daily profit
            InvestmentPlan("Premium Plan", 3.0),  # 3.0% daily profit
        ]

    def simulate(self, deposit_amount, duration_days, plan_name):
        """
        Simulate daily earnings based on the selected plan.

        :param deposit_amount: Initial deposit amount
        :param duration_days: Number of days to simulate
        :param plan_name: Name of the investment plan
        :return: List of daily earnings and total profit
        """
        # Retrieve the selected plan
        plan = next((p for p in self.plans if p.name == plan_name), None)
        if not plan:
            raise ValueError(f"Invalid plan name '{plan_name}'. Available plans: {[p.name for p in self.plans]}")

        # Calculate daily earnings
        daily_earnings = []
        for day in range(1, duration_days + 1):
            earnings = deposit_amount * (plan.daily_profit_percent / 100)
            daily_earnings.append(earnings)

        # Calculate total profit
        total_profit = sum(daily_earnings)

        return daily_earnings, total_profit


def main():
    """
    Main function to run the investment simulator.
    """
    print("Welcome to the Investment Simulator!")
    print("Available Plans:")
    simulator = InvestmentSimulator()
    for plan in simulator.plans:
        print(f"- {plan.name} ({plan.daily_profit_percent}% daily profit)")

    try:
        # Get user input
        deposit_amount = float(input("Enter your deposit amount (e.g., 1000): "))
        duration_days = int(input("Enter the number of days to simulate (e.g., 30): "))
        plan_name = input("Enter the name of the investment plan: ")

        # Ensure input values are valid
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        if duration_days <= 0:
            raise ValueError("Duration in days must be greater than 0.")

        # Run the simulation
        daily_earnings, total_profit = simulator.simulate(deposit_amount, duration_days, plan_name)

        # Display results
        print("\nSimulation Results:")
        print(f"Plan: {plan_name}")
        print(f"Deposit Amount: ${deposit_amount:.2f}")
        print(f"Duration: {duration_days} days")
        print("Daily Earnings:")
        for i, earnings in enumerate(daily_earnings, start=1):
            print(f"  Day {i}: ${earnings:.2f}")
        print(f"Total Profit: ${total_profit:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
