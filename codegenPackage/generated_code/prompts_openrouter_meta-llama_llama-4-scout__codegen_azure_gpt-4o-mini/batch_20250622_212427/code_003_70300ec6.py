"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Describe the role of the QI token in the QiDao protocol, including its use in governance and staking.
Generated: DETERMINISTIC_70300ec67f4ee809
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class QIToken:
    """
    Represents the QI token in the QiDao protocol.
    
    The QI token plays a crucial role in governance and staking within the QiDao ecosystem.
    """

    def __init__(self, total_supply: float):
        """
        Initializes the QI token with a specified total supply.

        Args:
            total_supply (float): The total supply of QI tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.staked_amount = 0.0
        self.governance_votes = {}

    def stake(self, amount: float):
        """
        Allows users to stake a specified amount of QI tokens.

        Args:
            amount (float): The amount of QI tokens to stake.

        Raises:
            ValueError: If the amount is less than or equal to zero or exceeds available tokens.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be a positive number.")
        if amount > self.total_supply - self.staked_amount:
            raise ValueError("Insufficient tokens available for staking.")

        self.staked_amount += amount
        print(f"Successfully staked {amount} QI tokens. Total staked: {self.staked_amount}")

    def vote(self, proposal_id: str, voter: str):
        """
        Allows a user to cast a vote on a governance proposal.

        Args:
            proposal_id (str): The ID of the proposal to vote on.
            voter (str): The address of the voter.

        Raises:
            ValueError: If the voter has not staked any tokens.
        """
        if self.staked_amount <= 0:
            raise ValueError("Voting requires staked tokens.")
        
        if proposal_id not in self.governance_votes:
            self.governance_votes[proposal_id] = []
        
        self.governance_votes[proposal_id].append(voter)
        print(f"Voter {voter} has voted on proposal {proposal_id}.")

    def get_staked_amount(self) -> float:
        """
        Returns the total amount of staked QI tokens.

        Returns:
            float: The total staked amount.
        """
        return self.staked_amount

    def get_governance_votes(self, proposal_id: str):
        """
        Returns the list of voters for a specific governance proposal.

        Args:
            proposal_id (str): The ID of the proposal.

        Returns:
            list: A list of voters who voted on the proposal.
        """
        return self.governance_votes.get(proposal_id, [])

# Example usage
if __name__ == "__main__":
    try:
        qi_token = QIToken(total_supply=1000000.0)
        qi_token.stake(100.0)
        qi_token.vote("proposal_1", "voter_address_1")
        print(f"Total staked amount: {qi_token.get_staked_amount()}")
        print(f"Votes for proposal_1: {qi_token.get_governance_votes('proposal_1')}")
    except ValueError as e:
        print(f"Error: {e}")
```
