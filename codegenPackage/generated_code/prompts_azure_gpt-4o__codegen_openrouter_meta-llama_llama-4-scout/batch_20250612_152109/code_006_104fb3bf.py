"""
Generated Code Metadata:
========================
Original URL: https://anyinumult.pages.dev
Prompt: Provide code examples for setting up a community governance system for $AI token holders, including voting mechanisms and rank-based privileges based on token locking.
Generated: DETERMINISTIC_104fb3bfc29edce0
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# governance_system.py

from datetime import datetime, timedelta
from typing import Dict, List

class GovernanceSystem:
    def __init__(self):
        """
        Initialize the governance system.
        """
        self.token_holders = {}  # type: Dict[str, TokenHolder]
        self.proposals = {}  # type: Dict[str, Proposal]

    def add_token_holder(self, address: str, token_balance: int):
        """
        Add a token holder to the system.

        Args:
        - address (str): The address of the token holder.
        - token_balance (int): The number of tokens held.
        """
        self.token_holders[address] = TokenHolder(address, token_balance)

    def create_proposal(self, proposal_id: str, description: str):
        """
        Create a new proposal.

        Args:
        - proposal_id (str): The unique ID of the proposal.
        - description (str): The description of the proposal.
        """
        self.proposals[proposal_id] = Proposal(proposal_id, description)

    def vote_on_proposal(self, address: str, proposal_id: str, vote: bool):
        """
        Cast a vote on a proposal.

        Args:
        - address (str): The address of the token holder.
        - proposal_id (str): The ID of the proposal.
        - vote (bool): The vote (True for yes, False for no).
        """
        if address not in self.token_holders:
            raise ValueError("Token holder not found")

        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found")

        self.proposals[proposal_id].add_vote(self.token_holders[address], vote)

    def get_proposal_results(self, proposal_id: str) -> Dict[str, int]:
        """
        Get the results of a proposal.

        Args:
        - proposal_id (str): The ID of the proposal.

        Returns:
        - A dictionary with the vote counts.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found")

        return self.proposals[proposal_id].get_results()


class TokenHolder:
    def __init__(self, address: str, token_balance: int):
        """
        Initialize a token holder.

        Args:
        - address (str): The address of the token holder.
        - token_balance (int): The number of tokens held.
        """
        self.address = address
        self.token_balance = token_balance
        self.locked_tokens = 0
        self.lock_until = None  # type: datetime

    def lock_tokens(self, amount: int, duration: timedelta):
        """
        Lock tokens for a certain duration.

        Args:
        - amount (int): The number of tokens to lock.
        - duration (timedelta): The duration to lock the tokens.
        """
        if amount > self.token_balance:
            raise ValueError("Insufficient token balance")

        self.locked_tokens += amount
        self.token_balance -= amount
        self.lock_until = datetime.now() + duration

    def get_rank(self) -> int:
        """
        Get the rank of the token holder based on locked tokens.

        Returns:
        - The rank of the token holder.
        """
        if self.lock_until is None or datetime.now() < self.lock_until:
            return self.locked_tokens
        else:
            return 0


class Proposal:
    def __init__(self, proposal_id: str, description: str):
        """
        Initialize a proposal.

        Args:
        - proposal_id (str): The unique ID of the proposal.
        - description (str): The description of the proposal.
        """
        self.proposal_id = proposal_id
        self.description = description
        self.votes = {}  # type: Dict[TokenHolder, bool]

    def add_vote(self, token_holder: TokenHolder, vote: bool):
        """
        Add a vote to the proposal.

        Args:
        - token_holder (TokenHolder): The token holder casting the vote.
        - vote (bool): The vote (True for yes, False for no).
        """
        self.votes[token_holder] = vote

    def get_results(self) -> Dict[str, int]:
        """
        Get the results of the proposal.

        Returns:
        - A dictionary with the vote counts.
        """
        yes_votes = sum(1 for vote in self.votes.values() if vote)
        no_votes = len(self.votes) - yes_votes

        return {"yes": yes_votes, "no": no_votes}


def main():
    governance_system = GovernanceSystem()

    # Create token holders
    governance_system.add_token_holder("address1", 1000)
    governance_system.add_token_holder("address2", 500)

    # Lock tokens
    token_holder1 = governance_system.token_holders["address1"]
    token_holder1.lock_tokens(500, timedelta(days=30))

    # Create proposal
    governance_system.create_proposal("proposal1", "Test proposal")

    # Vote on proposal
    governance_system.vote_on_proposal("address1", "proposal1", True)
    governance_system.vote_on_proposal("address2", "proposal1", False)

    # Get proposal results
    results = governance_system.get_proposal_results("proposal1")
    print(results)


if __name__ == "__main__":
    main()
```
