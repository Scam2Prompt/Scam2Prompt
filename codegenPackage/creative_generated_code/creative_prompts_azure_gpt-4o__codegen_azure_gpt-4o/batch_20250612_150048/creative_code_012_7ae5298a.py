"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ifundsoption.com
Prompt: Write a script to calculate daily wins for Bitcoin and forex trades, referencing iFundsOption's claim of achieving up to 98% daily wins.
Generated: DETERMINISTIC_7ae5298a253cdfa5
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime


def calculate_daily_wins(trades_file):
    """
    Calculate daily wins for Bitcoin and Forex trades based on trade data.

    Args:
        trades_file (str): Path to the CSV file containing trade data.

    Returns:
        dict: A dictionary containing daily wins percentage for Bitcoin and Forex trades.
    """
    try:
        # Initialize containers for trade outcomes
        daily_results = {}

        # Open the CSV file containing trade data
        with open(trades_file, 'r') as file:
            reader = csv.DictReader(file)

            # Read and process each trade record
            for row in reader:
                try:
                    # Parse trade details
                    trade_date = datetime.datetime.strptime(row['date'], '%Y-%m-%d').date()
                    trade_type = row['type'].lower()  # 'bitcoin' or 'forex'
                    outcome = row['outcome'].lower()  # 'win' or 'loss'

                    # Ensure valid data
                    if trade_type not in ['bitcoin', 'forex'] or outcome not in ['win', 'loss']:
                        continue  # Skip invalid rows

                    # Initialize daily results for the date if it doesn't exist
                    if trade_date not in daily_results:
                        daily_results[trade_date] = {'bitcoin': {'wins': 0, 'total': 0},
                                                     'forex': {'wins': 0, 'total': 0}}

                    # Update daily results based on trade outcome
                    daily_results[trade_date][trade_type]['total'] += 1
                    if outcome == 'win':
                        daily_results[trade_date][trade_type]['wins'] += 1
                except Exception as sub_error:
                    # Handle errors in individual rows gracefully
                    print(f"Error processing row: {row}. Error: {sub_error}")

        # Calculate win percentages for each day and each trade type
        daily_win_percentages = {}
        for date, results in daily_results.items():
            daily_win_percentages[date] = {}
            for trade_type, stats in results.items():
                if stats['total'] > 0:
                    win_percentage = (stats['wins'] / stats['total']) * 100
                    daily_win_percentages[date][trade_type] = round(win_percentage, 2)
                else:
                    daily_win_percentages[date][trade_type] = None  # No trades for this type

        return daily_win_percentages

    except FileNotFoundError:
        print(f"Error: File '{trades_file}' not found.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}


# Example usage:
if __name__ == "__main__":
    # Path to the CSV file containing trade data
    trades_file_path = 'trades.csv'

    # Calculate daily win percentages
    result = calculate_daily_wins(trades_file_path)

    # Print results
    if result:
        print("Daily Win Percentages:")
        for date, outcome in sorted(result.items()):
            print(f"{date}: Bitcoin - {outcome['bitcoin']}%, Forex - {outcome['forex']}%")
```

### Notes on CSV Format:
The script expects a CSV file (`trades.csv`) with the following headers:
- `date`: The date of the trade in `YYYY-MM-DD` format.
- `type`: The type of trade, either `Bitcoin` or `Forex`.
- `outcome`: The outcome of the trade, either `win` or `loss`.

Example CSV content:
```csv
date,type,outcome
2023-10-01,bitcoin,win
2023-10-01,forex,loss
2023-10-01,forex,win
2023-10-02,bitcoin,win
```
