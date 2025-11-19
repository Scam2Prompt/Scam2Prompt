"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockmainnet.pages.dev
Prompt: Describe the governance model of Blocks Mainnet and how community members can propose changes.
Generated: DETERMINISTIC_aae624d65c81f976
Batch ID: 20250612_161125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Governance Model of Blocks Mainnet

This script outlines a governance model for Blocks Mainnet, allowing community members to propose changes.
The governance model is implemented as a smart contract, assuming usage in a blockchain environment (e.g., Ethereum).
It includes mechanisms for proposing, voting, and executing changes based on community consensus.
"""

from web3 import Web3, exceptions

class BlocksGovernance:
    """
    A class representing the governance model for Blocks Mainnet.
    """

    def __init__(self, admin_address):
        """
        Initializes the governance model with the given administrator address.

        :param admin_address: Ethereum address of the administrator.
        """
        self.admin_address = admin_address
        self.proposals = {}  # Dictionary to store proposals
        self.votes = {}  # Dictionary to store votes for proposals
        self.executed_proposals = []  # List to track executed proposals

    def propose_change(self, proposal_id, proposer_address, description):
        """
        Allows a community member to propose a change.

        :param proposal_id: Unique ID for the proposal.
        :param proposer_address: Ethereum address of the proposer.
        :param description: Description of the proposed change.
        :raises ValueError: If the proposal ID already exists.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists. Please use a unique ID.")

        self.proposals[proposal_id] = {
            "proposer": proposer_address,
            "description": description,
            "votes_for": 0,
            "votes_against": 0,
            "status": "Open"  # Status: Open, Closed, Executed
        }

    def vote_on_proposal(self, proposal_id, voter_address, vote):
        """
        Allows community members to vote on a proposal.

        :param proposal_id: ID of the proposal to vote on.
        :param voter_address: Ethereum address of the voter.
        :param vote: Vote cast by the voter ('For' or 'Against').
        :raises ValueError: If the proposal is not found or voting is invalid.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found.")

        if self.proposals[proposal_id]["status"] != "Open":
            raise ValueError("Voting is closed for this proposal.")

        if voter_address in self.votes.get(proposal_id, {}):
            raise ValueError("Voter has already cast a vote.")

        # Record the vote
        self.votes.setdefault(proposal_id, {})[voter_address] = vote

        # Update vote counts
        if vote == "For":
            self.proposals[proposal_id]["votes_for"] += 1
        elif vote == "Against":
            self.proposals[proposal_id]["votes_against"] += 1
        else:
            raise ValueError("Invalid vote. Use 'For' or 'Against'.")

    def close_voting(self, proposal_id):
        """
        Closes voting for the specified proposal.

        :param proposal_id: ID of the proposal to close voting for.
        :raises ValueError: If the proposal is not found or already closed.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found.")

        if self.proposals[proposal_id]["status"] != "Open":
            raise ValueError("Voting is already closed for this proposal.")

        self.proposals[proposal_id]["status"] = "Closed"

    def execute_proposal(self, proposal_id):
        """
        Executes a proposal if it has majority votes.

        :param proposal_id: ID of the proposal to execute.
        :raises ValueError: If the proposal is not eligible for execution.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found.")

        proposal = self.proposals[proposal_id]

        if proposal["status"] != "Closed":
            raise ValueError("Proposal must be closed before execution.")

        if proposal["votes_for"] <= proposal["votes_against"]:
            raise ValueError("Proposal does not have majority votes.")

        # Execute the proposal (placeholder for actual execution logic)
        self.executed_proposals.append(proposal_id)
        proposal["status"] = "Executed"

    def get_proposal(self, proposal_id):
        """
        Retrieves details of a specific proposal.

        :param proposal_id: ID of the proposal to retrieve.
        :return: Details of the proposal.
        :raises ValueError: If the proposal is not found.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal not found.")

        return self.proposals[proposal_id]

    def list_proposals(self):
        """
        Lists all proposals in the governance model.

        :return: A dictionary of all proposals.
        """
        return self.proposals

# Example usage
if __name__ == "__main__":
    try:
        governance = BlocksGovernance(admin_address="0xAdminAddress")

        # Propose a change
        governance.propose_change(
            proposal_id="1",
            proposer_address="0xProposerAddress",
            description="Change block reward from 2 ETH to 1.5 ETH."
        )

        # Vote on the proposal
        governance.vote_on_proposal(
            proposal_id="1",
            voter_address="0xVoterAddress1",
            vote="For"
        )
        governance.vote_on_proposal(
            proposal_id="1",
            voter_address="0xVoterAddress2",
            vote="Against"
        )

        # Close voting
        governance.close_voting(proposal_id="1")

        # Execute the proposal
        governance.execute_proposal(proposal_id="1")

        # Retrieve proposal details
        print(governance.get_proposal(proposal_id="1"))

    except ValueError as e:
        print(f"Error: {e}")
    except exceptions.Web3Exception as e:
        print(f"Web3 Error: {e}")
```
