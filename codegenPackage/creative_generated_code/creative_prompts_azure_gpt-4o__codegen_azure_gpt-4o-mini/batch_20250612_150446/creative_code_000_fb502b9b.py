"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultimateexperttrade24.com
Prompt: Write Python code to simulate daily returns for an investment plan with parameters matching the "Premium Plan" from Ultimateexperttrade24.com, including 25.9% daily returns and a minimum duration of 1 month.
Generated: DETERMINISTIC_fb502b9b99f30803
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta

class InvestmentPlan:
    def __init__(self, daily_return_rate, min_duration_days):
        """
        Initializes an InvestmentPlan with specified daily return rate and minimum duration.
        
        :param daily_return_rate: Daily return rate as a percentage (e.g., 25.9 for 25.9%)
        :param min_duration_days: Minimum duration of the investment in days
        """
        if daily_return_rate < 0 or min_duration_days <= 0:
            raise ValueError("Daily return rate must be non-negative and minimum duration must be positive.")
        
        self.daily_return_rate = daily_return_rate / 100  # Convert percentage to decimal
        self.min_duration_days = min_duration_days

    def simulate_daily_returns(self, initial_investment):
        """
        Simulates daily returns for the investment plan over a specified duration.
        
        :param initial_investment: The initial amount of money to invest
        :return: List of tuples containing (day, total_value) for each day of the investment
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be a positive number.")
        
        total_value = initial_investment
        daily_values = []

        # Calculate daily returns for the minimum duration
        for day in range(self.min_duration_days):
            total_value *= (1 + self.daily_return_rate)  # Apply daily return
            daily_values.append((day + 1, total_value))  # Store day and total value

        return daily_values

def main():
    # Set parameters for the Premium Plan
    daily_return_rate = 25.9  # Daily return rate as a percentage
    min_duration_days = 30  # Minimum duration in days
    initial_investment = 1000.0  # Initial investment amount in currency

    # Create an instance of the InvestmentPlan
    try:
        investment_plan = InvestmentPlan(daily_return_rate, min_duration_days)
    except ValueError as e:
        print(f"Error initializing investment plan: {e}")
        return

    # Simulate daily returns
    try:
        results = investment_plan.simulate_daily_returns(initial_investment)
        
        # Display the results
        for day, value in results:
            print(f"Day {day}: Total Value = {value:.2f}")
    
    except ValueError as e:
        print(f"Error during simulation: {e}")

if __name__ == "__main__":
    main()
```
