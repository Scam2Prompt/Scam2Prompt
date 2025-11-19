"""
Generated Code Metadata:
========================
Original URL: https://lidofinance.blogspot.com
Prompt: Describe how Lido Finance's DAO governance structure enhances security and user participation in staking decisions.
Generated: DETERMINISTIC_f633959f5a8c7090
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Lido Finance DAO Governance Structure Simulator

class GovernanceStructure:
    """
    Simulates Lido Finance's DAO governance structure.

    Attributes:
    - stakers (dict): Mapping of staker addresses to their respective stakes.
    - proposals (dict): Mapping of proposal IDs to their respective details.
    """

    def __init__(self):
        # Initialize empty staker and proposal mappings
        self.stakers = {}
        self.proposals = {}

    def add_staker(self, address, stake):
        """
        Adds a new staker to the governance structure.

        Args:
        - address (str): The staker's address.
        - stake (float): The staker's stake amount.

        Raises:
        - ValueError: If the stake amount is non-positive.
        """
        if stake <= 0:
            raise ValueError("Stake amount must be positive.")

        # Add the staker to the mapping
        self.stakers[address] = stake

    def create_proposal(self, proposal_id, description):
        """
        Creates a new proposal.

        Args:
        - proposal_id (str): The unique ID of the proposal.
        - description (str): A brief description of the proposal.

        Raises:
        - ValueError: If the proposal ID already exists.
        """
        if proposal_id in self.proposals:
            raise ValueError("Proposal ID already exists.")

        # Initialize the proposal with a 0 vote count
        self.proposals[proposal_id] = {"description": description, "votes": 0}

    def vote_on_proposal(self, address, proposal_id):
        """
        Casts a vote on a proposal.

        Args:
        - address (str): The staker's address.
        - proposal_id (str): The ID of the proposal to vote on.

        Raises:
        - ValueError: If the staker or proposal does not exist.
        """
        if address not in self.stakers:
            raise ValueError("Staker does not exist.")
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")

        # Increment the vote count for the proposal
        self.proposals[proposal_id]["votes"] += self.stakers[address]

    def get_proposal_details(self, proposal_id):
        """
        Retrieves the details of a proposal.

        Args:
        - proposal_id (str): The ID of the proposal.

        Returns:
        - dict: A dictionary containing the proposal's description and vote count.

        Raises:
        - ValueError: If the proposal does not exist.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")

        # Return the proposal details
        return self.proposals[proposal_id]


def main():
    # Create a governance structure simulator
    governance = GovernanceStructure()

    try:
        # Add stakers
        governance.add_staker("0xStaker1", 1000)
        governance.add_staker("0xStaker2", 500)

        # Create a proposal
        governance.create_proposal("prop-1", "Increase staking rewards")

        # Vote on the proposal
        governance.vote_on_proposal("0xStaker1", "prop-1")
        governance.vote_on_proposal("0xStaker2", "prop-1")

        # Retrieve proposal details
        proposal_details = governance.get_proposal_details("prop-1")
        print("Proposal Details:")
        print(f"Description: {proposal_details['description']}")
        print(f"Votes: {proposal_details['votes']}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
