"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shiba.dorik.io
Prompt: Explain how to implement a function that allows users to vote in the Doggy DAO governance system on ShibaSwap.
Generated: DETERMINISTIC_bd7816022a3018b9
Batch ID: 20250612_163051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Dict, List, Any

class VotingError(Exception):
    """Custom exception class for voting errors."""
    pass

class DoggyDAOGovernance:
    def __init__(self):
        # Initialize a dictionary to store votes
        self.votes: Dict[str, int] = {}
        # Initialize a set to store the voters to prevent double voting
        self.voters: set = set()

    def cast_vote(self, voter_id: str, proposal_id: str, vote_value: int) -> None:
        """
        Allows a user to cast a vote on a specific proposal.

        :param voter_id: Unique identifier for the voter
        :param proposal_id: Unique identifier for the proposal being voted on
        :param vote_value: The value of the vote, typically 1 for 'yes' and -1 for 'no'
        :raises VotingError: If the voter has already voted or if the vote_value is invalid
        """
        # Check if the voter has already voted
        if voter_id in self.voters:
            raise VotingError(f"Voter {voter_id} has already cast their vote.")

        # Validate the vote value
        if vote_value not in [1, -1]:
            raise VotingError("Invalid vote value. Use 1 for 'yes' or -1 for 'no'.")

        # Cast the vote
        if proposal_id not in self.votes:
            self.votes[proposal_id] = 0  # Initialize the proposal vote count
        self.votes[proposal_id] += vote_value
        self.voters.add(voter_id)  # Mark the voter as having voted
        
        print(f"Vote cast by {voter_id} for proposal {proposal_id}: {vote_value}")

    def get_votes(self, proposal_id: str) -> int:
        """
        Retrieve the total votes for a given proposal.

        :param proposal_id: Unique identifier for the proposal
        :return: Total count of votes for the proposal
        """
        return self.votes.get(proposal_id, 0)

    def reset_votes(self) -> None:
        """
        Resets all votes and voters in the system. 
        Useful for starting a new voting cycle.
        """
        self.votes.clear()
        self.voters.clear()
        print("All votes have been reset.")

# Example usage
if __name__ == "__main__":
    dao = DoggyDAOGovernance()
    
    try:
        # Voters cast their votes
        dao.cast_vote("voter1", "proposal1", 1)  # Vote 'yes'
        dao.cast_vote("voter2", "proposal1", -1) # Vote 'no'
        
        # Retrieve and print the current vote tally
        print(f"Total votes for proposal1: {dao.get_votes('proposal1')}")
        
        # Attempting to cast a vote from the same voter again
        dao.cast_vote("voter1", "proposal1", 1)  # This should raise an error

    except VotingError as e:
        print(f"Voting error occurred: {e}")
    
    # Resetting votes for a new voting cycle
    dao.reset_votes()
```
