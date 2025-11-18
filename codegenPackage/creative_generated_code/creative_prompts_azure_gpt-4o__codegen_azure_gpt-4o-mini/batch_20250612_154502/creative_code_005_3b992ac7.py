"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradefirmcapital.com
Prompt: Develop a Python program to calculate total deposits, withdrawals, and user statistics for an investment platform, referencing the financial statistics section of Tradefirm Capital's website.
Generated: DETERMINISTIC_3b992ac784d3854a
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class InvestmentPlatform:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction_type: str, amount: float) -> None:
        """
        Adds a transaction to the platform.

        :param transaction_type: Type of transaction ('deposit' or 'withdrawal').
        :param amount: Amount of the transaction.
        :raises ValueError: If the transaction type is invalid or amount is negative.
        """
        if transaction_type not in ['deposit', 'withdrawal']:
            raise ValueError("Transaction type must be 'deposit' or 'withdrawal'.")
        if amount < 0:
            raise ValueError("Transaction amount must be non-negative.")
        
        self.transactions.append({
            'type': transaction_type,
            'amount': amount
        })

    def calculate_totals(self) -> Dict[str, float]:
        """
        Calculates total deposits and withdrawals.

        :return: A dictionary with totals for deposits and withdrawals.
        """
        total_deposits = sum(t['amount'] for t in self.transactions if t['type'] == 'deposit')
        total_withdrawals = sum(t['amount'] for t in self.transactions if t['type'] == 'withdrawal')

        return {
            'total_deposits': total_deposits,
            'total_withdrawals': total_withdrawals
        }

    def user_statistics(self) -> Dict[str, Any]:
        """
        Provides statistics about the user's transactions.

        :return: A dictionary containing the total deposits, withdrawals, and net balance.
        """
        totals = self.calculate_totals()
        net_balance = totals['total_deposits'] - totals['total_withdrawals']

        return {
            'total_deposits': totals['total_deposits'],
            'total_withdrawals': totals['total_withdrawals'],
            'net_balance': net_balance
        }

def main():
    # Initialize the investment platform
    platform = InvestmentPlatform()

    # Simulated transactions (In a real application, this could come from a database or external API)
    transactions = [
        ('deposit', 1000.00),
        ('withdrawal', 250.00),
        ('deposit', 500.00),
        ('withdrawal', 100.00),
        ('deposit', 200.00)
    ]

    # Add transactions to the platform
    for transaction in transactions:
        try:
            platform.add_transaction(transaction[0], transaction[1])
        except ValueError as e:
            print(f"Error adding transaction: {e}")

    # Generate user statistics
    stats = platform.user_statistics()

    # Output the statistics
    print(json.dumps(stats, indent=4))

if __name__ == "__main__":
    main()
```
