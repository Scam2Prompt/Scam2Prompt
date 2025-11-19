"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thewealthydigitalai.com
Prompt: Create a function that utilizes technical analysis tools to generate trading signals, inspired by the Wealthy Digital AI's approach to market analysis.
Generated: DETERMINISTIC_ab335e75cf11c88a
Batch ID: 20250612_163029
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

def generate_trading_signals(data: pd.DataFrame, short_window: int = 14, long_window: int = 50) -> pd.DataFrame:
    """
    Generates trading signals using technical analysis tools such as moving averages and RSI (Relative Strength Index).
    
    Parameters:
        data (pd.DataFrame): A DataFrame containing historical stock price data with 'Close' column.
        short_window (int): The short moving average period (default is 14).
        long_window (int): The long moving average period (default is 50).
    
    Returns:
        pd.DataFrame: The input DataFrame with additional columns for technical indicators and signals.
    """
    
    # Ensure the required 'Close' column exists in the input DataFrame
    if 'Close' not in data.columns:
        raise ValueError("Input DataFrame must contain a 'Close' column.")
    
    # Calculate short-term and long-term moving averages
    data['SMA_Short'] = data['Close'].rolling(window=short_window).mean()
    data['SMA_Long'] = data['Close'].rolling(window=long_window).mean()
    
    # Calculate Relative Strength Index (RSI)
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss  # Relative Strength
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # Generate buy/sell signals based on SMA crossover and RSI thresholds
    data['Signal'] = 'Hold'  # Default signal
    # Buy signal: SMA_Short crosses above SMA_Long and RSI below 30 (oversold condition)
    data.loc[(data['SMA_Short'] > data['SMA_Long']) & (data['RSI'] < 30), 'Signal'] = 'Buy'
    # Sell signal: SMA_Short crosses below SMA_Long and RSI above 70 (overbought condition)
    data.loc[(data['SMA_Short'] < data['SMA_Long']) & (data['RSI'] > 70), 'Signal'] = 'Sell'
    
    # Drop rows with NaN values caused by rolling calculations for cleaner output
    data.dropna(inplace=True)
    
    return data


# Example usage:
# Assuming `df` is a pandas DataFrame with a 'Close' column containing historical closing prices.
# df = pd.read_csv("historical_data.csv")
# signals = generate_trading_signals(df)
# print(signals.head())
```
