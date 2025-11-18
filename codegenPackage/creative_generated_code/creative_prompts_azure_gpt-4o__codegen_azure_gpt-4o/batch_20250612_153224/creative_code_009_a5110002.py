"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learnatcheap.com
Prompt: Write a Python script to calculate optimal entry and exit points in Forex trading based on the Sunil Minglani course offered on LearningAtCheap.com.
Generated: DETERMINISTIC_a5110002029b1c5a
Batch ID: 20250612_153224
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

# Forex Trading Analysis Script
# Author: Your Name
# Date: YYYY-MM-DD

# Constants
RSI_PERIOD = 14  # Period for Relative Strength Index
EMA_SHORT_PERIOD = 9  # Short-term EMA period
EMA_LONG_PERIOD = 21  # Long-term EMA period
OVERBOUGHT_THRESHOLD = 70  # RSI overbought level
OVERSOLD_THRESHOLD = 30  # RSI oversold level

def calculate_rsi(data, period=RSI_PERIOD):
    """
    Calculate the Relative Strength Index (RSI).

    Args:
        data (pd.Series): Series of closing prices.
        period (int): Look-back period for RSI calculation.

    Returns:
        pd.Series: RSI values.
    """
    delta = data.diff()  # Calculate price changes
    gain = delta.where(delta > 0, 0)  # Keep only positive changes
    loss = -delta.where(delta < 0, 0)  # Keep only negative changes

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_ema(data, period):
    """
    Calculate the Exponential Moving Average (EMA).

    Args:
        data (pd.Series): Series of closing prices.
        period (int): EMA period.

    Returns:
        pd.Series: EMA values.
    """
    return data.ewm(span=period, adjust=False).mean()

def find_entry_exit_points(data):
    """
    Identify optimal entry and exit points based on RSI and EMA.

    Args:
        data (pd.DataFrame): DataFrame containing price data.

    Returns:
        pd.DataFrame: Data with entry and exit points marked.
    """
    # Calculate RSI and EMAs
    data['RSI'] = calculate_rsi(data['Close'], RSI_PERIOD)
    data['EMA_Short'] = calculate_ema(data['Close'], EMA_SHORT_PERIOD)
    data['EMA_Long'] = calculate_ema(data['Close'], EMA_LONG_PERIOD)

    # Strategy: Entry when RSI < OVERSOLD_THRESHOLD and EMA_Short > EMA_Long.
    # Exit when RSI > OVERBOUGHT_THRESHOLD or EMA_Short < EMA_Long.
    data['Entry'] = (data['RSI'] < OVERSOLD_THRESHOLD) & (data['EMA_Short'] > data['EMA_Long'])
    data['Exit'] = (data['RSI'] > OVERBOUGHT_THRESHOLD) | (data['EMA_Short'] < data['EMA_Long'])

    return data

def main():
    """
    Main function to execute the script.
    """
    # Load Forex data (Assumes you have a CSV file with 'Date', 'Close' columns)
    try:
        file_path = 'forex_data.csv'  # Replace with your file path
        forex_data = pd.read_csv(file_path)

        # Validate the required columns exist
        if 'Date' not in forex_data.columns or 'Close' not in forex_data.columns:
            raise ValueError("Input data must contain 'Date' and 'Close' columns.")

        # Process data
        forex_data['Date'] = pd.to_datetime(forex_data['Date'])
        forex_analysis = find_entry_exit_points(forex_data)

        # Save results to a new CSV
        output_path = 'forex_analysis_results.csv'
        forex_analysis.to_csv(output_path, index=False)
        print(f"Analysis complete. Results saved to {output_path}")

    except FileNotFoundError:
        print("Error: Forex data file not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
```
