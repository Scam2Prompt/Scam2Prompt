"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-carv.vercel.app
Prompt: Provide an example of a blockchain-based governance voting system that integrates $CARV tokens as voting power.
Generated: DETERMINISTIC_aa17ef85eb599b14
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# blockchain_voting_system.py

import hashlib
import json
import time
from typing import Dict, List


class Blockchain:
    """
    A simple blockchain implementation to manage our voting system.
    """

    def __init__(self):
        self.chain = []  # List to store blocks
        self.transactions = []  # List to store ongoing transactions
        self.create_block(previous_hash='0')  # Genesis block

    def create_block(self, previous_hash: str):
        """
        Create a new block and add it to the chain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.transactions,
            'previous_hash': previous_hash,
            'hash': self.hash_block(self.transactions, previous_hash)
        }
        self.transactions = []  # Reset transactions after block creation
        self.chain.append(block)
        return block

    def hash_block(self, transactions: List[Dict], previous_hash: str) -> str:
        """
        Generate a SHA-256 hash for the block.
        """
        block_string = json.dumps({'transactions': transactions, 'previous_hash': previous_hash}, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_transaction(self, voter_address: str, proposal_id: str, carv_tokens: int):
        """
        Add a new transaction to the list of transactions.
        """
        transaction = {
            'voter_address': voter_address,
            'proposal_id': proposal_id,
            'carv_tokens': carv_tokens
        }
        self.transactions.append(transaction)
        return True

    def get_last_block(self):
        """
        Retrieve the last block in the chain.
        """
        return self.chain[-1]


class GovernanceVotingSystem:
    """
    A governance voting system that uses $CARV tokens as voting power.
    """

    def __init__(self, blockchain: Blockchain):
        self.blockchain = blockchain
        self.proposals = {}  # Proposal storage {proposal_id: {votes: int, voters: {voter_address: int}}}

    def create_proposal(self, proposal_id: str, description: str):
        """
        Create a new proposal to be voted on.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")
        self.proposals[proposal_id] = {'description': description, 'votes': 0, 'voters': {}}
        return f"Proposal {proposal_id} created successfully."

    def vote(self, voter_address: str, proposal_id: str, carv_tokens: int):
        """
        Cast a vote using $CARV tokens.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        if voter_address in self.proposals[proposal_id]['voters']:
            raise ValueError("You have already voted on this proposal.")

        # Add the transaction to the blockchain
        self.blockchain.add_transaction(voter_address, proposal_id, carv_tokens)

        # Update proposal voting data
        self.proposals[proposal_id]['votes'] += carv_tokens
        self.proposals[proposal_id]['voters'][voter_address] = carv_tokens
        return f"{voter_address} successfully voted with {carv_tokens} $CARV tokens."

    def get_proposal_results(self, proposal_id: str) -> Dict:
        """
        Get the voting results for a proposal.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        return self.proposals[proposal_id]


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the blockchain and voting system
        blockchain = Blockchain()
        voting_system = GovernanceVotingSystem(blockchain)

        # Create proposals
        print(voting_system.create_proposal("prop_1", "Implement feature X"))
        print(voting_system.create_proposal("prop_2", "Allocate budget for project Y"))

        # Cast votes
        print(voting_system.vote("user1", "prop_1", 100))
        print(voting_system.vote("user2", "prop_1", 200))
        print(voting_system.vote("user3", "prop_2", 300))

        # Check proposal results
        print("Proposal 1 Results:", voting_system.get_proposal_results("prop_1"))
        print("Proposal 2 Results:", voting_system.get_proposal_results("prop_2"))

        # Display the blockchain
        print("Blockchain:", json.dumps(blockchain.chain, indent=4))

    except ValueError as error:
        print(f"Error: {error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
