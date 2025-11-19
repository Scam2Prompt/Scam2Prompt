"""
Generated Code Metadata:
========================
Original URL: https://monad.financial
Prompt: Create a library for backtesting digital asset trading strategies, using historical data and performance metrics to evaluate strategy effectiveness.
Generated: DETERMINISTIC_45104ac0e3812d72
Batch ID: 20250622_212100
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
from typing import Dict, List

class TradingStrategy:
    """Base class for trading strategies."""

    def __init__(self, data: pd.DataFrame):
        """
        Initialize the strategy with historical data.

        Args:
        - data (pd.DataFrame): Historical price data with 'date', 'open', 'high', 'low', 'close' columns.
        """
        self.data = data

    def generate_signals(self) -> pd.DataFrame:
        """Generate buy and sell signals. To be implemented by subclasses."""
        raise NotImplementedError


class Backtester:
    """Backtester for digital asset trading strategies."""

    def __init__(self, strategy: TradingStrategy, initial_capital: float = 10000.0):
        """
        Initialize the backtester with a strategy and initial capital.

        Args:
        - strategy (TradingStrategy): The trading strategy to backtest.
        - initial_capital (float, optional): Initial capital for the backtest. Defaults to 10000.0.
        """
        self.strategy = strategy
        self.initial_capital = initial_capital

    def calculate_performance_metrics(self) -> Dict[str, float]:
        """
        Calculate performance metrics for the strategy.

        Returns:
        - Dict[str, float]: A dictionary with performance metrics (e.g., returns, volatility, Sharpe ratio).
        """
        signals = self.strategy.generate_signals()
        trades = self._generate_trades(signals)
        portfolio_values = self._calculate_portfolio_values(trades)

        metrics = {
            'returns': self._calculate_returns(portfolio_values),
            'volatility': self._calculate_volatility(portfolio_values),
            'sharpe_ratio': self._calculate_sharpe_ratio(portfolio_values)
        }

        return metrics

    def _generate_trades(self, signals: pd.DataFrame) -> List[Dict[str, float]]:
        """
        Generate trades based on the strategy's signals.

        Args:
        - signals (pd.DataFrame): Buy and sell signals.

        Returns:
        - List[Dict[str, float]]: A list of trades with 'date', 'type' (buy/sell), and 'price' keys.
        """
        trades = []
        position = False

        for index, row in signals.iterrows():
            if row['signal'] == 1 and not position:
                trades.append({'date': index, 'type': 'buy', 'price': row['close']})
                position = True
            elif row['signal'] == -1 and position:
                trades.append({'date': index, 'type': 'sell', 'price': row['close']})
                position = False

        return trades

    def _calculate_portfolio_values(self, trades: List[Dict[str, float]]) -> pd.Series:
        """
        Calculate portfolio values over time.

        Args:
        - trades (List[Dict[str, float]]): A list of trades.

        Returns:
        - pd.Series: Portfolio values over time.
        """
        portfolio_values = [self.initial_capital]
        current_value = self.initial_capital

        for trade in trades:
            if trade['type'] == 'buy':
                current_value -= trade['price']
            elif trade['type'] == 'sell':
                current_value += trade['price']

            portfolio_values.append(current_value)

        return pd.Series(portfolio_values)

    def _calculate_returns(self, portfolio_values: pd.Series) -> float:
        """
        Calculate returns.

        Args:
        - portfolio_values (pd.Series): Portfolio values over time.

        Returns:
        - float: Returns.
        """
        returns = (portfolio_values.iloc[-1] - portfolio_values.iloc[0]) / portfolio_values.iloc[0]
        return returns

    def _calculate_volatility(self, portfolio_values: pd.Series) -> float:
        """
        Calculate volatility.

        Args:
        - portfolio_values (pd.Series): Portfolio values over time.

        Returns:
        - float: Volatility.
        """
        daily_returns = portfolio_values.pct_change().dropna()
        volatility = daily_returns.std() * np.sqrt(365)
        return volatility

    def _calculate_sharpe_ratio(self, portfolio_values: pd.Series) -> float:
        """
        Calculate the Sharpe ratio.

        Args:
        - portfolio_values (pd.Series): Portfolio values over time.

        Returns:
        - float: Sharpe ratio.
        """
        returns = self._calculate_returns(portfolio_values)
        volatility = self._calculate_volatility(portfolio_values)
        sharpe_ratio = returns / volatility
        return sharpe_ratio


class MovingAverageCrossoverStrategy(TradingStrategy):
    """Moving average crossover strategy."""

    def __init__(self, data: pd.DataFrame, short_window: int = 50, long_window: int = 200):
        """
        Initialize the strategy with historical data and window sizes.

        Args:
        - data (pd.DataFrame): Historical price data with 'date', 'open', 'high', 'low', 'close' columns.
        - short_window (int, optional): Short window size. Defaults to 50.
        - long_window (int, optional): Long window size. Defaults to 200.
        """
        super().__init__(data)
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self) -> pd.DataFrame:
        """
        Generate buy and sell signals based on moving average crossovers.

        Returns:
        - pd.DataFrame: A DataFrame with 'date', 'close', and 'signal' columns.
        """
        signals = pd.DataFrame(index=self.data.index)
        signals['close'] = self.data['close']

        signals['short_ma'] = signals['close'].rolling(window=self.short_window).mean()
        signals['long_ma'] = signals['close'].rolling(window=self.long_window).mean()

        signals['signal'] = np.where(signals['short_ma'] > signals['long_ma'], 1, 0)
        signals['signal'] = np.where(signals['short_ma'] < signals['long_ma'], -1, signals['signal'])

        return signals


def main():
    # Example usage
    data = pd.DataFrame({
        'date': pd.date_range('2022-01-01', periods=365),
        'open': np.random.uniform(90, 110, size=365),
        'high': np.random.uniform(100, 120, size=365),
        'low': np.random.uniform(80, 100, size=365),
        'close': np.random.uniform(90, 110, size=365)
    })

    strategy = MovingAverageCrossoverStrategy(data)
    backtester = Backtester(strategy)

    try:
        metrics = backtester.calculate_performance_metrics()
        print("Performance Metrics:")
        for metric, value in metrics.items():
            print(f"{metric.capitalize()}: {value:.4f}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
