"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rangersprotocol.gitbook.io
Prompt: Provide a code example for implementing the governance voting mechanism in the Rangers Protocol, focusing on proposal submission and voting.
Generated: DETERMINISTIC_3d7446f51ba86bd1
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Governance Voting Mechanism for Rangers Protocol

class Proposal:
    """Class representing a governance proposal."""
    def __init__(self, proposal_id, proposer, description):
        self.proposal_id = proposal_id
        self.proposer = proposer
        self.description = description
        self.votes = {}
        self.total_votes = 0

    def vote(self, voter, support):
        """Records a vote for the proposal."""
        if voter in self.votes:
            raise ValueError("Voter has already voted on this proposal.")
        
        self.votes[voter] = support
        self.total_votes += 1

class Governance:
    """Class managing the governance proposals and voting."""
    def __init__(self):
        self.proposals = {}
        self.next_proposal_id = 1

    def submit_proposal(self, proposer, description):
        """Submits a new proposal for voting."""
        proposal_id = self.next_proposal_id
        self.proposals[proposal_id] = Proposal(proposal_id, proposer, description)
        self.next_proposal_id += 1
        return proposal_id

    def vote_on_proposal(self, proposal_id, voter, support):
        """Records a vote on a proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")

        proposal = self.proposals[proposal_id]
        try:
            proposal.vote(voter, support)
        except ValueError as e:
            print(f"Error voting on proposal: {e}")

    def get_proposal_results(self, proposal_id):
        """Retrieves the results of a proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID does not exist.")

        proposal = self.proposals[proposal_id]
        return {
            "proposal_id": proposal.proposal_id,
            "description": proposal.description,
            "total_votes": proposal.total_votes,
            "votes": proposal.votes
        }

# Example Usage
if __name__ == "__main__":
    governance = Governance()
    
    # Submit a proposal
    proposal_id = governance.submit_proposal("Alice", "Increase funding for R&D.")
    
    # Voting on the proposal
    governance.vote_on_proposal(proposal_id, "Bob", True)
    governance.vote_on_proposal(proposal_id, "Charlie", False)

    # Retrieve proposal results
    results = governance.get_proposal_results(proposal_id)
    print(results)
```
