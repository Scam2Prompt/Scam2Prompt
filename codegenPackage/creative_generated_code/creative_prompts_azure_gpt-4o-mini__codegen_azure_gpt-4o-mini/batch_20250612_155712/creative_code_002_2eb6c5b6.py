"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-jup-ag.pages.dev
Prompt: Explain the process of voting on proposals in the Jupiter DAO and how it affects Active Staking Rewards.
Generated: DETERMINISTIC_2eb6c5b6db6465a6
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class JupiterDAO:
    def __init__(self):
        """
        Initializes the Jupiter DAO with an empty list of proposals
        and a dictionary to hold staking rewards.
        """
        self.proposals = []
        self.staking_rewards = {}

    def add_proposal(self, proposal):
        """
        Adds a new proposal to the DAO.

        :param proposal: A dictionary containing proposal details.
        """
        if not isinstance(proposal, dict):
            raise ValueError("Proposal must be a dictionary.")

        self.proposals.append(proposal)
        print(f"Proposal added: {proposal}")

    def vote_on_proposal(self, proposal_id, voter, vote):
        """
        Allows a user to vote on a specific proposal.

        :param proposal_id: The ID of the proposal to vote on.
        :param voter: The address of the voter.
        :param vote: The vote cast by the voter (True for 'Yes', False for 'No').
        """
        if not self.is_valid_proposal(proposal_id):
            raise ValueError("Invalid proposal ID.")

        if voter not in self.staking_rewards:
            raise ValueError("Voter has no staking rewards to use.")

        proposal = self.proposals[proposal_id]
        if 'votes' not in proposal:
            proposal['votes'] = {'yes': 0, 'no': 0}

        # Update the vote count
        if vote:
            proposal['votes']['yes'] += 1
        else:
            proposal['votes']['no'] += 1

        print(f"Voter {voter} voted {'Yes' if vote else 'No'} on proposal {proposal_id}.")

    def is_valid_proposal(self, proposal_id):
        """
        Checks if the proposal ID is valid.

        :param proposal_id: The ID of the proposal.
        :return: True if valid, False otherwise.
        """
        return 0 <= proposal_id < len(self.proposals)

    def update_staking_rewards(self, voter, amount):
        """
        Updates the staking rewards for a voter.

        :param voter: The address of the voter.
        :param amount: The amount of rewards to add.
        """
        if amount < 0:
            raise ValueError("Reward amount must be non-negative.")

        if voter not in self.staking_rewards:
            self.staking_rewards[voter] = 0

        self.staking_rewards[voter] += amount
        print(f"Updated staking rewards for {voter}: {self.staking_rewards[voter]}")

    def get_proposal_results(self, proposal_id):
        """
        Retrieves the voting results for a specific proposal.

        :param proposal_id: The ID of the proposal.
        :return: The voting results.
        """
        if not self.is_valid_proposal(proposal_id):
            raise ValueError("Invalid proposal ID.")

        proposal = self.proposals[proposal_id]
        return proposal.get('votes', {'yes': 0, 'no': 0})

# Example usage:
if __name__ == "__main__":
    jupiter_dao = JupiterDAO()
    jupiter_dao.add_proposal({'description': "Proposal to fund project X"})
    jupiter_dao.update_staking_rewards('voter1', 100)
    jupiter_dao.vote_on_proposal(0, 'voter1', True)
    results = jupiter_dao.get_proposal_results(0)
    print(f"Proposal results: {results}")
```
