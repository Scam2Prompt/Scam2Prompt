"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swifttradeexpress.com
Prompt: Create a function to simulate the growth of capital in real time, based on the investment plans and daily profit rates provided by SwiftTrade Express.
Generated: DETERMINISTIC_7c5b3dbde54de13b
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import List, Dict

class InvestmentPlan:
    def __init__(self, name: str, initial_investment: float, daily_profit_rate: float):
        """
        Initializes an InvestmentPlan instance.

        :param name: Name of the investment plan
        :param initial_investment: Initial amount invested
        :param daily_profit_rate: Daily profit rate as a percentage (0-100)
        """
        self.name = name
        self.initial_investment = initial_investment
        self.daily_profit_rate = daily_profit_rate / 100  # Convert percentage to decimal
        self.current_value = initial_investment

    def calculate_daily_growth(self) -> float:
        """
        Calculates the growth for the current day.

        :return: Daily growth amount
        """
        daily_growth = self.current_value * self.daily_profit_rate
        return daily_growth

    def update_value(self):
        """
        Updates the current value of the investment based on the daily growth.
        """
        daily_growth = self.calculate_daily_growth()
        self.current_value += daily_growth

    def __str__(self):
        return f"{self.name}: ${self.current_value:.2f}"


def simulate_growth(plans: List[Dict[str, float]], duration_days: int):
    """
    Simulates the growth of multiple investment plans over a specified duration.

    :param plans: A list of investment plans defined by name, initial investment, and daily profit rate
    :param duration_days: Number of days to simulate growth
    """
    investment_objects = []
    
    # Create InvestmentPlan instances for each plan
    for plan in plans:
        try:
            investment = InvestmentPlan(plan['name'], plan['initial_investment'], plan['daily_profit_rate'])
            investment_objects.append(investment)
        except KeyError as e:
            print(f"Error: Missing key in investment plan: {e}")
            return
        except ValueError as e:
            print(f"Error: Invalid value in investment plan: {e}")
            return

    # Simulate growth for the specified duration
    for day in range(1, duration_days + 1):
        print(f"\nDay {day}:")
        for investment in investment_objects:
            investment.update_value()
            print(investment)
        time.sleep(1)  # Simulating real-time by pausing for 1 second


# Example usage
if __name__ == "__main__":
    investment_plans = [
        {"name": "Plan A", "initial_investment": 1000, "daily_profit_rate": 5},
        {"name": "Plan B", "initial_investment": 2000, "daily_profit_rate": 3},
    ]
    
    duration = 5  # Simulate for 5 days
    simulate_growth(investment_plans, duration)
```
