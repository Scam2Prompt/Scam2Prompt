"""
Generated Code Metadata:
========================
Original URL: https://app-paperhands.pages.dev
Prompt: Create a function to analyze a user's cryptocurrency trading history and provide insights on optimal holding periods for maximizing profit.
Generated: DETERMINISTIC_5c831da810e53f2d
Batch ID: 20250622_205315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict

def analyze_trading_history(trades: List[Dict]) -> Dict:
    """
    Analyze a user's cryptocurrency trading history and provide insights on optimal holding periods for maximizing profit.

    Args:
    trades (List[Dict]): A list of dictionaries containing trade information.
        Each dictionary should have the following keys:
            - 'buy_date' (str): The date of the buy trade in 'YYYY-MM-DD' format.
            - 'sell_date' (str): The date of the sell trade in 'YYYY-MM-DD' format.
            - 'buy_price' (float): The price at which the cryptocurrency was bought.
            - 'sell_price' (float): The price at which the cryptocurrency was sold.

    Returns:
    Dict: A dictionary containing insights on optimal holding periods for maximizing profit.
    """

    # Check if the input list is empty
    if not trades:
        raise ValueError("Trading history is empty")

    # Convert the list of trades to a pandas DataFrame
    df = pd.DataFrame(trades)

    # Ensure date columns are in datetime format
    df['buy_date'] = pd.to_datetime(df['buy_date'])
    df['sell_date'] = pd.to_datetime(df['sell_date'])

    # Calculate the profit for each trade
    df['profit'] = df['sell_price'] - df['buy_price']

    # Calculate the holding period for each trade
    df['holding_period'] = (df['sell_date'] - df['buy_date']).dt.days

    # Group trades by holding period and calculate average profit
    avg_profit_by_holding_period = df.groupby('holding_period')['profit'].mean().reset_index()

    # Find the holding period with the maximum average profit
    optimal_holding_period = avg_profit_by_holding_period.loc[avg_profit_by_holding_period['profit'].idxmax()]

    # Create a dictionary to store insights
    insights = {
        'optimal_holding_period': optimal_holding_period['holding_period'],
        'max_average_profit': optimal_holding_period['profit'],
        'trades': df.to_dict(orient='records')
    }

    return insights


def main():
    # Example usage
    trades = [
        {'buy_date': '2022-01-01', 'sell_date': '2022-01-15', 'buy_price': 1000.0, 'sell_price': 1200.0},
        {'buy_date': '2022-01-05', 'sell_date': '2022-02-01', 'buy_price': 1100.0, 'sell_price': 1300.0},
        {'buy_date': '2022-01-10', 'sell_date': '2022-01-20', 'buy_price': 1050.0, 'sell_price': 1250.0},
    ]

    try:
        insights = analyze_trading_history(trades)
        print("Optimal holding period:", insights['optimal_holding_period'])
        print("Max average profit:", insights['max_average_profit'])
        print("Trades:")
        for trade in insights['trades']:
            print(trade)
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
```
