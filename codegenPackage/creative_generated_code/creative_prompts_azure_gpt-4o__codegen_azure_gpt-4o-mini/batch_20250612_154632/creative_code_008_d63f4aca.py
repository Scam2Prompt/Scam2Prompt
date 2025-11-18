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
import pandas as pd

class CoindexeFX:
    """
    A class to manage user financial transactions for Coindexe FX.
    """

    def __init__(self):
        """Initialize an empty DataFrame to store transactions."""
        self.transactions = pd.DataFrame(columns=['user_id', 'transaction_type', 'amount'])

    def add_transaction(self, user_id: str, transaction_type: str, amount: float) -> None:
        """
        Add a transaction to the record.

        Args:
            user_id (str): The ID of the user making the transaction.
            transaction_type (str): The type of transaction ('deposit', 'investment', 'withdrawal').
            amount (float): The amount of the transaction.

        Raises:
            ValueError: If transaction_type is invalid or amount is negative.
        """
        if transaction_type not in ['deposit', 'investment', 'withdrawal']:
            raise ValueError("transaction_type must be 'deposit', 'investment', or 'withdrawal'.")
        if amount < 0:
            raise ValueError("Amount must be a non-negative value.")

        # Append the new transaction to the DataFrame
        self.transactions = self.transactions.append({'user_id': user_id, 'transaction_type': transaction_type, 'amount': amount}, ignore_index=True)

    def calculate_totals(self, user_id: str) -> dict:
        """
        Calculate total deposits, investments, and withdrawals for a given user.

        Args:
            user_id (str): The ID of the user for whom to calculate totals.

        Returns:
            dict: A dictionary containing total deposits, investments, and withdrawals.

        Raises:
            ValueError: If no transactions exist for the user.
        """
        user_transactions = self.transactions[self.transactions['user_id'] == user_id]

        if user_transactions.empty:
            raise ValueError(f"No transactions found for user with ID: {user_id}")

        # Calculate totals
        total_deposit = user_transactions[user_transactions['transaction_type'] == 'deposit']['amount'].sum()
        total_investment = user_transactions[user_transactions['transaction_type'] == 'investment']['amount'].sum()
        total_withdrawal = user_transactions[user_transactions['transaction_type'] == 'withdrawal']['amount'].sum()

        return {
            'total_deposit': total_deposit,
            'total_investment': total_investment,
            'total_withdrawal': total_withdrawal
        }

    def display_totals(self, user_id: str) -> None:
        """
        Display the total deposits, investments, and withdrawals for the specified user.

        Args:
            user_id (str): The ID of the user to display totals for.
        """
        try:
            totals = self.calculate_totals(user_id)
            print(f"User ID: {user_id}")
            print(f"Total Deposits: {totals['total_deposit']:.2f}")
            print(f"Total Investments: {totals['total_investment']:.2f}")
            print(f"Total Withdrawals: {totals['total_withdrawal']:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage:
if __name__ == "__main__":
    coindexe_fx = CoindexeFX()
    
    # Adding some transactions
    coindexe_fx.add_transaction('user1', 'deposit', 500.0)
    coindexe_fx.add_transaction('user1', 'investment', 200.0)
    coindexe_fx.add_transaction('user1', 'withdrawal', 150.0)
    
    # Display totals for user1
    coindexe_fx.display_totals('user1')
```
