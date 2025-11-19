"""
Generated Code Metadata:
========================
Original URL: https://kayenferno.pages.dev
Prompt: Generate code to calculate points earned from multiple DEX transactions per day, including swaps and wraps, as described in KAYEN League.
Generated: DETERMINISTIC_688cef85916f414c
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class TransactionType(str, Enum):
    """Transaction type enum"""
    SWAP = "swap"
    WRAP = "wrap"

@dataclass
class Transaction:
    """Transaction data class"""
    transaction_type: TransactionType
    amount: float
    timestamp: datetime

def calculate_points(transactions: List[Transaction]) -> Dict[datetime.date, float]:
    """
    Calculate points earned from multiple DEX transactions per day.

    :param transactions: List of transactions
    :return: Dictionary with date as key and points as value
    """
    points_per_day: Dict[datetime.date, float] = {}

    for transaction in transactions:
        # KAYEN League points calculation formula (example)
        if transaction.transaction_type == TransactionType.SWAP:
            points = transaction.amount * 0.1
        elif transaction.transaction_type == TransactionType.WRAP:
            points = transaction.amount * 0.05

        date = transaction.timestamp.date()

        if date in points_per_day:
            points_per_day[date] += points
        else:
            points_per_day[date] = points

    return points_per_day

def main():
    try:
        # Example transactions
        transactions: List[Transaction] = [
            Transaction(TransactionType.SWAP, 100.0, datetime(2024, 9, 16, 10, 0, 0)),
            Transaction(TransactionType.WRAP, 50.0, datetime(2024, 9, 16, 12, 0, 0)),
            Transaction(TransactionType.SWAP, 200.0, datetime(2024, 9, 17, 10, 0, 0)),
        ]

        points_per_day = calculate_points(transactions)

        for date, points in points_per_day.items():
            print(f"Date: {date}, Points: {points}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
