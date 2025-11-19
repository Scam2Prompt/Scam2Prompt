"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stekecoredao.org
Prompt: How does CoreDAO ensure transparent governance through decentralized voting mechanisms? Provide a code example for implementing voting.
Generated: DETERMINISTIC_869639757d3f9dc5
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Voting System for Decentralized Governance

class VotingSystem:
    def __init__(self):
        """Initializes the Voting System with a list of proposals and a mapping of votes."""
        self.proposals = {}
        self.votes = {}

    def create_proposal(self, proposal_id: str, description: str):
        """
        Creates a new proposal in the system.

        Args:
            proposal_id (str): Unique identifier for the proposal.
            description (str): Description of the proposal.
        """
        if proposal_id in self.proposals:
            raise ValueError(f"Proposal ID '{proposal_id}' already exists.")
        self.proposals[proposal_id] = description
        self.votes[proposal_id] = {'for': 0, 'against': 0}
        print(f"Proposal '{proposal_id}' created.")

    def vote(self, proposal_id: str, vote: str):
        """
        Records a vote for a given proposal.

        Args:
            proposal_id (str): The ID of the proposal to vote on.
            vote (str): The vote type, either 'for' or 'against'.
        
        Raises:
            ValueError: If the proposal ID does not exist or if the vote is invalid.
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal ID '{proposal_id}' does not exist.")
        if vote not in ['for', 'against']:
            raise ValueError("Vote must be 'for' or 'against'.")

        self.votes[proposal_id][vote] += 1
        print(f"Vote recorded: {vote} for proposal '{proposal_id}'.")

    def tally_votes(self, proposal_id: str):
        """
        Tallies the votes for a given proposal and returns the result.

        Args:
            proposal_id (str): The ID of the proposal to tally votes for.
        
        Returns:
            dict: A dictionary containing the vote counts.
        
        Raises:
            ValueError: If the proposal ID does not exist.
        """
        if proposal_id not in self.proposals:
            raise ValueError(f"Proposal ID '{proposal_id}' does not exist.")
        
        result = self.votes[proposal_id]
        print(f"Tally for proposal '{proposal_id}': {result}")
        return result

# Example usage
if __name__ == "__main__":
    try:
        voting_system = VotingSystem()
        voting_system.create_proposal("1", "Increase the budget for community projects")
        voting_system.vote("1", "for")
        voting_system.vote("1", "against")
        voting_system.vote("1", "for")
        results = voting_system.tally_votes("1")
        print(f"Final results: {results}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
