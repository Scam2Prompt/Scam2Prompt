"""
Generated Code Metadata:
========================
Original URL: https://bitdegree.pages.dev
Prompt: Create a code snippet that simulates signing up for Blockpit, earning the 5,000 Bits bonus, and tracking transactions to accumulate additional Bits rewards.
Generated: DETERMINISTIC_814e79671e58cae1
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockpit_simulator.py

class BlockpitUser:
    """Simulates a Blockpit user."""

    def __init__(self, username, email):
        """
        Initializes a Blockpit user.

        Args:
            username (str): The user's chosen username.
            email (str): The user's email address.
        """
        self.username = username
        self.email = email
        self.bits_balance = 0  # Initial bits balance
        self.transactions = []  # List to track transactions

    def sign_up(self):
        """Simulates signing up for Blockpit and earns the 5,000 Bits bonus."""
        try:
            # Simulate sign-up process
            print(f"User '{self.username}' signed up successfully.")
            # Earn 5,000 Bits bonus
            self.bits_balance += 5000
            print("Earned 5,000 Bits bonus.")
        except Exception as e:
            print(f"Error during sign-up: {str(e)}")

    def track_transaction(self, amount):
        """
        Simulates tracking a transaction and earns additional Bits rewards.

        Args:
            amount (float): The transaction amount.

        Note:
            For simplicity, assume 1% of transaction amount is earned as Bits.
        """
        try:
            if amount <= 0:
                raise ValueError("Transaction amount must be positive.")
            # Simulate tracking transaction
            self.transactions.append(amount)
            # Earn Bits reward (1% of transaction amount)
            bits_reward = int(amount * 0.01)
            self.bits_balance += bits_reward
            print(f"Tracked transaction of {amount}. Earned {bits_reward} Bits.")
        except Exception as e:
            print(f"Error tracking transaction: {str(e)}")

    def get_bits_balance(self):
        """Returns the current Bits balance."""
        return self.bits_balance

    def get_transaction_history(self):
        """Returns the transaction history."""
        return self.transactions


def main():
    # Example usage
    user = BlockpitUser("example_user", "user@example.com")
    user.sign_up()
    print(f"Initial Bits balance: {user.get_bits_balance()}")

    # Track some transactions
    transactions = [100, 200, 50, 75]
    for amount in transactions:
        user.track_transaction(amount)

    print(f"Updated Bits balance: {user.get_bits_balance()}")
    print("Transaction history:")
    for i, amount in enumerate(user.get_transaction_history()):
        print(f"{i+1}. {amount}")


if __name__ == "__main__":
    main()
```
