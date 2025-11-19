"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-inqubeta.pages.dev
Prompt: How can token holders participate in governance decisions on the InQubeta platform using $QUBE?
Generated: DETERMINISTIC_fc85d27f7592a054
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# GovernanceParticipation.py

class GovernanceParticipation:
    """
    A class to represent the governance participation of token holders on the InQubeta platform using $QUBE.
    """

    def __init__(self):
        self.token_holders = {}
        self.proposals = []

    def add_token_holder(self, address, tokens):
        """
        Add a token holder to the governance system.
        
        Args:
            address (str): The wallet address of the token holder.
            tokens (int): The amount of $QUBE tokens held by the token holder.
        """
        if address in self.token_holders:
            raise ValueError("Address already registered as a token holder.")

        if tokens <= 0:
            raise ValueError("Token amount must be greater than zero.")

        self.token_holders[address] = tokens

    def create_proposal(self, proposal):
        """
        Create a new governance proposal.
        
        Args:
            proposal (str): The details of the governance proposal.
        """
        if not proposal:
            raise ValueError("Proposal cannot be empty.")

        self.proposals.append({
            'proposal': proposal,
            'votes': {}
        })

    def vote_on_proposal(self, address, proposal_index, vote):
        """
        Allow token holders to vote on a specific proposal.
        
        Args:
            address (str): The wallet address of the token holder.
            proposal_index (int): The index of the proposal on which the vote is cast.
            vote (bool): The vote; True for 'yes' and False for 'no'.
        """
        if address not in self.token_holders:
            raise ValueError("Address is not a registered token holder.")

        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")

        if address in self.proposals[proposal_index]['votes']:
            raise ValueError("You have already voted on this proposal.")

        # Record the vote
        self.proposals[proposal_index]['votes'][address] = vote

    def tally_votes(self, proposal_index):
        """
        Tally the votes for a specific proposal.
        
        Args:
            proposal_index (int): The index of the proposal to tally votes for.

        Returns:
            dict: A summary of the vote tally.
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index out of range.")

        proposal_votes = self.proposals[proposal_index]['votes']
        yes_votes = sum(1 for vote in proposal_votes.values() if vote)
        no_votes = len(proposal_votes) - yes_votes

        return {
            'proposal': self.proposals[proposal_index]['proposal'],
            'yes_votes': yes_votes,
            'no_votes': no_votes,
            'total_votes': len(proposal_votes)
        }


# Example usage
if __name__ == "__main__":
    try:
        governance = GovernanceParticipation()
        governance.add_token_holder("0x12345", 100)
        governance.create_proposal("Should we increase the project funding?")
        governance.vote_on_proposal("0x12345", 0, True)

        # Tally and print results
        results = governance.tally_votes(0)
        print(results)

    except (ValueError, IndexError) as e:
        print(f"Error: {e}")
```
