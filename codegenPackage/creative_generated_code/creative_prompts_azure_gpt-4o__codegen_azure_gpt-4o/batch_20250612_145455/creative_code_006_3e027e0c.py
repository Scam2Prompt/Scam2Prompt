"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-sophon.xyz
Prompt: Provide code for a blockchain-based voting system that could be used to rank user-generated content on an entertainment platform like Sophon.
Generated: DETERMINISTIC_3e027e0cb388b4a0
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
import json
import time


class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with a genesis block and an empty list of pending votes.
        """
        self.chain = []  # List to store validated blocks
        self.pending_votes = []  # Queue to store votes before they are added to a block
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the first block in the blockchain (genesis block).
        """
        genesis_block = {
            'index': 0,
            'timestamp': time.time(),
            'votes': [],
            'previous_hash': '0',
            'nonce': 0
        }
        genesis_block['hash'] = self.compute_hash(genesis_block)
        self.chain.append(genesis_block)

    def get_last_block(self):
        """
        Return the last block in the chain.
        """
        return self.chain[-1]

    def compute_hash(self, block):
        """
        Compute the SHA-256 hash of a block.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def proof_of_work(self, block, difficulty=4):
        """
        Simple PoW algorithm to find a hash with a specified number of leading zeros.
        """
        block['nonce'] = 0
        computed_hash = self.compute_hash(block)
        while not computed_hash.startswith('0' * difficulty):
            block['nonce'] += 1
            computed_hash = self.compute_hash(block)
        return computed_hash

    def add_block(self, block, proof):
        """
        Add a validated block to the blockchain.
        """
        last_block = self.get_last_block()
        if last_block['hash'] != block['previous_hash']:
            raise ValueError("Previous hash does not match!")

        if not proof.startswith('0' * 4):
            raise ValueError("Invalid proof of work!")

        if proof != self.compute_hash(block):
            raise ValueError("Proof does not match computed hash!")

        self.chain.append(block)

    def add_vote(self, user_id, content_id, vote_type):
        """
        Add a vote to the list of pending votes.
        """
        if vote_type not in ('upvote', 'downvote'):
            raise ValueError("Vote type must be 'upvote' or 'downvote'!")

        vote = {
            'user_id': user_id,
            'content_id': content_id,
            'vote_type': vote_type,
            'timestamp': time.time()
        }
        self.pending_votes.append(vote)

    def mine_block(self):
        """
        Mine a new block containing pending votes.
        """
        if not self.pending_votes:
            raise ValueError("No votes to mine!")

        block = {
            'index': len(self.chain),
            'timestamp': time.time(),
            'votes': self.pending_votes,
            'previous_hash': self.get_last_block()['hash'],
        }
        # Perform proof of work
        proof = self.proof_of_work(block)
        # Add block to the chain
        self.add_block(block, proof)
        # Reset pending votes
        self.pending_votes = []


# Example Usage
if __name__ == "__main__":
    blockchain = Blockchain()

    # Add votes
    blockchain.add_vote(user_id="user1", content_id="content123", vote_type="upvote")
    blockchain.add_vote(user_id="user2", content_id="content123", vote_type="downvote")
    blockchain.add_vote(user_id="user3", content_id="content456", vote_type="upvote")

    # Mine the pending votes into a block
    try:
        blockchain.mine_block()
        print("Block mined successfully!")
    except ValueError as e:
        print(f"Error: {e}")

    # Print the blockchain
    print(json.dumps(blockchain.chain, indent=4))
```
