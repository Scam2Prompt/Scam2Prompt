"""
Generated Code Metadata:
========================
Original URL: https://gcapmarkets.com
Prompt: Write a Python function that demonstrates how to implement a simple trading strategy based on continuous improvement and dedication to client satisfaction.
Generated: DETERMINISTIC_8a0406e294c59b5c
Batch ID: 20250622_211504
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

def simple_trading_strategy(data: pd.DataFrame, short_window: int = 40, long_window: int = 100):
    """
    Implements a simple trading strategy based on moving averages.

    Parameters:
        data (pd.DataFrame): A DataFrame containing 'Date' and 'Close' columns.
        short_window (int): The short moving average window size.
        long_window (int): The long moving average window size.

    Returns:
        pd.DataFrame: A DataFrame with trading signals and performance metrics.
    """
    try:
        # Ensure the input DataFrame has the required columns
        if 'Date' not in data.columns or 'Close' not in data.columns:
            raise ValueError("Input data must contain 'Date' and 'Close' columns.")

        # Sort data by date to ensure chronological order
        data = data.sort_values(by='Date').reset_index(drop=True)

        # Calculate short and long moving averages
        data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
        data['Long_MA'] = data['Close'].rolling(window=long_window).mean()

        # Generate trading signals
        data['Signal'] = np.where(data['Short_MA'] > data['Long_MA'], 1, 0)  # 1 = Buy, 0 = Sell

        # Calculate daily returns
        data['Daily_Return'] = data['Close'].pct_change()

        # Calculate strategy returns based on signals
        data['Strategy_Return'] = data['Signal'].shift(1) * data['Daily_Return']

        # Calculate cumulative returns for both the strategy and the market
        data['Cumulative_Market_Return'] = (1 + data['Daily_Return']).cumprod()
        data['Cumulative_Strategy_Return'] = (1 + data['Strategy_Return']).cumprod()

        # Drop rows with NaN values (due to rolling calculations)
        data = data.dropna()

        return data

    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=200),
        'Close': np.random.uniform(100, 200, 200)
    })

    # Run the trading strategy
    result = simple_trading_strategy(sample_data)

    # Display the first few rows of the result
    print(result.head())
```
