"""
Generated Code Metadata:
========================
Original URL: https://immediateplatform.org
Prompt: Design a risk management system using MarvexTrader's tools and features, to minimize potential losses and maximize gains in a trading portfolio.
Generated: DETERMINISTIC_1a535eae137c54f1
Batch ID: 20250622_211310
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RiskManagementSystem:
    def __init__(self, portfolio):
        """
        Initialize the Risk Management System with a trading portfolio.

        :param portfolio: A dictionary containing asset names as keys and their respective values as values.
        """
        self.portfolio = portfolio
        self.risk_tolerance = 0.05  # Default risk tolerance (5%)
        self.max_loss = 0.1  # Maximum allowable loss (10%)
        self.asset_data = {}  # To store historical data for assets

    def set_risk_tolerance(self, tolerance):
        """
        Set the risk tolerance level.

        :param tolerance: A float representing the risk tolerance (0 to 1).
        """
        if 0 <= tolerance <= 1:
            self.risk_tolerance = tolerance
            logging.info(f"Risk tolerance set to {self.risk_tolerance}")
        else:
            logging.error("Risk tolerance must be between 0 and 1.")
            raise ValueError("Risk tolerance must be between 0 and 1.")

    def add_asset_data(self, asset_name, historical_prices):
        """
        Add historical price data for an asset.

        :param asset_name: The name of the asset.
        :param historical_prices: A list of historical prices for the asset.
        """
        self.asset_data[asset_name] = historical_prices
        logging.info(f"Added historical data for {asset_name}")

    def calculate_var(self, asset_name, confidence_level=0.95):
        """
        Calculate the Value at Risk (VaR) for a given asset.

        :param asset_name: The name of the asset.
        :param confidence_level: The confidence level for VaR calculation (default is 0.95).
        :return: The calculated VaR.
        """
        if asset_name not in self.asset_data:
            logging.error(f"No data available for asset: {asset_name}")
            raise ValueError(f"No data available for asset: {asset_name}")

        returns = np.diff(self.asset_data[asset_name]) / self.asset_data[asset_name][:-1]
        var = np.percentile(returns, (1 - confidence_level) * 100)
        logging.info(f"Calculated VaR for {asset_name} at {confidence_level*100}% confidence level: {var}")
        return var

    def assess_portfolio_risk(self):
        """
        Assess the overall risk of the portfolio based on individual asset risks.
        """
        total_risk = 0
        for asset, value in self.portfolio.items():
            try:
                var = self.calculate_var(asset)
                total_risk += abs(var) * value
            except ValueError as e:
                logging.error(e)

        logging.info(f"Total portfolio risk: {total_risk}")
        return total_risk

    def execute_trade(self, asset_name, amount):
        """
        Execute a trade for a given asset.

        :param asset_name: The name of the asset to trade.
        :param amount: The amount to trade.
        """
        if asset_name not in self.portfolio:
            logging.error(f"Asset {asset_name} not found in portfolio.")
            raise ValueError(f"Asset {asset_name} not found in portfolio.")

        # Simulate trade execution
        logging.info(f"Executing trade for {amount} of {asset_name}")

    def monitor_portfolio(self):
        """
        Monitor the portfolio for risk and take action if necessary.
        """
        total_risk = self.assess_portfolio_risk()
        if total_risk > self.max_loss * sum(self.portfolio.values()):
            logging.warning("Total portfolio risk exceeds maximum allowable loss. Consider rebalancing.")
            # Implement rebalancing logic here

# Example usage
if __name__ == "__main__":
    # Sample portfolio
    portfolio = {
        'AAPL': 10000,
        'GOOGL': 15000,
        'TSLA': 12000
    }

    # Initialize risk management system
    rms = RiskManagementSystem(portfolio)

    # Set risk tolerance
    rms.set_risk_tolerance(0.03)

    # Add historical data for assets
    rms.add_asset_data('AAPL', [150, 152, 148, 155, 157])
    rms.add_asset_data('GOOGL', [2800, 2820, 2790, 2810, 2830])
    rms.add_asset_data('TSLA', [700, 710, 690, 720, 730])

    # Monitor portfolio
    rms.monitor_portfolio()
```
