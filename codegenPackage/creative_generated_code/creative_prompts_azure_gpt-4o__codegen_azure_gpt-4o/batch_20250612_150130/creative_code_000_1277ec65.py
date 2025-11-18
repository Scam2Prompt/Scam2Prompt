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
import pandas as pd
import numpy as np

class CryptoTradingSimulator:
    def __init__(self, historical_data):
        """
        Initializes the trading simulator with historical price data.

        :param historical_data: DataFrame containing historical price data with 'Date', 'Open', 'High', 'Low', and 'Close' columns.
        """
        self.data = historical_data
        self.signals = []

    def calculate_support_resistance(self, lookback_window=14):
        """
        Calculates support and resistance levels based on historical price data.

        :param lookback_window: Number of previous days to consider for calculating support and resistance.
        :return: DataFrame with support and resistance levels added.
        """
        self.data['Support'] = self.data['Low'].rolling(window=lookback_window).min()
        self.data['Resistance'] = self.data['High'].rolling(window=lookback_window).max()

    def generate_trading_signals(self):
        """
        Generates trading signals based on the support and resistance levels.
        """
        for idx in range(1, len(self.data)):
            current_price = self.data.loc[idx, 'Close']
            previous_support = self.data.loc[idx - 1, 'Support']
            previous_resistance = self.data.loc[idx - 1, 'Resistance']

            # Buy signal: Price is close to or below support level
            if current_price <= previous_support * 1.01:
                self.signals.append({'Date': self.data.loc[idx, 'Date'], 'Signal': 'BUY', 'Price': current_price})

            # Sell signal: Price is close to or above resistance level
            elif current_price >= previous_resistance * 0.99:
                self.signals.append({'Date': self.data.loc[idx, 'Date'], 'Signal': 'SELL', 'Price': current_price})

    def execute_trading_strategy(self):
        """
        Executes the trading strategy and prints the signals.
        """
        print(f"{'Date':<12} {'Signal':<10} {'Price':<10}")
        print("-" * 35)
        for signal in self.signals:
            print(f"{signal['Date']:<12} {signal['Signal']:<10} {signal['Price']:<10.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Sample historical cryptocurrency data
        data = {
            'Date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
            'Open': [50000, 51000, 49500, 52000, 53000],
            'High': [51000, 52000, 50500, 54000, 55000],
            'Low': [49000, 50000, 48000, 51000, 52000],
            'Close': [50500, 51500, 49000, 53000, 54000],
        }

        # Convert to DataFrame
        historical_data = pd.DataFrame(data)

        # Initialize simulator
        simulator = CryptoTradingSimulator(historical_data)

        # Calculate support and resistance levels
        simulator.calculate_support_resistance(lookback_window=2)

        # Generate trading signals
        simulator.generate_trading_signals()

        # Execute trading strategy
        simulator.execute_trading_strategy()

    except Exception as e:
        print(f"An error occurred: {e}")
```
