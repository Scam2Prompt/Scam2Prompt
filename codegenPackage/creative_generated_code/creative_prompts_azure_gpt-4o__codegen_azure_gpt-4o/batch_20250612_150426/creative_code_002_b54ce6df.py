"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invistribe.com
Prompt: Create a script to simulate token transactions for INVISTECH (INVS) on the BSC network, including buying and selling tokens and calculating transaction fees.
Generated: DETERMINISTIC_b54ce6df5b4607d2
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from decimal import Decimal

class TokenTransactionSimulator:
    """
    A simulator for token transactions of INVISTECH (INVS) on the Binance Smart Chain (BSC) network.
    """

    def __init__(self, initial_balance=1000, transaction_fee_percent=0.1):
        """
        Initializes the simulator with an initial balance and transaction fee rate.

        :param initial_balance: The starting balance of INVS tokens (default: 1000)
        :param transaction_fee_percent: The transaction fee percentage (default: 0.1%)
        """
        self.balance = Decimal(initial_balance)
        self.transaction_fee_percent = Decimal(transaction_fee_percent)

    def calculate_transaction_fee(self, amount):
        """
        Calculates the transaction fee for a given transaction amount.

        :param amount: The amount of tokens to transact
        :return: The transaction fee
        """
        return (amount * self.transaction_fee_percent) / 100

    def buy_tokens(self, amount):
        """
        Simulates buying tokens. Adds tokens to the balance after deducting transaction fees.

        :param amount: The amount of tokens to buy
        :return: None
        :raises ValueError: If the amount is invalid
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        amount = Decimal(amount)
        fee = self.calculate_transaction_fee(amount)
        self.balance += amount - fee
        print(f"Bought {amount} INVS tokens. Fee: {fee:.6f} INVS. New Balance: {self.balance:.6f} INVS.")

    def sell_tokens(self, amount):
        """
        Simulates selling tokens. Deducts tokens from the balance after calculating transaction fees.

        :param amount: The amount of tokens to sell
        :return: None
        :raises ValueError: If the amount is invalid or exceeds the balance
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        amount = Decimal(amount)
        if amount > self.balance:
            raise ValueError("Insufficient balance for the transaction.")
        fee = self.calculate_transaction_fee(amount)
        self.balance -= amount + fee
        if self.balance < 0:
            self.balance += amount + fee  # Rollback the transaction in case of negative balance
            raise ValueError("Insufficient balance after fees for the transaction.")
        print(f"Sold {amount} INVS tokens. Fee: {fee:.6f} INVS. New Balance: {self.balance:.6f} INVS.")

    def simulate_random_transactions(self, num_transactions=10, max_amount=100):
        """
        Simulates a series of random buy and sell transactions.

        :param num_transactions: The number of transactions to simulate
        :param max_amount: The maximum amount per transaction
        :return: None
        """
        for i in range(num_transactions):
            action = random.choice(["buy", "sell"])
            amount = random.uniform(1, max_amount)
            print(f"\nTransaction {i + 1}/{num_transactions}:")
            try:
                if action == "buy":
                    self.buy_tokens(amount)
                elif action == "sell":
                    self.sell_tokens(amount)
            except ValueError as e:
                print(f"Transaction failed: {e}")

if __name__ == "__main__":
    # Configure the simulator
    simulator = TokenTransactionSimulator(initial_balance=1000, transaction_fee_percent=0.1)

    print("Starting INVISTECH (INVS) Token Transaction Simulator on BSC Network.")
    print(f"Initial Balance: {simulator.balance:.6f} INVS\n")

    # Simulate 10 random transactions
    simulator.simulate_random_transactions(num_transactions=10, max_amount=100)

    print(f"\nFinal Balance: {simulator.balance:.6f} INVS")
```
