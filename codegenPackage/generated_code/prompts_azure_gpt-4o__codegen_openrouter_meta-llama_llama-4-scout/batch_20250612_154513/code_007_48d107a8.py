"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Generate code to analyze the financial performance of TPCPLC using its actively traded shares on the Dar es Salaam Stock Exchange (DSE).
Generated: DETERMINISTIC_48d107a8380cffc8
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime

class TPCPLCAnalyzer:
    """
    Analyzes the financial performance of TPCPLC using its actively traded shares on the Dar es Salaam Stock Exchange (DSE).
    """

    def __init__(self, stock_data):
        """
        Initializes the TPCPLCAnalyzer with stock data.

        Args:
            stock_data (pd.DataFrame): A DataFrame containing the stock data with columns 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'.
        """
        self.stock_data = stock_data

    def calculate_daily_returns(self):
        """
        Calculates the daily returns of TPCPLC stock.

        Returns:
            pd.Series: A Series containing the daily returns.
        """
        # Ensure 'Date' column is of datetime type
        self.stock_data['Date'] = pd.to_datetime(self.stock_data['Date'])

        # Sort data by date
        self.stock_data = self.stock_data.sort_values(by='Date')

        # Calculate daily returns
        self.stock_data['Return'] = self.stock_data['Close'].pct_change()

        return self.stock_data['Return']

    def calculate_moving_averages(self, window_sizes):
        """
        Calculates the moving averages of TPCPLC stock.

        Args:
            window_sizes (list): A list of window sizes for the moving averages.

        Returns:
            dict: A dictionary containing the moving averages for each window size.
        """
        moving_averages = {}

        for window_size in window_sizes:
            moving_averages[window_size] = self.stock_data['Close'].rolling(window=window_size).mean()

        return moving_averages

    def calculate_volatility(self, window_size):
        """
        Calculates the volatility of TPCPLC stock.

        Args:
            window_size (int): The window size for the volatility calculation.

        Returns:
            pd.Series: A Series containing the volatility.
        """
        return self.stock_data['Close'].rolling(window=window_size).std()

    def analyze_performance(self):
        """
        Analyzes the financial performance of TPCPLC stock.

        Returns:
            dict: A dictionary containing the analysis results.
        """
        analysis_results = {}

        # Calculate daily returns
        daily_returns = self.calculate_daily_returns()

        # Calculate moving averages
        window_sizes = [7, 14, 30]
        moving_averages = self.calculate_moving_averages(window_sizes)

        # Calculate volatility
        window_size = 30
        volatility = self.calculate_volatility(window_size)

        # Store analysis results
        analysis_results['Daily Returns'] = daily_returns
        analysis_results['Moving Averages'] = moving_averages
        analysis_results['Volatility'] = volatility

        return analysis_results


def main():
    try:
        # Sample stock data
        stock_data = pd.DataFrame({
            'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
            'Open': [100.0, 110.0, 120.0, 130.0, 140.0],
            'High': [110.0, 120.0, 130.0, 140.0, 150.0],
            'Low': [90.0, 100.0, 110.0, 120.0, 130.0],
            'Close': [105.0, 115.0, 125.0, 135.0, 145.0],
            'Volume': [1000, 2000, 3000, 4000, 5000]
        })

        # Create TPCPLCAnalyzer instance
        analyzer = TPCPLCAnalyzer(stock_data)

        # Analyze performance
        analysis_results = analyzer.analyze_performance()

        # Print analysis results
        print("Daily Returns:")
        print(analysis_results['Daily Returns'])
        print("\nMoving Averages:")
        for window_size, moving_average in analysis_results['Moving Averages'].items():
            print(f"Window Size: {window_size}")
            print(moving_average)
        print("\nVolatility:")
        print(analysis_results['Volatility'])

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
