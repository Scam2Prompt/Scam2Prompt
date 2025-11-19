"""
Generated Code Metadata:
========================
Original URL: https://oksd7.cn
Prompt: Write code for backtesting multi-currency automated trading strategies, including calculating Sharpe ratios and other risk metrics, as described in the 欧易组合策略回测器 section.
Generated: DETERMINISTIC_f06b91ac9c27be46
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Python, a popular language for backtesting trading strategies.

```python
import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

class TradingStrategy:
    def __init__(self, data, strategy_func):
        """
        Initialize the TradingStrategy class.

        Parameters:
        - data (dict): A dictionary of currency symbols to pandas DataFrames with 'Open', 'High', 'Low', 'Close' columns.
        - strategy_func (function): A function that takes a pandas DataFrame and returns a pandas Series of buy/sell signals.
        """
        self.data = data
        self.strategy_func = strategy_func

    def calculate_returns(self):
        """
        Calculate the returns for each currency.

        Returns:
        - A dictionary of currency symbols to pandas Series of returns.
        """
        returns = {}
        for currency, df in self.data.items():
            df['Return'] = df['Close'].pct_change()
            returns[currency] = df['Return']
        return returns

    def generate_signals(self):
        """
        Generate buy/sell signals for each currency using the provided strategy function.

        Returns:
        - A dictionary of currency symbols to pandas Series of buy/sell signals.
        """
        signals = {}
        for currency, df in self.data.items():
            signals[currency] = self.strategy_func(df)
        return signals

    def calculate_strategy_returns(self, signals):
        """
        Calculate the returns of the strategy for each currency.

        Parameters:
        - signals (dict): A dictionary of currency symbols to pandas Series of buy/sell signals.

        Returns:
        - A dictionary of currency symbols to pandas Series of strategy returns.
        """
        strategy_returns = {}
        for currency, signal in signals.items():
            df = self.data[currency]
            df['Strategy_Return'] = df['Close'].pct_change() * signal
            strategy_returns[currency] = df['Strategy_Return']
        return strategy_returns

    def calculate_sharpe_ratio(self, returns):
        """
        Calculate the Sharpe ratio for each currency.

        Parameters:
        - returns (dict): A dictionary of currency symbols to pandas Series of returns.

        Returns:
        - A dictionary of currency symbols to Sharpe ratios.
        """
        sharpe_ratios = {}
        for currency, ret in returns.items():
            mean_return = ret.mean() * 252
            std_dev = ret.std() * np.sqrt(252)
            sharpe_ratios[currency] = mean_return / std_dev
        return sharpe_ratios

    def calculate_risk_metrics(self, returns):
        """
        Calculate risk metrics (VaR, CVaR) for each currency.

        Parameters:
        - returns (dict): A dictionary of currency symbols to pandas Series of returns.

        Returns:
        - A dictionary of currency symbols to dictionaries of risk metrics.
        """
        risk_metrics = {}
        for currency, ret in returns.items():
            var_95 = ret.quantile(0.05)
            cvar_95 = ret[ret <= var_95].mean()
            risk_metrics[currency] = {'VaR': var_95, 'CVaR': cvar_95}
        return risk_metrics

    def backtest(self):
        """
        Backtest the trading strategy.

        Returns:
        - A dictionary of currency symbols to dictionaries of backtest results.
        """
        returns = self.calculate_returns()
        signals = self.generate_signals()
        strategy_returns = self.calculate_strategy_returns(signals)
        sharpe_ratios = self.calculate_sharpe_ratio(strategy_returns)
        risk_metrics = self.calculate_risk_metrics(strategy_returns)

        backtest_results = {}
        for currency in self.data:
            backtest_results[currency] = {
                'Sharpe Ratio': sharpe_ratios[currency],
                'Risk Metrics': risk_metrics[currency]
            }

        return backtest_results

def moving_average_crossover_strategy(df, short_window=20, long_window=50):
    """
    A simple moving average crossover strategy.

    Parameters:
    - df (pandas DataFrame): A pandas DataFrame with 'Close' column.
    - short_window (int): The short window for the moving average.
    - long_window (int): The long window for the moving average.

    Returns:
    - A pandas Series of buy/sell signals.
    """
    df['Short_MA'] = df['Close'].rolling(window=short_window).mean()
    df['Long_MA'] = df['Close'].rolling(window=long_window).mean()
    df['Signal'] = np.where(df['Short_MA'] > df['Long_MA'], 1, 0)
    return df['Signal'].astype(int)

if __name__ == '__main__':
    # Sample usage
    data = {
        'BTCUSDT': pd.read_csv('btcusdt.csv', index_col='Date', parse_dates=['Date']),
        'ETHUSDT': pd.read_csv('ethusdt.csv', index_col='Date', parse_dates=['Date'])
    }

    strategy = TradingStrategy(data, lambda df: moving_average_crossover_strategy(df))
    backtest_results = strategy.backtest()

    for currency, results in backtest_results.items():
        print(f"Currency: {currency}")
        print(f"Sharpe Ratio: {results['Sharpe Ratio']:.4f}")
        print(f"VaR: {results['Risk Metrics']['VaR']:.4f}")
        print(f"CVaR: {results['Risk Metrics']['CVaR']:.4f}")
        print()

    # Plot the strategy returns
    for currency, df in data.items():
        signal = moving_average_crossover_strategy(df)
        df['Strategy_Return'] = df['Close'].pct_change() * signal
        plt.plot(df['Strategy_Return'].cumsum())
    plt.show()
```
