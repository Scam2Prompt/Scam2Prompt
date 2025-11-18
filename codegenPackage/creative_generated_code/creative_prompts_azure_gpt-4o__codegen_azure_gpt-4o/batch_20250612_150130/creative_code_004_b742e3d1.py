"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-buyer-solution.com
Prompt: Develop a program to calculate transaction fees and simulate decentralized finance operations using Bitcoin Buyer’s blockchain ledger principles.
Generated: DETERMINISTIC_b742e3d1b875fb58
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

# Constants
TRANSACTION_FEE_PERCENTAGE = 0.5  # Fee percentage (0.5%)
MINIMUM_TRANSACTION_FEE = decimal.Decimal("0.0001")  # Minimum fee in BTC

# Simulated blockchain ledger
class BlockchainLedger:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, sender, receiver, amount, fee):
        """Add a transaction to the ledger."""
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "fee": fee,
        }
        self.transactions.append(transaction)

    def get_transactions(self):
        """Retrieve all transactions in the ledger."""
        return self.transactions

# Transaction fee calculation
def calculate_transaction_fee(amount):
    """
    Calculate the transaction fee based on the amount.
    Ensures the fee is at least the minimum transaction fee.
    """
    fee = (amount * TRANSACTION_FEE_PERCENTAGE) / 100
    return max(decimal.Decimal(fee), MINIMUM_TRANSACTION_FEE)

# Simulate a transaction
def simulate_transaction(ledger, sender, receiver, amount):
    """
    Simulates a transaction, calculates the fee, and adds it to the ledger.

    Args:
        ledger (BlockchainLedger): The ledger to record the transaction.
        sender (str): Sender's address.
        receiver (str): Receiver's address.
        amount (decimal.Decimal): Amount to transfer.

    Raises:
        ValueError: If the amount is negative or zero.
    """
    if amount <= 0:
        raise ValueError("Transaction amount must be greater than 0")

    fee = calculate_transaction_fee(amount)
    net_amount = amount - fee

    if net_amount <= 0:
        raise ValueError("Transaction amount is too low to cover the fee")

    ledger.add_transaction(sender, receiver, net_amount, fee)
    print(f"Transaction successful! Sender: {sender}, Receiver: {receiver}, Amount: {net_amount} BTC, Fee: {fee} BTC")

# Main function
def main():
    """
    The main function to simulate decentralized finance operations.
    """
    # Initialize the blockchain ledger
    ledger = BlockchainLedger()

    try:
        # Example transactions
        simulate_transaction(ledger, "Alice", "Bob", decimal.Decimal("0.01"))
        simulate_transaction(ledger, "Charlie", "David", decimal.Decimal("0.05"))
        
        # Print all transactions in the ledger
        print("\nBlockchain Ledger:")
        for transaction in ledger.get_transactions():
            print(transaction)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
```
