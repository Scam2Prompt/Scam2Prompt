"""
Generated Code Metadata:
========================
Original URL: https://dao1.shop
Prompt: Explain the role of a digital wallet in sending, receiving, and storing assets on DAO1.
Generated: DETERMINISTIC_1f9881a3e9c04f58
Batch ID: 20250622_212139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Wallet Class for DAO1

This class represents a digital wallet that allows users to send, receive, and store assets
on the DAO1 platform. It includes methods for transaction handling, balance management, and
error handling to ensure a robust implementation.
"""

class DigitalWallet:
    def __init__(self, owner):
        """
        Initializes a new digital wallet for the specified owner.

        :param owner: The name of the wallet owner
        """
        self.owner = owner
        self.balance = 0.0  # Initial balance is set to zero
        self.transactions = []  # List to store transaction history

    def deposit(self, amount):
        """
        Deposits a specified amount into the wallet.

        :param amount: The amount to deposit
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the wallet.

        :param amount: The amount to withdraw
        :raises ValueError: If the amount is negative or exceeds the balance
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        print(f"{amount} withdrawn. New balance: {self.balance}")

    def send(self, recipient_wallet, amount):
        """
        Sends a specified amount to another wallet.

        :param recipient_wallet: The wallet to send the amount to
        :param amount: The amount to send
        :raises ValueError: If the amount is negative or exceeds the balance
        """
        if amount < 0:
            raise ValueError("Send amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance to send.")
        
        self.withdraw(amount)  # Withdraw from current wallet
        recipient_wallet.deposit(amount)  # Deposit into recipient wallet
        self.transactions.append(f"Sent: {amount} to {recipient_wallet.owner}")
        print(f"Sent {amount} to {recipient_wallet.owner}. New balance: {self.balance}")

    def receive(self, amount):
        """
        Receives a specified amount into the wallet.

        :param amount: The amount to receive
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Receive amount must be positive.")
        
        self.deposit(amount)  # Deposit into current wallet
        self.transactions.append(f"Received: {amount}")
        print(f"Received {amount}. New balance: {self.balance}")

    def get_balance(self):
        """
        Returns the current balance of the wallet.

        :return: The current balance
        """
        return self.balance

    def get_transaction_history(self):
        """
        Returns the transaction history of the wallet.

        :return: A list of transactions
        """
        return self.transactions

# Example usage
if __name__ == "__main__":
    # Create two digital wallets
    wallet1 = DigitalWallet("Alice")
    wallet2 = DigitalWallet("Bob")

    # Perform transactions
    try:
        wallet1.deposit(100)
        wallet1.send(wallet2, 50)
        wallet2.receive(50)
        print(f"Alice's balance: {wallet1.get_balance()}")
        print(f"Bob's balance: {wallet2.get_balance()}")
        print("Transaction History:", wallet1.get_transaction_history())
    except ValueError as e:
        print(f"Error: {e}")
```
