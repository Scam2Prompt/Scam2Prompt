"""
Generated Code Metadata:
========================
Original URL: https://hehe-verse.pages.dev
Prompt: Explain how to implement a decentralized governance model for the $HEHE ecosystem, including community voting mechanisms as mentioned in the content.
Generated: DETERMINISTIC_68896989ae5e114a
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Any
import json

class GovernanceModel:
    def __init__(self):
        # Initialize the governance model with an empty list of proposals and votes
        self.proposals: List[Dict[str, Any]] = []
        self.votes: Dict[str, Dict[str, int]] = {}  # proposal_id -> {voter_id: vote_value}

    def create_proposal(self, proposal_id: str, description: str) -> None:
        """
        Create a new proposal in the governance model.

        :param proposal_id: Unique identifier for the proposal
        :param description: Description of the proposal
        """
        if any(proposal['id'] == proposal_id for proposal in self.proposals):
            raise ValueError("Proposal ID already exists.")
        
        self.proposals.append({
            'id': proposal_id,
            'description': description,
            'votes_for': 0,
            'votes_against': 0
        })

    def vote(self, proposal_id: str, voter_id: str, vote_value: str) -> None:
        """
        Cast a vote on a proposal.

        :param proposal_id: The ID of the proposal to vote on
        :param voter_id: The ID of the voter
        :param vote_value: The value of the vote ('for' or 'against')
        """
        if proposal_id not in [proposal['id'] for proposal in self.proposals]:
            raise ValueError("Proposal does not exist.")
        
        if voter_id in self.votes.get(proposal_id, {}):
            raise ValueError("Voter has already voted on this proposal.")
        
        # Initialize votes for the proposal if not already done
        if proposal_id not in self.votes:
            self.votes[proposal_id] = {}

        # Record the vote
        self.votes[proposal_id][voter_id] = vote_value
        
        # Update the proposal's vote counts
        if vote_value == 'for':
            self._update_vote_count(proposal_id, votes_for=1)
        elif vote_value == 'against':
            self._update_vote_count(proposal_id, votes_against=1)
        else:
            raise ValueError("Invalid vote value. Must be 'for' or 'against'.")

    def _update_vote_count(self, proposal_id: str, votes_for: int = 0, votes_against: int = 0) -> None:
        """
        Update the vote counts for a proposal.

        :param proposal_id: The ID of the proposal
        :param votes_for: Number of votes for the proposal
        :param votes_against: Number of votes against the proposal
        """
        for proposal in self.proposals:
            if proposal['id'] == proposal_id:
                proposal['votes_for'] += votes_for
                proposal['votes_against'] += votes_against
                break

    def get_results(self, proposal_id: str) -> Dict[str, Any]:
        """
        Get the voting results for a proposal.

        :param proposal_id: The ID of the proposal
        :return: A dictionary containing the proposal's results
        """
        if proposal_id not in [proposal['id'] for proposal in self.proposals]:
            raise ValueError("Proposal does not exist.")
        
        for proposal in self.proposals:
            if proposal['id'] == proposal_id:
                return {
                    'id': proposal['id'],
                    'description': proposal['description'],
                    'votes_for': proposal['votes_for'],
                    'votes_against': proposal['votes_against']
                }

    def export_data(self) -> str:
        """
        Export the governance model data to JSON format.

        :return: JSON string representation of the governance model
        """
        return json.dumps({
            'proposals': self.proposals,
            'votes': self.votes
        }, indent=4)

# Example usage
if __name__ == "__main__":
    governance = GovernanceModel()
    
    # Create proposals
    governance.create_proposal("1", "Proposal to increase community funding.")
    governance.create_proposal("2", "Proposal to reduce transaction fees.")
    
    # Cast votes
    governance.vote("1", "voter1", "for")
    governance.vote("1", "voter2", "against")
    governance.vote("2", "voter1", "for")
    
    # Get results
    print(governance.get_results("1"))
    print(governance.get_results("2"))
    
    # Export data
    print(governance.export_data())
```
