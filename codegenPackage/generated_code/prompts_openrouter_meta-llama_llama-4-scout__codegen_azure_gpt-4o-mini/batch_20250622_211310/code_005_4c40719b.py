"""
Generated Code Metadata:
========================
Original URL: https://immediatecode.app
Prompt: "Design a risk management system for investment portfolios, incorporating features such as stop-loss orders and position sizing, and provide an example code in a programming language of choice."
Generated: DETERMINISTIC_4c40719b29f89ce3
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

class InvestmentPortfolio:
    def __init__(self):
        """Initialize an empty investment portfolio."""
        self.positions = {}
    
    def add_position(self, symbol, quantity, entry_price):
        """
        Add a new position to the portfolio.
        
        :param symbol: The stock symbol for the investment.
        :param quantity: The number of shares purchased.
        :param entry_price: The price at which the shares were purchased.
        """
        if symbol in self.positions:
            raise ValueError(f"Position for {symbol} already exists.")
        self.positions[symbol] = {
            'quantity': quantity,
            'entry_price': entry_price,
            'stop_loss': None
        }
    
    def set_stop_loss(self, symbol, stop_loss_price):
        """
        Set a stop-loss order for a specific position.
        
        :param symbol: The stock symbol for the investment.
        :param stop_loss_price: The price at which to trigger the stop-loss.
        """
        if symbol not in self.positions:
            raise ValueError(f"No position found for {symbol}.")
        self.positions[symbol]['stop_loss'] = stop_loss_price
    
    def calculate_position_size(self, total_capital, risk_per_trade, entry_price):
        """
        Calculate the position size based on total capital and risk parameters.
        
        :param total_capital: The total capital available for investment.
        :param risk_per_trade: The amount of capital to risk on a single trade.
        :param entry_price: The price at which the shares will be purchased.
        :return: The number of shares to purchase.
        """
        if entry_price <= 0:
            raise ValueError("Entry price must be greater than zero.")
        position_size = risk_per_trade / (entry_price * 0.1)  # Assuming a 10% stop-loss
        return int(position_size)
    
    def check_stop_loss(self, current_prices):
        """
        Check if any positions have hit their stop-loss prices.
        
        :param current_prices: A dictionary of current prices for each symbol.
        :return: A list of symbols that have hit their stop-loss.
        """
        stopped_out = []
        for symbol, data in self.positions.items():
            if data['stop_loss'] is not None and current_prices.get(symbol, float('inf')) <= data['stop_loss']:
                stopped_out.append(symbol)
        return stopped_out

# Example usage
if __name__ == "__main__":
    try:
        portfolio = InvestmentPortfolio()
        portfolio.add_position('AAPL', 10, 150.00)
        portfolio.set_stop_loss('AAPL', 135.00)
        
        total_capital = 10000
        risk_per_trade = 200
        entry_price = 150.00
        position_size = portfolio.calculate_position_size(total_capital, risk_per_trade, entry_price)
        print(f"Calculated position size for AAPL: {position_size} shares")
        
        # Simulate current prices
        current_prices = {'AAPL': 130.00}
        stopped_out_positions = portfolio.check_stop_loss(current_prices)
        if stopped_out_positions:
            print(f"Stopped out positions: {stopped_out_positions}")
        else:
            print("No positions hit stop-loss.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
