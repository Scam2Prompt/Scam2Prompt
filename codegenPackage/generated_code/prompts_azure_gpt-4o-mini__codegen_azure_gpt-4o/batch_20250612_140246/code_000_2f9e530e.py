"""
Generated Code Metadata:
========================
Original URL: https://pushd-stores.web.app
Prompt: How can I implement a secure transaction system using blockchain technology for a decentralized marketplace like Pushd?
Generated: DETERMINISTIC_2f9e530e2cc46e79
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
import time
from typing import List, Dict

class Blockchain:
    """
    A simple implementation of a blockchain for secure transactions in a decentralized marketplace.
    """

    def __init__(self):
        # Initialize the blockchain with a genesis block
        self.chain: List[Dict] = []
        self.pending_transactions: List[Dict] = []
        self.create_block(previous_hash="0", proof=1)  # Genesis block

    def create_block(self, proof: int, previous_hash: str) -> Dict:
        """
        Create a new block and add it to the blockchain.

        :param proof: The proof of work for the block.
        :param previous_hash: The hash of the previous block in the chain.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.pending_transactions = []  # Reset the list of pending transactions
        self.chain.append(block)
        return block

    def add_transaction(self, sender: str, receiver: str, amount: float) -> int:
        """
        Add a new transaction to the list of pending transactions.

        :param sender: The sender's address.
        :param receiver: The receiver's address.
        :param amount: The amount to be transferred.
        :return: The index of the block that will hold this transaction.
        """
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.get_last_block()['index'] + 1

    def get_last_block(self) -> Dict:
        """
        Get the last block in the blockchain.

        :return: The last block.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof: int) -> int:
        """
        Perform the proof of work algorithm to find the next proof.

        :param previous_proof: The proof of the previous block.
        :return: The new proof.
        """
        new_proof = 1
        while True:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":  # Difficulty level: 4 leading zeros
                return new_proof
            new_proof += 1

    def hash(self, block: Dict) -> str:
        """
        Generate a SHA-256 hash of a block.

        :param block: The block to be hashed.
        :return: The hash of the block.
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self) -> bool:
        """
        Verify the integrity of the blockchain.

        :return: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the previous block matches the stored previous_hash
            if current_block['previous_hash'] != self.hash(previous_block):
                return False

            # Check if the proof of work is valid
            previous_proof = previous_block['proof']
            current_proof = current_block['proof']
            hash_operation = hashlib.sha256(str(current_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != "0000":
                return False

        return True


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    marketplace_blockchain = Blockchain()

    # Add transactions
    marketplace_blockchain.add_transaction(sender="Alice", receiver="Bob", amount=50)
    marketplace_blockchain.add_transaction(sender="Bob", receiver="Charlie", amount=30)

    # Mine a new block
    previous_proof = marketplace_blockchain.get_last_block()['proof']
    proof = marketplace_blockchain.proof_of_work(previous_proof)
    previous_hash = marketplace_blockchain.hash(marketplace_blockchain.get_last_block())
    marketplace_blockchain.create_block(proof, previous_hash)

    # Validate the blockchain
    print("Blockchain valid:", marketplace_blockchain.is_chain_valid())

    # Print the blockchain
    print(json.dumps(marketplace_blockchain.chain, indent=4))
```
