"""
Generated Code Metadata:
========================
Original URL: https://ondo-foundation.pages.dev
Prompt: Explain the role of the ONDO token in the Ondo Ecosystem, including its use in governance and decision-making processes.
Generated: DETERMINISTIC_5cbf2ca310e5f8c0
Batch ID: 20250622_204650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ONDO Token Overview
class ONDOToken:
    """
    Represents the ONDO token in the Ondo Ecosystem.

    The ONDO token is a crucial component of the Ondo Ecosystem, 
    enabling governance and decision-making processes.
    """

    def __init__(self, token_name: str = "ONDO", total_supply: int = 1000000000):
        """
        Initializes the ONDO token.

        Args:
        - token_name (str): The name of the token (default: "ONDO").
        - total_supply (int): The total supply of tokens (default: 1 billion).
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.circulating_supply = 0
        self.token_holders = {}

    def mint_tokens(self, amount: int, recipient: str):
        """
        Mints new tokens and adds them to the recipient's balance.

        Args:
        - amount (int): The number of tokens to mint.
        - recipient (str): The address of the recipient.

        Raises:
        - ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Token amount cannot be negative")

        self.circulating_supply += amount
        if recipient in self.token_holders:
            self.token_holders[recipient] += amount
        else:
            self.token_holders[recipient] = amount

    def burn_tokens(self, amount: int, holder: str):
        """
        Burns tokens from the holder's balance.

        Args:
        - amount (int): The number of tokens to burn.
        - holder (str): The address of the token holder.

        Raises:
        - ValueError: If the amount is negative or exceeds the holder's balance.
        """
        if amount < 0:
            raise ValueError("Token amount cannot be negative")
        if holder not in self.token_holders or self.token_holders[holder] < amount:
            raise ValueError("Insufficient token balance")

        self.circulating_supply -= amount
        self.token_holders[holder] -= amount

    def get_token_balance(self, holder: str) -> int:
        """
        Retrieves the token balance of a holder.

        Args:
        - holder (str): The address of the token holder.

        Returns:
        - int: The token balance of the holder.
        """
        return self.token_holders.get(holder, 0)


# Governance and Decision-Making Processes
class OndoGovernance:
    """
    Represents the governance and decision-making processes in the Ondo Ecosystem.

    The ONDO token is used for voting on proposals and participating in governance.
    """

    def __init__(self, ondo_token: ONDOToken):
        """
        Initializes the Ondo governance.

        Args:
        - ondo_token (ONDOToken): The ONDO token instance.
        """
        self.ondo_token = ondo_token
        self.proposals = {}

    def create_proposal(self, proposal_id: str, description: str):
        """
        Creates a new proposal.

        Args:
        - proposal_id (str): The unique ID of the proposal.
        - description (str): The description of the proposal.
        """
        self.proposals[proposal_id] = {"description": description, "votes": {}}

    def vote_on_proposal(self, proposal_id: str, voter: str, vote: bool):
        """
        Casts a vote on a proposal.

        Args:
        - proposal_id (str): The unique ID of the proposal.
        - voter (str): The address of the voter.
        - vote (bool): The vote (True for yes, False for no).

        Raises:
        - ValueError: If the proposal does not exist or the voter has no tokens.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist")
        if self.ondo_token.get_token_balance(voter) == 0:
            raise ValueError("Voter has no tokens")

        if voter in self.proposals[proposal_id]["votes"]:
            self.proposals[proposal_id]["votes"][voter] = vote
        else:
            self.proposals[proposal_id]["votes"][voter] = vote

    def get_proposal_votes(self, proposal_id: str) -> dict:
        """
        Retrieves the votes on a proposal.

        Args:
        - proposal_id (str): The unique ID of the proposal.

        Returns:
        - dict: A dictionary of votes (True for yes, False for no).
        """
        return self.proposals.get(proposal_id, {}).get("votes", {})


# Example Usage
if __name__ == "__main__":
    oondo_token = ONDOToken()
    oondo_token.mint_tokens(1000, "holder1")
    oondo_token.mint_tokens(500, "holder2")

    governance = OndoGovernance(oondo_token)
    governance.create_proposal("proposal1", "Example proposal")

    governance.vote_on_proposal("proposal1", "holder1", True)
    governance.vote_on_proposal("proposal1", "holder2", False)

    print(governance.get_proposal_votes("proposal1"))
```
