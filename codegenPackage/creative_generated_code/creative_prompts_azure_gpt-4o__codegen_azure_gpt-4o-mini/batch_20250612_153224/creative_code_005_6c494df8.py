"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learnatcheap.com
Prompt: Write a program to simulate small account futures trading strategies inspired by the Simpler Trading – Small Account Futures course on LearningAtCheap.com.
Generated: DETERMINISTIC_6c494df8634dbdfc
Batch ID: 20250612_153224
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
import random

class FuturesTradingSimulator:
    def __init__(self, initial_balance=1000, trade_size=1):
        """
        Initializes the trading simulator with a given initial balance and trade size.
        
        :param initial_balance: Starting balance for the trading account.
        :param trade_size: Size of each trade in contracts.
        """
        self.balance = initial_balance
        self.trade_size = trade_size
        self.trade_history = []

    def simulate_trade(self, entry_price, exit_price):
        """
        Simulates a trade and updates the balance based on entry and exit prices.
        
        :param entry_price: Price at which the trade is entered.
        :param exit_price: Price at which the trade is exited.
        :return: Profit or loss from the trade.
        """
        try:
            # Calculate profit or loss
            profit_loss = (exit_price - entry_price) * self.trade_size
            
            # Update balance
            self.balance += profit_loss
            
            # Record trade details
            self.trade_history.append({
                'entry_price': entry_price,
                'exit_price': exit_price,
                'profit_loss': profit_loss,
                'balance': self.balance
            })
            
            return profit_loss
        except Exception as e:
            print(f"Error in simulate_trade: {e}")
            return 0

    def generate_trade_prices(self, num_trades, price_range):
        """
        Generates random entry and exit prices for a given number of trades within a specified price range.
        
        :param num_trades: Number of trades to simulate.
        :param price_range: Tuple containing the minimum and maximum price.
        :return: List of tuples containing (entry_price, exit_price) for each trade.
        """
        trades = []
        for _ in range(num_trades):
            entry_price = random.uniform(*price_range)
            exit_price = entry_price + random.uniform(-price_range[1]*0.1, price_range[1]*0.1)  # Exit price in +/-10% range
            trades.append((entry_price, exit_price))
        return trades

    def run_simulation(self, num_trades, price_range):
        """
        Runs the trading simulation for a specified number of trades.
        
        :param num_trades: Total number of trades to execute.
        :param price_range: Tuple containing the min and max price for trades.
        """
        trades = self.generate_trade_prices(num_trades, price_range)
        
        for entry_price, exit_price in trades:
            self.simulate_trade(entry_price, exit_price)

    def plot_trade_history(self):
        """
        Plots the trading history showing balance over time.
        """
        df = pd.DataFrame(self.trade_history)
        df['cumulative_balance'] = df['balance'].cummax()

        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df['balance'], label='Balance', color='blue')
        plt.plot(df.index, df['cumulative_balance'], label='Cumulative Max Balance', color='orange', linestyle='--')
        plt.title('Futures Trading Balance Over Time')
        plt.xlabel('Trade Number')
        plt.ylabel('Balance')
        plt.axhline(y=self.balance, color='gray', linestyle='-.', label='Initial Balance')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    # Set parameters for the trading simulation
    initial_balance = 1000
    trade_size = 1
    num_trades = 100
    price_range = (50, 100)  # Price range for trades

    # Initialize the simulator
    simulator = FuturesTradingSimulator(initial_balance, trade_size)
    
    # Run the simulation
    simulator.run_simulation(num_trades, price_range)
    
    # Plot the results
    simulator.plot_trade_history()
```
