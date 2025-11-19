"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-extra.fi
Prompt: Describe the governance mechanisms in Extra Finance and how token holders can influence platform features.
Generated: DETERMINISTIC_2d48a7d40e4dfb51
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation of the requested functionality:

```python
"""
Extra Finance Governance Mechanisms

This script simulates governance mechanisms in Extra Finance. It outlines how token holders
can influence platform features via voting on proposals.
"""

class Proposal:
    """
    Represents a governance proposal in the platform.

    Attributes:
        id (int): Unique identifier for the proposal.
        description (str): Description of the proposal.
        votes_for (int): Number of votes in favor of the proposal.
        votes_against (int): Number of votes against the proposal.
        passed (bool): Whether the proposal has passed.
    """
    def __init__(self, proposal_id, description):
        self.id = proposal_id
        self.description = description
        self.votes_for = 0
        self.votes_against = 0
        self.passed = False

    def vote(self, token_holder, in_favor=True):
        """
        Allows a token holder to vote on the proposal.

        Args:
            token_holder (TokenHolder): The token holder casting the vote.
            in_favor (bool): Whether the vote is in favor (True) or against (False).
        """
        if token_holder.tokens > 0:
            if in_favor:
                self.votes_for += token_holder.tokens
            else:
                self.votes_against += token_holder.tokens
        else:
            raise ValueError("Token holder does not have enough tokens to vote.")

    def tally_votes(self):
        """
        Determines the outcome of the proposal based on votes.

        Updates the `passed` attribute to reflect the proposal's result.
        """
        self.passed = self.votes_for > self.votes_against


class TokenHolder:
    """
    Represents a token holder in Extra Finance.

    Attributes:
        address (str): Unique identifier for the token holder (e.g., wallet address).
        tokens (int): Number of governance tokens the token holder owns.
    """
    def __init__(self, address, tokens):
        self.address = address
        self.tokens = tokens


class ExtraFinanceGovernance:
    """
    Manages the governance mechanism of Extra Finance.

    Attributes:
        proposals (dict): A dictionary of active proposals.
    """
    def __init__(self):
        self.proposals = {}

    def create_proposal(self, description):
        """
        Creates a new proposal for governance voting.

        Args:
            description (str): Description of the proposal.

        Returns:
            Proposal: The created proposal object.
        """
        proposal_id = len(self.proposals) + 1
        new_proposal = Proposal(proposal_id, description)
        self.proposals[proposal_id] = new_proposal
        return new_proposal

    def list_proposals(self):
        """
        Lists all active proposals.

        Returns:
            list: A list of active proposals.
        """
        return list(self.proposals.values())

    def finalize_proposal(self, proposal_id):
        """
        Finalizes the voting for a proposal and determines its outcome.

        Args:
            proposal_id (int): The ID of the proposal to finalize.

        Returns:
            bool: Whether the proposal passed or failed.
        """
        proposal = self.proposals.get(proposal_id)
        if not proposal:
            raise KeyError(f"Proposal ID {proposal_id} not found.")
        proposal.tally_votes()
        return proposal.passed


# Example Usage:
if __name__ == '__main__':
    governance = ExtraFinanceGovernance()

    # Create token holders
    alice = TokenHolder(address="Alice", tokens=10)
    bob = TokenHolder(address="Bob", tokens=5)

    # Create a proposal
    proposal = governance.create_proposal("Add new staking feature.")

    # Token holders vote
    proposal.vote(alice, in_favor=True)
    proposal.vote(bob, in_favor=False)

    # Finalize proposal voting
    result = governance.finalize_proposal(proposal.id)
    print(f"Proposal '{proposal.description}' {'passed' if result else 'failed'}.")

    # List all proposals
    print("Active proposals:")
    for p in governance.list_proposals():
        print(f"ID: {p.id}, Description: {p.description}, Votes For: {p.votes_for}, Votes Against: {p.votes_against}, Passed: {p.passed}")
```

This code simulates governance mechanisms in Extra Finance, allowing token holders to vote on proposals to influence platform features. It includes error handling, follows Python best practices, and is well-documented.
