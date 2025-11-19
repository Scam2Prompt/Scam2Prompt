"""
Generated Code Metadata:
========================
Original URL: https://gorodshansona.ru
Prompt: "Discuss the role of the IMX token in the Immutable X ecosystem, including its use in governance and the distribution of tokens."
Generated: DETERMINISTIC_af782710dd83e478
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ImmutableXToken:
    """
    A class to represent the IMX token in the Immutable X ecosystem.
    
    Attributes:
        total_supply (int): The total supply of IMX tokens.
        circulating_supply (int): The current circulating supply of IMX tokens.
        governance_votes (dict): A dictionary to track governance votes by address.
    """

    def __init__(self, total_supply: int):
        """
        Initializes the IMX token with a total supply.
        
        Args:
            total_supply (int): The total number of IMX tokens available.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        
        self.total_supply = total_supply
        self.circulating_supply = total_supply  # Initially, all tokens are in circulation
        self.governance_votes = {}

    def distribute_tokens(self, amount: int):
        """
        Distributes tokens to the ecosystem participants.
        
        Args:
            amount (int): The number of tokens to distribute.
        
        Raises:
            ValueError: If the amount exceeds the circulating supply.
        """
        if amount < 0:
            raise ValueError("Amount to distribute must be non-negative.")
        if amount > self.circulating_supply:
            raise ValueError("Cannot distribute more tokens than are in circulation.")
        
        self.circulating_supply -= amount
        print(f"Distributed {amount} IMX tokens. Remaining circulating supply: {self.circulating_supply}")

    def vote(self, voter_address: str, proposal_id: str, vote_value: bool):
        """
        Allows a token holder to cast a vote on a governance proposal.
        
        Args:
            voter_address (str): The address of the voter.
            proposal_id (str): The ID of the proposal being voted on.
            vote_value (bool): The value of the vote (True for 'yes', False for 'no').
        
        Raises:
            ValueError: If the voter address is invalid or if the vote value is not a boolean.
        """
        if not isinstance(voter_address, str) or not voter_address:
            raise ValueError("Invalid voter address.")
        if not isinstance(vote_value, bool):
            raise ValueError("Vote value must be a boolean.")
        
        if proposal_id not in self.governance_votes:
            self.governance_votes[proposal_id] = {}
        
        self.governance_votes[proposal_id][voter_address] = vote_value
        print(f"Voter {voter_address} voted {'yes' if vote_value else 'no'} on proposal {proposal_id}.")

    def get_governance_results(self, proposal_id: str):
        """
        Retrieves the results of a governance proposal.
        
        Args:
            proposal_id (str): The ID of the proposal.
        
        Returns:
            dict: A dictionary containing the vote counts.
        
        Raises:
            ValueError: If the proposal ID is invalid.
        """
        if proposal_id not in self.governance_votes:
            raise ValueError("Invalid proposal ID.")
        
        results = {
            'yes': sum(1 for vote in self.governance_votes[proposal_id].values() if vote),
            'no': sum(1 for vote in self.governance_votes[proposal_id].values() if not vote)
        }
        return results


# Example usage
if __name__ == "__main__":
    try:
        imx_token = ImmutableXToken(total_supply=1000000)
        imx_token.distribute_tokens(10000)
        imx_token.vote("0x123", "proposal_1", True)
        imx_token.vote("0x456", "proposal_1", False)
        results = imx_token.get_governance_results("proposal_1")
        print(f"Governance results for proposal_1: {results}")
    except ValueError as e:
        print(f"Error: {e}")
```
