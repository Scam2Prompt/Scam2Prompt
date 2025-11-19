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

class InvestmentStrategyManager:
    """
    A class to manage investment strategies using historical data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the InvestmentStrategyManager with historical data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing historical investment data with 'Date' and 'Price' columns.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        
        if 'Date' not in data.columns or 'Price' not in data.columns:
            raise ValueError("Data must contain 'Date' and 'Price' columns.")
        
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data.set_index('Date', inplace=True)

    def calculate_moving_average(self, window: int) -> pd.Series:
        """
        Calculates the moving average of the price data.

        Parameters:
        window (int): The number of periods to calculate the moving average.

        Returns:
        pd.Series: A Series containing the moving average.
        """
        if window <= 0:
            raise ValueError("Window size must be a positive integer.")
        
        return self.data['Price'].rolling(window=window).mean()

    def generate_signals(self, short_window: int, long_window: int) -> pd.DataFrame:
        """
        Generates buy/sell signals based on moving averages.

        Parameters:
        short_window (int): The short moving average window.
        long_window (int): The long moving average window.

        Returns:
        pd.DataFrame: A DataFrame containing the signals.
        """
        if short_window <= 0 or long_window <= 0:
            raise ValueError("Window sizes must be positive integers.")
        
        signals = pd.DataFrame(index=self.data.index)
        signals['Price'] = self.data['Price']
        signals['Short_MA'] = self.calculate_moving_average(short_window)
        signals['Long_MA'] = self.calculate_moving_average(long_window)

        # Create signals
        signals['Signal'] = 0
        signals['Signal'][short_window:] = np.where(
            signals['Short_MA'][short_window:] > signals['Long_MA'][short_window:], 1, 0
        )
        signals['Position'] = signals['Signal'].diff()

        return signals

    def backtest_strategy(self, signals: pd.DataFrame, initial_capital: float = 10000.0) -> pd.DataFrame:
        """
        Backtests the investment strategy based on generated signals.

        Parameters:
        signals (pd.DataFrame): A DataFrame containing the signals.
        initial_capital (float): The initial capital for the backtest.

        Returns:
        pd.DataFrame: A DataFrame containing the portfolio value over time.
        """
        if initial_capital <= 0:
            raise ValueError("Initial capital must be a positive number.")
        
        portfolio = signals.copy()
        portfolio['Holdings'] = (signals['Position'].cumsum() * signals['Price']).fillna(0)
        portfolio['Cash'] = initial_capital - (signals['Position'] * signals['Price']).cumsum().fillna(0)
        portfolio['Total_Value'] = portfolio['Holdings'] + portfolio['Cash']

        return portfolio[['Price', 'Holdings', 'Cash', 'Total_Value']]

# Example usage
if __name__ == "__main__":
    # Sample historical data
    data = {
        'Date': pd.date_range(start='2020-01-01', periods=100),
        'Price': np.random.rand(100) * 100  # Random prices
    }
    historical_data = pd.DataFrame(data)

    # Initialize the investment strategy manager
    manager = InvestmentStrategyManager(historical_data)

    # Generate signals
    signals = manager.generate_signals(short_window=5, long_window=20)

    # Backtest the strategy
    portfolio = manager.backtest_strategy(signals)

    # Display the portfolio value over time
    print(portfolio)
```
