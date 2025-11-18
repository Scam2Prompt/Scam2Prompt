"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website2-70z.pages.dev
Prompt: Generate code to simulate a blockchain-based voting system for transparent decision-making, inspired by the values of Innodapter ApS.
Generated: DETERMINISTIC_3f54f71efbd95b17
Batch ID: 20250612_150226
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
import time


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains a list of votes, a timestamp, a previous hash, and a unique hash.
    """

    def __init__(self, index, previous_hash, votes):
        """
        Initializes a block with the given parameters.

        :param index: Index of the block in the chain
        :param previous_hash: Hash of the previous block in the chain
        :param votes: List of votes recorded in this block
        """
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.votes = votes
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the hash of the block using its attributes.

        :return: A string representing the hash of the block
        """
        block_data = {
            'index': self.index,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'votes': self.votes
        }
        block_string = json.dumps(block_data, sort_keys=True).encode('utf-8')
        return hashlib.sha256(block_string).hexdigest()


class Blockchain:
    """
    Represents a blockchain that stores blocks securely.
    """

    def __init__(self):
        """
        Initializes the blockchain with a genesis block.
        """
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates the initial block in the blockchain (genesis block).
        """
        genesis_block = Block(0, "0", [])
        self.chain.append(genesis_block)

    def get_latest_block(self):
        """
        Retrieves the latest block in the chain.

        :return: The latest block
        """
        return self.chain[-1]

    def add_block(self, votes):
        """
        Adds a new block to the blockchain.

        :param votes: List of votes to be included in the block
        """
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, votes)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the integrity of the blockchain.

        :return: True if the blockchain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate hash of the current block
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate previous hash linkage
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


class VotingSystem:
    """
    Represents the voting system that utilizes a blockchain for transparency.
    """

    def __init__(self):
        """
        Initializes the voting system with an empty blockchain.
        """
        self.blockchain = Blockchain()

    def cast_vote(self, voter_id, candidate):
        """
        Casts a vote for a candidate and adds it to the blockchain.

        :param voter_id: Unique ID of the voter
        :param candidate: Name of the candidate being voted for
        """
        vote = {
            'voter_id': voter_id,
            'candidate': candidate,
            'timestamp': time.time()
        }
        self.blockchain.add_block([vote])

    def display_chain(self):
        """
        Displays the blockchain in a readable format.
        """
        for block in self.blockchain.chain:
            print(json.dumps({
                'index': block.index,
                'timestamp': block.timestamp,
                'previous_hash': block.previous_hash,
                'hash': block.hash,
                'votes': block.votes
            }, indent=4))


# Example usage
if __name__ == "__main__":
    voting_system = VotingSystem()

    # Cast some votes
    voting_system.cast_vote("voter_1", "Candidate_A")
    voting_system.cast_vote("voter_2", "Candidate_B")
    voting_system.cast_vote("voter_3", "Candidate_A")

    # Display the blockchain
    voting_system.display_chain()

    # Validate the blockchain
    if voting_system.blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")
```
