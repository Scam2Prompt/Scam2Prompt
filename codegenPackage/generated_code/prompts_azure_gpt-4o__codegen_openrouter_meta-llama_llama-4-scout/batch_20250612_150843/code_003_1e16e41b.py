"""
Generated Code Metadata:
========================
Original URL: https://theimmediatebitxdr.com
Prompt: Implement a strategy tester for evaluating trading performance across multiple assets, based on Immediate Bitxdr's robust testing modes.
Generated: DETERMINISTIC_1e16e41bbf9043a3
Batch ID: 20250612_150843
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

class StrategyTester:
    """
    A class used to evaluate trading performance across multiple assets.

    Attributes:
    ----------
    assets : List[str]
        A list of asset names.
    data : Dict[str, pd.DataFrame]
        A dictionary of historical data for each asset.
    strategy : callable
        A function that implements the trading strategy.

    Methods:
    -------
    run_test(asset: str, initial_capital: float, test_mode: str)
        Runs the strategy test for a given asset and test mode.
    evaluate_performance(asset: str, trades: List[Dict])
        Evaluates the trading performance for a given asset.
    """

    def __init__(self, assets: List[str], data: Dict[str, pd.DataFrame], strategy: callable):
        """
        Initializes the StrategyTester instance.

        Parameters:
        ----------
        assets : List[str]
            A list of asset names.
        data : Dict[str, pd.DataFrame]
            A dictionary of historical data for each asset.
        strategy : callable
            A function that implements the trading strategy.
        """
        self.assets = assets
        self.data = data
        self.strategy = strategy

    def run_test(self, asset: str, initial_capital: float, test_mode: str):
        """
        Runs the strategy test for a given asset and test mode.

        Parameters:
        ----------
        asset : str
            The name of the asset to test.
        initial_capital : float
            The initial capital for the test.
        test_mode : str
            The test mode (e.g., 'backtest', 'walkforward').

        Returns:
        -------
        List[Dict]
            A list of trades executed during the test.
        """
        if asset not in self.assets:
            raise ValueError(f"Asset '{asset}' not found")

        if test_mode not in ['backtest', 'walkforward']:
            raise ValueError(f"Invalid test mode '{test_mode}'")

        data = self.data[asset]
        trades = self.strategy(data, initial_capital)

        return trades

    def evaluate_performance(self, asset: str, trades: List[Dict]):
        """
        Evaluates the trading performance for a given asset.

        Parameters:
        ----------
        asset : str
            The name of the asset to evaluate.
        trades : List[Dict]
            A list of trades executed during the test.

        Returns:
        -------
        Dict[str, float]
            A dictionary of performance metrics (e.g., profit, return, Sharpe ratio).
        """
        # Calculate performance metrics
        profit = sum(trade['profit'] for trade in trades)
        returns = np.mean([trade['return'] for trade in trades])
        sharpe_ratio = self.sharpe_ratio([trade['return'] for trade in trades])

        return {
            'profit': profit,
            'return': returns,
            'sharpe_ratio': sharpe_ratio
        }

    @staticmethod
    def sharpe_ratio(returns: List[float]):
        """
        Calculates the Sharpe ratio.

        Parameters:
        ----------
        returns : List[float]
            A list of returns.

        Returns:
        -------
        float
            The Sharpe ratio.
        """
        mean_return = np.mean(returns)
        std_dev = np.std(returns)

        if std_dev == 0:
            return 0

        return mean_return / std_dev


def example_strategy(data: pd.DataFrame, initial_capital: float):
    """
    An example trading strategy.

    Parameters:
    ----------
    data : pd.DataFrame
        Historical data for the asset.
    initial_capital : float
        The initial capital.

    Returns:
    -------
    List[Dict]
        A list of trades executed during the test.
    """
    trades = []
    position = 0
    capital = initial_capital

    for i in range(len(data)):
        if data['close'].iloc[i] > data['close'].iloc[i-1] and position == 0:
            # Buy
            position = 1
            capital -= data['close'].iloc[i]
            trades.append({
                'type': 'buy',
                'price': data['close'].iloc[i],
                'profit': 0,
                'return': 0
            })
        elif data['close'].iloc[i] < data['close'].iloc[i-1] and position == 1:
            # Sell
            position = 0
            capital += data['close'].iloc[i]
            trades.append({
                'type': 'sell',
                'price': data['close'].iloc[i],
                'profit': data['close'].iloc[i] - trades[-1]['price'],
                'return': (data['close'].iloc[i] - trades[-1]['price']) / trades[-1]['price']
            })

    return trades


if __name__ == '__main__':
    assets = ['AAPL', 'GOOGL']
    data = {
        'AAPL': pd.DataFrame({
            'close': [100, 110, 120, 130, 140]
        }),
        'GOOGL': pd.DataFrame({
            'close': [500, 510, 520, 530, 540]
        })
    }

    strategy_tester = StrategyTester(assets, data, example_strategy)

    for asset in assets:
        trades = strategy_tester.run_test(asset, 10000, 'backtest')
        performance = strategy_tester.evaluate_performance(asset, trades)

        print(f"Asset: {asset}")
        print(f"Trades: {trades}")
        print(f"Performance: {performance}")
        print()
```
