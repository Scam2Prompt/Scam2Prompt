"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdstarfx.com
Prompt: Develop a Python program to analyze the profitability of trading with raw spreads and $5 commission per lot, as described for the "ECN" account type on S D STAR FX LTD.
Generated: DETERMINISTIC_3cca0376ce5191cc
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

def read_trading_data(file_path):
    """
    Reads trading data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing trading data.

    Returns:
        list[dict[str, float]]: List of dictionaries with trading data.
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            trading_data = []
            for row in reader:
                trading_data.append({
                    'trade_id': row['trade_id'],
                    'spread': float(row['spread']),
                    'lot_size': float(row['lot_size']),
                    'profit_or_loss': float(row['profit_or_loss'])
                })
            return trading_data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return []
    except ValueError:
        print("Error: Invalid data format in the file.")
        return []


def calculate_commission(lot_size):
    """
    Calculates the commission cost based on lot size.

    Args:
        lot_size (float): The size of the trade in lots.

    Returns:
        float: Commission cost for the trade.
    """
    return lot_size * 5  # $5 commission per lot


def analyze_profitability(trading_data):
    """
    Analyzes the profitability of trades, factoring in raw spread and commission.

    Args:
        trading_data (list[dict[str, float]]): List of dictionaries with trading data.

    Returns:
        dict[str, float]: Summary of profitability analysis.
    """
    total_profit_or_loss = 0
    total_commission = 0
    total_spread_cost = 0

    for trade in trading_data:
        # Calculate commission cost
        commission = calculate_commission(trade['lot_size'])
        total_commission += commission

        # Calculate spread cost (spread is given in pips, assuming 1 pip = $1 per lot)
        spread_cost = trade['spread'] * trade['lot_size']
        total_spread_cost += spread_cost

        # Adjust profit/loss after factoring commission and spread costs
        adjusted_profit_or_loss = trade['profit_or_loss'] - commission - spread_cost
        total_profit_or_loss += adjusted_profit_or_loss

    return {
        'total_profit_or_loss': total_profit_or_loss,
        'total_commission': total_commission,
        'total_spread_cost': total_spread_cost
    }


def main():
    """
    Main function to execute profitability analysis.
    """
    # Specify the path to the CSV file containing trading data
    file_path = 'trading_data.csv'

    # Read trading data from the file
    trading_data = read_trading_data(file_path)

    if not trading_data:
        print("No trading data to analyze.")
        return

    # Perform profitability analysis
    result = analyze_profitability(trading_data)

    # Display results
    print("Profitability Analysis Results:")
    print(f"Total Profit or Loss (after commission and spread): ${result['total_profit_or_loss']:.2f}")
    print(f"Total Commission Cost: ${result['total_commission']:.2f}")
    print(f"Total Spread Cost: ${result['total_spread_cost']:.2f}")


if __name__ == '__main__':
    main()
```
