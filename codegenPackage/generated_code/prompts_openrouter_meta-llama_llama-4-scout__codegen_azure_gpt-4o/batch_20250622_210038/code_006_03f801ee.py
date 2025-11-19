"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Explain how a cashless medium like the Crypto N' Kafe token can promote fair trade and low inflation in the African coffee supply chain.
Generated: DETERMINISTIC_03f801ee3552efbf
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how a cashless medium like the Crypto N' Kafe token can promote fair trade 
and low inflation in the African coffee supply chain. The code simulates transactions between 
farmers, distributors, and consumers using blockchain-based tokens. It ensures transparency, 
fair pricing, and reduced reliance on volatile fiat currencies.
"""

import hashlib
import time
from typing import List, Dict

class Blockchain:
    """
    A simple blockchain implementation to simulate Crypto N' Kafe token transactions.
    """

    def __init__(self):
        self.chain = []  # List to store the blockchain
        self.pending_transactions = []  # List to store transactions waiting to be added to the blockchain
        self.create_block(previous_hash="0")  # Create the genesis block

    def create_block(self, previous_hash: str) -> Dict:
        """
        Creates a new block and adds it to the blockchain.
        :param previous_hash: Hash of the previous block in the chain.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'hash': self.hash_block(self.pending_transactions, previous_hash)
        }
        self.pending_transactions = []  # Reset pending transactions
        self.chain.append(block)
        return block

    @staticmethod
    def hash_block(transactions: List[Dict], previous_hash: str) -> str:
        """
        Generates a hash for a block using its transactions and previous hash.
        :param transactions: List of transactions in the block.
        :param previous_hash: Hash of the previous block.
        :return: The hash of the block.
        """
        block_string = f"{transactions}{previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_transaction(self, sender: str, receiver: str, amount: float, description: str) -> None:
        """
        Adds a new transaction to the list of pending transactions.
        :param sender: Address of the sender.
        :param receiver: Address of the receiver.
        :param amount: Amount of tokens to transfer.
        :param description: Description of the transaction (e.g., payment for coffee beans).
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'description': description,
            'timestamp': time.time()
        }
        self.pending_transactions.append(transaction)

    def get_chain(self) -> List[Dict]:
        """
        Returns the current blockchain.
        :return: List of blocks in the blockchain.
        """
        return self.chain

    def validate_chain(self) -> bool:
        """
        Validates the integrity of the blockchain.
        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the current block is valid
            if current_block['hash'] != self.hash_block(current_block['transactions'], current_block['previous_hash']):
                return False

            # Check if the previous hash matches the hash of the previous block
            if current_block['previous_hash'] != previous_block['hash']:
                return False

        return True


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    crypto_n_kafe = Blockchain()

    # Simulate transactions in the coffee supply chain
    try:
        crypto_n_kafe.add_transaction(sender="Farmer_A", receiver="Distributor_B", amount=100, description="Payment for coffee beans")
        crypto_n_kafe.add_transaction(sender="Distributor_B", receiver="Consumer_C", amount=150, description="Payment for roasted coffee")

        # Create a new block to add the transactions to the blockchain
        crypto_n_kafe.create_block(previous_hash=crypto_n_kafe.chain[-1]['hash'])

        # Display the blockchain
        print("Blockchain:")
        for block in crypto_n_kafe.get_chain():
            print(block)

        # Validate the blockchain
        is_valid = crypto_n_kafe.validate_chain()
        print(f"Is blockchain valid? {is_valid}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
