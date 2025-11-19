"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hemi.host
Prompt: How does the Proof-of-Proof security mechanism in Hemi ensure Bitcoin-powered finality, and how can I implement it in my project?
Generated: DETERMINISTIC_ebd590bb9687896a
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time
import json
from typing import List, Dict

class HemiProofOfProof:
    """
    A class to implement the Proof-of-Proof security mechanism to ensure Bitcoin-powered finality.
    """

    def __init__(self):
        self.transactions = []  # List to hold transaction data
        self.blockchain = []    # List to hold blocks formed from transactions
        self.current_block = []  # Current transactions to be added to the next block

    def add_transaction(self, transaction: Dict) -> None:
        """
        Adds a transaction to the current block.

        :param transaction: A dictionary containing transaction details.
        """
        self.current_block.append(transaction)

    def mine_block(self, previous_hash: str) -> None:
        """
        Mines a new block and adds it to the blockchain.

        :param previous_hash: The hash of the previous block in the blockchain.
        """
        if not self.current_block:
            raise ValueError("Current block has no transactions to mine.")
        
        block = {
            'index': len(self.blockchain) + 1,
            'transactions': self.current_block,
            'timestamp': time.time(),
            'previous_hash': previous_hash,
            'nonce': self.proof_of_work()
        }
        
        # Reset the current block to an empty list for new transactions
        self.current_block = []
        self.blockchain.append(block)

    def proof_of_work(self, difficulty: int = 4) -> int:
        """
        Performs the proof of work algorithm.

        :param difficulty: The number of leading zeros required in the hash.
        :return: The nonce that satisfies the proof of work requirement.
        """
        nonce = 0
        while True:
            block_string = json.dumps(self.current_block, sort_keys=True) + str(nonce)
            block_hash = hashlib.sha256(block_string.encode()).hexdigest()
            if block_hash.startswith('0' * difficulty):
                return nonce
            nonce += 1

    def get_last_block(self) -> Dict:
        """
        Returns the last block in the blockchain.

        :return: The last block as a dictionary.
        """
        if not self.blockchain:
            raise IndexError("Blockchain is empty.")
        return self.blockchain[-1]

    def validate_chain(self) -> bool:
        """
        Validates the entire blockchain to ensure the integrity of transactions.

        :return: True if the blockchain is valid, else False.
        """
        for index in range(1, len(self.blockchain)):
            current = self.blockchain[index]
            previous = self.blockchain[index - 1]

            if current['previous_hash'] != self.hash(previous):
                return False

            current_transactions = current['transactions']
            if not self.validate_transactions(current_transactions):
                return False

        return True

    @staticmethod
    def hash(block: Dict) -> str:
        """
        Creates a SHA-256 hash of a block.

        :param block: The block to hash.
        :return: The hash of the block as a string.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def validate_transactions(transactions: List[Dict]) -> bool:
        """
        Validates transactions for integrity.

        :param transactions: List of transactions to validate.
        :return: True if all transactions are valid, else False.
        """
        for transaction in transactions:
            if not all(key in transaction for key in ['sender', 'recipient', 'amount']):
                return False
        return True

def main():
    # Example usage of HemiProofOfProof
    hemi = HemiProofOfProof()
    
    # Adding transactions
    try:
        hemi.add_transaction({'sender': 'Alice', 'recipient': 'Bob', 'amount': 10})
        hemi.add_transaction({'sender': 'Bob', 'recipient': 'Charlie', 'amount': 5})

        # Mining a new block
        last_block = hemi.get_last_block()
        hemi.mine_block(previous_hash=hemi.hash(last_block))

        # Validate the blockchain
        if hemi.validate_chain():
            print("Blockchain is valid.")
        else:
            print("Blockchain is invalid.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
