"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-masafinance.pages.dev
Prompt: Develop a blockchain-based solution to track and manage Masa rewards earned through wallet connections.
Generated: DETERMINISTIC_af79293de928a327
Batch ID: 20250612_153400
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
from time import time
from typing import List, Dict, Any


class Blockchain:
    """
    Blockchain class to manage Masa reward transactions.
    Each block contains Masa rewards earned, wallet connection data,
    and a hash of the previous block.
    """

    def __init__(self):
        self.chain = []  # List to store the chain (blocks)
        self.current_transactions = []  # List to store ongoing transactions
        self.create_block(previous_hash='1', proof=100)  # Create the genesis block

    def create_block(self, proof: int, previous_hash: str = None) -> Dict[str, Any]:
        """
        Create a new block in the blockchain.

        :param proof: The proof (result of Proof of Work algorithm)
        :param previous_hash: Hash of the previous block
        :return: The newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current transactions
        self.current_transactions = []

        # Add the block to the chain
        self.chain.append(block)
        return block

    def add_transaction(self, wallet_id: str, reward_amount: float) -> int:
        """
        Add a new Masa reward transaction.

        :param wallet_id: Unique identifier for the wallet
        :param reward_amount: The amount of Masa rewards earned
        :return: Index of the block that will hold this transaction
        """
        self.current_transactions.append({
            'wallet_id': wallet_id,
            'reward_amount': reward_amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        """
        Generate a SHA-256 hash of a block.

        :param block: The block to hash
        :return: The SHA-256 hash of the block
        """
        # Ensure the block dictionary is ordered to have consistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self) -> Dict[str, Any]:
        """
        Return the last block in the chain.

        :return: The last block in the blockchain
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work algorithm.

        :param last_proof: The proof of the previous block
        :return: The new proof
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validate the Proof of Work.

        :param last_proof: Previous block's proof
        :param proof: Current proof
        :return: True if valid, False otherwise
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


# Example usage:
if __name__ == "__main__":
    # Initialize the blockchain
    blockchain = Blockchain()

    # Add wallet transactions
    blockchain.add_transaction(wallet_id="wallet1", reward_amount=50)
    blockchain.add_transaction(wallet_id="wallet2", reward_amount=30)

    # Perform Proof of Work to add a new block
    last_proof = blockchain.last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Create a new block after doing Proof of Work
    previous_hash = blockchain.hash(blockchain.last_block)
    blockchain.create_block(proof, previous_hash)

    # Print the blockchain
    print(json.dumps(blockchain.chain, indent=4))
```
