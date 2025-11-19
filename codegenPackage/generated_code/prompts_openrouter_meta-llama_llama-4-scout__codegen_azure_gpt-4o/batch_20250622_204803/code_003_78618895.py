"""
Generated Code Metadata:
========================
Original URL: https://pepe-buy.pages.dev
Prompt: Design a tokenomics system for a new meme coin ecosystem, inspired by Pepe Unchained's allocation of 20% for presale, 30% for staking rewards, and 20% for marketing.
Generated: DETERMINISTIC_78618895e50dc820
Batch ID: 20250622_204803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tokenomics_system.py

class TokenomicsSystem:
    """
    A class to manage the tokenomics of a meme coin ecosystem.
    Inspired by Pepe Unchained's allocation strategy.
    """

    def __init__(self, total_supply):
        """
        Initialize the tokenomics system with the total supply of tokens.

        :param total_supply: The total supply of tokens in the ecosystem.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0,
            "staking_rewards": 0,
            "marketing": 0,
            "liquidity_pool": 0,
            "team": 0,
        }

    def allocate_tokens(self, presale_pct, staking_rewards_pct, marketing_pct, liquidity_pool_pct, team_pct):
        """
        Allocate tokens based on the specified percentages.

        :param presale_pct: Percentage of tokens allocated for presale.
        :param staking_rewards_pct: Percentage of tokens allocated for staking rewards.
        :param marketing_pct: Percentage of tokens allocated for marketing.
        :param liquidity_pool_pct: Percentage of tokens allocated for liquidity pool.
        :param team_pct: Percentage of tokens allocated for the team.
        """
        total_pct = presale_pct + staking_rewards_pct + marketing_pct + liquidity_pool_pct + team_pct

        # Ensure the total allocation does not exceed 100%
        if total_pct != 100:
            raise ValueError("Total allocation percentages must equal 100%.")

        # Calculate token allocations
        self.allocations["presale"] = self._calculate_allocation(presale_pct)
        self.allocations["staking_rewards"] = self._calculate_allocation(staking_rewards_pct)
        self.allocations["marketing"] = self._calculate_allocation(marketing_pct)
        self.allocations["liquidity_pool"] = self._calculate_allocation(liquidity_pool_pct)
        self.allocations["team"] = self._calculate_allocation(team_pct)

    def _calculate_allocation(self, percentage):
        """
        Calculate the number of tokens for a given percentage.

        :param percentage: The percentage of the total supply to allocate.
        :return: The number of tokens allocated.
        """
        return int((percentage / 100) * self.total_supply)

    def get_allocation(self, category):
        """
        Get the token allocation for a specific category.

        :param category: The category to retrieve the allocation for.
        :return: The number of tokens allocated to the category.
        """
        if category not in self.allocations:
            raise ValueError(f"Invalid category: {category}")
        return self.allocations[category]

    def display_allocations(self):
        """
        Display the token allocations for all categories.
        """
        print("Token Allocations:")
        for category, amount in self.allocations.items():
            print(f"  {category.capitalize()}: {amount} tokens")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tokenomics system with a total supply of 1,000,000 tokens
        total_supply = 1_000_000
        tokenomics = TokenomicsSystem(total_supply)

        # Allocate tokens based on the specified percentages
        tokenomics.allocate_tokens(
            presale_pct=20,          # 20% for presale
            staking_rewards_pct=30,  # 30% for staking rewards
            marketing_pct=20,        # 20% for marketing
            liquidity_pool_pct=20,   # 20% for liquidity pool
            team_pct=10              # 10% for the team
        )

        # Display the allocations
        tokenomics.display_allocations()

    except ValueError as e:
        print(f"Error: {e}")
```
