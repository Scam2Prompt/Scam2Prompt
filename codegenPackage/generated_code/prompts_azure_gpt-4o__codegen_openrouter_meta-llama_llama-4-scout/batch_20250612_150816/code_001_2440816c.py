"""
Generated Code Metadata:
========================
Original URL: https://check-halo.pages.dev
Prompt: Generate code to analyze missed trading opportunities ("paperhanded" amounts) and visualize the data in charts, as outlined in Halo's portfolio tracker.
Generated: DETERMINISTIC_2440816c388fe6df
Batch ID: 20250612_150816
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
import matplotlib.pyplot as plt

def calculate_paperhanded_amounts(trades):
    """
    Calculate missed trading opportunities ("paperhanded" amounts) from a list of trades.

    Args:
        trades (list): A list of trades, where each trade is a dictionary with 'side', 'entry_price', and 'exit_price' keys.

    Returns:
        pandas.DataFrame: A DataFrame containing the paperhanded amounts for each trade.
    """
    # Initialize an empty list to store paperhanded amounts
    paperhanded_amounts = []

    # Iterate over each trade
    for trade in trades:
        # Check if the trade was a buy or sell
        if trade['side'] == 'buy':
            # Calculate the paperhanded amount for a buy trade
            paperhanded_amount = (trade['exit_price'] - trade['entry_price']) * trade['quantity']
        elif trade['side'] == 'sell':
            # Calculate the paperhanded amount for a sell trade
            paperhanded_amount = (trade['entry_price'] - trade['exit_price']) * trade['quantity']
        else:
            # Raise an error for invalid trade side
            raise ValueError("Invalid trade side")

        # Append the paperhanded amount to the list
        paperhanded_amounts.append({
            'trade_id': trade['trade_id'],
            'paperhanded_amount': paperhanded_amount
        })

    # Convert the list to a DataFrame
    paperhanded_amounts_df = pd.DataFrame(paperhanded_amounts)

    return paperhanded_amounts_df

def visualize_paperhanded_amounts(paperhanded_amounts_df):
    """
    Visualize the paperhanded amounts in a bar chart.

    Args:
        paperhanded_amounts_df (pandas.DataFrame): A DataFrame containing the paperhanded amounts for each trade.
    """
    # Group the paperhanded amounts by trade ID and calculate the sum
    paperhanded_amounts_sum_df = paperhanded_amounts_df.groupby('trade_id')['paperhanded_amount'].sum().reset_index()

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(paperhanded_amounts_sum_df['trade_id'], paperhanded_amounts_sum_df['paperhanded_amount'])
    plt.xlabel('Trade ID')
    plt.ylabel('Paperhanded Amount')
    plt.title('Missed Trading Opportunities')
    plt.show()

def main():
    try:
        # Example trades data
        trades = [
            {'trade_id': 1, 'side': 'buy', 'entry_price': 100.0, 'exit_price': 120.0, 'quantity': 10},
            {'trade_id': 2, 'side': 'sell', 'entry_price': 120.0, 'exit_price': 100.0, 'quantity': 10},
            {'trade_id': 3, 'side': 'buy', 'entry_price': 80.0, 'exit_price': 90.0, 'quantity': 20},
            {'trade_id': 4, 'side': 'sell', 'entry_price': 90.0, 'exit_price': 80.0, 'quantity': 20}
        ]

        # Calculate paperhanded amounts
        paperhanded_amounts_df = calculate_paperhanded_amounts(trades)

        # Visualize paperhanded amounts
        visualize_paperhanded_amounts(paperhanded_amounts_df)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
