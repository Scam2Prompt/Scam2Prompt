"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-buyer-solution.com
Prompt: How does Bitcoin Buyer ensure transparency and security in its decentralized finance ecosystem?
Generated: DETERMINISTIC_2f5a084dc8070e28
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from typing import List, Dict, Any

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.transaction_id = self.create_transaction_id()

    def create_transaction_id(self) -> str:
        """
        Generates a unique transaction ID using the SHA-256 hash of the transaction details.
        """
        transaction_str = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(transaction_str).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain: List[Dict[str, Any]] = []
        self.current_transactions: List[Transaction] = []
        self.create_block(previous_hash='1')  # Creating the genesis block

    def create_block(self, nonce: int = 0, previous_hash: str = None) -> Dict[str, Any]:
        """
        Creates a new block in the blockchain and adds it to the chain.
        :param nonce: The proof of work.
        :param previous_hash: The hash of the previous block.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'transactions': [tx.__dict__ for tx in self.current_transactions],
            'nonce': nonce,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []  # Reset the current transactions
        self.chain.append(block)
        return block

    def new_transaction(self, sender: str, recipient: str, amount: float) -> str:
        """
        Creates a new transaction to go into the next mined block.
        :param sender: Address of the sender.
        :param recipient: Address of the recipient.
        :param amount: Amount of Bitcoin to be transferred.
        :return: The transaction ID of the new transaction.
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)
        return transaction.transaction_id

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        """
        Creates a SHA-256 hash of a block.
        :param block: Block to hash.
        :return: The hash of the block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def print_chain(self):
        """
        Prints the entire blockchain for transparency.
        """
        for block in self.chain:
            print(json.dumps(block, indent=4))

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the blockchain
        bitcoin_chain = Blockchain()

        # Creating transactions
        tx1_id = bitcoin_chain.new_transaction("Alice", "Bob", 1.0)
        tx2_id = bitcoin_chain.new_transaction("Bob", "Charlie", 0.5)

        # Mine a new block
        bitcoin_chain.create_block(nonce=12345)

        # Print the blockchain
        bitcoin_chain.print_chain()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
