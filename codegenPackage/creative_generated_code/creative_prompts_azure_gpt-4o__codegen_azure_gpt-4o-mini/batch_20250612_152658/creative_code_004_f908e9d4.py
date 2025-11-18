"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoreumdashboard.com
Prompt: Write a Python script to calculate the projected market cap growth of Thoreum based on its bonding mechanism and liquidity increase rate of 25% per quarter.
Generated: DETERMINISTIC_f908e9d418ba7ae4
Batch ID: 20250612_152658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class MarketCapCalculator:
    """
    A class to calculate the projected market cap growth based on 
    bonding mechanism and liquidity increase rate.
    """

    def __init__(self, initial_market_cap, growth_rate=0.25, quarters=10):
        """
        Initializes the MarketCapCalculator with initial parameters.

        :param initial_market_cap: Initial market cap value in USD
        :param growth_rate: Quarterly liquidity increase rate (default is 25%)
        :param quarters: Number of quarters to project (default is 10)
        """
        if initial_market_cap < 0:
            raise ValueError("Initial market cap must be a non-negative value.")
        if not (0 <= growth_rate <= 1):
            raise ValueError("Growth rate must be between 0 and 1.")
        if quarters < 0:
            raise ValueError("Number of quarters must be a non-negative integer.")

        self.initial_market_cap = initial_market_cap
        self.growth_rate = growth_rate
        self.quarters = quarters

    def calculate_projected_market_cap(self):
        """
        Calculates the projected market cap growth over the specified number of quarters.

        :return: A list of projected market cap values for each quarter
        """
        projected_caps = []
        current_market_cap = self.initial_market_cap

        for quarter in range(1, self.quarters + 1):
            current_market_cap *= (1 + self.growth_rate)
            projected_caps.append(current_market_cap)

        return projected_caps

def main():
    """
    Main function to execute the market cap calculation.
    """
    try:
        # User-defined parameters
        initial_market_cap = float(input("Enter the initial market cap (in USD): "))
        growth_rate = 0.25  # 25% quarterly growth
        quarters = int(input("Enter the number of quarters to project: "))

        # Initialize the MarketCapCalculator
        calculator = MarketCapCalculator(initial_market_cap, growth_rate, quarters)
        
        # Calculate projected market caps
        projected_caps = calculator.calculate_projected_market_cap()

        # Display the results
        print("\nProjected Market Cap Growth Over Quarters:")
        for i, cap in enumerate(projected_caps, start=1):
            print(f"Quarter {i}: ${cap:,.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
