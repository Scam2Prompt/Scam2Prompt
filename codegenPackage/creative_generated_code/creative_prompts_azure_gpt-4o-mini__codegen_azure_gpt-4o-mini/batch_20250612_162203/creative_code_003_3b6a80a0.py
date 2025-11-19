"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earns-pupstoken.pages.dev
Prompt: How can I implement a community voting mechanism for a memecoin like $PUPS, based on the principles outlined in the Earns PUPS Token documentation?
Generated: DETERMINISTIC_3b6a80a07d4e0b2a
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from typing import List, Dict
import random

class VotingSystem:
    def __init__(self, voting_duration: int):
        """
        Initialize the VotingSystem with a specified voting duration.

        :param voting_duration: The duration of the voting period in minutes
        """
        self.voting_duration = timedelta(minutes=voting_duration)
        self.votes: Dict[str, List[str]] = {}  # Maps proposal ID to list of voter addresses
        self.proposals: Dict[str, datetime] = {}  # Maps proposal ID to end time of voting
        self.voters: set = set()  # Set of voters to prevent double voting

    def create_proposal(self, proposal_id: str):
        """
        Create a new voting proposal.

        :param proposal_id: Unique identifier for the proposal
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal already exists")
        end_time = datetime.now() + self.voting_duration
        self.proposals[proposal_id] = end_time

    def vote(self, proposal_id: str, voter_address: str):
        """
        Cast a vote for a proposal.

        :param proposal_id: Unique identifier for the proposal
        :param voter_address: Address of the voter
        """
        # Check if the proposal exists
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        
        # Check if voting period is active
        if datetime.now() > self.proposals[proposal_id]:
            raise ValueError("Voting period has ended")
        
        # Check if voter has already voted
        if voter_address in self.voters:
            raise ValueError("Voter has already cast a vote")
        
        # Record the vote
        if proposal_id not in self.votes:
            self.votes[proposal_id] = []
        self.votes[proposal_id].append(voter_address)
        self.voters.add(voter_address)  # Prevent double voting

    def get_results(self) -> Dict[str, int]:
        """
        Get the results of the voting for each proposal.

        :return: A dictionary mapping proposal IDs to the number of votes
        """
        results = {proposal_id: len(voters) for proposal_id, voters in self.votes.items()}
        return results

    def reset_voting(self):
        """
        Reset the voting system for a new round of proposals.
        """
        self.votes.clear()
        self.proposals.clear()
        self.voters.clear()

# Example usage:
if __name__ == "__main__":
    try:
        voting_system = VotingSystem(voting_duration=10)  # Voting lasts for 10 minutes
        voting_system.create_proposal("proposal_1")
        
        # Simulate voting
        voting_system.vote("proposal_1", "0xVoterAddress1")
        voting_system.vote("proposal_1", "0xVoterAddress2")

        # Wait for some time...
        print(voting_system.get_results())  # Display results
        
        # Reset for new voting
        voting_system.reset_voting()

    except ValueError as e:
        print(f"Error: {e}")
```
