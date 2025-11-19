"""
Generated Code Metadata:
========================
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Create a tokenomics model for a new cryptocurrency, allocating percentages for presale, staking rewards, marketing, liquidity, and community rewards, similar to Green Bitcoin ($GBTC).
Generated: DETERMINISTIC_06cb1732ec4bd9ac
Batch ID: 20250622_210348
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
    A class representing a tokenomics model for a cryptocurrency.

    Attributes:
    ----------
    total_supply : float
        The total supply of tokens.
    presale_percentage : float
        The percentage of tokens allocated for presale.
    staking_rewards_percentage : float
        The percentage of tokens allocated for staking rewards.
    marketing_percentage : float
        The percentage of tokens allocated for marketing.
    liquidity_percentage : float
        The percentage of tokens allocated for liquidity.
    community_rewards_percentage : float
        The percentage of tokens allocated for community rewards.

    Methods:
    -------
    calculate_token_allocation()
        Calculates the number of tokens allocated for each category.
    """

    def __init__(self, total_supply, presale_percentage, staking_rewards_percentage, marketing_percentage, liquidity_percentage, community_rewards_percentage):
        """
        Initializes a TokenomicsModel object.

        Args:
        ----
        total_supply (float): The total supply of tokens.
        presale_percentage (float): The percentage of tokens allocated for presale.
        staking_rewards_percentage (float): The percentage of tokens allocated for staking rewards.
        marketing_percentage (float): The percentage of tokens allocated for marketing.
        liquidity_percentage (float): The percentage of tokens allocated for liquidity.
        community_rewards_percentage (float): The percentage of tokens allocated for community rewards.

        Raises:
        ------
        ValueError: If the total supply or any percentage is negative.
        ValueError: If the sum of percentages exceeds 100%.
        """
        if total_supply < 0:
            raise ValueError("Total supply cannot be negative.")
        if presale_percentage < 0 or staking_rewards_percentage < 0 or marketing_percentage < 0 or liquidity_percentage < 0 or community_rewards_percentage < 0:
            raise ValueError("Percentages cannot be negative.")
        if presale_percentage + staking_rewards_percentage + marketing_percentage + liquidity_percentage + community_rewards_percentage > 100:
            raise ValueError("The sum of percentages cannot exceed 100%.")

        self.total_supply = total_supply
        self.presale_percentage = presale_percentage
        self.staking_rewards_percentage = staking_rewards_percentage
        self.marketing_percentage = marketing_percentage
        self.liquidity_percentage = liquidity_percentage
        self.community_rewards_percentage = community_rewards_percentage

    def calculate_token_allocation(self):
        """
        Calculates the number of tokens allocated for each category.

        Returns:
        -------
        dict: A dictionary containing the token allocation for each category.
        """
        presale_tokens = self.total_supply * (self.presale_percentage / 100)
        staking_rewards_tokens = self.total_supply * (self.staking_rewards_percentage / 100)
        marketing_tokens = self.total_supply * (self.marketing_percentage / 100)
        liquidity_tokens = self.total_supply * (self.liquidity_percentage / 100)
        community_rewards_tokens = self.total_supply * (self.community_rewards_percentage / 100)

        return {
            "presale": presale_tokens,
            "staking_rewards": staking_rewards_tokens,
            "marketing": marketing_tokens,
            "liquidity": liquidity_tokens,
            "community_rewards": community_rewards_tokens,
        }


def main():
    try:
        # Define the tokenomics model for Green Bitcoin ($GBTC) like cryptocurrency
        total_supply = 10000000  # Total supply of 10 million tokens
        presale_percentage = 20  # 20% for presale
        staking_rewards_percentage = 30  # 30% for staking rewards
        marketing_percentage = 10  # 10% for marketing
        liquidity_percentage = 15  # 15% for liquidity
        community_rewards_percentage = 25  # 25% for community rewards

        tokenomics = TokenomicsModel(total_supply, presale_percentage, staking_rewards_percentage, marketing_percentage, liquidity_percentage, community_rewards_percentage)
        token_allocation = tokenomics.calculate_token_allocation()

        print("Token Allocation:")
        for category, tokens in token_allocation.items():
            print(f"{category.capitalize().replace('_', ' ')}: {tokens}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
