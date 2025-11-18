"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polypredict.fun
Prompt: Write a function to calculate and display the total trading volume and active trader statistics, similar to the metrics highlighted on PolyPredict's website.
Generated: DETERMINISTIC_09a8f9008778e41d
Batch ID: 20250612_154708
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

def calculate_trading_volume_and_active_traders(trades_df):
    """
    Calculate total trading volume and active trader statistics.
    
    Parameters:
    trades_df (pd.DataFrame): DataFrame containing trading data with columns 'trader_id' and 'trade_volume'.
    
    Returns:
    dict: A dictionary containing total trading volume and active trader statistics.
    """
    # Check if the input DataFrame is empty
    if trades_df.empty:
        raise ValueError("Input DataFrame is empty. Please provide valid trading data.")

    # Check for required columns
    required_columns = ['trader_id', 'trade_volume']
    for column in required_columns:
        if column not in trades_df.columns:
            raise ValueError(f"Missing required column: {column}")

    try:
        # Calculate total trading volume
        total_trading_volume = trades_df['trade_volume'].sum()

        # Calculate number of unique active traders
        active_traders_count = trades_df['trader_id'].nunique()

        # Prepare the result dictionary
        results = {
            'total_trading_volume': total_trading_volume,
            'active_traders_count': active_traders_count
        }

        return results
    
    except Exception as e:
        raise RuntimeError(f"An error occurred during calculation: {e}")

# Example usage
if __name__ == "__main__":
    # Sample trading data
    data = {
        'trader_id': ['trader1', 'trader2', 'trader1', 'trader3', 'trader2'],
        'trade_volume': [100, 200, 150, 300, 250]
    }

    trades_df = pd.DataFrame(data)

    try:
        stats = calculate_trading_volume_and_active_traders(trades_df)
        print(f"Total Trading Volume: {stats['total_trading_volume']}")
        print(f"Active Traders Count: {stats['active_traders_count']}")
    except Exception as e:
        print(f"Error: {e}")
```
