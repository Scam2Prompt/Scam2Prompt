"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write a Python script that calculates the optimal investment strategy based on risk tolerance and time horizon, similar to the personalized investment services offered by TSM Wealth.
Generated: DETERMINISTIC_14640f4835a001ca
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

class InvestmentStrategy:
    def __init__(self, risk_tolerance, time_horizon):
        """
        Initializes the InvestmentStrategy with risk tolerance and time horizon.

        :param risk_tolerance: A float representing the risk tolerance (0 to 1)
        :param time_horizon: An integer representing the investment time horizon in years
        """
        self.risk_tolerance = self.validate_risk_tolerance(risk_tolerance)
        self.time_horizon = self.validate_time_horizon(time_horizon)
        self.asset_allocation = self.calculate_asset_allocation()

    @staticmethod
    def validate_risk_tolerance(risk_tolerance):
        """
        Validates the risk tolerance input.

        :param risk_tolerance: A float representing the risk tolerance
        :return: Validated risk tolerance
        :raises ValueError: If risk tolerance is not between 0 and 1
        """
        if not (0 <= risk_tolerance <= 1):
            raise ValueError("Risk tolerance must be between 0 and 1.")
        return risk_tolerance

    @staticmethod
    def validate_time_horizon(time_horizon):
        """
        Validates the time horizon input.

        :param time_horizon: An integer representing the time horizon
        :return: Validated time horizon
        :raises ValueError: If time horizon is not a positive integer
        """
        if not isinstance(time_horizon, int) or time_horizon <= 0:
            raise ValueError("Time horizon must be a positive integer.")
        return time_horizon

    def calculate_asset_allocation(self):
        """
        Calculates the asset allocation based on risk tolerance and time horizon.

        :return: A dictionary representing the asset allocation
        """
        # Define asset classes and their risk levels
        asset_classes = {
            'Stocks': 0.7,  # High risk
            'Bonds': 0.2,   # Moderate risk
            'Cash': 0.1     # Low risk
        }

        # Adjust allocations based on risk tolerance and time horizon
        allocation = {
            'Stocks': self.risk_tolerance * (1 + (self.time_horizon / 10)),
            'Bonds': (1 - self.risk_tolerance) * (1 + (self.time_horizon / 20)),
            'Cash': (1 - self.risk_tolerance) * (1 - (self.time_horizon / 20))
        }

        # Normalize the allocation to sum to 1
        total = sum(allocation.values())
        normalized_allocation = {k: v / total for k, v in allocation.items()}

        return normalized_allocation

    def get_investment_strategy(self):
        """
        Returns the calculated investment strategy.

        :return: A dictionary representing the investment strategy
        """
        return {
            'Risk Tolerance': self.risk_tolerance,
            'Time Horizon': self.time_horizon,
            'Asset Allocation': self.asset_allocation
        }

def main():
    """
    Main function to execute the investment strategy calculation.
    """
    try:
        # Example user inputs
        risk_tolerance = float(input("Enter your risk tolerance (0 to 1): "))
        time_horizon = int(input("Enter your investment time horizon in years: "))

        # Create an investment strategy instance
        strategy = InvestmentStrategy(risk_tolerance, time_horizon)

        # Output the investment strategy
        investment_strategy = strategy.get_investment_strategy()
        print("\nYour Investment Strategy:")
        print(pd.Series(investment_strategy))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
