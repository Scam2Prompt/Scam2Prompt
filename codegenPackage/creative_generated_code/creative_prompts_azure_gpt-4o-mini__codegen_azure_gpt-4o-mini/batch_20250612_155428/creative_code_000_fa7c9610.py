"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonflip-presale.vercel.app
Prompt: Generate code for a decentralized exchange (DEX) using the Moon Flip AI framework.
Generated: DETERMINISTIC_fa7c9610bf183eae
Batch ID: 20250612_155428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from moon_flip import MoonFlip, Transaction, User
from moon_flip.exceptions import InsufficientFundsError, TransactionError
from decimal import Decimal

# Initialize the Moon Flip DEX class
class DecentralizedExchange:
    def __init__(self):
        """Initialize the decentralized exchange with Moon Flip framework."""
        self.moon_flip = MoonFlip()

    def create_user(self, username: str, initial_balance: Decimal) -> User:
        """Create a new user with a specified initial balance.

        Args:
            username (str): The username for the new user.
            initial_balance (Decimal): The initial balance for the user.

        Returns:
            User: The created user object.
        """
        user = self.moon_flip.create_user(username, initial_balance)
        return user

    def execute_transaction(self, user: User, amount: Decimal, token: str) -> Transaction:
        """Execute a transaction for the user.

        Args:
            user (User): The user executing the transaction.
            amount (Decimal): The amount to be transacted.
            token (str): The token type being exchanged.

        Returns:
            Transaction: The executed transaction object.
        
        Raises:
            InsufficientFundsError: If the user does not have enough funds.
            TransactionError: For any other transaction related errors.
        """
        try:
            transaction = self.moon_flip.create_transaction(user, amount, token)
            return transaction
        except InsufficientFundsError:
            print(f"Error: {user.username} has insufficient funds for this transaction.")
            raise
        except TransactionError as e:
            print(f"Transaction failed: {e}")
            raise

    def get_user_balance(self, user: User) -> Decimal:
        """Get the balance of a user.

        Args:
            user (User): The user whose balance is to be retrieved.

        Returns:
            Decimal: The user's current balance.
        """
        balance = self.moon_flip.get_balance(user)
        return balance

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the decentralized exchange
        dex = DecentralizedExchange()

        # Create a user with an initial balance of 1000
        user1 = dex.create_user('Alice', Decimal('1000.00'))

        # Check user balance
        print(f"{user1.username}'s balance: {dex.get_user_balance(user1)}")

        # Execute a transaction
        transaction = dex.execute_transaction(user1, Decimal('150.00'), 'TOKEN_A')
        print(f"Transaction successful: {transaction}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
