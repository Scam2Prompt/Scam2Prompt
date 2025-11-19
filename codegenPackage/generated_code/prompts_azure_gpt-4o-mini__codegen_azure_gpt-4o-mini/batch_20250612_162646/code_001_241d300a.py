"""
Generated Code Metadata:
========================
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: What steps are involved in creating a proposal within the Futarchy framework on MetaDAO?
Generated: DETERMINISTIC_241d300ab217535c
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FutarchyProposal:
    """
    A class to represent a proposal within the Futarchy framework on MetaDAO.
    """

    def __init__(self, proposal_id, description, outcome, voting_period):
        """
        Initializes a new Futarchy proposal.

        :param proposal_id: Unique identifier for the proposal
        :param description: Description of the proposal
        :param outcome: Expected outcome of the proposal
        :param voting_period: Duration for which the proposal will be voted on
        """
        self.proposal_id = proposal_id
        self.description = description
        self.outcome = outcome
        self.voting_period = voting_period
        self.votes = {}
        self.is_active = True

    def cast_vote(self, voter_id, vote):
        """
        Cast a vote for the proposal.

        :param voter_id: Unique identifier for the voter
        :param vote: The vote cast by the voter (True for support, False for oppose)
        :raises ValueError: If the proposal is not active or the voter has already voted
        """
        if not self.is_active:
            raise ValueError("Cannot vote on an inactive proposal.")
        if voter_id in self.votes:
            raise ValueError("Voter has already cast a vote.")

        self.votes[voter_id] = vote

    def close_proposal(self):
        """
        Closes the proposal, marking it as inactive.
        """
        self.is_active = False

    def tally_votes(self):
        """
        Tally the votes and determine the outcome of the proposal.

        :return: A dictionary with the results of the voting
        :raises ValueError: If the proposal is still active
        """
        if self.is_active:
            raise ValueError("Cannot tally votes on an active proposal.")

        total_votes = len(self.votes)
        if total_votes == 0:
            return {"support": 0, "oppose": 0, "total": 0}

        support_votes = sum(1 for vote in self.votes.values() if vote)
        oppose_votes = total_votes - support_votes

        return {
            "support": support_votes,
            "oppose": oppose_votes,
            "total": total_votes
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a new proposal
        proposal = FutarchyProposal(proposal_id=1, description="Implement new governance model", outcome="Increased efficiency", voting_period=7)

        # Cast votes
        proposal.cast_vote(voter_id="user1", vote=True)
        proposal.cast_vote(voter_id="user2", vote=False)

        # Close the proposal after the voting period
        proposal.close_proposal()

        # Tally the votes
        results = proposal.tally_votes()
        print("Voting Results:", results)

    except ValueError as e:
        print("Error:", e)
```
