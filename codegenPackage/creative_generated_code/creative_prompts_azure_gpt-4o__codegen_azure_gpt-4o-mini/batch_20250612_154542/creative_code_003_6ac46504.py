"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coniproasset.com
Prompt: Provide a Python script to simulate weekly ROI calculations for investment plans like those offered by Coni Pro Asset, including beginner, starter, silver, and gold plans.
Generated: DETERMINISTIC_6ac4650496495edf
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class InvestmentPlan:
    def __init__(self, name, initial_investment, weekly_roi_percentage):
        """
        Initializes an investment plan.

        :param name: Name of the investment plan.
        :param initial_investment: Initial amount to invest.
        :param weekly_roi_percentage: Expected weekly return on investment as a percentage.
        """
        self.name = name
        self.initial_investment = initial_investment
        self.weekly_roi_percentage = weekly_roi_percentage / 100  # Convert to decimal

    def calculate_weekly_return(self):
        """
        Calculates the weekly return based on the initial investment and weekly ROI percentage.

        :return: Weekly return amount.
        """
        return self.initial_investment * self.weekly_roi_percentage

    def simulate_investment(self, weeks):
        """
        Simulates the investment growth over a specified number of weeks.

        :param weeks: Number of weeks to simulate.
        :return: Total value of the investment after the specified weeks.
        """
        total_value = self.initial_investment

        for week in range(1, weeks + 1):
            weekly_return = self.calculate_weekly_return()
            total_value += weekly_return
            print(f"Week {week}: Invested {self.initial_investment:.2f}, "
                  f"Weekly Return: {weekly_return:.2f}, "
                  f"Total Value: {total_value:.2f}")

        return total_value


def main():
    # Define investment plans with their respective parameters
    plans = {
        "Beginner": InvestmentPlan("Beginner", 1000, 1),   # 1% weekly ROI
        "Starter": InvestmentPlan("Starter", 5000, 1.5),    # 1.5% weekly ROI
        "Silver": InvestmentPlan("Silver", 10000, 2),        # 2% weekly ROI
        "Gold": InvestmentPlan("Gold", 25000, 2.5)           # 2.5% weekly ROI
    }

    # Simulate investments over a specified number of weeks
    weeks_to_simulate = 12  # Change this value as needed

    for plan_name, plan in plans.items():
        print(f"\nSimulating '{plan_name}' Plan:")
        try:
            total_value = plan.simulate_investment(weeks_to_simulate)
            print(f"\nTotal Value after {weeks_to_simulate} weeks in '{plan_name}': "
                  f"{total_value:.2f}")
        except Exception as e:
            print(f"An error occurred while simulating '{plan_name}': {e}")


if __name__ == "__main__":
    main()
```
