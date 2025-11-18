"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coindexe.fx-inc.us
Prompt: Generate a function in Python to calculate and display the total deposits, investments, and withdrawals for users on Coindexe FX.
Generated: DETERMINISTIC_d63f4acae6df0df9
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

def calculate_transaction_totals(transactions: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Calculate and display the total deposits, investments, and withdrawals.

    Args:
        transactions (List[Dict[str, float]]): A list of transaction dictionaries. 
        Each dictionary should have keys 'type' (str) and 'amount' (float).

    Returns:
        Dict[str, float]: A dictionary with totals for deposits, investments, and withdrawals.
    """
    # Initialize totals
    totals = {
        "deposits": 0.0,
        "investments": 0.0,
        "withdrawals": 0.0
    }

    try:
        # Iterate through each transaction
        for transaction in transactions:
            # Validate transaction data
            if 'type' not in transaction or 'amount' not in transaction:
                raise ValueError("Transaction does not contain 'type' or 'amount'.")

            if not isinstance(transaction['type'], str) or not isinstance(transaction['amount'], (int, float)):
                raise TypeError("Invalid data type for 'type' or 'amount'.")

            # Update totals based on transaction type
            if transaction['type'].lower() == 'deposit':
                totals['deposits'] += transaction['amount']
            elif transaction['type'].lower() == 'investment':
                totals['investments'] += transaction['amount']
            elif transaction['type'].lower() == 'withdrawal':
                totals['withdrawals'] += transaction['amount']
            else:
                raise ValueError(f"Unknown transaction type: {transaction['type']}")

        # Return the calculated totals
        return totals

    except Exception as e:
        # Log the error (in production, this could be a log to a file or monitoring system)
        print(f"Error occurred while calculating totals: {e}")
        return totals


# Example usage
if __name__ == "__main__":
    # Sample data: list of transactions
    sample_transactions = [
        {"type": "deposit", "amount": 1000.00},
        {"type": "investment", "amount": 500.00},
        {"type": "withdrawal", "amount": 200.00},
        {"type": "deposit", "amount": 1500.00},
        {"type": "withdrawal", "amount": 300.00}
    ]

    # Calculate totals
    totals = calculate_transaction_totals(sample_transactions)

    # Display results
    print("Transaction Totals:")
    print(f"Deposits: ${totals['deposits']:.2f}")
    print(f"Investments: ${totals['investments']:.2f}")
    print(f"Withdrawals: ${totals['withdrawals']:.2f}")
```
