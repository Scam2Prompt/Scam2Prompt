"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Create a Python script to simulate the 65-day investment cycle for MET LIFE INVESTS' plans, including daily profit accumulation and capital return.
Generated: DETERMINISTIC_f88f1a4cb82f9523
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd

class InvestmentCycle:
    def __init__(self, initial_investment, daily_profit_rate, cycle_days=65):
        """
        Initializes the InvestmentCycle with the given parameters.

        :param initial_investment: The amount of money to invest initially.
        :param daily_profit_rate: The daily profit rate as a decimal (e.g., 0.01 for 1%).
        :param cycle_days: The number of days for the investment cycle (default is 65).
        """
        self.initial_investment = initial_investment
        self.daily_profit_rate = daily_profit_rate
        self.cycle_days = cycle_days

    def simulate(self):
        """
        Simulates the investment cycle over the specified number of days.

        :return: A DataFrame containing daily profit accumulation and total capital.
        """
        # Check for valid input values
        if self.initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 < self.daily_profit_rate < 1):
            raise ValueError("Daily profit rate must be between 0 and 1.")

        # Create a list to store daily results
        daily_results = []
        
        # Initialize capital and profit
        total_capital = self.initial_investment
        total_profit = 0
        
        # Simulate each day
        for day in range(1, self.cycle_days + 1):
            daily_profit = total_capital * self.daily_profit_rate
            total_profit += daily_profit
            total_capital += daily_profit
            
            # Append the results for the day
            daily_results.append({
                'Day': day,
                'Daily Profit': daily_profit,
                'Total Capital': total_capital
            })
        
        # Create a DataFrame from the results
        return pd.DataFrame(daily_results)

def main():
    # Parameters for investment simulation
    initial_investment = 1000  # Starting investment amount
    daily_profit_rate = 0.01    # Daily profit rate (1%)

    try:
        # Create an instance of InvestmentCycle
        investment = InvestmentCycle(initial_investment, daily_profit_rate)
        
        # Run the simulation
        results = investment.simulate()
        
        # Display the results
        print(results)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
