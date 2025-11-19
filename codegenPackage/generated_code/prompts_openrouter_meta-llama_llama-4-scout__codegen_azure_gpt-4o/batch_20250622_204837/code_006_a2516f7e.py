"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: "Explain how to integrate blockchain technology into a platform for transparent, secure, and instantaneous transactions in the oil and gas industry, using the Crudo Protocol as a case study."
Generated: DETERMINISTIC_a2516f7e14898864
Batch ID: 20250622_204837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation of a blockchain integration for transparent, secure, and instantaneous transactions in the oil and gas industry using the Crudo Protocol as a case study. This code is designed to be clean, well-documented, and production-ready.

```python
import hashlib
import json
import time
from typing import List, Dict, Any


class Blockchain:
    """
    A simple implementation of a blockchain for secure and transparent transactions.
    This class represents the Crudo Protocol blockchain.
    """

    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain: List[Dict[str, Any]] = []  # List to store the chain of blocks
        self.pending_transactions: List[Dict[str, Any]] = []  # List to store transactions waiting to be added to a block
        self.create_block(proof=1, previous_hash="0")  # Create the genesis block

    def create_block(self, proof: int, previous_hash: str) -> Dict[str, Any]:
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
        self.pending_transactions = []  # Clear the list of pending transactions
        self.chain.append(block)  # Add the block to the chain
        return block

    def add_transaction(self, sender: str, receiver: str, amount: float, metadata: str) -> int:
        """
        Add a new transaction to the list of pending transactions.

        :param sender: The sender's address.
        :param receiver: The receiver's address.
        :param amount: The amount to be transferred.
        :param metadata: Additional metadata for the transaction (e.g., oil and gas details).
        :return: The index of the block that will contain this transaction.
        """
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'metadata': metadata,
            'timestamp': time.time()
        }
        self.pending_transactions.append(transaction)
        return self.get_last_block()['index'] + 1

    def get_last_block(self) -> Dict[str, Any]:
        """
        Get the last block in the blockchain.

        :return: The last block in the chain.
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
            if hash_operation[:4] == "0000":  # Check if the hash starts with four leading zeros
                return new_proof
            new_proof += 1

    def hash_block(self, block: Dict[str, Any]) -> str:
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
            if current_block['previous_hash'] != self.hash_block(previous_block):
                return False

            # Check if the proof of work is valid
            previous_proof = previous_block['proof']
            current_proof = current_block['proof']
            hash_operation = hashlib.sha256(str(current_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != "0000":
                return False

        return True


# Example usage of the Blockchain class
if __name__ == "__main__":
    # Initialize the blockchain
    crudo_blockchain = Blockchain()

    # Add transactions (e.g., oil and gas transactions)
    crudo_blockchain.add_transaction(sender="CompanyA", receiver="CompanyB", amount=1000.0, metadata="Crude Oil Shipment")
    crudo_blockchain.add_transaction(sender="CompanyC", receiver="CompanyD", amount=500.0, metadata="Natural Gas Delivery")

    # Perform proof of work and create a new block
    previous_proof = crudo_blockchain.get_last_block()['proof']
    proof = crudo_blockchain.proof_of_work(previous_proof)
    previous_hash = crudo_blockchain.hash_block(crudo_blockchain.get_last_block())
    crudo_blockchain.create_block(proof, previous_hash)

    # Print the blockchain
    print(json.dumps(crudo_blockchain.chain, indent=4))

    # Validate the blockchain
    is_valid = crudo_blockchain.is_chain_valid()
    print(f"Is the blockchain valid? {is_valid}")
```

This code provides a basic implementation of a blockchain tailored for the oil and gas industry, with features for secure transactions and validation. It can be extended further to include more advanced features like smart contracts, distributed consensus, and integration with IoT devices for real-time data tracking.
