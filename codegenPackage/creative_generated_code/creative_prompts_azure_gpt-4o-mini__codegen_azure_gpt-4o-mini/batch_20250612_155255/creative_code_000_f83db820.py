"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfi.pages.dev
Prompt: Generate a code snippet that simulates the governance voting process for non-transferable tokens in a DeFi project like WorldLibertyFi.
Generated: DETERMINISTIC_f83db820c914002c
Batch ID: 20250612_155255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional

class NonTransferableToken:
    def __init__(self, token_id: str):
        """
        Initialize a non-transferable token with a unique ID.
        :param token_id: Unique identifier for the token
        """
        self.token_id = token_id
        self.votes = 0

class GovernanceVote:
    def __init__(self):
        """
        Initialize the governance voting system.
        """
        self.proposals: Dict[str, List[NonTransferableToken]] = {}
        self.votes: Dict[str, int] = {}

    def create_proposal(self, proposal_id: str):
        """
        Create a new proposal for voting.
        :param proposal_id: Unique identifier for the proposal
        """
        if proposal_id in self.proposals:
            raise ValueError(f"Proposal {proposal_id} already exists.")
        self.proposals[proposal_id] = []
        self.votes[proposal_id] = 0

    def issue_token(self, proposal_id: str, token: NonTransferableToken):
        """
        Issue a non-transferable token for a specific proposal.
        :param proposal_id: The proposal to which the token is issued
        :param token: The non-transferable token to be issued
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal {proposal_id} does not exist.")
        self.proposals[proposal_id].append(token)

    def vote(self, proposal_id: str, token: NonTransferableToken):
        """
        Vote on a proposal using a non-transferable token.
        :param proposal_id: The proposal to vote on
        :param token: The non-transferable token used for voting
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal {proposal_id} does not exist.")
        if token not in self.proposals[proposal_id]:
            raise ValueError("Token is not valid for this proposal.")

        self.votes[proposal_id] += 1
        print(f"Vote registered for proposal {proposal_id}. Total votes: {self.votes[proposal_id]}")

    def get_vote_count(self, proposal_id: str) -> Optional[int]:
        """
        Get the total vote count for a proposal.
        :param proposal_id: The proposal ID to check
        :return: Total number of votes, or None if the proposal does not exist
        """
        return self.votes.get(proposal_id, None)

# Example usage
if __name__ == "__main__":
    governance = GovernanceVote()

    # Create a proposal
    governance.create_proposal("proposal_1")

    # Issue tokens for the proposal
    token1 = NonTransferableToken("token_1")
    token2 = NonTransferableToken("token_2")
    governance.issue_token("proposal_1", token1)
    governance.issue_token("proposal_1", token2)

    # Vote using the tokens
    governance.vote("proposal_1", token1)
    governance.vote("proposal_1", token2)

    # Retrieve the vote count
    print(f"Total votes for proposal_1: {governance.get_vote_count('proposal_1')}")
```
