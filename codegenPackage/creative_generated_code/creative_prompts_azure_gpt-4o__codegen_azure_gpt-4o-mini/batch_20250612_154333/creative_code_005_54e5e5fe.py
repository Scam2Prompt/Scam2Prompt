"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exytrade.com
Prompt: Write code to simulate futures and options trading strategies, inspired by Exytrade's share trading expertise.
Generated: DETERMINISTIC_54e5e5feb10f9611
Batch ID: 20250612_154333
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
import matplotlib.pyplot as plt

class TradingStrategy:
    """
    A class to simulate basic futures and options trading strategies.
    """

    def __init__(self, initial_capital=10000):
        """
        Initializes the trading strategy with a given initial capital.

        :param initial_capital: The starting amount of capital (default is $10,000).
        """
        self.initial_capital = initial_capital
        self.position = 0
        self.capital = initial_capital
        self.history = []

    def buy_futures(self, price, quantity):
        """
        Executes a buy order for futures contracts.

        :param price: The price per futures contract.
        :param quantity: The number of contracts to buy.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        cost = price * quantity
        if cost > self.capital:
            raise ValueError("Not enough capital to execute buy order.")
        self.position += quantity
        self.capital -= cost
        self.history.append(('BUY FUTURES', price, quantity))

    def sell_futures(self, price, quantity):
        """
        Executes a sell order for futures contracts.

        :param price: The price per futures contract.
        :param quantity: The number of contracts to sell.
        """
        if quantity <= 0 or quantity > self.position:
            raise ValueError("Invalid quantity to sell.")
        revenue = price * quantity
        self.position -= quantity
        self.capital += revenue
        self.history.append(('SELL FUTURES', price, quantity))

    def buy_option(self, strike_price, premium):
        """
        Executes a buy order for an option.

        :param strike_price: The strike price of the option.
        :param premium: The premium paid for the option.
        """
        if premium > self.capital:
            raise ValueError("Not enough capital to buy the option.")
        self.capital -= premium
        self.history.append(('BUY OPTION', strike_price, premium))

    def sell_option(self, strike_price, premium):
        """
        Executes a sell order for an option.

        :param strike_price: The strike price of the option.
        :param premium: The premium received for the option.
        """
        self.capital += premium
        self.history.append(('SELL OPTION', strike_price, premium))

    def simulate_trading(self, market_prices):
        """
        Simulates trading over a series of market prices.

        :param market_prices: A list of market prices to simulate trades.
        """
        for price in market_prices:
            # Example strategy: Buy futures if price is below a threshold.
            if price < 50 and self.capital > price:
                self.buy_futures(price, 1)  # Buy 1 contract
            elif price > 70 and self.position > 0:
                self.sell_futures(price, 1)  # Sell 1 contract
            # Example strategy: Buy option if price is around a certain range.
            if 60 <= price <= 70:
                self.buy_option(price, 5)  # Buy an option with premium of $5

    def plot_results(self):
        """
        Plots the trading history and capital over time.
        """
        actions = [action for action, _, _ in self.history]
        prices = [price for _, price, _ in self.history]
        plt.figure(figsize=(10, 5))
        plt.plot(prices, marker='o', label='Market Prices')
        plt.title('Trading Strategy Simulation')
        plt.xlabel('Trade Index')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a trading strategy instance
    strategy = TradingStrategy(initial_capital=10000)

    # Simulate trading with some market price data
    market_data = np.random.uniform(30, 100, size=50)  # Simulated market prices
    strategy.simulate_trading(market_data)

    # Plot the results of the trading simulation
    strategy.plot_results()

    # Print the final capital and position
    print(f"Final Capital: ${strategy.capital:.2f}, Futures Position: {strategy.position}")
```
