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

class InvestmentStrategyCalculator:
    """
    A class to calculate optimal investment strategy based on risk tolerance and time horizon.
    """

    def __init__(self, risk_tolerance: str, time_horizon: int):
        """
        Initializes the investment strategy calculator.

        :param risk_tolerance: A string indicating the risk tolerance ('low', 'medium', 'high').
        :param time_horizon: An integer representing the time horizon in years.
        """
        self.risk_tolerance = risk_tolerance.lower()
        self.time_horizon = time_horizon
        self.validate_inputs()

    def validate_inputs(self):
        """
        Validates the input parameters to ensure they are correct.
        Raises ValueError for invalid inputs.
        """
        if self.risk_tolerance not in ('low', 'medium', 'high'):
            raise ValueError("Risk tolerance must be 'low', 'medium', or 'high'.")
        if not isinstance(self.time_horizon, int) or self.time_horizon <= 0:
            raise ValueError("Time horizon must be a positive integer.")

    def allocate_assets(self):
        """
        Allocates assets based on risk tolerance and time horizon.

        :return: Dictionary indicating the percentage allocation for stocks, bonds, and cash.
        """
        if self.risk_tolerance == 'low':
            # Conservative risk tolerance
            stock_allocation = max(20, self.time_horizon * 2)
            bond_allocation = min(70, 100 - stock_allocation - 10)
            cash_allocation = 10
        elif self.risk_tolerance == 'medium':
            # Balanced risk tolerance
            stock_allocation = max(50, self.time_horizon * 3)
            bond_allocation = min(40, 100 - stock_allocation - 10)
            cash_allocation = 10
        else:
            # Aggressive risk tolerance
            stock_allocation = max(80, self.time_horizon * 4)
            bond_allocation = min(10, 100 - stock_allocation)
            cash_allocation = 10

        return {
            "Stocks (%)": stock_allocation,
            "Bonds (%)": bond_allocation,
            "Cash (%)": cash_allocation
        }

    def simulate_growth(self, initial_investment: float, annual_return_rates: dict):
        """
        Simulates portfolio growth over the time horizon.

        :param initial_investment: Initial amount of money to invest.
        :param annual_return_rates: Dictionary with annual return rates for stocks, bonds, and cash.
        :return: Projected portfolio value at the end of the time horizon.
        """
        if not isinstance(initial_investment, (int, float)) or initial_investment <= 0:
            raise ValueError("Initial investment must be a positive number.")

        allocations = self.allocate_assets()
        total_value = initial_investment

        for year in range(1, self.time_horizon + 1):
            stocks_growth = total_value * (allocations["Stocks (%)"] / 100) * (1 + annual_return_rates.get('stocks', 0))
            bonds_growth = total_value * (allocations["Bonds (%)"] / 100) * (1 + annual_return_rates.get('bonds', 0))
            cash_growth = total_value * (allocations["Cash (%)"] / 100) * (1 + annual_return_rates.get('cash', 0))
            total_value = stocks_growth + bonds_growth + cash_growth

        return round(total_value, 2)

def main():
    """
    Main function to demonstrate the investment strategy calculator.
    """
    try:
        # Input parameters
        risk_tolerance = input("Enter your risk tolerance (low/medium/high): ").strip()
        time_horizon = int(input("Enter your time horizon in years: "))
        initial_investment = float(input("Enter your initial investment amount: "))

        # Annual return rates (example values)
        annual_return_rates = {
            'stocks': 0.07,  # 7% annual return
            'bonds': 0.03,   # 3% annual return
            'cash': 0.01     # 1% annual return
        }

        # Calculate investment strategy
        calculator = InvestmentStrategyCalculator(risk_tolerance, time_horizon)
        allocations = calculator.allocate_assets()
        projected_value = calculator.simulate_growth(initial_investment, annual_return_rates)

        # Display results
        print("\nRecommended Asset Allocation:")
        for asset, percentage in allocations.items():
            print(f"{asset}: {percentage}%")
        print(f"\nProjected portfolio value after {time_horizon} years: ${projected_value}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
