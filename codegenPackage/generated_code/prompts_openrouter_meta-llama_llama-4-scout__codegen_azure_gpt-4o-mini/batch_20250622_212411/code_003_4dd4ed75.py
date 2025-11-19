"""
Generated Code Metadata:
========================
Original URL: https://uni-stores-info.com
Prompt: Describe the role of Uniswap's native token in governance and protocol upgrades within the DeFi ecosystem.
Generated: DETERMINISTIC_4dd4ed7573c9d0fa
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UniswapGovernance:
    """
    A class to represent the governance mechanism of Uniswap's native token (UNI).
    This class includes methods to handle governance proposals and voting.
    """

    def __init__(self):
        """
        Initializes the governance system with an empty list of proposals and a dictionary for votes.
        """
        self.proposals = []
        self.votes = {}

    def create_proposal(self, proposal_description):
        """
        Creates a new governance proposal.

        Args:
            proposal_description (str): A description of the proposal.

        Returns:
            dict: A dictionary representing the created proposal.
        """
        proposal = {
            'id': len(self.proposals) + 1,
            'description': proposal_description,
            'votes_for': 0,
            'votes_against': 0,
            'voters': set()
        }
        self.proposals.append(proposal)
        return proposal

    def vote(self, proposal_id, voter, vote_type):
        """
        Allows a user to vote on a proposal.

        Args:
            proposal_id (int): The ID of the proposal to vote on.
            voter (str): The address of the voter.
            vote_type (str): The type of vote ('for' or 'against').

        Raises:
            ValueError: If the vote_type is not 'for' or 'against'.
            Exception: If the voter has already voted on this proposal.
        """
        if vote_type not in ['for', 'against']:
            raise ValueError("vote_type must be 'for' or 'against'.")

        proposal = self.get_proposal(proposal_id)
        if voter in proposal['voters']:
            raise Exception("Voter has already voted on this proposal.")

        proposal['voters'].add(voter)
        if vote_type == 'for':
            proposal['votes_for'] += 1
        else:
            proposal['votes_against'] += 1

    def get_proposal(self, proposal_id):
        """
        Retrieves a proposal by its ID.

        Args:
            proposal_id (int): The ID of the proposal.

        Returns:
            dict: The proposal with the given ID.

        Raises:
            IndexError: If the proposal ID does not exist.
        """
        if proposal_id < 1 or proposal_id > len(self.proposals):
            raise IndexError("Proposal ID does not exist.")
        return self.proposals[proposal_id - 1]

    def tally_votes(self, proposal_id):
        """
        Tally the votes for a given proposal.

        Args:
            proposal_id (int): The ID of the proposal.

        Returns:
            str: The result of the voting.
        """
        proposal = self.get_proposal(proposal_id)
        if proposal['votes_for'] > proposal['votes_against']:
            return "Proposal passed."
        else:
            return "Proposal failed."

# Example usage
if __name__ == "__main__":
    governance = UniswapGovernance()
    proposal = governance.create_proposal("Upgrade the liquidity pool mechanism.")
    governance.vote(proposal['id'], "0x123", "for")
    governance.vote(proposal['id'], "0x456", "against")
    result = governance.tally_votes(proposal['id'])
    print(result)  # Output: Proposal passed or Proposal failed
```
