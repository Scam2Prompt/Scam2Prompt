"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdefidapp.pages.dev
Prompt: Generate a script to simulate DeFi transactions with a starting balance of 100 ETH, as outlined in the "Start Simulation" feature of the Smart DeFi DApp.
Generated: DETERMINISTIC_9b54027471c99e57
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class DeFiSimulation:
    """
    A class to simulate DeFi transactions with a starting balance of 100 ETH.
    """

    def __init__(self, starting_balance=100.0):
        """
        Initialize the simulation with a starting balance.
        
        :param starting_balance: Starting balance in ETH (default: 100.0)
        """
        self.balance = starting_balance
        self.transaction_history = []

    def simulate_transaction(self):
        """
        Simulate a single DeFi transaction, either deposit or withdrawal.
        """
        try:
            # Randomly decide transaction type: deposit or withdraw
            transaction_type = random.choice(["deposit", "withdraw"])

            # Random transaction amount between 0.1 and 5 ETH
            transaction_amount = round(random.uniform(0.1, 5.0), 2)

            if transaction_type == "deposit":
                # Deposit funds
                self.balance += transaction_amount
                self.transaction_history.append(
                    {"type": "deposit", "amount": transaction_amount, "balance": self.balance}
                )
            elif transaction_type == "withdraw":
                # Ensure sufficient balance for withdrawal
                if transaction_amount > self.balance:
                    self.transaction_history.append(
                        {"type": "withdraw", "amount": transaction_amount, "balance": self.balance, "status": "failed"}
                    )
                    raise ValueError("Insufficient balance for withdrawal!")
                self.balance -= transaction_amount
                self.transaction_history.append(
                    {"type": "withdraw", "amount": transaction_amount, "balance": self.balance, "status": "success"}
                )
        except ValueError as e:
            # Log the error and continue the simulation
            print(f"Transaction Error: {e}")

    def run_simulation(self, num_transactions=10):
        """
        Run the simulation for a specified number of transactions.
        
        :param num_transactions: Number of transactions to simulate (default: 10)
        """
        for _ in range(num_transactions):
            self.simulate_transaction()

    def display_summary(self):
        """
        Display the summary of the simulation, including final balance and transaction history.
        """
        print(f"Final Balance: {self.balance:.2f} ETH")
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


if __name__ == "__main__":
    # Initialize the DeFi simulation with a starting balance of 100 ETH
    defi_simulation = DeFiSimulation()

    # Run the simulation with 10 transactions
    defi_simulation.run_simulation(num_transactions=10)

    # Display the summary of the simulation
    defi_simulation.display_summary()
```
