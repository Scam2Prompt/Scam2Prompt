"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintrends.org
Prompt: Generate a Python script that implements a trading strategy based on the "3 high-probability trading setups" discussed in the FinTrends trading courses.
Generated: DETERMINISTIC_fcfba088e0581969
Batch ID: 20250612_164104
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
import datetime as dt
import logging

# Setup logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("trading_strategy.log"), logging.StreamHandler()]
)

class TradingStrategy:
    """
    A class implementing a trading strategy based on "3 high-probability trading setups."
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the TradingStrategy instance.

        Args:
            data (pd.DataFrame): Historical price data containing 'Date', 'Open', 'High', 'Low', 'Close', and 'Volume'.
        """
        self.data = data
        self.signals = pd.DataFrame(index=data.index)

    def calculate_indicators(self):
        """
        Calculate technical indicators used in the strategy.
        """
        try:
            # Calculate Moving Averages (Simple Moving Average - SMA)
            self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()
            self.data['SMA_200'] = self.data['Close'].rolling(window=200).mean()

            # Calculate Relative Strength Index (RSI)
            delta = self.data['Close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            self.data['RSI'] = 100 - (100 / (1 + rs))

            # Calculate Bollinger Bands
            self.data['BB_Middle'] = self.data['Close'].rolling(window=20).mean()
            self.data['BB_Upper'] = self.data['BB_Middle'] + 2 * self.data['Close'].rolling(window=20).std()
            self.data['BB_Lower'] = self.data['BB_Middle'] - 2 * self.data['Close'].rolling(window=20).std()

        except Exception as e:
            logging.error(f"Error calculating indicators: {e}")

    def generate_signals(self):
        """
        Generate trading signals based on the strategy.
        """
        try:
            # Setup #1: SMA crossover
            self.signals['Buy_SMA_Crossover'] = (
                (self.data['SMA_50'] > self.data['SMA_200']) & 
                (self.data['SMA_50'].shift(1) <= self.data['SMA_200'].shift(1))
            )
            self.signals['Sell_SMA_Crossover'] = (
                (self.data['SMA_50'] < self.data['SMA_200']) & 
                (self.data['SMA_50'].shift(1) >= self.data['SMA_200'].shift(1))
            )

            # Setup #2: RSI oversold/overbought conditions
            self.signals['Buy_RSI'] = self.data['RSI'] < 30
            self.signals['Sell_RSI'] = self.data['RSI'] > 70

            # Setup #3: Bollinger Bands breakout
            self.signals['Buy_BB_Breakout'] = self.data['Close'] < self.data['BB_Lower']
            self.signals['Sell_BB_Breakout'] = self.data['Close'] > self.data['BB_Upper']

            # Combine signals into a final decision
            self.signals['Final_Buy'] = self.signals[['Buy_SMA_Crossover', 'Buy_RSI', 'Buy_BB_Breakout']].any(axis=1)
            self.signals['Final_Sell'] = self.signals[['Sell_SMA_Crossover', 'Sell_RSI', 'Sell_BB_Breakout']].any(axis=1)

        except Exception as e:
            logging.error(f"Error generating signals: {e}")

    def backtest_strategy(self, initial_balance=10000):
        """
        Backtest the trading strategy.

        Args:
            initial_balance (float): Starting balance for the backtest.

        Returns:
            pd.DataFrame: Results of the backtest including balance over time.
        """
        try:
            balance = initial_balance
            position = 0  # Number of shares held
            self.data['Balance'] = balance

            for i in range(len(self.data)):
                # Get Buy/Sell signals for the current day
                if self.signals['Final_Buy'].iloc[i]:
                    # Buy logic: Assume we buy with the full balance
                    position = balance / self.data['Close'].iloc[i]
                    balance = 0

                elif self.signals['Final_Sell'].iloc[i] and position > 0:
                    # Sell logic: Assume we sell all held positions
                    balance = position * self.data['Close'].iloc[i]
                    position = 0

                # Update balance column
                self.data.at[self.data.index[i], 'Balance'] = balance + (position * self.data['Close'].iloc[i])

            return self.data[['Date', 'Balance']]

        except Exception as e:
            logging.error(f"Error during backtest: {e}")
            return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    try:
        # Load historical price data
        data = pd.read_csv("historical_data.csv", parse_dates=['Date'])
        data.set_index('Date', inplace=True)

        # Initialize and run strategy
        strategy = TradingStrategy(data)
        strategy.calculate_indicators()
        strategy.generate_signals()
        backtest_results = strategy.backtest_strategy()

        # Save backtest results
        backtest_results.to_csv("backtest_results.csv", index=False)
        logging.info("Backtest completed successfully. Results saved to 'backtest_results.csv'.")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except Exception as e:
        logging.error(f"Unhandled exception occurred: {e}")
```
