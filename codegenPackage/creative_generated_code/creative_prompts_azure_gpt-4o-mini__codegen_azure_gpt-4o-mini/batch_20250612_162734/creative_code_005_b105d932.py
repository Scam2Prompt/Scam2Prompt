"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakingstory.org
Prompt: Explain how to participate in governance within the Story Staking ecosystem and the benefits it provides to users.
Generated: DETERMINISTIC_b105d932b9369400
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StoryStakingGovernance:
    """
    A class to represent the governance participation in the Story Staking ecosystem.
    
    Attributes
    ----------
    stakeholders : dict
        A dictionary to hold stakeholders and their voting power.
    proposals : list
        A list to hold governance proposals.
    """

    def __init__(self):
        """
        Initializes the StoryStakingGovernance with empty stakeholders and proposals.
        """
        self.stakeholders = {}
        self.proposals = []

    def add_stakeholder(self, stakeholder: str, voting_power: int):
        """
        Adds a stakeholder to the governance system.

        Parameters
        ----------
        stakeholder : str
            The name of the stakeholder.
        voting_power : int
            The voting power assigned to the stakeholder.

        Raises
        ------
        ValueError
            If the voting power is not positive.
        """
        if voting_power <= 0:
            raise ValueError("Voting power must be a positive integer.")
        self.stakeholders[stakeholder] = voting_power

    def create_proposal(self, proposal: str):
        """
        Creates a new governance proposal.

        Parameters
        ----------
        proposal : str
            The proposal description.
        """
        self.proposals.append(proposal)

    def vote_on_proposal(self, stakeholder: str, proposal_index: int):
        """
        Allows a stakeholder to vote on a proposal.

        Parameters
        ----------
        stakeholder : str
            The name of the stakeholder.
        proposal_index : int
            The index of the proposal to vote on.

        Raises
        ------
        ValueError
            If the stakeholder does not exist or the proposal index is invalid.
        """
        if stakeholder not in self.stakeholders:
            raise ValueError(f"Stakeholder '{stakeholder}' does not exist.")
        if proposal_index < 0 or proposal_index >= len(self.proposals):
            raise ValueError("Invalid proposal index.")

        # Simulate a voting process
        print(f"{stakeholder} voted on proposal '{self.proposals[proposal_index]}'.")

    def get_proposals(self):
        """
        Returns the list of proposals.

        Returns
        -------
        list
            A list of current proposals.
        """
        return self.proposals

    def get_stakeholders(self):
        """
        Returns the list of stakeholders.

        Returns
        -------
        dict
            A dictionary of stakeholders and their voting power.
        """
        return self.stakeholders


# Example usage
if __name__ == "__main__":
    governance = StoryStakingGovernance()

    # Adding stakeholders
    try:
        governance.add_stakeholder("Alice", 10)
        governance.add_stakeholder("Bob", 20)
    except ValueError as e:
        print(e)

    # Creating proposals
    governance.create_proposal("Increase staking rewards")
    governance.create_proposal("Implement new governance model")

    # Voting on proposals
    try:
        governance.vote_on_proposal("Alice", 0)
        governance.vote_on_proposal("Bob", 1)
    except ValueError as e:
        print(e)

    # Displaying proposals and stakeholders
    print("Current Proposals:", governance.get_proposals())
    print("Stakeholders and Voting Power:", governance.get_stakeholders())
```
