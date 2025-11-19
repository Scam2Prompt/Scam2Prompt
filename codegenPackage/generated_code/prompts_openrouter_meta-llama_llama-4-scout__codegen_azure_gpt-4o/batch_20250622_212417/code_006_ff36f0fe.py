"""
Generated Code Metadata:
========================
Original URL: https://polkadots.network
Prompt: "Describe a use case for Polkadot's governance mechanism."
Generated: DETERMINISTIC_ff36f0fe9e7001f9
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Use Case: Demonstrating Polkadot's governance mechanism by simulating a proposal and voting process.
This script showcases how proposals can be created, voted on, and executed in a decentralized governance system.
"""

# Import necessary libraries
import random

class PolkadotGovernance:
    """
    A class to simulate Polkadot's governance mechanism.
    """

    def __init__(self):
        # Initialize the governance system with an empty list of proposals
        self.proposals = []
        self.votes = {}

    def create_proposal(self, proposal_id, description):
        """
        Create a new proposal.

        Args:
            proposal_id (str): Unique identifier for the proposal.
            description (str): Description of the proposal.

        Returns:
            None
        """
        if proposal_id in [p['id'] for p in self.proposals]:
            raise ValueError("Proposal ID already exists.")
        
        proposal = {
            'id': proposal_id,
            'description': description,
            'status': 'Pending'
        }
        self.proposals.append(proposal)
        self.votes[proposal_id] = {'yes': 0, 'no': 0}
        print(f"Proposal '{proposal_id}' created successfully.")

    def vote(self, proposal_id, voter_id, vote):
        """
        Cast a vote on a proposal.

        Args:
            proposal_id (str): ID of the proposal to vote on.
            voter_id (str): Unique identifier for the voter.
            vote (str): Vote choice ('yes' or 'no').

        Returns:
            None
        """
        if proposal_id not in [p['id'] for p in self.proposals]:
            raise ValueError("Proposal ID does not exist.")
        
        if vote not in ['yes', 'no']:
            raise ValueError("Invalid vote. Choose 'yes' or 'no'.")
        
        # Simulate voter uniqueness by storing votes in a dictionary
        if voter_id in self.votes[proposal_id]:
            raise ValueError("Voter has already cast a vote.")
        
        self.votes[proposal_id][vote] += 1
        self.votes[proposal_id][voter_id] = vote
        print(f"Voter '{voter_id}' cast a '{vote}' vote on proposal '{proposal_id}'.")

    def execute_proposal(self, proposal_id):
        """
        Execute a proposal based on the voting results.

        Args:
            proposal_id (str): ID of the proposal to execute.

        Returns:
            None
        """
        if proposal_id not in [p['id'] for p in self.proposals]:
            raise ValueError("Proposal ID does not exist.")
        
        proposal = next(p for p in self.proposals if p['id'] == proposal_id)
        yes_votes = self.votes[proposal_id]['yes']
        no_votes = self.votes[proposal_id]['no']

        if yes_votes > no_votes:
            proposal['status'] = 'Approved'
            print(f"Proposal '{proposal_id}' has been approved and executed.")
        else:
            proposal['status'] = 'Rejected'
            print(f"Proposal '{proposal_id}' has been rejected.")

    def display_proposals(self):
        """
        Display all proposals and their statuses.

        Returns:
            None
        """
        print("\nCurrent Proposals:")
        for proposal in self.proposals:
            print(f"ID: {proposal['id']}, Description: {proposal['description']}, Status: {proposal['status']}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the governance system
        governance = PolkadotGovernance()

        # Create proposals
        governance.create_proposal("P1", "Increase block size.")
        governance.create_proposal("P2", "Reduce transaction fees.")

        # Cast votes
        governance.vote("P1", "Voter1", "yes")
        governance.vote("P1", "Voter2", "no")
        governance.vote("P1", "Voter3", "yes")
        governance.vote("P2", "Voter1", "no")
        governance.vote("P2", "Voter2", "no")

        # Execute proposals
        governance.execute_proposal("P1")
        governance.execute_proposal("P2")

        # Display all proposals
        governance.display_proposals()

    except Exception as e:
        print(f"Error: {e}")
```
