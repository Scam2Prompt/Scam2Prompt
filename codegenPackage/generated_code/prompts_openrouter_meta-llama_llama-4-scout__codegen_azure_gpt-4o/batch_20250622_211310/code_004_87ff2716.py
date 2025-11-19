"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Develop a basic understanding of tax-loss harvesting and write a Python function to calculate capital gains and losses for tax purposes.
Generated: DETERMINISTIC_87ff2716b4379523
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Module: Tax Loss Harvesting Calculator

This module provides a function to calculate capital gains and losses for tax purposes.
It takes a list of transactions (buy and sell) and computes the net capital gain or loss.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

from typing import List, Dict

def calculate_capital_gains(transactions: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Calculate capital gains and losses for tax purposes.

    Args:
        transactions (List[Dict[str, float]]): A list of transaction dictionaries.
            Each transaction should have the following keys:
            - 'type': 'buy' or 'sell' (str)
            - 'quantity': Number of shares (float)
            - 'price': Price per share (float)

    Returns:
        Dict[str, float]: A dictionary containing:
            - 'total_gain': Total capital gain (float)
            - 'total_loss': Total capital loss (float)
            - 'net_result': Net capital gain or loss (float)
    """
    # Validate input
    if not isinstance(transactions, list):
        raise ValueError("Transactions must be a list of dictionaries.")
    
    # Initialize variables
    total_gain = 0.0
    total_loss = 0.0
    remaining_shares = []  # List to track remaining shares from buy transactions

    for transaction in transactions:
        # Validate transaction structure
        if not all(key in transaction for key in ['type', 'quantity', 'price']):
            raise ValueError("Each transaction must contain 'type', 'quantity', and 'price' keys.")
        
        transaction_type = transaction['type'].lower()
        quantity = transaction['quantity']
        price = transaction['price']

        if transaction_type == 'buy':
            # Add buy transaction to remaining shares
            remaining_shares.append({'quantity': quantity, 'price': price})
        elif transaction_type == 'sell':
            # Process sell transaction
            if quantity <= 0:
                raise ValueError("Sell quantity must be greater than zero.")
            
            shares_to_sell = quantity
            while shares_to_sell > 0:
                if not remaining_shares:
                    raise ValueError("Not enough shares to sell.")
                
                # Use FIFO (First-In-First-Out) method for tax calculation
                first_buy = remaining_shares[0]
                if shares_to_sell >= first_buy['quantity']:
                    # Sell all shares from the first buy transaction
                    gain_or_loss = (price - first_buy['price']) * first_buy['quantity']
                    shares_to_sell -= first_buy['quantity']
                    remaining_shares.pop(0)
                else:
                    # Sell partial shares from the first buy transaction
                    gain_or_loss = (price - first_buy['price']) * shares_to_sell
                    first_buy['quantity'] -= shares_to_sell
                    shares_to_sell = 0
                
                # Categorize as gain or loss
                if gain_or_loss > 0:
                    total_gain += gain_or_loss
                else:
                    total_loss += abs(gain_or_loss)
        else:
            raise ValueError("Transaction type must be 'buy' or 'sell'.")
    
    # Calculate net result
    net_result = total_gain - total_loss

    return {
        'total_gain': total_gain,
        'total_loss': total_loss,
        'net_result': net_result
    }

# Example usage
if __name__ == "__main__":
    # Sample transactions
    sample_transactions = [
        {'type': 'buy', 'quantity': 100, 'price': 50.0},
        {'type': 'buy', 'quantity': 50, 'price': 55.0},
        {'type': 'sell', 'quantity': 120, 'price': 60.0},
        {'type': 'sell', 'quantity': 30, 'price': 45.0}
    ]

    # Calculate capital gains and losses
    result = calculate_capital_gains(sample_transactions)
    print("Capital Gains and Losses:")
    print(f"Total Gain: ${result['total_gain']:.2f}")
    print(f"Total Loss: ${result['total_loss']:.2f}")
    print(f"Net Result: ${result['net_result']:.2f}")
```
