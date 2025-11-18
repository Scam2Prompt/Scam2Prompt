"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomaniaapp.com
Prompt: Write Python code to simulate cryptocurrency trading decisions using mathematical indicators like support and resistance levels, as described in the Crypto Mania platform.
Generated: DETERMINISTIC_1277ec65367dfb23
Batch ID: 20250612_150130
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

class CryptoTrader:
    def __init__(self, data):
        """
        Initializes the CryptoTrader with price data.

        :param data: A pandas DataFrame containing cryptocurrency price data with a 'Close' column.
        """
        self.data = data
        self.support_levels = []
        self.resistance_levels = []
        self.signals = []

    def calculate_support_resistance(self, window=14):
        """
        Calculate support and resistance levels using rolling minima and maxima.

        :param window: The period for calculating support and resistance.
        """
        self.data['Support'] = self.data['Close'].rolling(window=window).min()
        self.data['Resistance'] = self.data['Close'].rolling(window=window).max()
        self.support_levels = self.data['Support'].dropna().tolist()
        self.resistance_levels = self.data['Resistance'].dropna().tolist()

    def generate_signals(self):
        """
        Generate trading signals based on support and resistance levels.
        A buy signal is generated when the price crosses above the resistance level,
        and a sell signal is generated when the price crosses below the support level.
        """
        self.signals = []

        for i in range(len(self.data)):
            if i == 0:
                continue
            
            if self.data['Close'][i] > self.data['Resistance'][i - 1]:
                self.signals.append('Buy')
            elif self.data['Close'][i] < self.data['Support'][i - 1]:
                self.signals.append('Sell')
            else:
                self.signals.append('Hold')

        self.data['Signals'] = ['None'] + self.signals  # First entry has no signal

    def plot_signals(self):
        """
        Plots the closing prices, support, resistance levels, and trading signals.
        """
        plt.figure(figsize=(14, 7))

        plt.plot(self.data['Close'], label='Close Price', color='blue', alpha=0.5)
        plt.plot(self.data['Support'], label='Support Level', color='green', linestyle='--')
        plt.plot(self.data['Resistance'], label='Resistance Level', color='red', linestyle='--')

        # Mark buy/sell signals
        buy_signals = self.data[self.data['Signals'] == 'Buy']
        sell_signals = self.data[self.data['Signals'] == 'Sell']

        plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', label='Buy Signal', s=100)
        plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', label='Sell Signal', s=100)

        plt.title('Cryptocurrency Trading Signals')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to execute the trading simulation.
    """
    # Load sample cryptocurrency data (ensure this CSV file exists)
    try:
        data = pd.read_csv('cryptocurrency_data.csv', parse_dates=True, index_col='Date')
        trader = CryptoTrader(data)

        # Calculate support and resistance levels
        trader.calculate_support_resistance(window=14)

        # Generate trading signals
        trader.generate_signals()

        # Plot the signals
        trader.plot_signals()

    except FileNotFoundError as e:
        print(f"Error: The specified data file was not found. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
