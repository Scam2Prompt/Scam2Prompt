"""
Generated Code Metadata:
========================
Original URL: https://worldlibertyfi.pages.dev
Prompt: Generate a code snippet that simulates the governance voting process for non-transferable tokens in a DeFi project like WorldLibertyFi.
Generated: DETERMINISTIC_f83db820c914002c
Batch ID: 20250612_155255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# governance_voting.py

from typing import Dict, List
from datetime import datetime, timedelta

class GovernanceVoting:
    def __init__(self):
        # Initialize an empty dictionary to store votes
        self.votes: Dict[str, Dict[str, int]] = {}
        # Initialize an empty dictionary to store proposals
        self.proposals: Dict[str, Dict[str, str]] = {}

    def create_proposal(self, proposal_id: str, description: str, start_time: datetime, end_time: datetime):
        """
        Create a new proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.
        - description (str): Brief description of the proposal.
        - start_time (datetime): Start time of the voting period.
        - end_time (datetime): End time of the voting period.
        """
        # Check if proposal already exists
        if proposal_id in self.proposals:
            raise ValueError("Proposal already exists")

        # Validate start and end times
        if start_time >= end_time:
            raise ValueError("Invalid start and end times")

        # Create a new proposal
        self.proposals[proposal_id] = {
            "description": description,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "votes": {"yes": 0, "no": 0}
        }

    def cast_vote(self, proposal_id: str, user: str, vote: str):
        """
        Cast a vote on a proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.
        - user (str): User casting the vote.
        - vote (str): Vote type ("yes" or "no").
        """
        # Check if proposal exists
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")

        # Check if user has already voted
        if user in self.votes.get(proposal_id, {}):
            raise ValueError("User has already voted")

        # Validate vote type
        if vote not in ["yes", "no"]:
            raise ValueError("Invalid vote type")

        # Get current proposal
        proposal = self.proposals[proposal_id]

        # Check if voting period has ended
        end_time = datetime.fromisoformat(proposal["end_time"])
        if datetime.now() > end_time:
            raise ValueError("Voting period has ended")

        # Cast the vote
        if proposal_id not in self.votes:
            self.votes[proposal_id] = {}
        self.votes[proposal_id][user] = 1 if vote == "yes" else 0

        # Update proposal vote count
        proposal["votes"]["yes"] += 1 if vote == "yes" else 0
        proposal["votes"]["no"] += 1 if vote == "no" else 0

    def get_proposal_results(self, proposal_id: str) -> Dict[str, int]:
        """
        Get the results of a proposal.

        Args:
        - proposal_id (str): Unique identifier for the proposal.

        Returns:
        - A dictionary containing the vote counts for "yes" and "no".
        """
        # Check if proposal exists
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")

        # Return proposal vote counts
        return self.proposals[proposal_id]["votes"]

def main():
    governance = GovernanceVoting()

    # Create a new proposal
    proposal_id = "WLF-001"
    description = "Proposal to update the tokenomics"
    start_time = datetime.now()
    end_time = start_time + timedelta(days=7)
    governance.create_proposal(proposal_id, description, start_time, end_time)

    # Cast some votes
    users: List[str] = ["user1", "user2", "user3", "user4"]
    for user in users:
        governance.cast_vote(proposal_id, user, "yes" if user in ["user1", "user2"] else "no")

    # Get proposal results
    results = governance.get_proposal_results(proposal_id)
    print("Proposal Results:")
    print(f"Yes: {results['yes']}")
    print(f"No: {results['no']}")

if __name__ == "__main__":
    main()
```
