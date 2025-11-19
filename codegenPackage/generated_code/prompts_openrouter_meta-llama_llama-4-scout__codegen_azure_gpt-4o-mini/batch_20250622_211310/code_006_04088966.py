"""
Generated Code Metadata:
========================
Original URL: https://immediateflow.co
Prompt: "Outline a structured approach to building a diversified investment portfolio, considering factors like risk tolerance, investment horizon, and asset allocation, in line with Petrolio Italiano's educational philosophy."
Generated: DETERMINISTIC_040889664114621e
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPortfolio:
    """
    A class to represent a diversified investment portfolio.

    Attributes:
        risk_tolerance (str): The risk tolerance of the investor ('low', 'medium', 'high').
        investment_horizon (int): The investment horizon in years.
        asset_allocation (dict): A dictionary representing the asset allocation.
    """

    def __init__(self, risk_tolerance: str, investment_horizon: int):
        """
        Initializes the InvestmentPortfolio with risk tolerance and investment horizon.

        Args:
            risk_tolerance (str): The risk tolerance of the investor.
            investment_horizon (int): The investment horizon in years.

        Raises:
            ValueError: If risk_tolerance is not one of 'low', 'medium', 'high'.
            ValueError: If investment_horizon is not a positive integer.
        """
        if risk_tolerance not in ['low', 'medium', 'high']:
            raise ValueError("Risk tolerance must be 'low', 'medium', or 'high'.")
        if investment_horizon <= 0:
            raise ValueError("Investment horizon must be a positive integer.")

        self.risk_tolerance = risk_tolerance
        self.investment_horizon = investment_horizon
        self.asset_allocation = self.calculate_asset_allocation()

    def calculate_asset_allocation(self) -> dict:
        """
        Calculates the asset allocation based on risk tolerance and investment horizon.

        Returns:
            dict: A dictionary representing the asset allocation.
        """
        allocation = {
            'stocks': 0,
            'bonds': 0,
            'real_estate': 0,
            'cash': 0
        }

        if self.risk_tolerance == 'low':
            allocation['bonds'] = 70
            allocation['stocks'] = 20
            allocation['real_estate'] = 5
            allocation['cash'] = 5
        elif self.risk_tolerance == 'medium':
            allocation['bonds'] = 50
            allocation['stocks'] = 40
            allocation['real_estate'] = 5
            allocation['cash'] = 5
        else:  # high risk tolerance
            allocation['bonds'] = 20
            allocation['stocks'] = 70
            allocation['real_estate'] = 5
            allocation['cash'] = 5

        # Adjust allocation based on investment horizon
        if self.investment_horizon < 5:
            allocation['bonds'] += 10
            allocation['stocks'] -= 10

        return allocation

    def display_portfolio(self):
        """
        Displays the current asset allocation of the portfolio.
        """
        print("Current Asset Allocation:")
        for asset, percentage in self.asset_allocation.items():
            print(f"{asset.capitalize()}: {percentage}%")

# Example usage
if __name__ == "__main__":
    try:
        # Create an investment portfolio with specified risk tolerance and investment horizon
        portfolio = InvestmentPortfolio(risk_tolerance='medium', investment_horizon=10)
        portfolio.display_portfolio()
    except ValueError as e:
        print(f"Error: {e}")
```
