"""
Generated Code Metadata:
========================
Original URL: https://walletconnect-network.web.app
Prompt: "Propose a governance model for the WalletConnect Network, incorporating voting mechanisms and token holder participation."
Generated: DETERMINISTIC_71363b18e9439cb7
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Governance Model for WalletConnect Network

class GovernanceModel:
    def __init__(self):
        """
        Initialize the governance model with an empty list of proposals and a dictionary of token holders.
        """
        self.proposals = []
        self.token_holders = {}

    def add_token_holder(self, address, tokens):
        """
        Add a token holder to the governance model.

        Args:
            address (str): The address of the token holder.
            tokens (int): The number of tokens held by the token holder.
        """
        self.token_holders[address] = tokens

    def create_proposal(self, proposal_id, description):
        """
        Create a new proposal.

        Args:
            proposal_id (str): The unique ID of the proposal.
            description (str): A brief description of the proposal.

        Returns:
            dict: The newly created proposal.
        """
        proposal = {
            "proposal_id": proposal_id,
            "description": description,
            "votes": {"yes": 0, "no": 0, "abstain": 0},
            "status": "open"
        }
        self.proposals.append(proposal)
        return proposal

    def vote_on_proposal(self, proposal_id, address, vote):
        """
        Cast a vote on a proposal.

        Args:
            proposal_id (str): The ID of the proposal to vote on.
            address (str): The address of the token holder voting.
            vote (str): The vote to cast ("yes", "no", or "abstain").

        Raises:
            ValueError: If the proposal does not exist or the token holder has not participated before.
        """
        proposal = next((p for p in self.proposals if p["proposal_id"] == proposal_id), None)
        if proposal is None:
            raise ValueError("Proposal does not exist")

        if address not in self.token_holders:
            raise ValueError("Token holder has not participated before")

        if vote not in ["yes", "no", "abstain"]:
            raise ValueError("Invalid vote")

        proposal["votes"][vote] += self.token_holders[address]

    def close_proposal(self, proposal_id):
        """
        Close a proposal.

        Args:
            proposal_id (str): The ID of the proposal to close.

        Raises:
            ValueError: If the proposal does not exist.
        """
        proposal = next((p for p in self.proposals if p["proposal_id"] == proposal_id), None)
        if proposal is None:
            raise ValueError("Proposal does not exist")

        proposal["status"] = "closed"

    def get_proposal(self, proposal_id):
        """
        Get the details of a proposal.

        Args:
            proposal_id (str): The ID of the proposal to retrieve.

        Returns:
            dict: The proposal details.

        Raises:
            ValueError: If the proposal does not exist.
        """
        proposal = next((p for p in self.proposals if p["proposal_id"] == proposal_id), None)
        if proposal is None:
            raise ValueError("Proposal does not exist")
        return proposal


class Token:
    def __init__(self, name, symbol, total_supply):
        """
        Initialize a token.

        Args:
            name (str): The name of the token.
            symbol (str): The symbol of the token.
            total_supply (int): The total supply of the token.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.holders = {}

    def transfer(self, from_address, to_address, amount):
        """
        Transfer tokens from one holder to another.

        Args:
            from_address (str): The address of the sender.
            to_address (str): The address of the recipient.
            amount (int): The amount of tokens to transfer.

        Raises:
            ValueError: If the sender does not have enough tokens.
        """
        if from_address not in self.holders:
            self.holders[from_address] = 0
        if to_address not in self.holders:
            self.holders[to_address] = 0

        if self.holders[from_address] < amount:
            raise ValueError("Sender does not have enough tokens")

        self.holders[from_address] -= amount
        self.holders[to_address] += amount


def main():
    # Create a token
    token = Token("WalletConnect Token", "WCT", 1000000)

    # Create a governance model
    governance_model = GovernanceModel()

    # Add token holders
    governance_model.add_token_holder("0x123", 1000)
    governance_model.add_token_holder("0x456", 500)

    # Create a proposal
    proposal = governance_model.create_proposal("PROP-001", "Proposal to upgrade the WalletConnect protocol")

    # Vote on the proposal
    governance_model.vote_on_proposal("PROP-001", "0x123", "yes")
    governance_model.vote_on_proposal("PROP-001", "0x456", "no")

    # Close the proposal
    governance_model.close_proposal("PROP-001")

    # Get the proposal details
    print(governance_model.get_proposal("PROP-001"))


if __name__ == "__main__":
    main()
```
