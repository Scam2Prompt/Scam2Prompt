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
class DexTransaction:
    """Class to represent a single DEX transaction."""

    def __init__(self, transaction_type, amount, is_successful=True):
        """
        Initialize a DEX transaction.
        
        Parameters:
            transaction_type (str): Type of the transaction ('swap' or 'wrap').
            amount (float): Amount involved in the transaction.
            is_successful (bool): Whether the transaction was successful.
        """
        self.transaction_type = transaction_type
        self.amount = amount
        self.is_successful = is_successful

    def __str__(self):
        return f"{self.transaction_type.capitalize()} of {self.amount} {'successful' if self.is_successful else 'failed'}"


class KayenLeague:
    """Class to calculate points earned from multiple DEX transactions per day."""

    def __init__(self):
        """Initialize the KayenLeague with an empty list of transactions."""
        self.transactions = []

    def add_transaction(self, transaction):
        """
        Add a transaction to the league.
        
        Parameters:
            transaction (DexTransaction): Instance of DexTransaction to add.
        """
        if not isinstance(transaction, DexTransaction):
            raise ValueError("Invalid transaction. Must be an instance of DexTransaction.")
        self.transactions.append(transaction)

    def calculate_points(self):
        """
        Calculate total points based on transactions.
        
        Returns:
            float: Total points earned.
        """
        total_points = 0.0
        
        for transaction in self.transactions:
            if transaction.is_successful:
                if transaction.transaction_type == 'swap':
                    total_points += transaction.amount * 1.0  # 1 point per swap amount
                elif transaction.transaction_type == 'wrap':
                    total_points += transaction.amount * 0.5  # 0.5 points per wrap amount

        return total_points

    def reset_transactions(self):
        """Reset the list of transactions for a new day."""
        self.transactions = []


# Example usage
if __name__ == "__main__":
    try:
        league = KayenLeague()

        # Adding transactions
        league.add_transaction(DexTransaction('swap', 100))
        league.add_transaction(DexTransaction('wrap', 200))
        league.add_transaction(DexTransaction('swap', 150, is_successful=False))  # Unsuccessful transaction

        # Calculate points
        points = league.calculate_points()
        print(f"Total points earned today: {points}")

        # Reset for a new day
        league.reset_transactions()
    except Exception as e:
        print(f"An error occurred: {e}")
```
