"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://projectdeksa.pages.dev
Prompt: Create a blockchain-based voting system for the DEKSA community to decide on future virtual kingdom features, using $MASA tokens as voting power.
Generated: DETERMINISTIC_cab762088661671e
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
import time

class BlockchainVotingSystem:
    def __init__(self):
        """
        Initialize the blockchain voting system with an empty chain and a set of pending votes.
        """
        self.chain = []  # Blockchain to store blocks
        self.pending_votes = []  # Votes waiting to be added to the chain
        self.create_genesis_block()  # Create the first block in the chain

    def create_genesis_block(self):
        """
        Create the genesis block. This is the first block of the blockchain.
        """
        genesis_block = {
            'index': 0,
            'timestamp': time.time(),
            'votes': [],
            'previous_hash': "0",
            'nonce': 0
        }
        genesis_block['hash'] = self.calculate_hash(genesis_block)
        self.chain.append(genesis_block)

    def calculate_hash(self, block):
        """
        Calculate the hash of a block using its contents.
        """
        block_string = f"{block['index']}{block['timestamp']}{block['votes']}{block['previous_hash']}{block['nonce']}"
        return sha256(block_string.encode()).hexdigest()

    def add_vote(self, voter_id, feature, token_amount):
        """
        Add a vote to the list of pending votes.
        """
        if token_amount <= 0:
            raise ValueError("Token amount must be greater than zero.")
        vote = {
            'voter_id': voter_id,
            'feature': feature,
            'token_amount': token_amount
        }
        self.pending_votes.append(vote)

    def proof_of_work(self, block):
        """
        Simple proof-of-work algorithm to calculate a valid nonce.
        """
        block['nonce'] = 0
        computed_hash = self.calculate_hash(block)
        while not computed_hash.startswith('0000'):  # Difficulty is defined as hash starting with '0000'
            block['nonce'] += 1
            computed_hash = self.calculate_hash(block)
        return computed_hash

    def create_new_block(self):
        """
        Create a new block with the pending votes and add it to the blockchain.
        """
        if not self.pending_votes:
            raise ValueError("No votes to add to the blockchain.")
        previous_block = self.chain[-1]
        new_block = {
            'index': len(self.chain),
            'timestamp': time.time(),
            'votes': self.pending_votes,
            'previous_hash': previous_block['hash'],
            'nonce': 0
        }
        new_block['hash'] = self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.pending_votes = []  # Clear pending votes after block creation

    def get_voting_results(self):
        """
        Calculate the voting results by tallying token amounts for each feature.
        """
        results = {}
        for block in self.chain:
            for vote in block['votes']:
                feature = vote['feature']
                token_amount = vote['token_amount']
                if feature not in results:
                    results[feature] = 0
                results[feature] += token_amount
        return results

    def validate_chain(self):
        """
        Validate the integrity of the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            # Validate hash
            if current_block['hash'] != self.calculate_hash(current_block):
                return False
            # Validate previous hash
            if current_block['previous_hash'] != previous_block['hash']:
                return False
        return True


# Example usage
if __name__ == "__main__":
    voting_system = BlockchainVotingSystem()

    # Adding votes
    try:
        voting_system.add_vote("user1", "feature_x", 10)
        voting_system.add_vote("user2", "feature_y", 20)
        voting_system.add_vote("user3", "feature_x", 15)
    except ValueError as e:
        print(f"Error adding vote: {e}")

    # Create a new block
    try:
        voting_system.create_new_block()
    except ValueError as e:
        print(f"Error creating new block: {e}")

    # Display voting results
    results = voting_system.get_voting_results()
    print("Voting Results:", results)

    # Validate the blockchain
    is_valid = voting_system.validate_chain()
    print("Blockchain Valid:", is_valid)
```
