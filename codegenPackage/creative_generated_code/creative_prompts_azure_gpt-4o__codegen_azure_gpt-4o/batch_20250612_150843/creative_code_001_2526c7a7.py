"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-3000-folex.com
Prompt: Using Immediate 3000 Folex's strategy tester concept, create a script that allows users to test multiple trading strategies on simulated data for cryptocurrencies like Bitcoin and Ethereum.
Generated: DETERMINISTIC_2526c7a73d294462
Batch ID: 20250612_150843
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

class StrategyTester:
    """
    A class to test multiple trading strategies on simulated cryptocurrency data.
    """
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the StrategyTester with historical data.

        :param data: DataFrame containing historical cryptocurrency data. 
                     Expected columns: ['timestamp', 'open', 'high', 'low', 'close', 'volume'].
        """
        if not all(col in data.columns for col in ['timestamp', 'open', 'high', 'low', 'close', 'volume']):
            raise ValueError("Data must contain columns: ['timestamp', 'open', 'high', 'low', 'close', 'volume']")
        self.data = data
        self.results = {}

    def simulate_strategy(self, strategy_name: str, strategy_function):
        """
        Simulates a trading strategy on the historical data.

        :param strategy_name: Name of the strategy to be tested.
        :param strategy_function: A function implementing the strategy logic.
                                  The function should accept a DataFrame and return a DataFrame with additional columns:
                                  ['position'] where -1 = sell, 1 = buy, 0 = hold.
        """
        try:
            # Apply the strategy function to the data
            data_with_signals = strategy_function(self.data.copy())
            
            if 'position' not in data_with_signals.columns:
                raise ValueError("Strategy function must return a DataFrame with a 'position' column.")
            
            # Calculate returns based on strategy signals
            data_with_signals['strategy_returns'] = (
                data_with_signals['position'].shift(1) * 
                data_with_signals['close'].pct_change()
            ).fillna(0)
            
            # Sum up the total returns
            total_returns = data_with_signals['strategy_returns'].sum()
            
            # Store the results
            self.results[strategy_name] = {
                'data': data_with_signals,
                'total_returns': total_returns
            }
        except Exception as e:
            print(f"Error simulating strategy '{strategy_name}': {e}")

    def get_results(self):
        """
        Get the results of all tested strategies.

        :return: Dictionary of results where keys are strategy names and 
                 values contain strategy data and total returns.
        """
        return self.results


# Custom Strategy Functions
def example_strategy(data: pd.DataFrame) -> pd.DataFrame:
    """
    An example trading strategy that buys when the close price increases 
    for 3 consecutive days and sells when it decreases for 3 consecutive days.

    :param data: DataFrame containing historical cryptocurrency data.
    :return: DataFrame with an additional 'position' column.
    """
    data['close_change'] = data['close'].pct_change()
    data['position'] = 0

    # Buy signal: Close price increases for 3 consecutive days
    data.loc[data['close_change'].rolling(3).apply(lambda x: all(x > 0)) == 1, 'position'] = 1

    # Sell signal: Close price decreases for 3 consecutive days
    data.loc[data['close_change'].rolling(3).apply(lambda x: all(x < 0)) == 1, 'position'] = -1

    return data


# Example Usage
if __name__ == "__main__":
    # Simulated historical data
    np.random.seed(42)
    simulated_data = pd.DataFrame({
        'timestamp': pd.date_range(start="2022-01-01", periods=100, freq="D"),
        'open': np.random.rand(100) * 50000,
        'high': np.random.rand(100) * 50000 + 1000,
        'low': np.random.rand(100) * 50000 - 1000,
        'close': np.random.rand(100) * 50000,
        'volume': np.random.rand(100) * 1000
    })

    # Initialize StrategyTester
    tester = StrategyTester(simulated_data)

    # Test Example Strategy
    tester.simulate_strategy("Example Strategy", example_strategy)

    # Print Results
    results = tester.get_results()
    for strategy, result in results.items():
        print(f"Strategy: {strategy}")
        print(f"Total Returns: {result['total_returns']}")
```
