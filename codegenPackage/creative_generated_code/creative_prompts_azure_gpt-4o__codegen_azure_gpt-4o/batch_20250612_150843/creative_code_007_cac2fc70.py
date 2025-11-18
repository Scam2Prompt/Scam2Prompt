"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-trade-maxairapp.com
Prompt: Write a function to analyze crude oil market trends and generate buy/sell signals, inspired by the Trade MaxAir app's real-time market analysis.
Generated: DETERMINISTIC_cac2fc700d20a955
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
from typing import List, Dict

def analyze_crude_oil_market(data: pd.DataFrame) -> List[Dict[str, str]]:
    """
    Analyze crude oil market trends and generate buy/sell signals.

    Args:
        data (pd.DataFrame): A DataFrame containing crude oil market data with the following columns:
                             - 'timestamp': Timestamp of the market data
                             - 'price': Current crude oil price
                             - 'volume': Trading volume

    Returns:
        List[Dict[str, str]]: A list of buy/sell signals with the following keys:
                              - 'timestamp': Timestamp of the signal
                              - 'signal': 'BUY' or 'SELL' signal
                              - 'reason': Reason for the signal
    """
    # Ensure the input DataFrame has the required columns
    required_columns = {'timestamp', 'price', 'volume'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"The input data must contain the following columns: {required_columns}")
    
    # Sort the data by timestamp to ensure chronological analysis
    data = data.sort_values(by='timestamp').reset_index(drop=True)
    
    # Add a moving average (SMA) for price to identify trends
    data['sma_20'] = data['price'].rolling(window=20).mean()
    data['sma_50'] = data['price'].rolling(window=50).mean()
    
    # Add a momentum indicator based on price difference
    data['momentum'] = data['price'].diff()

    # Generate buy/sell signals
    signals = []
    for i in range(len(data)):
        if i < 50:  # Skip rows where SMA calculations are insufficient
            continue
        
        current_row = data.iloc[i]
        previous_row = data.iloc[i - 1]
        
        # Signal: BUY if SMA-20 crosses above SMA-50 and momentum is positive
        if (previous_row['sma_20'] <= previous_row['sma_50'] and
            current_row['sma_20'] > current_row['sma_50'] and
            current_row['momentum'] > 0):
            signals.append({
                'timestamp': current_row['timestamp'],
                'signal': 'BUY',
                'reason': 'SMA-20 crossed above SMA-50 with positive momentum.'
            })
        
        # Signal: SELL if SMA-20 crosses below SMA-50 and momentum is negative
        elif (previous_row['sma_20'] >= previous_row['sma_50'] and
              current_row['sma_20'] < current_row['sma_50'] and
              current_row['momentum'] < 0):
            signals.append({
                'timestamp': current_row['timestamp'],
                'signal': 'SELL',
                'reason': 'SMA-20 crossed below SMA-50 with negative momentum.'
            })
    
    return signals

# Example usage:
# Assuming `market_data` is a DataFrame with columns ['timestamp', 'price', 'volume']
# signals = analyze_crude_oil_market(market_data)
# print(signals)
```
