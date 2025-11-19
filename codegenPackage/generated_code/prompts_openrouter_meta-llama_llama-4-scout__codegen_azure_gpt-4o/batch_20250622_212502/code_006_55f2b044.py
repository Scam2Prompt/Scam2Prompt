"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Describe how Polkadot's governance model enables token holders to participate in decision-making, and propose a code implementation for on-chain governance.
Generated: DETERMINISTIC_55f2b044ec60b27d
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Polkadot Governance Model Implementation
This Python script demonstrates a simplified on-chain governance model inspired by Polkadot's governance system.
Token holders can propose changes, vote on proposals, and execute approved decisions.
"""

from typing import Dict, List
import time

class Governance:
    def __init__(self):
        # Initialize governance system with empty proposals and token holders
        self.proposals: Dict[int, Dict] = {}  # Proposal ID mapped to proposal details
        self.token_holders: Dict[str, int] = {}  # Token holder address mapped to token balance
        self.proposal_id_counter: int = 0  # Unique ID for proposals

    def register_token_holder(self, address: str, balance: int):
        """
        Register a token holder with their address and token balance.
        """
        if balance <= 0:
            raise ValueError("Token balance must be greater than zero.")
        self.token_holders[address] = balance

    def create_proposal(self, proposer: str, description: str, duration: int):
        """
        Create a new proposal for governance voting.
        :param proposer: Address of the proposer
        :param description: Description of the proposal
        :param duration: Voting duration in seconds
        """
        if proposer not in self.token_holders:
            raise ValueError("Proposer must be a registered token holder.")
        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")

        self.proposal_id_counter += 1
        proposal_id = self.proposal_id_counter
        self.proposals[proposal_id] = {
            "description": description,
            "proposer": proposer,
            "votes": {"yes": 0, "no": 0},
            "end_time": time.time() + duration,
            "executed": False
        }
        print(f"Proposal {proposal_id} created: {description}")

    def vote(self, voter: str, proposal_id: int, vote: str):
        """
        Cast a vote on a proposal.
        :param voter: Address of the voter
        :param proposal_id: ID of the proposal to vote on
        :param vote: 'yes' or 'no'
        """
        if voter not in self.token_holders:
            raise ValueError("Voter must be a registered token holder.")
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")
        if vote not in ["yes", "no"]:
            raise ValueError("Vote must be 'yes' or 'no'.")

        proposal = self.proposals[proposal_id]
        if time.time() > proposal["end_time"]:
            raise ValueError("Voting period has ended for this proposal.")

        # Add voter's token balance to the chosen vote
        proposal["votes"][vote] += self.token_holders[voter]
        print(f"{voter} voted '{vote}' on proposal {proposal_id}.")

    def execute_proposal(self, proposal_id: int):
        """
        Execute a proposal if it is approved.
        :param proposal_id: ID of the proposal to execute
        """
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID.")

        proposal = self.proposals[proposal_id]
        if time.time() <= proposal["end_time"]:
            raise ValueError("Voting period is still ongoing.")
        if proposal["executed"]:
            raise ValueError("Proposal has already been executed.")

        # Determine the outcome based on votes
        if proposal["votes"]["yes"] > proposal["votes"]["no"]:
            print(f"Proposal {proposal_id} approved and executed: {proposal['description']}")
        else:
            print(f"Proposal {proposal_id} rejected: {proposal['description']}")

        proposal["executed"] = True

# Example usage
if __name__ == "__main__":
    governance = Governance()

    # Register token holders
    governance.register_token_holder("Alice", 100)
    governance.register_token_holder("Bob", 50)

    # Create a proposal
    governance.create_proposal("Alice", "Increase block size", duration=10)

    # Cast votes
    governance.vote("Alice", 1, "yes")
    governance.vote("Bob", 1, "no")

    # Wait for voting period to end
    time.sleep(11)

    # Execute the proposal
    governance.execute_proposal(1)
```
