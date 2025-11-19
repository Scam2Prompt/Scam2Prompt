"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-unnfinance.pages.dev
Prompt: Explain how to use the $UNN token for governance in the UNION Finance ecosystem and provide an example of a voting process.
Generated: DETERMINISTIC_c9ec2dcd5d97fab3
Batch ID: 20250612_163948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This script demonstrates how to use the $UNN token for governance in the UNION Finance ecosystem.
# It includes an example of a voting process where token holders can vote on a proposal.

import time


class GovernanceSystem:
    """
    A simplified governance system for UNION Finance ecosystem using $UNN tokens.
    """

    def __init__(self):
        """
        Initialize the governance system with an empty list of proposals and voter registry.
        """
        self.proposals = []  # List of proposals
        self.votes = {}  # Maps proposal IDs to votes (e.g., {proposal_id: {user_address: vote}})
        self.token_balances = {}  # Maps token holder addresses to their $UNN balances

    def register_user(self, user_address, unn_balance):
        """
        Register a user with an initial $UNN token balance.

        :param user_address: The unique address of the user
        :param unn_balance: Initial $UNN token balance
        """
        if user_address in self.token_balances:
            raise ValueError("User is already registered.")
        self.token_balances[user_address] = unn_balance

    def create_proposal(self, proposal_title, proposal_description):
        """
        Create a governance proposal.

        :param proposal_title: Title of the proposal
        :param proposal_description: Description of the proposal
        :return: Proposal ID
        """
        proposal_id = len(self.proposals)
        self.proposals.append({
            "id": proposal_id,
            "title": proposal_title,
            "description": proposal_description,
            "created_at": time.time(),
            "votes": {}  # Tracks votes in format {user_address: vote}
        })
        return proposal_id

    def vote_on_proposal(self, user_address, proposal_id, vote):
        """
        Vote on a proposal using $UNN tokens.

        :param user_address: Address of the token holder
        :param proposal_id: ID of the proposal to vote on
        :param vote: Vote value, e.g., "yes" or "no"
        """
        # Validate user
        if user_address not in self.token_balances:
            raise ValueError("User is not registered.")
        if proposal_id >= len(self.proposals):
            raise ValueError("Invalid proposal ID.")

        # Each user can vote only once per proposal
        if user_address in self.proposals[proposal_id]["votes"]:
            raise ValueError("User has already voted on this proposal.")

        # Record the vote
        self.proposals[proposal_id]["votes"][user_address] = {
            "vote": vote,
            "weight": self.token_balances[user_address]  # Voting weight corresponds to $UNN balance
        }

    def tally_votes(self, proposal_id):
        """
        Tally the votes and determine the outcome of a proposal.

        :param proposal_id: ID of the proposal to tally votes for
        :return: Tally result (yes_votes, no_votes)
        """
        if proposal_id >= len(self.proposals):
            raise ValueError("Invalid proposal ID.")

        yes_votes = 0
        no_votes = 0

        for user_vote in self.proposals[proposal_id]["votes"].values():
            if user_vote["vote"] == "yes":
                yes_votes += user_vote["weight"]
            elif user_vote["vote"] == "no":
                no_votes += user_vote["weight"]

        return yes_votes, no_votes


# Example usage

if __name__ == "__main__":
    governance = GovernanceSystem()

    # Register token holders
    governance.register_user("user1", 100)  # User 1 has 100 $UNN tokens
    governance.register_user("user2", 50)   # User 2 has 50 $UNN tokens

    # Create a governance proposal
    proposal_id = governance.create_proposal(
        "Increase Staking Rewards",
        "Proposal to increase staking rewards for $UNN token holders."
    )
    print(f"Proposal ID {proposal_id} created.")

    # Users vote on the proposal
    governance.vote_on_proposal("user1", proposal_id, "yes")  # User 1 votes "yes"
    governance.vote_on_proposal("user2", proposal_id, "no")   # User 2 votes "no"

    # Tally votes
    yes_votes, no_votes = governance.tally_votes(proposal_id)
    print(f"Proposal ID {proposal_id} voting results:")
    print(f"YES votes: {yes_votes}")
    print(f"NO votes: {no_votes}")

    # Determine the outcome
    if yes_votes > no_votes:
        print("Proposal PASSED.")
    else:
        print("Proposal REJECTED.")
```
