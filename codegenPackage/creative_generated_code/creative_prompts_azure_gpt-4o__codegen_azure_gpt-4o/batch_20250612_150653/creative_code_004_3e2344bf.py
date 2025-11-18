"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinvest.finance.blog
Prompt: Develop a Python program that simulates the process of securely sending and receiving Bitcoin, inspired by the mission of Coinbase Invest to make crypto accessible to everyone.
Generated: DETERMINISTIC_3e2344bfc14f9914
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os
import random
import string


class BitcoinWallet:
    """
    Simulates a Bitcoin Wallet for securely sending and receiving Bitcoin.
    """

    def __init__(self):
        """
        Initializes the wallet with a unique address and balance.
        """
        self.address = self._generate_address()
        self.balance = 0.0

    def _generate_address(self):
        """
        Generates a unique Bitcoin address for the wallet.
        Returns:
            str: A simulated Bitcoin wallet address.
        """
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        return hashlib.sha256(random_string.encode()).hexdigest()

    def send_bitcoin(self, recipient_address, amount):
        """
        Sends Bitcoin to another wallet.
        Args:
            recipient_address (str): The Bitcoin address of the recipient.
            amount (float): The amount of Bitcoin to send.
        Returns:
            bool: True if the transaction is successful, False otherwise.
        """
        # Error handling: Validate recipient address and amount
        if not recipient_address or not isinstance(recipient_address, str):
            print("Invalid recipient address.")
            return False

        if amount <= 0:
            print("Amount must be greater than 0.")
            return False

        if self.balance < amount:
            print("Insufficient balance.")
            return False

        # Simulate sending Bitcoin
        self.balance -= amount
        print(f"Transaction successful! Sent {amount} BTC to {recipient_address}.")
        return True

    def receive_bitcoin(self, amount):
        """
        Receives Bitcoin into the wallet.
        Args:
            amount (float): The amount of Bitcoin to receive.
        """
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        self.balance += amount
        print(f"Received {amount} BTC. New balance: {self.balance:.8f} BTC.")

    def check_balance(self):
        """
        Checks the current balance of the wallet.
        Returns:
            float: The current balance of the wallet.
        """
        return self.balance


def simulate_bitcoin_transactions():
    """
    Simulates Bitcoin transactions between two wallets.
    """
    # Create two wallet objects
    alice_wallet = BitcoinWallet()
    bob_wallet = BitcoinWallet()

    print(f"--- Wallets Created ---")
    print(f"Alice's Address: {alice_wallet.address}")
    print(f"Bob's Address: {bob_wallet.address}\n")

    # Add initial balance to Alice's wallet
    alice_wallet.receive_bitcoin(10.0)  # Alice receives 10 BTC

    # Alice sends 3 BTC to Bob
    print("\n--- Transaction 1: Alice sends 3 BTC to Bob ---")
    if alice_wallet.send_bitcoin(bob_wallet.address, 3.0):
        bob_wallet.receive_bitcoin(3.0)

    # Check wallet balances
    print("\n--- Wallet Balances ---")
    print(f"Alice's Balance: {alice_wallet.check_balance():.8f} BTC")
    print(f"Bob's Balance: {bob_wallet.check_balance():.8f} BTC")


if __name__ == "__main__":
    """
    Entry point for the program.
    """
    try:
        simulate_bitcoin_transactions()
    except Exception as e:
        print(f"An error occurred during the simulation: {str(e)}")
```
