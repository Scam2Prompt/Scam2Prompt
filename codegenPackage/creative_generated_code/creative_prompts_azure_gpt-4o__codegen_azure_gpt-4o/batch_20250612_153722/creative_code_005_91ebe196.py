"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengwu.io
Prompt: Create a voting mechanism for token holders to influence community decisions, leveraging PENGWU tokens as described in the Voting feature.
Generated: DETERMINISTIC_91ebe196da3a22dd
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: voting_mechanism.py

import json
from typing import Dict, List, Tuple
from collections import defaultdict

class VotingMechanism:
    """
    A class to create and manage a voting mechanism for PENGWU token holders.
    Token holders can vote on community decisions, and votes are weighted based on token balance.
    """

    def __init__(self):
        """
        Initializes the VotingMechanism with empty token balances and proposals.
        """
        self.token_holders: Dict[str, int] = {}  # Mapping of holder's address to token balance
        self.proposals: Dict[int, Dict[str, int]] = {}  # Proposal ID mapped to votes
        self.next_proposal_id: int = 1  # Unique ID for proposals

    def add_token_holder(self, address: str, balance: int):
        """
        Adds a token holder with a specified balance to the system.
        
        Parameters:
            address (str): The token holder's address.
            balance (int): The number of PENGWU tokens the holder owns.
        """
        if balance <= 0:
            raise ValueError("Token balance must be positive.")
        self.token_holders[address] = balance

    def create_proposal(self, description: str) -> int:
        """
        Creates a new proposal and returns its unique ID.
        
        Parameters:
            description (str): A brief description of the proposal.
        
        Returns:
            int: The unique ID of the created proposal.
        """
        proposal_id = self.next_proposal_id
        self.proposals[proposal_id] = {"description": description, "votes": defaultdict(int)}
        self.next_proposal_id += 1
        return proposal_id

    def cast_vote(self, address: str, proposal_id: int, vote: int):
        """
        Allows a token holder to cast a vote on a proposal.
        Votes are weighted based on token balance.
        
        Parameters:
            address (str): The token holder's address.
            proposal_id (int): The ID of the proposal to vote on.
            vote (int): The vote value (+1 for approval, -1 for rejection).
        
        Raises:
            KeyError: If the proposal or token holder does not exist.
            ValueError: If the vote is not valid or the holder has insufficient tokens.
        """
        if address not in self.token_holders:
            raise KeyError("Token holder does not exist.")
        if proposal_id not in self.proposals:
            raise KeyError("Proposal does not exist.")
        if vote not in [1, -1]:
            raise ValueError("Vote must be +1 (approval) or -1 (rejection).")
        
        # Weighted vote based on token balance
        vote_weight = self.token_holders[address]
        self.proposals[proposal_id]["votes"][address] = vote * vote_weight

    def tally_votes(self, proposal_id: int) -> Tuple[int, int, str]:
        """
        Tallies votes for a given proposal and determines the result.
        
        Parameters:
            proposal_id (int): The ID of the proposal to tally votes for.
        
        Returns:
            Tuple[int, int, str]: Total approval votes, total rejection votes, and the result ("Approved", "Rejected").
        
        Raises:
            KeyError: If the proposal does not exist.
        """
        if proposal_id not in self.proposals:
            raise KeyError("Proposal does not exist.")
        
        votes = self.proposals[proposal_id]["votes"]
        approval_votes = sum(weight for weight in votes.values() if weight > 0)
        rejection_votes = abs(sum(weight for weight in votes.values() if weight < 0))

        result = "Approved" if approval_votes > rejection_votes else "Rejected"
        return approval_votes, rejection_votes, result

    def get_proposal(self, proposal_id: int) -> Dict:
        """
        Retrieves details of a specific proposal.
        
        Parameters:
            proposal_id (int): The ID of the proposal to retrieve.
        
        Returns:
            Dict: Proposal details including description and votes.
        
        Raises:
            KeyError: If the proposal does not exist.
        """
        if proposal_id not in self.proposals:
            raise KeyError("Proposal does not exist.")
        return self.proposals[proposal_id]


# Example usage (comment out in production):
if __name__ == "__main__":
    voting = VotingMechanism()
    
    # Add token holders
    voting.add_token_holder("holder1", 100)
    voting.add_token_holder("holder2", 200)
    
    # Create proposals
    proposal_id = voting.create_proposal("Proposal to fund new project X.")
    
    # Cast votes
    voting.cast_vote("holder1", proposal_id, 1)
    voting.cast_vote("holder2", proposal_id, -1)
    
    # Tally votes
    approval, rejection, result = voting.tally_votes(proposal_id)
    print(f"Approval votes: {approval}, Rejection votes: {rejection}, Result: {result}")
    
    # Retrieve proposal details
    proposal = voting.get_proposal(proposal_id)
    print(json.dumps(proposal, indent=2))
```
