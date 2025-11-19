"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Write a Python script that calculates the optimal investment strategy based on risk tolerance and time horizon, similar to the personalized investment services offered by TSM Wealth.
Generated: DETERMINISTIC_14640f4835a001ca
Batch ID: 20250612_162050
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

class InvestmentStrategy:
    def __init__(self, risk_tolerance: str, time_horizon: int):
        """
        Initializes the InvestmentStrategy with risk tolerance and time horizon.

        :param risk_tolerance: A string indicating the risk tolerance ('low', 'medium', 'high').
        :param time_horizon: An integer representing the time horizon in years.
        """
        self.risk_tolerance = risk_tolerance.lower()
        self.time_horizon = time_horizon
        self.asset_allocation = self.calculate_allocation()

    def calculate_allocation(self) -> dict:
        """
        Calculates the asset allocation based on risk tolerance and time horizon.

        :return: A dictionary representing the asset allocation.
        """
        allocation = {}
        try:
            if self.risk_tolerance == 'low':
                allocation = {'bonds': 70, 'stocks': 20, 'cash': 10}
            elif self.risk_tolerance == 'medium':
                allocation = {'bonds': 50, 'stocks': 40, 'cash': 10}
            elif self.risk_tolerance == 'high':
                allocation = {'bonds': 20, 'stocks': 70, 'cash': 10}
            else:
                raise ValueError("Invalid risk tolerance. Choose from 'low', 'medium', or 'high'.")

            # Adjust allocation based on time horizon
            if self.time_horizon < 5:
                allocation['bonds'] += 10  # More conservative for short time horizons
                allocation['stocks'] -= 10
            elif self.time_horizon > 10:
                allocation['stocks'] += 10  # More aggressive for long time horizons
                allocation['bonds'] -= 10

            # Ensure total allocation is 100%
            total_allocation = sum(allocation.values())
            if total_allocation != 100:
                raise ValueError(f"Total allocation must equal 100%, currently {total_allocation}%.")

        except Exception as e:
            print(f"Error calculating allocation: {e}")
            allocation = {}

        return allocation

    def get_investment_plan(self) -> pd.DataFrame:
        """
        Returns a DataFrame containing the investment plan with asset allocation.

        :return: A pandas DataFrame with the investment strategy.
        """
        try:
            allocation_df = pd.DataFrame(list(self.asset_allocation.items()), columns=['Asset Type', 'Allocation (%)'])
            return allocation_df
        except Exception as e:
            print(f"Error creating investment plan DataFrame: {e}")
            return pd.DataFrame()

if __name__ == "__main__":
    # Example usage
    risk_tolerance_input = input("Enter your risk tolerance (low, medium, high): ")
    time_horizon_input = int(input("Enter your time horizon in years: "))

    # Create an investment strategy object
    investment_strategy = InvestmentStrategy(risk_tolerance_input, time_horizon_input)

    # Get and display the investment plan
    investment_plan = investment_strategy.get_investment_plan()
    print("\nYour Investment Strategy:")
    print(investment_plan)
```
