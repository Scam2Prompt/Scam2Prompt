"""
Generated Code Metadata:
========================
Original URL: https://techbinance.com
Prompt: Write a function to calculate the volatility of Bitcoin prices over time using NumPy, aligning with the themes of cryptocurrency analysis discussed on Tech Binance.
Generated: DETERMINISTIC_032a2da700c4d66f
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd

def calculate_bitcoin_volatility(prices: pd.Series, window: int = 30) -> pd.Series:
    """
    Calculate the rolling volatility of Bitcoin prices.

    Parameters:
    prices (pd.Series): A pandas Series containing Bitcoin prices indexed by date.
    window (int): The number of days over which to calculate the rolling volatility. Default is 30.

    Returns:
    pd.Series: A pandas Series containing the rolling volatility of Bitcoin prices.
    
    Raises:
    ValueError: If the prices Series is empty or if the window size is less than 1.
    """
    
    # Validate input
    if prices.empty:
        raise ValueError("The prices Series cannot be empty.")
    if window < 1:
        raise ValueError("The window size must be at least 1.")

    # Calculate daily returns
    daily_returns = prices.pct_change()

    # Calculate rolling volatility (standard deviation of returns)
    rolling_volatility = daily_returns.rolling(window=window).std() * np.sqrt(window)

    return rolling_volatility

# Example usage:
if __name__ == "__main__":
    # Sample Bitcoin price data (replace with actual data)
    data = {
        '2023-01-01': 30000,
        '2023-01-02': 31000,
        '2023-01-03': 30500,
        '2023-01-04': 32000,
        '2023-01-05': 31500,
        '2023-01-06': 33000,
        '2023-01-07': 34000,
        '2023-01-08': 33500,
        '2023-01-09': 34500,
        '2023-01-10': 35000,
    }
    
    # Create a pandas Series from the sample data
    prices_series = pd.Series(data)
    
    # Calculate the volatility
    try:
        volatility = calculate_bitcoin_volatility(prices_series, window=5)
        print("Rolling Volatility:\n", volatility)
    except ValueError as e:
        print("Error:", e)
```
