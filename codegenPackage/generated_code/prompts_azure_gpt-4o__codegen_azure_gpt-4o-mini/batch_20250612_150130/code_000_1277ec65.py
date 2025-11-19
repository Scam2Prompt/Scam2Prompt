"""
Generated Code Metadata:
========================
Original URL: https://cryptomaniaapp.com
Prompt: Write Python code to simulate cryptocurrency trading decisions using mathematical indicators like support and resistance levels, as described in the Crypto Mania platform.
Generated: DETERMINISTIC_1277ec65367dfb23
Batch ID: 20250612_150130
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
import matplotlib.pyplot as plt

class CryptoTrader:
    def __init__(self, data):
        """
        Initialize the CryptoTrader with historical price data.

        :param data: A pandas DataFrame containing historical price data with a 'Close' column.
        """
        if 'Close' not in data.columns:
            raise ValueError("Data must contain a 'Close' column.")
        self.data = data
        self.support_levels = []
        self.resistance_levels = []

    def calculate_support_resistance(self, window=14):
        """
        Calculate support and resistance levels using rolling minimum and maximum.

        :param window: The number of periods to use for calculating support and resistance.
        """
        self.data['Support'] = self.data['Close'].rolling(window=window).min()
        self.data['Resistance'] = self.data['Close'].rolling(window=window).max()
        self.support_levels = self.data['Support'].dropna().tolist()
        self.resistance_levels = self.data['Resistance'].dropna().tolist()

    def generate_signals(self):
        """
        Generate buy/sell signals based on support and resistance levels.
        
        :return: A DataFrame with buy/sell signals.
        """
        signals = []
        for index, row in self.data.iterrows():
            if row['Close'] < row['Support']:
                signals.append('Buy')
            elif row['Close'] > row['Resistance']:
                signals.append('Sell')
            else:
                signals.append('Hold')
        self.data['Signal'] = signals
        return self.data[['Close', 'Support', 'Resistance', 'Signal']]

    def plot_signals(self):
        """
        Plot the closing prices along with support, resistance levels, and trading signals.
        """
        plt.figure(figsize=(14, 7))
        plt.plot(self.data['Close'], label='Close Price', color='blue', alpha=0.5)
        plt.plot(self.data['Support'], label='Support Level', color='green', linestyle='--')
        plt.plot(self.data['Resistance'], label='Resistance Level', color='red', linestyle='--')
        
        buy_signals = self.data[self.data['Signal'] == 'Buy']
        sell_signals = self.data[self.data['Signal'] == 'Sell']
        
        plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', label='Buy Signal', alpha=1)
        plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', label='Sell Signal', alpha=1)
        
        plt.title('Cryptocurrency Trading Signals')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Load historical price data (ensure you have a 'Close' column)
    try:
        # Replace 'your_data.csv' with your actual data file
        data = pd.read_csv('your_data.csv', parse_dates=True, index_col='Date')
        trader = CryptoTrader(data)
        trader.calculate_support_resistance(window=14)
        signals = trader.generate_signals()
        print(signals)
        trader.plot_signals()
    except Exception as e:
        print(f"An error occurred: {e}")
```
