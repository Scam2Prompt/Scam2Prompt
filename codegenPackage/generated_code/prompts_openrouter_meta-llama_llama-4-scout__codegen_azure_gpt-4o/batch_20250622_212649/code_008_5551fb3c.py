"""
Generated Code Metadata:
========================
Original URL: https://doubleton.pages.dev
Prompt: Propose a use case for TON's on-chain governance program and suggest how to implement it.
Generated: DETERMINISTIC_5551fb3cae1e1b58
Batch ID: 20250622_212649
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Use Case: On-chain governance for a decentralized voting system on TON blockchain.
This program allows users to propose and vote on governance decisions. Votes are tallied on-chain, and the results are stored immutably.

Implementation: Smart contract written in Python using TON's Fift or FunC language. Below is a Python simulation of the logic for clarity.
"""

from typing import Dict, List

class OnChainGovernance:
    def __init__(self):
        # Initialize the governance system with empty proposals and votes
        self.proposals: Dict[int, str] = {}  # Proposal ID -> Proposal description
        self.votes: Dict[int, Dict[str, str]] = {}  # Proposal ID -> {User -> Vote}
        self.results: Dict[int, Dict[str, int]] = {}  # Proposal ID -> {Option -> Vote Count}

    def create_proposal(self, proposal_id: int, description: str) -> None:
        """
        Create a new governance proposal.
        :param proposal_id: Unique ID for the proposal.
        :param description: Description of the proposal.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")
        self.proposals[proposal_id] = description
        self.votes[proposal_id] = {}
        self.results[proposal_id] = {}
        print(f"Proposal {proposal_id} created: {description}")

    def vote(self, proposal_id: int, user: str, option: str) -> None:
        """
        Cast a vote for a proposal.
        :param proposal_id: ID of the proposal to vote on.
        :param user: User casting the vote.
        :param option: Voting option (e.g., "yes", "no").
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        if user in self.votes[proposal_id]:
            raise ValueError("User has already voted.")
        
        # Record the vote
        self.votes[proposal_id][user] = option
        if option not in self.results[proposal_id]:
            self.results[proposal_id][option] = 0
        self.results[proposal_id][option] += 1
        print(f"User {user} voted '{option}' on proposal {proposal_id}.")

    def tally_votes(self, proposal_id: int) -> Dict[str, int]:
        """
        Tally the votes for a proposal.
        :param proposal_id: ID of the proposal to tally votes for.
        :return: Dictionary of vote counts per option.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")
        return self.results[proposal_id]

    def get_proposals(self) -> List[Dict[str, str]]:
        """
        Retrieve all proposals.
        :return: List of proposals with their IDs and descriptions.
        """
        return [{"id": pid, "description": desc} for pid, desc in self.proposals.items()]


# Example usage
if __name__ == "__main__":
    governance = OnChainGovernance()

    # Create proposals
    governance.create_proposal(1, "Increase block size limit.")
    governance.create_proposal(2, "Reduce transaction fees.")

    # Users vote on proposals
    governance.vote(1, "Alice", "yes")
    governance.vote(1, "Bob", "no")
    governance.vote(2, "Alice", "yes")

    # Tally votes
    print("Proposal 1 results:", governance.tally_votes(1))
    print("Proposal 2 results:", governance.tally_votes(2))

    # List all proposals
    print("All proposals:", governance.get_proposals())
```

This Python code simulates the logic for an on-chain governance program. In a real-world TON implementation, this would be translated into a smart contract using TON's native languages like FunC or Fift.
