"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skillchain.io
Prompt: Explain how Skillchain can be utilized by gaming companies to certify player achievements using blockchain.
Generated: DETERMINISTIC_f5a11350836cdf35
Batch ID: 20250612_155538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
A Python program to demonstrate how Skillchain can be utilized
by gaming companies to certify player achievements using blockchain.

Skillchain is a blockchain-based platform for certifying skills and achievements.
This example simulates certifying player achievements in a gaming environment using Skillchain.
"""

import hashlib
import json
from datetime import datetime


class Blockchain:
    """
    A simple implementation of a blockchain to store and certify player achievements.
    """

    def __init__(self):
        self.chain = []  # Blockchain ledger
        self.current_transactions = []  # Temporary storage for transactions
        self.create_block(proof=1, previous_hash="0")  # Genesis block

    def create_block(self, proof, previous_hash):
        """
        Create a new block and add it to the blockchain.
        :param proof: The proof of work for the block.
        :param previous_hash: Hash of the previous block.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.current_transactions = []  # Reset transactions
        self.chain.append(block)
        return block

    def add_transaction(self, player_id, achievement):
        """
        Add a new transaction (player achievement) to the block.
        :param player_id: Unique identifier for the player.
        :param achievement: The achievement details to be certified.
        :return: Index of the block that will hold this transaction.
        """
        self.current_transactions.append({
            'player_id': player_id,
            'achievement': achievement,
            'timestamp': str(datetime.now())
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block.
        :param block: The block to be hashed.
        :return: The hash string.
        """
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    @property
    def last_block(self):
        """
        Returns the last block in the blockchain.
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Proof of Work algorithm to secure the blockchain.
        :param last_proof: The proof of the last block.
        :return: A new proof of work.
        """
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof by checking if it satisfies the condition.
        :param last_proof: The proof of the last block.
        :param proof: Current proof to validate.
        :return: True if valid, False otherwise.
        """
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Difficulty level

    def verify_achievement(self, player_id, achievement):
        """
        Verify if a player's achievement is certified in the blockchain.
        :param player_id: Unique identifier for the player.
        :param achievement: The achievement details to verify.
        :return: True if certified, False otherwise.
        """
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['player_id'] == player_id and transaction['achievement'] == achievement:
                    return True
        return False


# Example Usage
if __name__ == "__main__":
    # Initialize the blockchain
    skillchain = Blockchain()

    # Simulate adding player achievements
    player_id = "player123"
    achievement = "Completed Level 10"

    print("Adding player achievement to blockchain...")
    skillchain.add_transaction(player_id, achievement)

    # Mining a new block to certify the achievement
    print("Mining a new block to certify the achievement...")
    last_proof = skillchain.last_block['proof']
    new_proof = skillchain.proof_of_work(last_proof)
    previous_hash = skillchain.hash(skillchain.last_block)
    skillchain.create_block(new_proof, previous_hash)

    # Verify the achievement certification
    print("Verifying achievement certification...")
    is_certified = skillchain.verify_achievement(player_id, achievement)
    if is_certified:
        print(f"Achievement '{achievement}' for player '{player_id}' is certified!")
    else:
        print(f"Achievement '{achievement}' for player '{player_id}' is NOT certified.")
```
