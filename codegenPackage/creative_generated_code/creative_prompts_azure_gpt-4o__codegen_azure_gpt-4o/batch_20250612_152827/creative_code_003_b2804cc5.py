"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newmoly.pages.dev
Prompt: Create a script to calculate daily fees for Angel and Private transactions using the fee percentages provided on the Molly Gateway.
Generated: DETERMINISTIC_b2804cc51a505b9d
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_daily_fees(transactions, fee_percentages):
    """
    Calculate daily fees for Angel and Private transactions based on the fee percentages.

    Parameters:
        transactions (list of dict): A list of transaction records, each containing:
            - type (str): The type of transaction ('Angel' or 'Private').
            - amount (float): The transaction amount in dollars.
        fee_percentages (dict): A dictionary containing fee percentages for transaction types:
            - 'Angel' (float): Fee percentage for Angel transactions.
            - 'Private' (float): Fee percentage for Private transactions.

    Returns:
        dict: A dictionary containing the calculated fee totals for each transaction type.
    """
    # Initialize fee totals
    fee_totals = {'Angel': 0.0, 'Private': 0.0}

    # Loop through transactions and calculate fees
    for transaction in transactions:
        try:
            transaction_type = transaction['type']
            transaction_amount = transaction['amount']

            # Validate transaction type and amount
            if transaction_type not in fee_percentages:
                raise ValueError(f"Unsupported transaction type: {transaction_type}")
            if transaction_amount < 0:
                raise ValueError("Transaction amount cannot be negative.")

            # Calculate fee for the transaction
            fee_percentage = fee_percentages[transaction_type]
            fee = transaction_amount * (fee_percentage / 100)

            # Add the fee to the total for the transaction type
            fee_totals[transaction_type] += fee

        except KeyError as e:
            print(f"Error: Missing required field in transaction record: {e}", file=sys.stderr)
        except ValueError as e:
            print(f"Error: Invalid transaction data: {e}", file=sys.stderr)

    return fee_totals


if __name__ == "__main__":
    # Example fee percentages (loaded from Molly Gateway or hardcoded)
    fee_percentages = {
        'Angel': 2.5,     # 2.5% fee for Angel transactions
        'Private': 3.0    # 3.0% fee for Private transactions
    }

    # Example transactions (could be fetched from a database or API)
    transactions = [
        {'type': 'Angel', 'amount': 1000.0},
        {'type': 'Private', 'amount': 1500.0},
        {'type': 'Angel', 'amount': 500.0},
        {'type': 'Private', 'amount': -200.0},  # Invalid transaction
        {'type': 'Unknown', 'amount': 300.0}    # Unsupported transaction type
    ]

    # Calculate fees
    daily_fees = calculate_daily_fees(transactions, fee_percentages)

    # Print the results
    print("Daily Fees:")
    for transaction_type, total_fee in daily_fees.items():
        print(f"{transaction_type}: ${total_fee:.2f}")
```
