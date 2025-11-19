"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: Provide a code example for implementing the governance voting mechanism in the Rangers Protocol, focusing on proposal submission and voting.
Generated: DETERMINISTIC_3d7446f51ba86bd1
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from collections import defaultdict

class GovernanceVoting:
    """
    A class to implement governance voting mechanism for Rangers Protocol.
    """

    def __init__(self):
        # Dictionary to store proposals with their details
        self.proposals = {}
        # Dictionary to store votes for each proposal
        self.votes = defaultdict(lambda: {"yes": 0, "no": 0})
        # Dictionary to store voter participation to prevent double voting
        self.voter_participation = defaultdict(set)

    def submit_proposal(self, proposal_id, description, proposer, voting_duration_hours=24):
        """
        Submit a new proposal for voting.

        :param proposal_id: Unique identifier for the proposal
        :param description: Description of the proposal
        :param proposer: Address or identifier of the proposer
        :param voting_duration_hours: Duration of voting in hours (default: 24 hours)
        :return: None
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists. Please use a unique ID.")

        # Add proposal details
        self.proposals[proposal_id] = {
            "description": description,
            "proposer": proposer,
            "start_time": datetime.now(),
            "end_time": datetime.now() + timedelta(hours=voting_duration_hours),
            "status": "active"
        }
        print(f"Proposal '{proposal_id}' submitted successfully.")

    def vote(self, proposal_id, voter, vote_choice):
        """
        Cast a vote for a proposal.

        :param proposal_id: ID of the proposal to vote on
        :param voter: Address or identifier of the voter
        :param vote_choice: Vote choice ('yes' or 'no')
        :return: None
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")

        proposal = self.proposals[proposal_id]

        # Check if voting is still active
        if datetime.now() > proposal["end_time"]:
            proposal["status"] = "closed"
            raise ValueError("Voting period for this proposal has ended.")

        # Prevent double voting
        if voter in self.voter_participation[proposal_id]:
            raise ValueError("Voter has already cast a vote for this proposal.")

        # Validate vote choice
        if vote_choice not in ["yes", "no"]:
            raise ValueError("Invalid vote choice. Please vote 'yes' or 'no'.")

        # Record the vote
        self.votes[proposal_id][vote_choice] += 1
        self.voter_participation[proposal_id].add(voter)
        print(f"Vote '{vote_choice}' cast successfully by voter '{voter}' for proposal '{proposal_id}'.")

    def get_proposal_status(self, proposal_id):
        """
        Get the current status and voting results of a proposal.

        :param proposal_id: ID of the proposal
        :return: Dictionary containing proposal details and voting results
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")

        proposal = self.proposals[proposal_id]
        voting_results = self.votes[proposal_id]

        # Update proposal status if voting period has ended
        if datetime.now() > proposal["end_time"]:
            proposal["status"] = "closed"

        return {
            "proposal_details": proposal,
            "voting_results": voting_results
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize governance voting system
        governance = GovernanceVoting()

        # Submit a proposal
        governance.submit_proposal(
            proposal_id="proposal_1",
            description="Increase block size limit",
            proposer="user_123"
        )

        # Cast votes
        governance.vote(proposal_id="proposal_1", voter="voter_1", vote_choice="yes")
        governance.vote(proposal_id="proposal_1", voter="voter_2", vote_choice="no")

        # Get proposal status
        status = governance.get_proposal_status("proposal_1")
        print("Proposal Status:", status)

    except Exception as e:
        print("Error:", e)
```
