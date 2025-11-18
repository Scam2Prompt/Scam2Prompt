"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.tax
Prompt: Develop a Python script that tracks Polymarket trading losses and offsets them against capital gains, ensuring compliance with IRS rules as explained on the PolyTax website.
Generated: DETERMINISTIC_8bbd0f412f5b718a
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime
from typing import List, Dict

# Define a class to track trades
class Trade:
    def __init__(self, date: str, trade_type: str, amount: float, price: float):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.trade_type = trade_type  # 'buy' or 'sell'
        self.amount = amount
        self.price = price
        self.total_value = amount * price
    
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} - {self.trade_type.capitalize()} {self.amount} @ ${self.price} = ${self.total_value}"

# Function to read trades from a CSV file
def read_trades_from_csv(file_path: str) -> List[Trade]:
    trades = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                trades.append(Trade(date=row['date'], trade_type=row['type'], amount=float(row['amount']), price=float(row['price'])))
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return trades

# Function to calculate net capital gains/losses
def calculate_net_gains(trades: List[Trade]) -> Dict[str, float]:
    total_gains = 0.0
    total_losses = 0.0

    for trade in trades:
        if trade.trade_type == 'sell':
            total_gains += trade.total_value
        elif trade.trade_type == 'buy':
            total_losses += trade.total_value

    return {
        'net_gains': total_gains,
        'net_losses': total_losses,
        'net_profit': total_gains - total_losses
    }

# Main function to execute the script
def main():
    # Path to the CSV file containing trades
    file_path = 'trades.csv'

    trades = read_trades_from_csv(file_path)
    
    if not trades:  # Check if trades were read successfully
        print("No trades to process.")
        return
    
    net_results = calculate_net_gains(trades)

    print(f"Net Gains: ${net_results['net_gains']:.2f}")
    print(f"Net Losses: ${net_results['net_losses']:.2f}")
    print(f"Net Profit: ${net_results['net_profit']:.2f}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `trades.csv` file format matches the expected structure with columns: `date`, `type`, `amount`, and `price`.
