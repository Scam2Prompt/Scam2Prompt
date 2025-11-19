"""
Generated Code Metadata:
========================
Original URL: https://meteora-ag.github.io
Prompt: Generate a code snippet that demonstrates how to integrate sustainability initiatives into a blockchain application, inspired by Meteora Crypto's approach to minimizing carbon footprint.
Generated: DETERMINISTIC_4d93e9f6516466c6
Batch ID: 20250612_155727
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
from typing import Dict, List

class Blockchain:
    """
    A simple blockchain implementation with sustainability tracking.
    Inspired by Meteora Crypto's approach to minimizing carbon footprint.
    """

    def __init__(self):
        self.chain: List[Dict] = []  # List to store the blockchain
        self.transactions: List[Dict] = []  # List to store current transactions
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof: int, previous_hash: str) -> Dict:
        """
        Create a new block and add it to the blockchain.
        Includes sustainability metrics for carbon offset tracking.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.transactions,
            'proof': proof,
            'previous_hash': previous_hash,
            'sustainability_metrics': {
                'carbon_offset': self.calculate_carbon_offset(),  # Example metric
                'energy_usage': self.calculate_energy_usage()  # Example metric
            }
        }
        self.transactions = []  # Reset the transaction list
        self.chain.append(block)
        return block

    def calculate_carbon_offset(self) -> float:
        """
        Calculate the carbon offset for the current block.
        This is a placeholder function and should be replaced with actual logic.
        """
        # Example: Offset based on number of transactions
        return len(self.transactions) * 0.01  # Offset 0.01 units per transaction

    def calculate_energy_usage(self) -> float:
        """
        Calculate the energy usage for the current block.
        This is a placeholder function and should be replaced with actual logic.
        """
        # Example: Energy usage based on proof-of-work difficulty
        return 0.5  # Placeholder value for energy usage

    def add_transaction(self, sender: str, receiver: str, amount: float) -> int:
        """
        Add a new transaction to the list of transactions.
        """
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }
        self.transactions.append(transaction)
        return self.get_last_block()['index'] + 1

    def get_last_block(self) -> Dict:
        """
        Get the last block in the blockchain.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof: int) -> int:
        """
        Proof of Work algorithm to find the next proof.
        """
        new_proof = 1
        while True:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  # Example difficulty level
                return new_proof
            new_proof += 1

    def hash(self, block: Dict) -> str:
        """
        Generate a SHA-256 hash of a block.
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self) -> bool:
        """
        Check if the blockchain is valid.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate hash of the block
            if current_block['previous_hash'] != self.hash(previous_block):
                return False

            # Validate proof of work
            previous_proof = previous_block['proof']
            current_proof = current_block['proof']
            hash_operation = hashlib.sha256(str(current_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':  # Example difficulty level
                return False

        return True


# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()

    # Add transactions
    blockchain.add_transaction(sender="Alice", receiver="Bob", amount=10)
    blockchain.add_transaction(sender="Bob", receiver="Charlie", amount=5)

    # Mine a new block
    previous_block = blockchain.get_last_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.create_block(proof, previous_hash)

    # Print the blockchain
    print(json.dumps(blockchain.chain, indent=4))

    # Validate the blockchain
    print("Is blockchain valid?", blockchain.is_chain_valid())
```
