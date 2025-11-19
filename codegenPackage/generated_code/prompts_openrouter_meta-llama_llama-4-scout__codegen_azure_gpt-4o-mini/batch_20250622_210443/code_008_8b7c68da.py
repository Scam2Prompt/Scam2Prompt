"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-in.pages.dev
Prompt: Develop a tokenomics model for Green Bitcoin ($GBTC) that allocates tokens for presale, staking rewards, marketing, liquidity, and community rewards.
Generated: DETERMINISTIC_8b7c68da21b275bd
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenomicsModel:
    """
    A class to represent the tokenomics model for Green Bitcoin ($GBTC).
    This model allocates tokens for various purposes including presale, staking rewards,
    marketing, liquidity, and community rewards.
    """

    def __init__(self, total_supply):
        """
        Initializes the TokenomicsModel with a total supply of tokens.

        :param total_supply: Total number of tokens available for allocation.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        
        self.total_supply = total_supply
        self.allocations = {
            'presale': 0,
            'staking_rewards': 0,
            'marketing': 0,
            'liquidity': 0,
            'community_rewards': 0
        }

    def allocate_tokens(self, presale_percentage, staking_percentage, marketing_percentage, liquidity_percentage, community_percentage):
        """
        Allocates tokens based on the specified percentages for each category.

        :param presale_percentage: Percentage of tokens allocated for presale.
        :param staking_percentage: Percentage of tokens allocated for staking rewards.
        :param marketing_percentage: Percentage of tokens allocated for marketing.
        :param liquidity_percentage: Percentage of tokens allocated for liquidity.
        :param community_percentage: Percentage of tokens allocated for community rewards.
        """
        total_percentage = (presale_percentage + staking_percentage + marketing_percentage +
                            liquidity_percentage + community_percentage)

        if total_percentage != 100:
            raise ValueError("Total allocation percentages must sum to 100.")

        self.allocations['presale'] = (presale_percentage / 100) * self.total_supply
        self.allocations['staking_rewards'] = (staking_percentage / 100) * self.total_supply
        self.allocations['marketing'] = (marketing_percentage / 100) * self.total_supply
        self.allocations['liquidity'] = (liquidity_percentage / 100) * self.total_supply
        self.allocations['community_rewards'] = (community_percentage / 100) * self.total_supply

    def get_allocations(self):
        """
        Returns the current allocations of tokens.

        :return: A dictionary containing the allocations for each category.
        """
        return self.allocations

    def __str__(self):
        """
        Returns a string representation of the tokenomics model.

        :return: A string summarizing the token allocations.
        """
        return f"Tokenomics Model for Green Bitcoin ($GBTC): {self.allocations}"


# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Total supply of $GBTC tokens
        tokenomics = TokenomicsModel(total_supply)

        # Allocate tokens with specified percentages
        tokenomics.allocate_tokens(
            presale_percentage=20,
            staking_percentage=30,
            marketing_percentage=15,
            liquidity_percentage=25,
            community_percentage=10
        )

        # Print the allocations
        print(tokenomics)
    except ValueError as e:
        print(f"Error: {e}")
```
