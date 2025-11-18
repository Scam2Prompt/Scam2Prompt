"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayenferno.pages.dev
Prompt: Generate code to calculate points earned from multiple DEX transactions per day, including swaps and wraps, as described in KAYEN League.
Generated: DETERMINISTIC_688cef85916f414c
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Transaction:
    """
    A class to represent a DEX transaction.
    Attributes:
        transaction_type (str): Type of transaction ('swap' or 'wrap').
        amount (float): Amount of tokens involved in the transaction.
        timestamp (datetime.datetime): Timestamp of the transaction.
    """
    def __init__(self, transaction_type: str, amount: float, timestamp: datetime.datetime):
        if transaction_type not in ('swap', 'wrap'):
            raise ValueError("Invalid transaction type. Must be 'swap' or 'wrap'.")
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp


class KayenLeaguePointsCalculator:
    """
    A class to calculate points earned from multiple DEX transactions per day
    according to Kayen League rules.
    """
    def __init__(self):
        # Define point rules (points per transaction type)
        self.points_per_swap = 2  # Points awarded for swap transactions
        self.points_per_wrap = 1  # Points awarded for wrap transactions

    def calculate_daily_points(self, transactions):
        """
        Calculate the total points earned for a given list of transactions within a single day.
        Arguments:
            transactions (list[Transaction]): List of transactions to calculate points for.
        Returns:
            dict: Dictionary mapping each day to total points for that day.
        """
        daily_points = {}
        
        for transaction in transactions:
            # Extract the date (without time) to group transactions by day
            transaction_date = transaction.timestamp.date()
            
            # Initialize the points for the day if not already set
            if transaction_date not in daily_points:
                daily_points[transaction_date] = 0
            
            # Add points according to the transaction type
            if transaction.transaction_type == 'swap':
                daily_points[transaction_date] += self.points_per_swap
            elif transaction.transaction_type == 'wrap':
                daily_points[transaction_date] += self.points_per_wrap

        return daily_points


# Example usage
if __name__ == "__main__":
    try:
        # Example list of transactions
        transactions = [
            Transaction('swap', 100.0, datetime.datetime(2023, 10, 1, 14, 30)),
            Transaction('wrap', 50.0, datetime.datetime(2023, 10, 1, 15, 45)),
            Transaction('swap', 200.0, datetime.datetime(2023, 10, 2, 10, 15)),
            Transaction('wrap', 120.0, datetime.datetime(2023, 10, 2, 11, 20)),
            Transaction('swap', 300.0, datetime.datetime(2023, 10, 1, 16, 50))
        ]
        
        calculator = KayenLeaguePointsCalculator()
        daily_points = calculator.calculate_daily_points(transactions)
        
        # Print daily points
        for date, points in daily_points.items():
            print(f"Date: {date}, Points Earned: {points}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
