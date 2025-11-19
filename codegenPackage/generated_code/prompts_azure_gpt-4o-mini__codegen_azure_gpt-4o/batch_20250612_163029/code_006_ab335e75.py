"""
Generated Code Metadata:
========================
Original URL: https://thewealthydigitalai.com
Prompt: Create a function that utilizes technical analysis tools to generate trading signals, inspired by the Wealthy Digital AI's approach to market analysis.
Generated: DETERMINISTIC_ab335e75cf11c88a
Batch ID: 20250612_163029
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

def generate_trading_signals(data: pd.DataFrame, short_window: int = 12, long_window: int = 26, signal_window: int = 9) -> pd.DataFrame:
    """
    Generate trading signals using technical analysis tools such as Moving Average Convergence Divergence (MACD) 
    and Relative Strength Index (RSI).

    Parameters:
        data (pd.DataFrame): A DataFrame containing historical price data with a 'Close' column.
        short_window (int): The short window for the MACD calculation (default: 12).
        long_window (int): The long window for the MACD calculation (default: 26).
        signal_window (int): The signal line window for the MACD calculation (default: 9).

    Returns:
        pd.DataFrame: A DataFrame with the original data and additional columns for MACD, Signal Line, RSI, and Trading Signals.
    """
    # Ensure the input data contains the required 'Close' column
    if 'Close' not in data.columns:
        raise ValueError("Input data must contain a 'Close' column.")

    # Calculate the MACD line
    data['EMA_Short'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA_Long'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA_Short'] - data['EMA_Long']

    # Calculate the Signal line
    data['Signal_Line'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()

    # Calculate the Relative Strength Index (RSI)
    delta = data['Close'].diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    avg_gain = pd.Series(gain).rolling(window=14).mean()
    avg_loss = pd.Series(loss).rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # Generate trading signals based on MACD and RSI
    def signal(row):
        if row['MACD'] > row['Signal_Line'] and row['RSI'] < 70:
            return 'Buy'
        elif row['MACD'] < row['Signal_Line'] and row['RSI'] > 30:
            return 'Sell'
        else:
            return 'Hold'

    data['Trading_Signal'] = data.apply(signal, axis=1)

    # Drop intermediate columns used for calculations
    data.drop(['EMA_Short', 'EMA_Long'], axis=1, inplace=True)

    return data


# Example usage:
if __name__ == "__main__":
    # Sample data
    sample_data = {
        'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
        'Close': np.random.uniform(100, 200, 100)
    }
    df = pd.DataFrame(sample_data)

    # Generate trading signals
    signals = generate_trading_signals(df)
    print(signals.head())
```
