"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapuni.com
Prompt: Describe the governance model of the UNI token and how it empowers users to influence the Uniswap protocol's future decisions.
Generated: DETERMINISTIC_7b7fe917bdc35cd0
Batch ID: 20250612_135940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Governance Model of the UNI Token

This script outlines the governance model of the UNI token, and how it empowers users 
to influence the Uniswap protocol's future decisions. It defines a simple framework 
to simulate governance actions using UNI tokens.
"""

class UniswapGovernance:
    def __init__(self):
        self.proposals = []
        self.voting_power = {}  # Dictionary to track voting power of each address

    def add_voter(self, address, tokens):
        """
        Allows a user to add their voting power based on the UNI tokens they hold.

        Args:
            address (str): The address of the user.
            tokens (int): The number of UNI tokens held by the user.
        """
        if tokens < 0:
            raise ValueError("Token count cannot be negative.")
        self.voting_power[address] = self.voting_power.get(address, 0) + tokens

    def create_proposal(self, proposal_description):
        """
        Creates a new governance proposal.

        Args:
            proposal_description (str): A description of the proposal.
        """
        proposal = {
            'description': proposal_description,
            'votes_for': 0,
            'votes_against': 0,
            'voters': set()  # To track who has voted
        }
        self.proposals.append(proposal)

    def vote_on_proposal(self, address, proposal_index, support=True):
        """
        Allows a user to vote on a proposal.

        Args:
            address (str): The address of the voter.
            proposal_index (int): The index of the proposal in the proposals list.
            support (bool): If True, vote in favor of the proposal; otherwise, vote against.
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index is out of range.")
        
        proposal = self.proposals[proposal_index]
        
        if address in proposal['voters']:
            raise Exception("This address has already voted on this proposal.")

        # Update the proposal votes based on the voter's support
        if support:
            proposal['votes_for'] += self.voting_power.get(address, 0)
        else:
            proposal['votes_against'] += self.voting_power.get(address, 0)
        
        proposal['voters'].add(address)  # Mark this address as having voted

    def get_proposal_results(self, proposal_index):
        """
        Returns the results of a specific proposal.

        Args:
            proposal_index (int): The index of the proposal to check.
        
        Returns:
            dict: A dictionary containing the proposal results.
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index is out of range.")
        
        proposal = self.proposals[proposal_index]
        return {
            'description': proposal['description'],
            'votes_for': proposal['votes_for'],
            'votes_against': proposal['votes_against'],
            'voters': len(proposal['voters'])
        }


# Example Usage
if __name__ == "__main__":
    governance = UniswapGovernance()
    
    # Adding voters
    governance.add_voter("0x123", 100)
    governance.add_voter("0x456", 200)

    # Creating a proposal
    governance.create_proposal("Increase liquidity mining rewards.")

    # Voting on the proposal
    governance.vote_on_proposal("0x123", 0, support=True)
    governance.vote_on_proposal("0x456", 0, support=False)

    # Getting results of the proposal
    results = governance.get_proposal_results(0)
    print(results)
```
