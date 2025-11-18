"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoin360-ai.com
Prompt: Develop a Python program to simulate cryptocurrency trading using backtesting with historical market data, similar to the features of Bitcoin 360 AI Elite.
Generated: DETERMINISTIC_8644a10034a755f2
Batch ID: 20250612_150048
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

class CryptoTrader:
    """
    A class to simulate cryptocurrency trading using backtesting on historical data.
    """

    def __init__(self, initial_balance=10000, transaction_fee=0.001):
        """
        Initialize the trader with a specified initial balance and transaction fee.
        
        :param initial_balance: Starting amount of capital for trading.
        :param transaction_fee: Fee charged for each transaction.
        """
        self.balance = initial_balance
        self.transaction_fee = transaction_fee
        self.position = 0  # Current holding in cryptocurrency
        self.trade_history = []  # To store trade information

    def buy(self, price, amount):
        """
        Execute a buy order.
        
        :param price: Current market price of the cryptocurrency.
        :param amount: Amount of cryptocurrency to buy.
        """
        total_cost = price * amount * (1 + self.transaction_fee)
        if total_cost <= self.balance:
            self.balance -= total_cost
            self.position += amount
            self.trade_history.append(('BUY', amount, price))
        else:
            print("Insufficient balance to buy.")

    def sell(self, price, amount):
        """
        Execute a sell order.
        
        :param price: Current market price of the cryptocurrency.
        :param amount: Amount of cryptocurrency to sell.
        """
        if amount <= self.position:
            total_revenue = price * amount * (1 - self.transaction_fee)
            self.balance += total_revenue
            self.position -= amount
            self.trade_history.append(('SELL', amount, price))
        else:
            print("Insufficient position to sell.")

    def get_portfolio_value(self, current_price):
        """
        Calculate the total value of the portfolio based on current market price.
        
        :param current_price: Current market price of the cryptocurrency.
        :return: Total value of the portfolio.
        """
        return self.balance + (self.position * current_price)

def backtest_trader(data, trader):
    """
    Backtest the trader using historical market data.
    
    :param data: Historical price data as a DataFrame.
    :param trader: Instance of the CryptoTrader class.
    """
    for index, row in data.iterrows():
        price = row['Close']
        # Simple strategy: Buy if price is lower than the previous day's price, sell if higher
        if index > 0:
            prev_price = data.iloc[index - 1]['Close']
            if price < prev_price:
                trader.buy(price, trader.balance / price)  # Use all remaining balance
            elif price > prev_price and trader.position > 0:
                trader.sell(price, trader.position)  # Sell all holdings

def plot_results(data, trader):
    """
    Plot the results of the backtest, showing the portfolio value over time.
    
    :param data: Historical price data as a DataFrame.
    :param trader: Instance of the CryptoTrader class.
    """
    portfolio_values = []
    for index, row in data.iterrows():
        price = row['Close']
        portfolio_value = trader.get_portfolio_value(price)
        portfolio_values.append(portfolio_value)

    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], portfolio_values, label='Portfolio Value', color='blue')
    plt.title('Portfolio Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value ($)')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    """
    Main function to run the backtest simulation.
    """
    try:
        # Load historical market data (CSV file should have columns: Date, Close)
        data = pd.read_csv('historical_data.csv', parse_dates=['Date'])
        data.sort_values('Date', inplace=True)

        # Initialize the trader
        trader = CryptoTrader(initial_balance=10000)

        # Run backtest
        backtest_trader(data, trader)

        # Plot results
        plot_results(data, trader)

    except FileNotFoundError:
        print("Error: The data file was not found. Please ensure the file path is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
