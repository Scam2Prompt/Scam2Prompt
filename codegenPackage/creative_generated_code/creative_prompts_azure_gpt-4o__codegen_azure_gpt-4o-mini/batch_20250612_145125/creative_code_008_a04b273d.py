"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptosolutionz.com
Prompt: Develop a portfolio management tool in Python that incorporates Crypto Solutionz's risk management strategies, including diversification and stop-loss mechanisms.
Generated: DETERMINISTIC_a04b273d884e399f
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

class PortfolioManager:
    """
    A class to manage a portfolio of assets with risk management strategies.
    """

    def __init__(self, assets, initial_investment):
        """
        Initialize the portfolio manager.

        :param assets: A list of asset symbols.
        :param initial_investment: Total initial investment amount.
        """
        self.assets = assets
        self.initial_investment = initial_investment
        self.portfolio = {asset: 0 for asset in self.assets}
        self.stop_loss_threshold = 0.1  # Set stop-loss at 10%
        self.diversification_limit = 0.2  # Maximum 20% in a single asset

    def buy_asset(self, asset, amount):
        """
        Buy a specific asset.

        :param asset: The asset symbol to buy.
        :param amount: The amount to invest in the asset.
        """
        if asset not in self.assets:
            raise ValueError(f"Asset {asset} is not in the portfolio.")
        
        if amount + self.portfolio[asset] > self.initial_investment * self.diversification_limit:
            raise ValueError(f"Investment exceeds diversification limit for {asset}.")

        self.portfolio[asset] += amount
        print(f"Bought {amount} of {asset}. Current allocation: {self.portfolio[asset]}")

    def sell_asset(self, asset, amount):
        """
        Sell a specific asset.

        :param asset: The asset symbol to sell.
        :param amount: The amount to sell.
        """
        if asset not in self.assets:
            raise ValueError(f"Asset {asset} is not in the portfolio.")
        
        if amount > self.portfolio[asset]:
            raise ValueError(f"Not enough {asset} to sell.")

        self.portfolio[asset] -= amount
        print(f"Sold {amount} of {asset}. Current allocation: {self.portfolio[asset]}")

    def check_stop_loss(self, current_prices):
        """
        Check and execute stop-loss for the portfolio.

        :param current_prices: A dictionary with asset prices.
        """
        for asset, allocation in self.portfolio.items():
            if allocation > 0:
                original_investment = allocation
                current_price = current_prices.get(asset)
                
                if current_price is None:
                    raise ValueError(f"Price for {asset} not provided.")
                
                # Stop-loss condition
                if (original_investment - current_price) / original_investment >= self.stop_loss_threshold:
                    self.sell_asset(asset, allocation)
                    print(f"Stop-loss executed for {asset}.")

    def get_portfolio_value(self, current_prices):
        """
        Calculate the total portfolio value based on current prices.

        :param current_prices: A dictionary with asset prices.
        :return: Total current value of the portfolio.
        """
        total_value = 0
        for asset, allocation in self.portfolio.items():
            price = current_prices.get(asset)
            total_value += allocation if price is None else allocation * price
        return total_value

    def print_portfolio(self):
        """
        Print the current state of the portfolio.
        """
        print("Current Portfolio Allocation:")
        for asset, allocation in self.portfolio.items():
            print(f"{asset}: {allocation}")

# Example usage
if __name__ == "__main__":
    assets = ['BTC', 'ETH', 'LTC']
    initial_investment = 10000

    # Instantiate the Portfolio Manager
    pm = PortfolioManager(assets, initial_investment)

    # Buy assets
    pm.buy_asset('BTC', 2000)
    pm.buy_asset('ETH', 1500)

    # Current prices (for demonstration purposes)
    current_prices = {'BTC': 50000, 'ETH': 3000, 'LTC': 200}

    # Check and execute stop-loss
    pm.check_stop_loss(current_prices)

    # Print portfolio value
    total_value = pm.get_portfolio_value(current_prices)
    print(f"Total Portfolio Value: {total_value}")

    # Print current portfolio
    pm.print_portfolio()
```
