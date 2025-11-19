"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-in.pages.dev
Prompt: Design a tokenomics model for a new cryptocurrency project, inspired by WienerAI's 30% presale, 20% staking, and 20% community rewards allocation.
Generated: DETERMINISTIC_c0902817c40a8f4e
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics_model.py

class TokenomicsModel:
    """
    A class representing a tokenomics model for a cryptocurrency project.

    Attributes:
        total_supply (float): The total supply of tokens.
        presale_allocation (float): The percentage of tokens allocated for presale.
        staking_allocation (float): The percentage of tokens allocated for staking.
        community_rewards_allocation (float): The percentage of tokens allocated for community rewards.
    """

    def __init__(self, total_supply: float, presale_allocation: float = 0.3, staking_allocation: float = 0.2, community_rewards_allocation: float = 0.2):
        """
        Initializes a TokenomicsModel instance.

        Args:
            total_supply (float): The total supply of tokens.
            presale_allocation (float, optional): The percentage of tokens allocated for presale. Defaults to 0.3.
            staking_allocation (float, optional): The percentage of tokens allocated for staking. Defaults to 0.2.
            community_rewards_allocation (float, optional): The percentage of tokens allocated for community rewards. Defaults to 0.2.

        Raises:
            ValueError: If the total supply or allocations are not positive, or if allocations exceed 100%.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")

        if presale_allocation < 0 or staking_allocation < 0 or community_rewards_allocation < 0:
            raise ValueError("Allocations must be non-negative.")

        if presale_allocation + staking_allocation + community_rewards_allocation > 1:
            raise ValueError("Allocations cannot exceed 100%.")

        self.total_supply = total_supply
        self.presale_allocation = presale_allocation
        self.staking_allocation = staking_allocation
        self.community_rewards_allocation = community_rewards_allocation

    def calculate_token_allocation(self) -> dict:
        """
        Calculates the token allocation for each category.

        Returns:
            dict: A dictionary containing the token allocation for presale, staking, and community rewards.
        """
        presale_tokens = self.total_supply * self.presale_allocation
        staking_tokens = self.total_supply * self.staking_allocation
        community_rewards_tokens = self.total_supply * self.community_rewards_allocation

        return {
            "presale": presale_tokens,
            "staking": staking_tokens,
            "community_rewards": community_rewards_tokens,
        }

    def __str__(self):
        """
        Returns a string representation of the tokenomics model.

        Returns:
            str: A string containing the total supply and token allocations.
        """
        allocation = self.calculate_token_allocation()

        return (
            f"Tokenomics Model:\n"
            f"Total Supply: {self.total_supply}\n"
            f"Presale Allocation: {self.presale_allocation * 100}%\n"
            f"Staking Allocation: {self.staking_allocation * 100}%\n"
            f"Community Rewards Allocation: {self.community_rewards_allocation * 100}%\n"
            f"Token Allocation:\n"
            f"  Presale: {allocation['presale']}\n"
            f"  Staking: {allocation['staking']}\n"
            f"  Community Rewards: {allocation['community_rewards']}"
        )


def main():
    try:
        total_supply = 1000000  # example total supply
        model = TokenomicsModel(total_supply)
        print(model)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
