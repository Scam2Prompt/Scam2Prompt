"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonkeeperweb.ru
Prompt: Create a script to simulate TON transactions with world-class speed, referencing the unique architecture of The Open Network.
Generated: DETERMINISTIC_5d3cc26905493e62
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class TONTransactionSimulator:
    """
    A class to simulate TON (The Open Network) transactions with high speed and reliability.
    """
    
    def __init__(self):
        """
        Initialize the simulator with a list of sample accounts.
        """
        self.accounts = {
            "alice_ton_address": 1000.0,  # Example balances (in TON coins)
            "bob_ton_address": 500.0,
            "charlie_ton_address": 750.0,
        }
        self.transaction_log = []  # A list to log transaction details

    def simulate_transaction(self, sender: str, receiver: str, amount: float):
        """
        Simulate a transaction between sender and receiver.

        :param sender: Address of the sender
        :param receiver: Address of the receiver
        :param amount: Amount to transfer (in TON coins)
        :return: None
        """
        try:
            # Validate sender and receiver addresses
            if sender not in self.accounts or receiver not in self.accounts:
                raise ValueError("Invalid sender or receiver address.")

            # Ensure sender has sufficient balance
            if self.accounts[sender] < amount:
                raise ValueError("Insufficient balance in sender's account.")

            # Perform the transaction
            self.accounts[sender] -= amount
            self.accounts[receiver] += amount

            # Log transaction
            transaction_details = {
                "timestamp": time.time(),
                "sender": sender,
                "receiver": receiver,
                "amount": amount
            }
            self.transaction_log.append(transaction_details)

            print(f"Transaction complete: {sender} -> {receiver}, Amount: {amount} TON")

        except ValueError as e:
            print(f"Transaction failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_balances(self):
        """
        Display the current account balances.
        """
        print("\nAccount Balances:")
        for account, balance in self.accounts.items():
            print(f"{account}: {balance} TON")

    def display_transaction_log(self):
        """
        Display the log of all transactions performed.
        """
        print("\nTransaction Log:")
        for transaction in self.transaction_log:
            readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(transaction["timestamp"]))
            print(f"{readable_time} | {transaction['sender']} -> {transaction['receiver']} | Amount: {transaction['amount']} TON")


# Entrypoint for the script
if __name__ == "__main__":
    simulator = TONTransactionSimulator()

    # Display initial balances
    simulator.display_balances()

    # Simulate transactions
    simulator.simulate_transaction("alice_ton_address", "bob_ton_address", 200.0)
    simulator.simulate_transaction("bob_ton_address", "charlie_ton_address", 100.0)

    # Display updated balances
    simulator.display_balances()

    # Display transaction log
    simulator.display_transaction_log()
```
