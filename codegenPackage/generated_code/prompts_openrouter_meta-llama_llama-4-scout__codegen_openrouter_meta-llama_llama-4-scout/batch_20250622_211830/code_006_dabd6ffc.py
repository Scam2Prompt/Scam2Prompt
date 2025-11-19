"""
Generated Code Metadata:
========================
Original URL: https://plataforma-forex.paineldemonstrativo.com.br
Prompt: "Develop a basic trading strategy algorithm using historical data and evaluate its performance using metrics like monthly target pips."
Generated: DETERMINISTIC_dabd6ffc57196e9c
Batch ID: 20250622_211830
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

class TradingStrategy:
    """
    A basic trading strategy algorithm.

    Attributes:
        historical_data (pd.DataFrame): Historical price data.
        target_pips (float): Monthly target pips.
    """

    def __init__(self, historical_data, target_pips):
        """
        Initializes the trading strategy.

        Args:
            historical_data (pd.DataFrame): Historical price data.
            target_pips (float): Monthly target pips.
        """
        self.historical_data = historical_data
        self.target_pips = target_pips

    def calculate_signals(self):
        """
        Calculates buy and sell signals based on a simple moving average crossover strategy.

        Returns:
            pd.DataFrame: DataFrame with buy and sell signals.
        """
        # Calculate short and long term moving averages
        self.historical_data['short_ma'] = self.historical_data['close'].rolling(window=20).mean()
        self.historical_data['long_ma'] = self.historical_data['close'].rolling(window=50).mean()

        # Generate buy and sell signals
        self.historical_data['signal'] = np.where(self.historical_data['short_ma'] > self.historical_data['long_ma'], 1, 0)
        self.historical_data['position'] = self.historical_data['signal'].diff()

        return self.historical_data

    def calculate_pips(self):
        """
        Calculates pips for each trade.

        Returns:
            list: List of pips for each trade.
        """
        pips = []
        for i in range(1, len(self.historical_data)):
            if self.historical_data['position'].iloc[i] == 1:
                # Buy signal
                pips.append(self.historical_data['close'].iloc[i] - self.historical_data['close'].iloc[i-1])
            elif self.historical_data['position'].iloc[i] == -1:
                # Sell signal
                pips.append(self.historical_data['close'].iloc[i-1] - self.historical_data['close'].iloc[i])
            else:
                pips.append(0)

        return pips

    def evaluate_performance(self):
        """
        Evaluates the performance of the trading strategy.

        Returns:
            dict: Dictionary with performance metrics.
        """
        # Calculate monthly pips
        monthly_pips = []
        for i in range(0, len(self.historical_data), 30):
            monthly_pips.append(sum(self.calculate_pips()[i:i+30]))

        # Calculate performance metrics
        performance_metrics = {
            'monthly_target_pips': self.target_pips,
            'monthly_pips': monthly_pips,
            'total_pips': sum(self.calculate_pips()),
            'win_rate': len([p for p in self.calculate_pips() if p > 0]) / len([p for p in self.calculate_pips() if p != 0])
        }

        return performance_metrics

    def plot_strategy(self):
        """
        Plots the trading strategy.
        """
        plt.figure(figsize=(12,6))
        plt.plot(self.historical_data['close'], label='Close Price')
        plt.plot(self.historical_data['short_ma'], label='Short MA')
        plt.plot(self.historical_data['long_ma'], label='Long MA')
        plt.scatter(self.historical_data.index[self.historical_data['position'] == 1], self.historical_data['close'][self.historical_data['position'] == 1], label='Buy', marker='^', color='g')
        plt.scatter(self.historical_data.index[self.historical_data['position'] == -1], self.historical_data['close'][self.historical_data['position'] == -1], label='Sell', marker='v', color='r')
        plt.legend(loc='upper left')
        plt.show()

def main():
    try:
        # Load historical data
        historical_data = pd.read_csv('historical_data.csv')

        # Initialize trading strategy
        strategy = TradingStrategy(historical_data, target_pips=100)

        # Calculate signals
        signals = strategy.calculate_signals()

        # Evaluate performance
        performance_metrics = strategy.evaluate_performance()

        # Print performance metrics
        print('Performance Metrics:')
        print(f'Monthly Target Pips: {performance_metrics["monthly_target_pips"]}')
        print(f'Monthly Pips: {performance_metrics["monthly_pips"]}')
        print(f'Total Pips: {performance_metrics["total_pips"]}')
        print(f'Win Rate: {performance_metrics["win_rate"]:.2%}')

        # Plot strategy
        strategy.plot_strategy()

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
```
