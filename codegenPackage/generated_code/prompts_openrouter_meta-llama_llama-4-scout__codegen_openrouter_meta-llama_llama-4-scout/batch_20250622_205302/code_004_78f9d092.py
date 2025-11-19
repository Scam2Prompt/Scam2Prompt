"""
Generated Code Metadata:
========================
Original URL: https://fennextradingservices.com
Prompt: "Create a simple investment strategy management system using a library like pandas and numpy, inspired by the services offered by Fennex Trading Services."
Generated: DETERMINISTIC_78f9d0929690bb90
Batch ID: 20250622_205302
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

class InvestmentStrategy:
    """
    A simple investment strategy management system.

    Attributes:
    -----------
    strategies : dict
        A dictionary of investment strategies.

    Methods:
    --------
    add_strategy(name, strategy)
        Adds a new investment strategy.
    remove_strategy(name)
        Removes an existing investment strategy.
    update_strategy(name, strategy)
        Updates an existing investment strategy.
    get_strategy(name)
        Retrieves an existing investment strategy.
    calculate_returns(strategy, data)
        Calculates the returns of an investment strategy.
    """

    def __init__(self):
        self.strategies = {}

    def add_strategy(self, name, strategy):
        """
        Adds a new investment strategy.

        Parameters:
        ----------
        name : str
            The name of the strategy.
        strategy : callable
            The strategy function.

        Raises:
        ------
        ValueError
            If the strategy name already exists.
        """
        if name in self.strategies:
            raise ValueError("Strategy name already exists")
        self.strategies[name] = strategy

    def remove_strategy(self, name):
        """
        Removes an existing investment strategy.

        Parameters:
        ----------
        name : str
            The name of the strategy.

        Raises:
        ------
        ValueError
            If the strategy name does not exist.
        """
        if name not in self.strategies:
            raise ValueError("Strategy name does not exist")
        del self.strategies[name]

    def update_strategy(self, name, strategy):
        """
        Updates an existing investment strategy.

        Parameters:
        ----------
        name : str
            The name of the strategy.
        strategy : callable
            The new strategy function.

        Raises:
        ------
        ValueError
            If the strategy name does not exist.
        """
        if name not in self.strategies:
            raise ValueError("Strategy name does not exist")
        self.strategies[name] = strategy

    def get_strategy(self, name):
        """
        Retrieves an existing investment strategy.

        Parameters:
        ----------
        name : str
            The name of the strategy.

        Returns:
        -------
        callable
            The strategy function.

        Raises:
        ------
        ValueError
            If the strategy name does not exist.
        """
        if name not in self.strategies:
            raise ValueError("Strategy name does not exist")
        return self.strategies[name]

    def calculate_returns(self, strategy, data):
        """
        Calculates the returns of an investment strategy.

        Parameters:
        ----------
        strategy : callable
            The strategy function.
        data : pandas.DataFrame
            The market data.

        Returns:
        -------
        pandas.Series
            The returns of the strategy.
        """
        try:
            returns = strategy(data)
            if not isinstance(returns, pd.Series):
                raise ValueError("Strategy returns must be a pandas Series")
            return returns
        except Exception as e:
            raise ValueError("Error calculating returns") from e


def moving_average_strategy(data, window):
    """
    A simple moving average strategy.

    Parameters:
    ----------
    data : pandas.DataFrame
        The market data.
    window : int
        The moving average window.

    Returns:
    -------
    pandas.Series
        The strategy returns.
    """
    ma = data['Close'].rolling(window=window).mean()
    signals = np.where(data['Close'] > ma, 1, 0)
    returns = data['Close'].pct_change() * signals
    return returns


def main():
    # Create an instance of the investment strategy management system
    strategy_manager = InvestmentStrategy()

    # Add a moving average strategy
    strategy_manager.add_strategy('MA_50', lambda data: moving_average_strategy(data, 50))

    # Create some sample market data
    np.random.seed(0)
    data = pd.DataFrame({
        'Close': np.random.rand(100)
    })

    # Get the moving average strategy
    ma_strategy = strategy_manager.get_strategy('MA_50')

    # Calculate the returns of the strategy
    returns = strategy_manager.calculate_returns(ma_strategy, data)

    # Print the returns
    print(returns)


if __name__ == "__main__":
    main()
```
