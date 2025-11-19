"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-yearnfinance.com
Prompt: Explain the community governance model of Yearn Finance and how YFI token holders can influence platform developments.
Generated: DETERMINISTIC_38773492de42c837
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class YearnFinanceGovernance:
    """
    A class to represent the community governance model of Yearn Finance.

    Attributes
    ----------
    yfi_token_holders : list
        A list of YFI token holder addresses.
    proposals : list
        A list of proposals for platform developments.
    voting_power : dict
        A dictionary mapping token holder addresses to their voting power.
    """

    def __init__(self):
        """Initialize the Yearn Finance governance model."""
        self.yfi_token_holders = []
        self.proposals = []
        self.voting_power = {}

    def add_token_holder(self, address: str, amount: float):
        """
        Add a YFI token holder along with their token amount.

        Parameters
        ----------
        address : str
            The address of the YFI token holder.
        amount : float
            The amount of YFI tokens held by the address.

        Raises
        ------
        ValueError
            If the amount of YFI is not positive.
        """
        if amount <= 0:
            raise ValueError("Amount of YFI tokens must be positive.")
        
        self.yfi_token_holders.append(address)
        self.voting_power[address] = amount

    def create_proposal(self, description: str):
        """
        Create a new proposal for platform development.

        Parameters
        ----------
        description : str
            A description of the proposal.
        """
        proposal = {
            'description': description,
            'votes': {}
        }
        self.proposals.append(proposal)

    def vote(self, address: str, proposal_index: int):
        """
        Allow a token holder to vote on a specific proposal.

        Parameters
        ----------
        address : str
            The address of the YFI token holder voting.
        proposal_index : int
            The index of the proposal in the proposals list.

        Raises
        ------
        IndexError
            If the proposal_index is out of range.
        ValueError
            If the address is not a recognized YFI token holder.
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index is out of range.")
        
        if address not in self.yfi_token_holders:
            raise ValueError("Address not recognized as a YFI token holder.")

        # Record the vote
        self.proposals[proposal_index]['votes'][address] = self.voting_power[address]

    def tally_votes(self, proposal_index: int) -> float:
        """
        Tally the votes for a specific proposal.

        Parameters
        ----------
        proposal_index : int
            The index of the proposal to tally.

        Returns
        -------
        float
            Total votes received by the proposal.

        Raises
        ------
        IndexError
            If the proposal_index is out of range.
        """
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise IndexError("Proposal index is out of range.")
        
        total_votes = sum(self.proposals[proposal_index]['votes'].values())
        return total_votes

# Example usage:
if __name__ == "__main__":
    governance = YearnFinanceGovernance()
    governance.add_token_holder("0x12345", 10)
    governance.create_proposal("Improve liquidity on the platform.")
    governance.vote("0x12345", 0)
    total_votes = governance.tally_votes(0)
    print(f"Total votes on proposal 0: {total_votes}")
```
