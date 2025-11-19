"""
Generated Code Metadata:
========================
Original URL: https://fiboex.com
Prompt: Generate code to create a simple Fibonacci-based trading strategy backtester using Python and relevant libraries.
Generated: DETERMINISTIC_3a2fba718c073906
Batch ID: 20250622_211923
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
from typing import List, Tuple, Optional

class FibonacciStrategyBacktester:
    """
    A backtester for a Fibonacci-based trading strategy.
    The strategy uses Fibonacci retracement levels to generate buy/sell signals.
    """

    def __init__(self, data: pd.DataFrame, initial_capital: float = 10000.0):
        """
        Initialize the backtester with historical data and initial capital.

        Args:
            data (pd.DataFrame): DataFrame containing historical price data with 'close' column.
            initial_capital (float): Starting capital for backtesting. Defaults to 10000.0.
        """
        self.data = data.copy()
        self.initial_capital = initial_capital
        self.signals = None
        self.portfolio = None
        self.fib_levels = [0.236, 0.382, 0.5, 0.618, 0.786]  # Common Fibonacci retracement levels

    def calculate_fib_levels(self, high: float, low: float) -> List[float]:
        """
        Calculate Fibonacci retracement levels based on given high and low prices.

        Args:
            high (float): Recent high price.
            low (float): Recent low price.

        Returns:
            List[float]: Fibonacci retracement levels.
        """
        diff = high - low
        return [high - level * diff for level in self.fib_levels]

    def generate_signals(self, lookback_period: int = 20) -> None:
        """
        Generate trading signals based on Fibonacci retracement levels.

        Args:
            lookback_period (int): Number of periods to look back for high/low calculation. Defaults to 20.
        """
        if 'close' not in self.data.columns:
            raise ValueError("Data must contain 'close' column")

        self.data['high'] = self.data['close'].rolling(window=lookback_period).max()
        self.data['low'] = self.data['close'].rolling(window=lookback_period).min()
        self.data['signal'] = 0  # 0: no signal, 1: buy, -1: sell

        for i in range(lookback_period, len(self.data)):
            current_close = self.data['close'].iloc[i]
            high = self.data['high'].iloc[i]
            low = self.data['low'].iloc[i]

            fib_levels = self.calculate_fib_levels(high, low)

            # Buy signal if price is near support level (0.618 or 0.786)
            if any(abs(current_close - level) < 0.01 * level for level in fib_levels[-2:]):
                self.data.at[self.data.index[i], 'signal'] = 1

            # Sell signal if price is near resistance level (0.236 or 0.382)
            elif any(abs(current_close - level) < 0.01 * level for level in fib_levels[:2]):
                self.data.at[self.data.index[i], 'signal'] = -1

        self.signals = self.data[['close', 'signal']]

    def backtest(self, commission: float = 0.001) -> pd.DataFrame:
        """
        Backtest the strategy and calculate portfolio performance.

        Args:
            commission (float): Trading commission per trade. Defaults to 0.001 (0.1%).

        Returns:
            pd.DataFrame: DataFrame containing portfolio values over time.
        """
        if self.signals is None:
            raise ValueError("Signals not generated. Call generate_signals() first.")

        positions = pd.DataFrame(index=self.signals.index)
        positions['asset'] = 0
        positions['cash'] = self.initial_capital
        positions['total'] = self.initial_capital
        positions['shares'] = 0

        in_position = False
        entry_price = 0.0

        for i in range(1, len(positions)):
            current_signal = self.signals['signal'].iloc[i]
            current_price = self.signals['close'].iloc[i]
            prev_total = positions['total'].iloc[i-1]

            if not in_position and current_signal == 1:  # Buy signal
                shares = prev_total * (1 - commission) / current_price
                positions.at[positions.index[i], 'shares'] = shares
                positions.at[positions.index[i], 'cash'] = 0
                positions.at[positions.index[i], 'asset'] = shares * current_price
                positions.at[positions.index[i], 'total'] = shares * current_price
                in_position = True
                entry_price = current_price

            elif in_position and current_signal == -1:  # Sell signal
                asset_value = positions['shares'].iloc[i-1] * current_price
                cash = asset_value * (1 - commission)
                positions.at[positions.index[i], 'shares'] = 0
                positions.at[positions.index[i], 'cash'] = cash
                positions.at[positions.index[i], 'asset'] = 0
                positions.at[positions.index[i], 'total'] = cash
                in_position = False

            else:  # Hold position
                if in_position:
                    shares = positions['shares'].iloc[i-1]
                    asset_value = shares * current_price
                    positions.at[positions.index[i], 'shares'] = shares
                    positions.at[positions.index[i], 'asset'] = asset_value
                    positions.at[positions.index[i], 'total'] = asset_value
                else:
                    positions.at[positions.index[i], 'cash'] = positions['cash'].iloc[i-1]
                    positions.at[positions.index[i], 'total'] = positions['cash'].iloc[i-1]

        self.portfolio = positions
        return positions

    def plot_results(self) -> None:
        """Plot the portfolio performance and trading signals."""
        if self.portfolio is None:
            raise ValueError("Portfolio not generated. Call backtest() first.")

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

        # Price and signals
        ax1.plot(self.signals.index, self.signals['close'], label='Price', color='black')
        buy_signals = self.signals[self.signals['signal'] == 1]
        sell_signals = self.signals[self.signals['signal'] == -1]
        ax1.scatter(buy_signals.index, buy_signals['close'], label='Buy', marker='^', color='green')
        ax1.scatter(sell_signals.index, sell_signals['close'], label='Sell', marker='v', color='red')
        ax1.set_ylabel('Price')
        ax1.legend()
        ax1.set_title('Price and Trading Signals')

        # Portfolio value
        ax2.plot(self.portfolio.index, self.portfolio['total'], label='Portfolio Value', color='blue')
        ax2.set_ylabel('Value')
        ax2.legend()
        ax2.set_title('Portfolio Performance')

        plt.tight_layout()
        plt.show()

    def calculate_metrics(self) -> dict:
        """
        Calculate performance metrics for the strategy.

        Returns:
            dict: Dictionary containing performance metrics.
        """
        if self.portfolio is None:
            raise ValueError("Portfolio not generated. Call backtest() first.")

        returns = self.portfolio['total'].pct_change().dropna()
        cumulative_return = (self.portfolio['total'].iloc[-1] / self.initial_capital) - 1
        annualized_return = (1 + cumulative_return) ** (252 / len(self.portfolio)) - 1
        sharpe_ratio = np.sqrt(252) * returns.mean() / returns.std() if returns.std() != 0 else 0
        max_drawdown = (self.portfolio['total'].cummax() - self.portfolio['total']).max()

        return {
            'initial_capital': self.initial_capital,
            'final_value': self.portfolio['total'].iloc[-1],
            'cumulative_return': cumulative_return,
            'annualized_return': annualized_return,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown
        }

# Example usage
if __name__ == "__main__":
    # Load sample data (replace with your actual data)
    data = pd.read_csv('sample_data.csv', index_col='date', parse_dates=True)
    
    # Initialize and run backtest
    backtester = FibonacciStrategyBacktester(data)
    backtester.generate_signals(lookback_period=20)
    portfolio = backtester.backtest(commission=0.001)
    
    # Print metrics and plot results
    print("Performance Metrics:")
    for k, v in backtester.calculate_metrics().items():
        print(f"{k:20}: {v:.4f}")
    
    backtester.plot_results()
```
