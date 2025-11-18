"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oksd7.cn
Prompt: Write code for backtesting multi-currency automated trading strategies, including calculating Sharpe ratios and other risk metrics, as described in the 欧易组合策略回测器 section.
Generated: DETERMINISTIC_f06b91ac9c27be46
Batch ID: 20250612_153925
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
from datetime import datetime
from typing import List, Dict

class BacktestEngine:
    """
    A backtesting engine for multi-currency trading strategies.
    Calculates performance metrics such as Sharpe ratio, max drawdown, and total return.
    """

    def __init__(self, initial_balance: float = 10000):
        """
        Initialize backtesting engine with an initial account balance.
        :param initial_balance: Starting balance for the backtest.
        """
        self.initial_balance = initial_balance
        self.portfolio_balance = initial_balance
        self.trades = []
        self.currency_balances = {}  # Holds balances for different currencies
        self.performance = None  # Holds computed performance metrics

    def load_data(self, data: Dict[str, pd.DataFrame]):
        """
        Load historical price data for multiple currencies.
        :param data: Dictionary where keys are currency pairs (e.g., 'BTC/USD') and values are price DataFrames.
        """
        self.data = data

    def execute_strategy(self, strategy: callable):
        """
        Execute the trading strategy over the historical data.
        :param strategy: A callable that implements the trading logic.
                         It should accept price data and return a list of trades.
        """
        for currency_pair, price_data in self.data.items():
            trades = strategy(currency_pair, price_data)
            self.trades.extend(trades)

    def calculate_metrics(self):
        """
        Calculate backtest performance metrics such as Sharpe ratio, max drawdown, and total return.
        """
        # Calculate portfolio returns based on trade results
        portfolio_value = self.initial_balance
        portfolio_values = [portfolio_value]

        for trade in self.trades:
            # Simulate portfolio value changes based on trades
            pnl = trade["pnl"]
            portfolio_value += pnl
            portfolio_values.append(portfolio_value)

        # Calculate metrics
        portfolio_values = np.array(portfolio_values)
        returns = np.diff(portfolio_values) / portfolio_values[:-1]

        sharpe_ratio = self._calculate_sharpe_ratio(returns)
        max_drawdown = self._calculate_max_drawdown(portfolio_values)
        total_return = (portfolio_values[-1] - portfolio_values[0]) / portfolio_values[0]

        self.performance = {
            "Sharpe Ratio": sharpe_ratio,
            "Max Drawdown": max_drawdown,
            "Total Return": total_return,
        }

    def _calculate_sharpe_ratio(self, returns: np.ndarray) -> float:
        """
        Calculate the Sharpe ratio for the given returns.
        :param returns: Array of portfolio returns.
        :return: Sharpe ratio.
        """
        risk_free_rate = 0.0  # Assume risk-free rate is 0 for simplicity
        excess_returns = returns - risk_free_rate
        return excess_returns.mean() / excess_returns.std()

    def _calculate_max_drawdown(self, portfolio_values: np.ndarray) -> float:
        """
        Calculate the maximum drawdown of the portfolio.
        :param portfolio_values: Array of portfolio values over time.
        :return: Maximum drawdown as a percentage.
        """
        peak = portfolio_values[0]
        drawdowns = []

        for value in portfolio_values:
            if value > peak:
                peak = value
            drawdowns.append((peak - value) / peak)

        return max(drawdowns)

    def generate_report(self):
        """
        Generate a report of backtest performance metrics.
        :return: Dictionary containing performance metrics.
        """
        if self.performance is None:
            self.calculate_metrics()
        return self.performance


def example_strategy(currency_pair: str, price_data: pd.DataFrame) -> List[Dict[str, float]]:
    """
    Example trading strategy that places trades based on simple moving average crossover.
    :param currency_pair: The currency pair being traded.
    :param price_data: Historical price data for the currency pair.
    :return: List of trades, where each trade is a dictionary containing trade details.
    """
    trades = []
    short_window = 5
    long_window = 20

    # Calculate moving averages
    price_data["short_ma"] = price_data["Close"].rolling(window=short_window).mean()
    price_data["long_ma"] = price_data["Close"].rolling(window=long_window).mean()

    position = 0  # 1 if we are holding the currency, 0 otherwise

    for i in range(long_window, len(price_data)):
        short_ma = price_data["short_ma"].iloc[i]
        long_ma = price_data["long_ma"].iloc[i]
        close_price = price_data["Close"].iloc[i]

        if short_ma > long_ma and position == 0:
            # Buy signal
            trades.append({"currency_pair": currency_pair, "price": close_price, "pnl": -close_price})
            position = 1  # Enter position
        elif short_ma < long_ma and position == 1:
            # Sell signal
            trades.append({"currency_pair": currency_pair, "price": close_price, "pnl": close_price})
            position = 0  # Exit position

    return trades


if __name__ == "__main__":
    # Example usage of the backtesting engine

    # Load example data for BTC/USD
    dates = pd.date_range(start="2023-01-01", end="2023-03-01", freq="D")
    btc_prices = pd.DataFrame({
        "Date": dates,
        "Close": np.linspace(20000, 30000, len(dates)) + np.random.normal(0, 500, len(dates))
    })
    btc_prices.set_index("Date", inplace=True)

    # Load data into the backtesting engine
    engine = BacktestEngine(initial_balance=10000)
    engine.load_data({"BTC/USD": btc_prices})

    # Run example strategy on the data
    engine.execute_strategy(example_strategy)

    # Generate and print a performance report
    report = engine.generate_report()
    print("Backtest Performance Report:")
    for metric, value in report.items():
        print(f"{metric}: {value:.2f}")
```
