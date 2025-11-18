"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bit-gpt-urex.com
Prompt: Write a Python script to simulate trading decisions based on historical price trends, technical indicators, and market conditions, as performed by the Bit GPT Urex app.
Generated: DETERMINISTIC_6badab56ec12a360
Batch ID: 20250612_150843
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
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingSimulator:
    """
    A class to simulate trading decisions based on historical price trends,
    technical indicators, and market conditions.
    """

    def __init__(self, historical_data):
        """
        Initializes the TradingSimulator with historical price data.

        :param historical_data: A pandas DataFrame with columns ['date', 'price'] containing historical price data.
        """
        self.data = historical_data
        self.data['SMA_20'] = None  # Simple Moving Average (20 days)
        self.data['SMA_50'] = None  # Simple Moving Average (50 days)
        self.data['RSI'] = None     # Relative Strength Index
        self.decisions = []

    def calculate_sma(self, window):
        """
        Calculate the Simple Moving Average (SMA) for the given window size.

        :param window: The number of days for the SMA calculation.
        :return: A pandas Series containing the SMA values.
        """
        return self.data['price'].rolling(window=window).mean()

    def calculate_rsi(self, window=14):
        """
        Calculate the Relative Strength Index (RSI).

        :param window: The number of days to consider for RSI calculation.
        :return: A pandas Series containing the RSI values.
        """
        delta = self.data['price'].diff()
        gain = np.maximum(delta, 0)
        loss = -np.minimum(delta, 0)

        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def evaluate_market_conditions(self):
        """
        Evaluate market conditions and make trading decisions based on SMA and RSI values.
        """
        for i in range(len(self.data)):
            # Skip rows without sufficient data for SMA and RSI calculations
            if pd.isna(self.data.loc[i, 'SMA_20']) or pd.isna(self.data.loc[i, 'SMA_50']) or pd.isna(self.data.loc[i, 'RSI']):
                self.decisions.append(None)
                continue

            # Trading logic
            if self.data.loc[i, 'SMA_20'] > self.data.loc[i, 'SMA_50'] and self.data.loc[i, 'RSI'] < 30:
                self.decisions.append("BUY")
            elif self.data.loc[i, 'SMA_20'] < self.data.loc[i, 'SMA_50'] and self.data.loc[i, 'RSI'] > 70:
                self.decisions.append("SELL")
            else:
                self.decisions.append("HOLD")

        self.data['decision'] = self.decisions

    def simulate_trading(self):
        """
        Simulates trading decisions based on historical data.

        :return: A pandas DataFrame with trading decisions appended.
        """
        try:
            # Calculate technical indicators
            self.data['SMA_20'] = self.calculate_sma(20)
            self.data['SMA_50'] = self.calculate_sma(50)
            self.data['RSI'] = self.calculate_rsi()

            # Evaluate market conditions and make decisions
            self.evaluate_market_conditions()

            logging.info("Trading simulation completed successfully.")
            return self.data
        except Exception as e:
            logging.error(f"Error during trading simulation: {str(e)}")
            raise

# Example usage:
if __name__ == "__main__":
    # Mock historical data for demonstration purposes
    historical_data = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'price': np.random.uniform(100, 200, 100)  # Random price data for simulation
    })

    simulator = TradingSimulator(historical_data)
    result = simulator.simulate_trading()

    # Display the result
    print(result[['date', 'price', 'SMA_20', 'SMA_50', 'RSI', 'decision']])
```
