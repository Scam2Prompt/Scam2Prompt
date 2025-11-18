"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blacksprut.shop
Prompt: Write code to simulate a cryptocurrency transaction confirmation process, including wallet deposit verification, as described in the Blacksprut ordering system.
Generated: DETERMINISTIC_3d03513298afb7d9
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class Wallet:
    def __init__(self, wallet_id, balance=0.0):
        """
        Initializes a Wallet instance with a unique wallet ID and balance.

        :param wallet_id: Unique identifier for the wallet
        :param balance: Initial balance for the wallet (default: 0.0)
        """
        self.wallet_id = wallet_id
        self.balance = balance

    def deposit(self, amount):
        """
        Adds the specified amount to the wallet's balance.

        :param amount: Amount to deposit
        :raises ValueError: If the deposit amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def get_balance(self):
        """
        Returns the wallet's current balance.

        :return: Current wallet balance
        """
        return self.balance


class Transaction:
    def __init__(self, sender_wallet, receiver_wallet, amount):
        """
        Initializes a Transaction instance.

        :param sender_wallet: Wallet sending the funds
        :param receiver_wallet: Wallet receiving the funds
        :param amount: Amount to transfer
        :raises ValueError: If the transaction amount is invalid
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        if sender_wallet.get_balance() < amount:
            raise ValueError("Insufficient funds in sender's wallet.")

        self.sender_wallet = sender_wallet
        self.receiver_wallet = receiver_wallet
        self.amount = amount
        self.confirmed = False

    def confirm_transaction(self):
        """
        Simulates transaction confirmation and updates wallet balances.

        :raises RuntimeError: If the transaction has already been confirmed
        """
        if self.confirmed:
            raise RuntimeError("Transaction has already been confirmed.")

        # Simulate transaction confirmation process
        time.sleep(random.uniform(1, 3))  # Simulating network delay
        self.sender_wallet.deposit(-self.amount)
        self.receiver_wallet.deposit(self.amount)
        self.confirmed = True


def simulate_transaction(sender_wallet, receiver_wallet, amount):
    """
    Simulates a cryptocurrency transaction between two wallets.

    :param sender_wallet: Wallet sending the funds
    :param receiver_wallet: Wallet receiving the funds
    :param amount: Amount to transfer
    """
    try:
        print(f"Initiating transaction of {amount} from Wallet {sender_wallet.wallet_id} to Wallet {receiver_wallet.wallet_id}...")
        transaction = Transaction(sender_wallet, receiver_wallet, amount)
        transaction.confirm_transaction()
        print("Transaction confirmed successfully!")
        print(f"Sender Wallet Balance: {sender_wallet.get_balance()}")
        print(f"Receiver Wallet Balance: {receiver_wallet.get_balance()}")
    except ValueError as e:
        print(f"Transaction Error: {e}")
    except RuntimeError as e:
        print(f"Transaction Error: {e}")


# Example usage
if __name__ == "__main__":
    # Create two wallets with initial balances
    wallet1 = Wallet(wallet_id="W1", balance=100.0)
    wallet2 = Wallet(wallet_id="W2", balance=50.0)

    # Simulate a transaction
    simulate_transaction(wallet1, wallet2, 30.0)
```
