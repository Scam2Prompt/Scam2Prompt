"""
Generated Code Metadata:
========================
Original URL: https://bakedbeans.io
Prompt: Write a code snippet to backtest a Forex trading strategy using historical data and performance metrics such as Sharpe ratio and drawdown.
Generated: DETERMINISTIC_dfa51372904ff6dd
Batch ID: 20250622_205436
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

# Function to calculate Sharpe Ratio
def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
    """
    Calculate the Sharpe Ratio for a series of returns.
    :param returns: Series of returns
    :param risk_free_rate: Risk-free rate (default is 0.0)
    :return: Sharpe Ratio
    """
    excess_returns = returns - risk_free_rate
    return excess_returns.mean() / excess_returns.std()

# Function to calculate maximum drawdown
def calculate_drawdown(equity_curve):
    """
    Calculate the maximum drawdown for an equity curve.
    :param equity_curve: Series of equity values
    :return: Maximum drawdown
    """
    running_max = equity_curve.cummax()
    drawdown = equity_curve / running_max - 1
    return drawdown.min()

# Backtesting function
def backtest_strategy(data, strategy_function, initial_balance=10000):
    """
    Backtest a trading strategy using historical data.
    :param data: DataFrame containing historical data (must include 'Close' prices)
    :param strategy_function: Function implementing the trading strategy
    :param initial_balance: Starting balance for the backtest
    :return: Dictionary containing performance metrics
    """
    try:
        # Ensure required columns exist
        if 'Close' not in data.columns:
            raise ValueError("Data must include a 'Close' column for price information.")

        # Apply the strategy to generate signals
        data['Signal'] = strategy_function(data)

        # Calculate daily returns based on signals
        data['Return'] = data['Signal'].shift(1) * data['Close'].pct_change()

        # Calculate equity curve
        data['Equity'] = (1 + data['Return']).cumprod() * initial_balance

        # Calculate performance metrics
        sharpe_ratio = calculate_sharpe_ratio(data['Return'].dropna())
        max_drawdown = calculate_drawdown(data['Equity'])

        return {
            "Final Balance": data['Equity'].iloc[-1],
            "Sharpe Ratio": sharpe_ratio,
            "Max Drawdown": max_drawdown,
            "Equity Curve": data['Equity']
        }
    except Exception as e:
        print(f"Error during backtest: {e}")
        return None

# Example strategy: Simple Moving Average Crossover
def sma_crossover_strategy(data, short_window=10, long_window=50):
    """
    Simple Moving Average Crossover Strategy.
    :param data: DataFrame containing historical data
    :param short_window: Window for short-term SMA
    :param long_window: Window for long-term SMA
    :return: Series of trading signals (1 for buy, -1 for sell, 0 for hold)
    """
    try:
        data['SMA_Short'] = data['Close'].rolling(window=short_window).mean()
        data['SMA_Long'] = data['Close'].rolling(window=long_window).mean()

        # Generate signals
        signals = np.where(data['SMA_Short'] > data['SMA_Long'], 1, -1)
        return pd.Series(signals, index=data.index)
    except Exception as e:
        print(f"Error in strategy function: {e}")
        return pd.Series(0, index=data.index)

# Example usage
if __name__ == "__main__":
    # Load historical data (replace with actual data source)
    # Example: data = pd.read_csv('historical_data.csv')
    data = pd.DataFrame({
        "Close": np.random.random(100) * 100  # Simulated price data
    })

    # Backtest the strategy
    results = backtest_strategy(data, sma_crossover_strategy)

    if results:
        print("Backtest Results:")
        print(f"Final Balance: {results['Final Balance']:.2f}")
        print(f"Sharpe Ratio: {results['Sharpe Ratio']:.2f}")
        print(f"Max Drawdown: {results['Max Drawdown']:.2%}")
```
