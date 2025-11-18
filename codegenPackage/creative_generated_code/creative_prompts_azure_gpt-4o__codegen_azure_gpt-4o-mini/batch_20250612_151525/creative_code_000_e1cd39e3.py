"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Write Python code to calculate a personalized asset allocation strategy based on a user's financial goals, as described in the Ahmeti Wealth Management process. Include risk-reward balancing in the calculation.
Generated: DETERMINISTIC_e1cd39e3d9d001c8
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np

class AssetAllocation:
    """
    A class to calculate personalized asset allocation based on user financial goals
    and risk tolerance.

    Attributes:
        risk_tolerance (float): The user's risk tolerance on a scale from 0 to 1.
        investment_horizon (int): The investment horizon in years.
        financial_goals (dict): A dictionary of financial goals with associated amounts.
    """

    def __init__(self, risk_tolerance: float, investment_horizon: int, financial_goals: dict):
        """
        Initializes the AssetAllocation class.

        Args:
            risk_tolerance (float): User's risk tolerance.
            investment_horizon (int): User's investment horizon in years.
            financial_goals (dict): User's financial goals.
        
        Raises:
            ValueError: If risk_tolerance is not between 0 and 1, or if investment_horizon is negative.
        """
        if not (0 <= risk_tolerance <= 1):
            raise ValueError("Risk tolerance must be between 0 and 1.")
        if investment_horizon < 0:
            raise ValueError("Investment horizon cannot be negative.")
        
        self.risk_tolerance = risk_tolerance
        self.investment_horizon = investment_horizon
        self.financial_goals = financial_goals
        self.asset_classes = {
            'stocks': 0.0,
            'bonds': 0.0,
            'real_estate': 0.0,
            'cash': 0.0
        }

    def calculate_asset_allocation(self):
        """
        Calculate the asset allocation based on risk tolerance, investment horizon,
        and financial goals.

        Returns:
            dict: Recommended asset allocation percentages for each asset class.
        """
        total_goals = sum(self.financial_goals.values())
        if total_goals == 0:
            raise ValueError("Total financial goals cannot be zero.")

        # Adjust weights based on risk tolerance and investment horizon
        self.asset_classes['stocks'] = min(1.0, self.risk_tolerance + (self.investment_horizon / 100))
        self.asset_classes['bonds'] = max(0.0, (1 - self.asset_classes['stocks']) * 0.7)
        self.asset_classes['real_estate'] = max(0.0, (self.risk_tolerance * 0.2))
        self.asset_classes['cash'] = 1 - (self.asset_classes['stocks'] + self.asset_classes['bonds'] + self.asset_classes['real_estate'])

        # Normalize asset classes to total 100%
        total_allocation = sum(self.asset_classes.values())
        self.asset_classes = {asset: allocation / total_allocation for asset, allocation in self.asset_classes.items()}

        return self.asset_classes

def main():
    """ 
    Main function to execute asset allocation calculation based on user input.
    """
    try:
        risk_tolerance = float(input("Enter your risk tolerance (0 to 1): "))
        investment_horizon = int(input("Enter your investment horizon in years: "))
        financial_goals = {
            'retirement': float(input("Enter amount needed for retirement: ")),
            'home_purchase': float(input("Enter amount needed for home purchase: ")),
            'education': float(input("Enter amount needed for education: "))
        }
        
        allocation = AssetAllocation(risk_tolerance, investment_horizon, financial_goals)
        asset_allocation = allocation.calculate_asset_allocation()
        
        print("Recommended Asset Allocation:")
        for asset, percentage in asset_allocation.items():
            print(f"{asset.capitalize()}: {percentage:.2%}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
