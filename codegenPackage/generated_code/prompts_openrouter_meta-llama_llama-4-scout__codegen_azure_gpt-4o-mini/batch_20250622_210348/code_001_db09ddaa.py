"""
Generated Code Metadata:
========================
Original URL: https://token-altsignal.web.app
Prompt: "Compare the performance of AltSignals' trade signals for Forex and cryptocurrency trading, focusing on win rates and profit percentages."
Generated: DETERMINISTIC_db09ddaae1b029b7
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TradeSignalAnalyzer:
    """
    A class to analyze trade signals for Forex and cryptocurrency trading.
    It calculates win rates and profit percentages based on provided trade data.
    """

    def __init__(self, forex_data: pd.DataFrame, crypto_data: pd.DataFrame):
        """
        Initializes the TradeSignalAnalyzer with Forex and cryptocurrency trade data.

        :param forex_data: DataFrame containing Forex trade signals with 'profit' and 'result' columns.
        :param crypto_data: DataFrame containing cryptocurrency trade signals with 'profit' and 'result' columns.
        """
        self.forex_data = forex_data
        self.crypto_data = crypto_data

    def calculate_win_rate(self, data: pd.DataFrame) -> float:
        """
        Calculates the win rate of trades.

        :param data: DataFrame containing trade results.
        :return: Win rate as a percentage.
        """
        if data.empty:
            raise ValueError("Trade data is empty.")
        
        wins = data[data['result'] == 'win'].shape[0]
        total_trades = data.shape[0]
        win_rate = (wins / total_trades) * 100 if total_trades > 0 else 0
        return win_rate

    def calculate_profit_percentage(self, data: pd.DataFrame) -> float:
        """
        Calculates the profit percentage of trades.

        :param data: DataFrame containing trade profits.
        :return: Profit percentage.
        """
        if data.empty:
            raise ValueError("Trade data is empty.")
        
        total_profit = data['profit'].sum()
        total_trades = data.shape[0]
        profit_percentage = (total_profit / total_trades) if total_trades > 0 else 0
        return profit_percentage

    def analyze(self):
        """
        Analyzes the Forex and cryptocurrency trade signals and prints the results.
        """
        try:
            forex_win_rate = self.calculate_win_rate(self.forex_data)
            forex_profit_percentage = self.calculate_profit_percentage(self.forex_data)

            crypto_win_rate = self.calculate_win_rate(self.crypto_data)
            crypto_profit_percentage = self.calculate_profit_percentage(self.crypto_data)

            print(f"Forex Win Rate: {forex_win_rate:.2f}%")
            print(f"Forex Profit Percentage: {forex_profit_percentage:.2f}")

            print(f"Crypto Win Rate: {crypto_win_rate:.2f}%")
            print(f"Crypto Profit Percentage: {crypto_profit_percentage:.2f}")

            self.plot_results(forex_win_rate, forex_profit_percentage, crypto_win_rate, crypto_profit_percentage)

        except ValueError as e:
            print(f"Error: {e}")

    def plot_results(self, forex_win_rate, forex_profit_percentage, crypto_win_rate, crypto_profit_percentage):
        """
        Plots the win rates and profit percentages for Forex and cryptocurrency.

        :param forex_win_rate: Win rate for Forex.
        :param forex_profit_percentage: Profit percentage for Forex.
        :param crypto_win_rate: Win rate for cryptocurrency.
        :param crypto_profit_percentage: Profit percentage for cryptocurrency.
        """
        categories = ['Forex Win Rate', 'Forex Profit %', 'Crypto Win Rate', 'Crypto Profit %']
        values = [forex_win_rate, forex_profit_percentage, crypto_win_rate, crypto_profit_percentage]

        plt.figure(figsize=(10, 6))
        plt.bar(categories, values, color=['blue', 'green', 'orange', 'red'])
        plt.title('Trade Signal Performance Comparison')
        plt.ylabel('Percentage')
        plt.ylim(0, 100)
        plt.axhline(0, color='black', linewidth=0.8)
        plt.grid(axis='y')
        plt.show()

# Example usage:
# forex_data = pd.DataFrame({'profit': [10, -5, 15, 0], 'result': ['win', 'loss', 'win', 'draw']})
# crypto_data = pd.DataFrame({'profit': [20, -10, 30, 5], 'result': ['win', 'loss', 'win', 'win']})
# analyzer = TradeSignalAnalyzer(forex_data, crypto_data)
# analyzer.analyze()
```
