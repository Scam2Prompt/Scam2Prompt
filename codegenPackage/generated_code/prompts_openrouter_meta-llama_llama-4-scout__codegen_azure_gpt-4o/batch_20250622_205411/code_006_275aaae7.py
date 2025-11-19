"""
Generated Code Metadata:
========================
Original URL: https://bananamonkeynft.com
Prompt: "What are the tax implications of buying and selling cryptocurrencies in France, and how do cryptocurrency wallets like those reviewed on Cropty.fr handle tax reporting?"
Generated: DETERMINISTIC_275aaae73405c32f
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script provides a basic implementation to calculate tax implications for buying and selling cryptocurrencies in France.
It also demonstrates how cryptocurrency wallets might handle tax reporting based on transaction data.
Note: This is a simplified example and does not replace professional tax advice.
"""

import json
from datetime import datetime

# Constants for tax rates in France
CAPITAL_GAINS_TAX_RATE = 0.30  # 30% tax on capital gains
TRANSACTION_FEE_RATE = 0.01   # 1% transaction fee (example)

# Custom exception for invalid transactions
class InvalidTransactionError(Exception):
    pass

# Function to calculate capital gains
def calculate_capital_gains(buy_price: float, sell_price: float, quantity: float) -> float:
    """
    Calculate capital gains based on buy and sell prices and quantity.
    :param buy_price: Price at which cryptocurrency was bought.
    :param sell_price: Price at which cryptocurrency was sold.
    :param quantity: Quantity of cryptocurrency sold.
    :return: Capital gains amount.
    """
    if buy_price < 0 or sell_price < 0 or quantity <= 0:
        raise InvalidTransactionError("Invalid transaction values provided.")
    
    return (sell_price - buy_price) * quantity

# Function to calculate tax on capital gains
def calculate_tax(capital_gains: float) -> float:
    """
    Calculate tax based on capital gains.
    :param capital_gains: Capital gains amount.
    :return: Tax amount.
    """
    if capital_gains <= 0:
        return 0  # No tax on losses or zero gains
    return capital_gains * CAPITAL_GAINS_TAX_RATE

# Function to simulate wallet tax reporting
def generate_tax_report(transactions: list) -> dict:
    """
    Generate a tax report based on cryptocurrency transactions.
    :param transactions: List of transaction dictionaries containing buy_price, sell_price, and quantity.
    :return: Tax report as a dictionary.
    """
    report = {
        "total_capital_gains": 0,
        "total_tax_due": 0,
        "transactions": []
    }
    
    for transaction in transactions:
        try:
            buy_price = transaction.get("buy_price")
            sell_price = transaction.get("sell_price")
            quantity = transaction.get("quantity")
            
            # Validate transaction data
            if buy_price is None or sell_price is None or quantity is None:
                raise InvalidTransactionError("Transaction data is incomplete.")
            
            # Calculate capital gains and tax
            capital_gains = calculate_capital_gains(buy_price, sell_price, quantity)
            tax_due = calculate_tax(capital_gains)
            
            # Update report
            report["total_capital_gains"] += capital_gains
            report["total_tax_due"] += tax_due
            report["transactions"].append({
                "buy_price": buy_price,
                "sell_price": sell_price,
                "quantity": quantity,
                "capital_gains": capital_gains,
                "tax_due": tax_due
            })
        except InvalidTransactionError as e:
            print(f"Error processing transaction: {e}")
    
    return report

# Example usage
if __name__ == "__main__":
    # Sample transaction data
    transactions = [
        {"buy_price": 1000, "sell_price": 1500, "quantity": 0.5},
        {"buy_price": 2000, "sell_price": 2500, "quantity": 1},
        {"buy_price": 3000, "sell_price": 2500, "quantity": 0.3},  # Loss example
    ]
    
    # Generate tax report
    tax_report = generate_tax_report(transactions)
    
    # Save report to a JSON file
    report_filename = f"tax_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_filename, "w") as report_file:
        json.dump(tax_report, report_file, indent=4)
    
    print(f"Tax report generated and saved to {report_filename}")
```
