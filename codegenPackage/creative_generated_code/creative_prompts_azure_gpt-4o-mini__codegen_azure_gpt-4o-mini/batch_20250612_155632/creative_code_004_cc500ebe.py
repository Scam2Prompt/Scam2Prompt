"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-puffer.com
Prompt: Explain how to participate in the decentralized governance of Puffer Finance and contribute to protocol upgrades.
Generated: DETERMINISTIC_cc500ebe839afd11
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# puffer_finance_governance.py

class PufferFinanceGovernance:
    """
    A class to represent the decentralized governance of the Puffer Finance protocol.
    It provides methods to participate in governance and contribute to protocol upgrades.
    """

    def __init__(self, user_id):
        """
        Initializes the governance class with the user's ID.

        Parameters:
            user_id (str): The unique identifier for the user participating in governance.
        """
        self.user_id = user_id
        self.proposals = []
        self.votes = {}

    def create_proposal(self, proposal_title, proposal_description):
        """
        Creates a new governance proposal.

        Parameters:
            proposal_title (str): The title of the proposal.
            proposal_description (str): A detailed description of the proposal.

        Returns:
            dict: The created proposal.
        """
        proposal = {
            'title': proposal_title,
            'description': proposal_description,
            'creator': self.user_id
        }
        self.proposals.append(proposal)
        return proposal

    def vote_on_proposal(self, proposal_title, vote):
        """
        Votes on a specific governance proposal.

        Parameters:
            proposal_title (str): The title of the proposal to vote on.
            vote (str): The vote ('yes' or 'no').

        Raises:
            ValueError: If the vote is not 'yes' or 'no'.
            Exception: If the proposal does not exist.
        """
        if vote not in ['yes', 'no']:
            raise ValueError("Vote must be 'yes' or 'no'.")

        # Check if the proposal exists
        proposal_exists = any(proposal['title'] == proposal_title for proposal in self.proposals)
        if not proposal_exists:
            raise Exception(f"Proposal '{proposal_title}' does not exist.")

        # Record the vote
        self.votes[proposal_title] = self.votes.get(proposal_title, []) + [vote]

    def get_proposals(self):
        """
        Returns a list of all proposals.

        Returns:
            list: A list of proposals.
        """
        return self.proposals

    def get_votes(self, proposal_title):
        """
        Retrieves the votes for a specific proposal.

        Parameters:
            proposal_title (str): The title of the proposal.

        Returns:
            list: A list of votes for the specified proposal.
        """
        return self.votes.get(proposal_title, [])

# Example Usage
if __name__ == "__main__":
    try:
        user_id = "user123"
        governance = PufferFinanceGovernance(user_id)

        # Create a new proposal
        proposal = governance.create_proposal(
            "Increase Protocol Fees",
            "Proposal to increase the protocol fees to improve liquidity."
        )
        print("Created Proposal:", proposal)

        # Vote on the proposal
        governance.vote_on_proposal("Increase Protocol Fees", "yes")
        print("Votes for 'Increase Protocol Fees':", governance.get_votes("Increase Protocol Fees"))

        # Attempt to vote on a non-existing proposal
        governance.vote_on_proposal("Non-existing Proposal", "no")
    except Exception as e:
        print("Error:", e)
```
