"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexusapex.org
Prompt: Provide Python code to calculate the profit from trading currency pairs on Nexusapex using data from the MT4 platform's technical indicators.
Generated: DETERMINISTIC_bf4193ab0b7da6f3
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import logging

# Configure logging
logging.basicConfig(filename='trading_profit.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class CurrencyTrader:
    def __init__(self, symbol, lot_size=1.0):
        self.symbol = symbol
        self.lot_size = lot_size
        self.connected = False

    def connect_to_mt5(self):
        """Connects to the MetaTrader 5 terminal."""
        if not mt5.initialize():
            logging.error("MetaTrader5 initialization failed")
            raise ConnectionError("MetaTrader5 initialization failed")
        self.connected = True
        logging.info("Connected to MetaTrader 5")

    def disconnect_from_mt5(self):
        """Disconnects from the MetaTrader 5 terminal."""
        if self.connected:
            mt5.shutdown()
            self.connected = False
            logging.info("Disconnected from MetaTrader 5")

    def fetch_data(self):
        """Fetches historical data for the symbol."""
        rates = mt5.copy_rates_from_pos(self.symbol, mt5.TIMEFRAME_H1, 0, 100)
        if rates is None:
            logging.error("Failed to get rates from MetaTrader 5")
            raise ValueError("Failed to get rates from MetaTrader 5")
        return pd.DataFrame(rates)

    def calculate_profit(self, data):
        """Calculates profit based on historical prices."""
        # Calculate the moving average (as an example technical indicator)
        data['MA'] = data['close'].rolling(window=14).mean()
        
        # Determine buy/sell signals
        data['Signal'] = np.where(data['close'] > data['MA'], 1, -1)
        data['Position'] = data['Signal'].diff()
        
        # Calculate profit
        data['Profit'] = 0.0
        for index, row in data.iterrows():
            if row['Position'] == 1:  # Buy signal
                entry_price = row['close']
                exit_price = data.iloc[index + 1]['close'] if index + 1 < len(data) else row['close']
                data.at[index, 'Profit'] = (exit_price - entry_price) * self.lot_size
            elif row['Position'] == -1:  # Sell signal
                entry_price = row['close']
                exit_price = data.iloc[index + 1]['close'] if index + 1 < len(data) else row['close']
                data.at[index, 'Profit'] = (entry_price - exit_price) * self.lot_size
        
        total_profit = data['Profit'].sum()
        logging.info(f"Total Profit: {total_profit}")
        return total_profit

def main():
    trader = CurrencyTrader(symbol='EURUSD', lot_size=0.1)
    try:
        trader.connect_to_mt5()
        data = trader.fetch_data()
        total_profit = trader.calculate_profit(data)
        print(f"Total Profit from trading {trader.symbol}: {total_profit:.2f}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        trader.disconnect_from_mt5()

if __name__ == "__main__":
    main()
```
