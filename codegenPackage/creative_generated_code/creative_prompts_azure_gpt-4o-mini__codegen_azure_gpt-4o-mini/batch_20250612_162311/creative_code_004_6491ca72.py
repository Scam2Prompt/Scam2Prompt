"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards.cow-ai.world
Prompt: Explain how to participate in governance within the CoW DAO using COW tokens and provide a sample proposal format.
Generated: DETERMINISTIC_6491ca72aa1ee85e
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
CoW DAO Governance Participation using COW Tokens

This script provides a basic framework for participating in governance within the CoW DAO using COW tokens. 
It includes functions for submitting proposals and voting on them.
"""

class CoWDAO:
    def __init__(self):
        """
        Initializes the CoW DAO with an empty list of proposals and a dictionary to track votes.
        """
        self.proposals = []
        self.votes = {}

    def submit_proposal(self, proposer: str, proposal_text: str):
        """
        Submits a new governance proposal.

        :param proposer: The address or identifier of the proposer.
        :param proposal_text: A description of the proposal.
        :raises ValueError: If the proposal text is empty.
        """
        if not proposal_text.strip():
            raise ValueError("Proposal text cannot be empty.")

        proposal = {
            'id': len(self.proposals) + 1,
            'proposer': proposer,
            'text': proposal_text,
            'votes_for': 0,
            'votes_against': 0
        }
        self.proposals.append(proposal)
        print(f"Proposal submitted: {proposal}")

    def vote(self, proposal_id: int, voter: str, support: bool):
        """
        Casts a vote on a proposal.

        :param proposal_id: The ID of the proposal to vote on.
        :param voter: The address or identifier of the voter.
        :param support: True if the voter supports the proposal, False otherwise.
        :raises ValueError: If the proposal ID is invalid or if the voter has already voted.
        """
        if proposal_id < 1 or proposal_id > len(self.proposals):
            raise ValueError("Invalid proposal ID.")

        if voter in self.votes:
            raise ValueError("Voter has already cast a vote.")

        if support:
            self.proposals[proposal_id - 1]['votes_for'] += 1
        else:
            self.proposals[proposal_id - 1]['votes_against'] += 1
        
        self.votes[voter] = proposal_id
        print(f"Vote cast by {voter} on proposal {proposal_id}: {'Support' if support else 'Against'}")

    def get_proposals(self):
        """
        Returns a list of current proposals.

        :return: List of proposals.
        """
        return self.proposals

# Example usage:
if __name__ == "__main__":
    dao = CoWDAO()

    # Submitting a proposal
    try:
        dao.submit_proposal("0x123", "Proposal to improve liquidity on the platform.")
    except ValueError as e:
        print(f"Error submitting proposal: {e}")

    # Voting on a proposal
    try:
        dao.vote(1, "0x456", support=True)
    except ValueError as e:
        print(f"Error casting vote: {e}")

    # Displaying proposals
    print("Current Proposals:")
    for proposal in dao.get_proposals():
        print(proposal)
```
