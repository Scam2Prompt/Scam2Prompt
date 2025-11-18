"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lynexfl.org
Prompt: Develop a governance voting system for Lynex FI that allows community members to participate in decisions about new features or liquidity distribution.
Generated: DETERMINISTIC_d7ff2bec22c05b13
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import uuid


class VotingSystem:
    """
    Governance Voting System for Lynex FI.
    This system allows community members to participate in decisions about 
    new features or liquidity distribution.
    """

    def __init__(self):
        """
        Initialize the voting system with an empty list of proposals and votes.
        """
        self.proposals = {}
        self.votes = {}

    class Proposal:
        """
        Represents a governance proposal.
        """
        def __init__(self, title, description, duration_days):
            self.id = str(uuid.uuid4())  # Unique identifier for the proposal
            self.title = title  # Title of the proposal
            self.description = description  # Detailed description of the proposal
            self.start_time = datetime.utcnow()  # Start time of the proposal
            self.end_time = self.start_time + timedelta(days=duration_days)  # End time of the proposal
            self.vote_counts = {"yes": 0, "no": 0}  # Vote count for "yes" and "no"

    def create_proposal(self, title, description, duration_days):
        """
        Create a new proposal.

        :param title: Title of the proposal
        :param description: Description of the proposal
        :param duration_days: Duration of the proposal voting period in days
        :return: ID of the created proposal
        """
        if duration_days <= 0:
            raise ValueError("Duration must be greater than 0 days.")

        proposal = self.Proposal(title, description, duration_days)
        self.proposals[proposal.id] = proposal
        self.votes[proposal.id] = set()  # Track voters to prevent double voting
        return proposal.id

    def vote(self, proposal_id, voter_id, vote_choice):
        """
        Cast a vote on a proposal.

        :param proposal_id: ID of the proposal to vote on
        :param voter_id: Unique identifier for the voter
        :param vote_choice: "yes" or "no"
        :return: None
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found.")

        proposal = self.proposals[proposal_id]

        # Ensure the voting period is still active
        current_time = datetime.utcnow()
        if current_time > proposal.end_time:
            raise ValueError("Voting period has ended for this proposal.")

        # Ensure the voter hasn't already voted
        if voter_id in self.votes[proposal_id]:
            raise ValueError("Voter has already voted on this proposal.")

        # Validate vote choice
        if vote_choice.lower() not in proposal.vote_counts:
            raise ValueError("Invalid vote choice. Choose 'yes' or 'no'.")

        # Record the vote
        proposal.vote_counts[vote_choice.lower()] += 1
        self.votes[proposal_id].add(voter_id)

    def get_results(self, proposal_id):
        """
        Get the voting results of a proposal.

        :param proposal_id: ID of the proposal to retrieve results for
        :return: Dictionary containing the vote counts
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found.")

        proposal = self.proposals[proposal_id]
        return {
            "title": proposal.title,
            "description": proposal.description,
            "start_time": proposal.start_time,
            "end_time": proposal.end_time,
            "vote_counts": proposal.vote_counts
        }

    def list_proposals(self):
        """
        List all proposals and their statuses.

        :return: List of dictionaries containing proposal details
        """
        current_time = datetime.utcnow()
        return [
            {
                "id": proposal_id,
                "title": proposal.title,
                "description": proposal.description,
                "start_time": proposal.start_time,
                "end_time": proposal.end_time,
                "status": "Active" if current_time <= proposal.end_time else "Closed"
            }
            for proposal_id, proposal in self.proposals.items()
        ]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the voting system
        voting_system = VotingSystem()

        # Create a new proposal
        proposal_id = voting_system.create_proposal(
            title="Increase Liquidity Distribution",
            description="Proposal to increase liquidity to new trading pairs by 30%.",
            duration_days=7
        )
        print(f"Proposal ID: {proposal_id}")

        # Cast votes
        voting_system.vote(proposal_id, voter_id="voter1", vote_choice="yes")
        voting_system.vote(proposal_id, voter_id="voter2", vote_choice="no")
        voting_system.vote(proposal_id, voter_id="voter3", vote_choice="yes")

        # Get voting results
        results = voting_system.get_results(proposal_id)
        print("Voting Results:", results)

        # List proposals
        proposals = voting_system.list_proposals()
        print("Proposals:", proposals)

    except Exception as e:
        print(f"Error: {e}")
```
