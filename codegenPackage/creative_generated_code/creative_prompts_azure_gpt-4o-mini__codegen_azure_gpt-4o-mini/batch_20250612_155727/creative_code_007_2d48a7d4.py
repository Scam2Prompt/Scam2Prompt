"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-extra.fi
Prompt: Describe the governance mechanisms in Extra Finance and how token holders can influence platform features.
Generated: DETERMINISTIC_2d48a7d40e4dfb51
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GovernanceMechanisms:
    """
    A class to represent the governance mechanisms of Extra Finance.
    This includes how token holders can influence platform features.
    """

    def __init__(self):
        """
        Initializes a new governance mechanism with default parameters.
        """
        self.token_holders = {}
        self.proposals = []

    def add_token_holder(self, address, tokens):
        """
        Adds a token holder to the governance system.

        Args:
            address (str): The wallet address of the token holder.
            tokens (int): The number of tokens owned by the holder.

        Raises:
            ValueError: If the number of tokens is not positive.
        """
        if tokens <= 0:
            raise ValueError("The number of tokens must be positive.")
        
        self.token_holders[address] = tokens

    def create_proposal(self, proposal_text, proposer_address):
        """
        Creates a new proposal that allows token holders to vote on.

        Args:
            proposal_text (str): The text of the proposal.
            proposer_address (str): The wallet address of the proposer.

        Raises:
            ValueError: If the proposer is not a token holder.
        """
        if proposer_address not in self.token_holders:
            raise ValueError("Only token holders can create proposals.")

        proposal = {
            'text': proposal_text,
            'votes': {},
            'status': 'open'
        }
        self.proposals.append(proposal)

    def vote(self, proposal_index, address, vote):
        """
        Allows a token holder to vote on a proposal.

        Args:
            proposal_index (int): The index of the proposal in the proposals list.
            address (str): The wallet address of the voter.
            vote (bool): The vote, True for 'yes', False for 'no'.

        Raises:
            IndexError: If the proposal index is out of bounds.
            ValueError: If the address is not a token holder or if the proposal is closed.
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index is out of bounds.")

        if address not in self.token_holders:
            raise ValueError("Only token holders can vote.")

        proposal = self.proposals[proposal_index]

        if proposal['status'] != 'open':
            raise ValueError("Voting is closed for this proposal.")

        # Record the vote
        proposal['votes'][address] = vote

    def close_proposal(self, proposal_index):
        """
        Closes a proposal for voting.

        Args:
            proposal_index (int): The index of the proposal to close.

        Raises:
            IndexError: If the proposal index is out of bounds.
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index is out of bounds.")

        self.proposals[proposal_index]['status'] = 'closed'

    def get_results(self, proposal_index):
        """
        Get the results of a proposal after it has been closed.

        Args:
            proposal_index (int): The index of the proposal.

        Returns:
            dict: A summary of the votes and the outcome of the proposal.

        Raises:
            IndexError: If the proposal index is out of bounds.
            ValueError: If the proposal is still open.
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index is out of bounds.")
        
        proposal = self.proposals[proposal_index]

        if proposal['status'] != 'closed':
            raise ValueError("Voting is still open for this proposal.")

        total_votes = len(proposal['votes'])
        yes_votes = sum(1 for vote in proposal['votes'].values() if vote)
        no_votes = total_votes - yes_votes

        return {
            'proposal_text': proposal['text'],
            'yes_votes': yes_votes,
            'no_votes': no_votes,
            'total_votes': total_votes
        }

# Example usage
if __name__ == "__main__":
    governance = GovernanceMechanisms()
    governance.add_token_holder("address1", 100)
    governance.add_token_holder("address2", 50)

    governance.create_proposal("Implement new feature X", "address1")
    governance.vote(0, "address1", True)
    governance.vote(0, "address2", False)

    governance.close_proposal(0)
    results = governance.get_results(0)
    print(results)
```
