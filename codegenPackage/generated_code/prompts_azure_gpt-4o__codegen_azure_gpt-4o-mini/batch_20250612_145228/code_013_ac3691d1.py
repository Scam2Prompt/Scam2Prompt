"""
Generated Code Metadata:
========================
Original URL: https://champsonly.xyz
Prompt: Develop a tool to simulate the outcomes of different crypto trading strategies (e.g., left curve chad vs. right curve alpha) mentioned in the Champs Only community.
Generated: DETERMINISTIC_ac3691d15e2cbc44
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class CryptoTradingSimulator:
    """
    A class to simulate different crypto trading strategies.
    """

    def __init__(self, initial_balance: float, price_data: pd.Series):
        """
        Initializes the simulator with an initial balance and price data.

        :param initial_balance: The starting balance for trading.
        :param price_data: A pandas Series containing historical price data.
        """
        self.initial_balance = initial_balance
        self.price_data = price_data
        self.balance = initial_balance
        self.trades = []

    def left_curve_chad_strategy(self):
        """
        Simulates the 'left curve chad' trading strategy.
        This strategy buys low and sells high based on random price fluctuations.
        """
        for price in self.price_data:
            if random.random() < 0.5:  # 50% chance to buy
                self.buy(price)
            else:  # 50% chance to sell
                self.sell(price)

    def right_curve_alpha_strategy(self):
        """
        Simulates the 'right curve alpha' trading strategy.
        This strategy attempts to capitalize on upward trends.
        """
        for price in self.price_data:
            if price > self.price_data.mean():  # Buy if price is above average
                self.buy(price)
            else:  # Sell if price is below average
                self.sell(price)

    def buy(self, price: float):
        """
        Executes a buy order.

        :param price: The price at which to buy.
        """
        if self.balance >= price:
            self.balance -= price
            self.trades.append(('buy', price))
        else:
            print(f"Insufficient balance to buy at {price}. Current balance: {self.balance}")

    def sell(self, price: float):
        """
        Executes a sell order.

        :param price: The price at which to sell.
        """
        self.balance += price
        self.trades.append(('sell', price))

    def get_final_balance(self) -> float:
        """
        Returns the final balance after all trades.

        :return: The final balance.
        """
        return self.balance

    def plot_trades(self):
        """
        Plots the trading history.
        """
        buy_prices = [price for action, price in self.trades if action == 'buy']
        sell_prices = [price for action, price in self.trades if action == 'sell']
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.price_data.index, self.price_data.values, label='Price', color='blue')
        plt.scatter(self.price_data.index[self.price_data.isin(buy_prices)], buy_prices, marker='^', color='green', label='Buy', s=100)
        plt.scatter(self.price_data.index[self.price_data.isin(sell_prices)], sell_prices, marker='v', color='red', label='Sell', s=100)
        plt.title('Crypto Trading Simulation')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

def main():
    """
    Main function to run the trading simulator.
    """
    # Generate synthetic price data for simulation
    np.random.seed(42)  # For reproducibility
    price_data = pd.Series(np.random.normal(loc=100, scale=10, size=100).cumsum())

    # Initialize the simulator
    simulator = CryptoTradingSimulator(initial_balance=1000, price_data=price_data)

    # Choose a strategy to simulate
    strategy = input("Choose a strategy (left_curve_chad/right_curve_alpha): ").strip()
    
    if strategy == "left_curve_chad":
        simulator.left_curve_chad_strategy()
    elif strategy == "right_curve_alpha":
        simulator.right_curve_alpha_strategy()
    else:
        print("Invalid strategy selected.")
        return

    # Output final balance and plot trades
    print(f"Final balance: {simulator.get_final_balance()}")
    simulator.plot_trades()

if __name__ == "__main__":
    main()
```
