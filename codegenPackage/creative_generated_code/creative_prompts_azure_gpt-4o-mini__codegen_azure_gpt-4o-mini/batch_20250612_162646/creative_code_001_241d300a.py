"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: What steps are involved in creating a proposal within the Futarchy framework on MetaDAO?
Generated: DETERMINISTIC_241d300ab217535c
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FutarchyProposal:
    """
    A class to represent a proposal within the Futarchy framework on MetaDAO.
    """

    def __init__(self, proposal_id, proposer, description, decision_token, outcome):
        """
        Initialize a new Futarchy proposal.

        Args:
            proposal_id (str): Unique identifier for the proposal.
            proposer (str): Address of the proposer.
            description (str): Description of the proposal.
            decision_token (str): Token used for decision-making.
            outcome (str): Expected outcome of the proposal.
        """
        self.proposal_id = proposal_id
        self.proposer = proposer
        self.description = description
        self.decision_token = decision_token
        self.outcome = outcome
        self.status = 'Draft'
        self.votes = {}

    def submit_proposal(self):
        """
        Submit the proposal for voting.

        Raises:
            Exception: If the proposal is already submitted.
        """
        if self.status != 'Draft':
            raise Exception("Proposal has already been submitted.")
        
        self.status = 'Submitted'
        # Log the submission (In production, use a logging framework)
        print(f"Proposal {self.proposal_id} submitted by {self.proposer}.")

    def vote(self, voter, vote_value):
        """
        Cast a vote for the proposal.

        Args:
            voter (str): Address of the voter.
            vote_value (bool): Vote value (True for 'yes', False for 'no').

        Raises:
            Exception: If the proposal is not submitted or the voter has already voted.
        """
        if self.status != 'Submitted':
            raise Exception("Proposal is not open for voting.")
        
        if voter in self.votes:
            raise Exception("Voter has already cast their vote.")

        self.votes[voter] = vote_value
        print(f"Voter {voter} has cast a vote: {'Yes' if vote_value else 'No'}.")

    def tally_votes(self):
        """
        Tally the votes and determine the outcome.

        Returns:
            str: Result of the voting process.

        Raises:
            Exception: If the proposal is still in draft or not yet submitted.
        """
        if self.status != 'Submitted':
            raise Exception("Proposal voting is not complete.")
        
        yes_votes = sum(vote for vote in self.votes.values() if vote)
        no_votes = len(self.votes) - yes_votes

        # Log the tally result (In production, use a logging framework)
        print(f"Tallying votes... Yes: {yes_votes}, No: {no_votes}")

        if yes_votes > no_votes:
            self.status = 'Approved'
            return "Proposal approved."
        else:
            self.status = 'Rejected'
            return "Proposal rejected."

# Example usage
if __name__ == "__main__":
    try:
        proposal = FutarchyProposal(
            proposal_id='PROP-001',
            proposer='0x1234567890abcdef1234567890abcdef12345678',
            description='Implement new governance model.',
            decision_token='GOVTOKEN',
            outcome='Increased community engagement.'
        )

        proposal.submit_proposal()
        proposal.vote('0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef01', True)
        proposal.vote('0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef02', False)
        print(proposal.tally_votes())

    except Exception as e:
        print(f"Error: {e}")
```
