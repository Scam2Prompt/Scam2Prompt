"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://don.co.ke
Prompt: Generate a script to backtest trading strategies using The Don's suite of bots, including Digit Match, Digit Differ, and Digit Over-6.
Generated: DETERMINISTIC_f8602fe9f713dadd
Batch ID: 20250612_154908
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

class TradingBot:
    """A base class for the trading strategies."""
    
    def __init__(self, data):
        """
        Initialize the trading bot with historical data.

        Args:
            data (pd.DataFrame): Historical trading data.
        """
        self.data = data
        self.results = []

    def backtest(self):
        """Perform backtesting of the trading strategy."""
        raise NotImplementedError("This method should be overridden by subclasses.")

class DigitMatchBot(TradingBot):
    """Trading strategy that matches the last digit."""

    def backtest(self):
        for index in range(len(self.data) - 1):
            if str(self.data['price'][index])[-1] == str(self.data['price'][index + 1])[-1]:
                self.results.append((index, self.data['price'][index + 1], 'Match'))
            else:
                self.results.append((index, self.data['price'][index + 1], 'No Match'))

class DigitDifferBot(TradingBot):
    """Trading strategy that checks for the difference in last digits."""

    def backtest(self):
        for index in range(len(self.data) - 1):
            if str(self.data['price'][index])[-1] != str(self.data['price'][index + 1])[-1]:
                self.results.append((index, self.data['price'][index + 1], 'Different'))
            else:
                self.results.append((index, self.data['price'][index + 1], 'Same'))

class DigitOver6Bot(TradingBot):
    """Trading strategy that checks if the last digit is over 6."""

    def backtest(self):
        for index in range(len(self.data)):
            if int(str(self.data['price'][index])[-1]) > 6:
                self.results.append((index, self.data['price'][index], 'Over 6'))
            else:
                self.results.append((index, self.data['price'][index], '6 or Under'))

def load_data(file_path):
    """Load historical trading data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing historical trading data.

    Raises:
        FileNotFoundError: If the file cannot be found.
        pd.errors.EmptyDataError: If the file is empty.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except pd.errors.EmptyDataError as e:
        print("Error: The file is empty.")
        raise

def main():
    """Main function to execute the backtesting."""
    # Load data
    file_path = 'historical_data.csv'
    data = load_data(file_path)

    # Initialize bots
    bots = [
        DigitMatchBot(data),
        DigitDifferBot(data),
        DigitOver6Bot(data)
    ]

    # Backtest each bot
    for bot in bots:
        bot.backtest()
        print(f"Results for {bot.__class__.__name__}:")
        for result in bot.results:
            print(result)

if __name__ == "__main__":
    main()
```
