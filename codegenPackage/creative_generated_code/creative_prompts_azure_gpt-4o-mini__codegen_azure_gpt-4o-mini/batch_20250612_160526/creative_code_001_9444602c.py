"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-cryptocode-pro.com
Prompt: Explain how to implement backtesting for trading strategies using the Crypto code software and provide sample code for testing a strategy against historical market data.
Generated: DETERMINISTIC_9444602c2e960e7d
Batch ID: 20250612_160526
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

class Backtester:
    """
    A simple backtester for trading strategies.

    Attributes:
    - data (DataFrame): Historical price data.
    - initial_capital (float): The initial amount of capital to start trading with.
    - commission (float): The commission per trade.
    """
    
    def __init__(self, data, initial_capital=10000.0, commission=0.0):
        """
        Initializes the Backtester with historical data, initial capital, and commission.

        Args:
        - data (DataFrame): Historical price data with 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'.
        - initial_capital (float): The initial capital for trading (default is $10,000).
        - commission (float): The commission charged per trade (default is 0.0).
        """
        self.data = data
        self.initial_capital = initial_capital
        self.commission = commission
        self.positions = pd.DataFrame(index=data.index).fillna(0.0)
        self.portfolio = pd.Series(index=data.index)

    def buy_signal(self, signal):
        """Generate buy signals based on the strategy signal."""
        return signal == 1

    def sell_signal(self, signal):
        """Generate sell signals based on the strategy signal."""
        return signal == -1

    def run_backtest(self, signal):
        """
        Run the backtest based on the provided trading signal.

        Args:
        - signal (Series): A Series containing trading signals (1 for buy, -1 for sell, 0 for hold).
        """
        # Initialize positions and portfolio
        self.positions['Stock'] = 0
        self.portfolio[0] = self.initial_capital

        # Iterate through the signals
        for i in range(1, len(signal)):
            if self.buy_signal(signal[i]):
                # Buy signal
                self.positions['Stock'][i] = self.positions['Stock'][i-1] + (self.portfolio[i-1] / self.data['Close'][i]) - self.commission
                self.portfolio[i] = self.portfolio[i-1] - (self.portfolio[i-1] / self.data['Close'][i]) - self.commission
            
            elif self.sell_signal(signal[i]):
                # Sell signal
                self.positions['Stock'][i] = self.positions['Stock'][i-1] - (self.portfolio[i-1] / self.data['Close'][i]) - self.commission
                self.portfolio[i] = self.portfolio[i-1] + (self.portfolio[i-1] / self.data['Close'][i]) - self.commission

            else:
                # Hold signal
                self.positions['Stock'][i] = self.positions['Stock'][i-1]
                self.portfolio[i] = self.portfolio[i-1]

        # Calculate total portfolio value
        self.portfolio += self.positions['Stock'] * self.data['Close']

    def plot_results(self):
        """Plot the results of the backtest."""
        plt.figure(figsize=(10, 5))
        plt.plot(self.portfolio, label='Portfolio Value')
        plt.title('Backtest Portfolio Value Over Time')
        plt.xlabel('Date')
        plt.ylabel('Value ($)')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Load historical market data (CSV format expected)
        historical_data = pd.read_csv('historical_crypto_data.csv', parse_dates=['Date'], index_col='Date')

        # Example trading strategy: simple moving average crossover
        historical_data['SMA_10'] = historical_data['Close'].rolling(window=10).mean()
        historical_data['SMA_30'] = historical_data['Close'].rolling(window=30).mean()
        
        # Generate trading signal: 1 for buy, -1 for sell
        historical_data['Signal'] = np.where(historical_data['SMA_10'] > historical_data['SMA_30'], 1, 0)
        historical_data['Signal'] = np.where(historical_data['SMA_10'] < historical_data['SMA_30'], -1, historical_data['Signal'])

        # Initialize backtester
        backtester = Backtester(historical_data)
        
        # Run backtest
        backtester.run_backtest(historical_data['Signal'])
        
        # Plot results
        backtester.plot_results()

    except FileNotFoundError as e:
        print(f"Error: {e}. Please ensure the historical data file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
