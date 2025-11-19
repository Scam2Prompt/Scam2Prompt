"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.nl
Prompt: Explain how to implement backtesting tools from Immediate Migna to evaluate different trading strategies for Ethereum.
Generated: DETERMINISTIC_8119d445f6f85651
Batch ID: 20250612_163052
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
import matplotlib.pyplot as plt

# Define the Backtesting class
class Backtester:
    """
    A backtesting tool to evaluate trading strategies for Ethereum.
    """

    def __init__(self, data: pd.DataFrame, initial_balance: float = 10000.0):
        """
        Initialize the backtester with historical data and initial account balance.
        
        :param data: A pandas DataFrame with at least columns 'Date', 'Close'.
        :param initial_balance: Starting balance for the backtest.
        """
        self.data = data
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.position = 0  # Ethereum held
        self.history = []  # Records all trades

    def apply_strategy(self, strategy_func):
        """
        Apply a given trading strategy function to the historical data.
        
        :param strategy_func: A function that takes a row and returns 'BUY', 'SELL', or 'HOLD'.
        """
        for i, row in self.data.iterrows():
            signal = strategy_func(row)
            self.execute_trade(signal, row)

    def execute_trade(self, signal: str, row: pd.Series):
        """
        Execute a trade based on the given signal.
        
        :param signal: 'BUY', 'SELL', or 'HOLD'.
        :param row: A row from the historical data containing price information.
        """
        price = row['Close']

        if signal == 'BUY' and self.balance > price:
            # Buy Ethereum
            eth_bought = self.balance / price  # Buy as much Ethereum as possible
            self.position += eth_bought
            self.balance = 0
            self.record_trade('BUY', eth_bought, price)

        elif signal == 'SELL' and self.position > 0:
            # Sell Ethereum
            self.balance += self.position * price
            eth_sold = self.position
            self.position = 0
            self.record_trade('SELL', eth_sold, price)

        # 'HOLD' does nothing

    def record_trade(self, action: str, amount: float, price: float):
        """
        Record trade details in the history.
        
        :param action: Trade action ('BUY' or 'SELL').
        :param amount: Amount of Ethereum bought or sold.
        :param price: Price at which the trade was executed.
        """
        self.history.append({
            'Action': action,
            'Amount': amount,
            'Price': price,
            'Balance': self.balance,
            'Position': self.position
        })

    def calculate_performance(self):
        """
        Calculate final performance metrics.
        
        :return: A dictionary with performance metrics.
        """
        final_balance = self.balance + (self.position * self.data.iloc[-1]['Close'])
        return {
            'Initial Balance': self.initial_balance,
            'Final Balance': final_balance,
            'Profit': final_balance - self.initial_balance
        }

    def plot_results(self):
        """
        Plot the trading results for visualization.
        """
        dates = self.data['Date']
        prices = self.data['Close']

        # Extract trade dates and prices
        trade_dates = [self.data.iloc[i]['Date'] for i in range(len(self.history))]
        trade_prices = [trade['Price'] for trade in self.history]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, prices, label='Ethereum Price', color='blue')
        plt.scatter(trade_dates, trade_prices, color='red', marker='o', label='Trades')
        plt.title('Backtesting Results')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

# Example strategy function: Moving Average Crossover
def moving_average_crossover_strategy(row, short_window=5, long_window=20):
    """
    A simple moving average crossover trading strategy.
    
    :param row: A row from the historical data.
    :param short_window: The short moving average window size.
    :param long_window: The long moving average window size.
    :return: 'BUY', 'SELL', or 'HOLD'.
    """
    short_ma = row['Short_MA']
    long_ma = row['Long_MA']

    if short_ma > long_ma:
        return 'BUY'
    elif short_ma < long_ma:
        return 'SELL'
    else:
        return 'HOLD'

# Load historical Ethereum data
def load_data(filepath: str) -> pd.DataFrame:
    """
    Load historical Ethereum data from a CSV file.
    
    :param filepath: Path to the CSV file.
    :return: A pandas DataFrame containing the historical data.
    """
    try:
        data = pd.read_csv(filepath)
        data['Short_MA'] = data['Close'].rolling(window=5).mean()  # Short moving average
        data['Long_MA'] = data['Close'].rolling(window=20).mean()  # Long moving average
        return data
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        exit(1)

# Usage example
if __name__ == "__main__":
    # Load data
    data = load_data("ethereum_data.csv")

    # Initialize the backtester
    backtester = Backtester(data)

    # Apply the strategy
    backtester.apply_strategy(moving_average_crossover_strategy)

    # Calculate performance
    performance = backtester.calculate_performance()
    print("Performance:", performance)

    # Plot results
    backtester.plot_results()
```
