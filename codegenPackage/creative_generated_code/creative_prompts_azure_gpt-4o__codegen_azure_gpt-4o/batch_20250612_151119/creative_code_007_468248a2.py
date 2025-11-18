"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bitkub.jp
Prompt: Develop a program to calculate profits and losses from cryptocurrency trades on Bitkub, incorporating the tax considerations for Thailand outlined on the Bitkub Japan website.
Generated: DETERMINISTIC_468248a29f97fef7
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Crypto Profit and Loss Calculator for Bitkub Trades
Author: [Your Name]
Date: [Today's Date]
Language: Python 3
Description: This program calculates profits and losses from cryptocurrency trades on Bitkub,
             incorporating Thai tax considerations as per Bitkub Japan website.
"""

import csv
from datetime import datetime

# Constants
TAX_RATE = 0.15  # Thailand's cryptocurrency capital gains tax rate (15%)

def read_trade_data(file_path):
    """
    Reads trade data from a CSV file.
    Each row should contain: Date, Buy/Sell, Amount, Price (per unit).
    
    :param file_path: Path to the trade data CSV file
    :return: List of trade records (dicts)
    """
    trades = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                trade = {
                    "date": datetime.strptime(row["Date"], "%Y-%m-%d"),
                    "type": row["Buy/Sell"].strip().lower(),
                    "amount": float(row["Amount"]),
                    "price": float(row["Price"])
                }
                trades.append(trade)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except KeyError:
        print("Error: Invalid CSV format. Ensure columns are 'Date', 'Buy/Sell', 'Amount', 'Price'.")
        return []
    except ValueError:
        print("Error: Invalid data type. Check that Amount and Price are numeric.")
        return []
    
    return trades


def calculate_profit_and_loss(trades):
    """
    Calculates profits and losses based on trades.
    
    :param trades: List of trade records (dicts)
    :return: Total profit/loss (float) and total tax (float)
    """
    total_profit_loss = 0.0
    total_tax = 0.0
    holdings = 0.0  # Tracks the amount of cryptocurrency held
    avg_buy_price = 0.0  # Tracks average buy price
    
    for trade in trades:
        if trade["type"] == "buy":
            # Adjust holdings and average buy price
            total_cost = holdings * avg_buy_price + trade["amount"] * trade["price"]
            holdings += trade["amount"]
            avg_buy_price = total_cost / holdings
        elif trade["type"] == "sell":
            if holdings >= trade["amount"]:
                # Calculate profit or loss for the sale
                profit_loss = trade["amount"] * (trade["price"] - avg_buy_price)
                total_profit_loss += profit_loss
                
                # Calculate tax
                if profit_loss > 0:
                    total_tax += profit_loss * TAX_RATE
                
                # Adjust holdings
                holdings -= trade["amount"]
            else:
                print("Error: Insufficient holdings for sell trade.")
        else:
            print(f"Error: Unknown trade type '{trade['type']}'. Only 'buy' and 'sell' are accepted.")
    
    return total_profit_loss, total_tax


def main():
    """
    Main entry point for the program.
    """
    print("==== Crypto Profit and Loss Calculator ====")
    
    # Prompt user for trade data file
    file_path = input("Enter the path to your trade data CSV file: ").strip()
    trades = read_trade_data(file_path)
    
    if not trades:
        print("No trade data found. Exiting.")
        return
    
    # Calculate profits and losses
    profit_loss, tax = calculate_profit_and_loss(trades)
    
    # Display results
    print(f"Total Profit/Loss: {profit_loss:.2f} THB")
    print(f"Total Tax: {tax:.2f} THB")


if __name__ == "__main__":
    main()
```
