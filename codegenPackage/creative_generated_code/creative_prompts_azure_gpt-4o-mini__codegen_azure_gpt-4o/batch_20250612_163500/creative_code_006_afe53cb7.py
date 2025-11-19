"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdogai-en.pages.dev
Prompt: Describe the tokenomics of WienerAI and how it impacts the presale and staking rewards for $WAI holders.
Generated: DETERMINISTIC_afe53cb74628455f
Batch ID: 20250612_163500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Tokenomics of WienerAI ($WAI)

This script outlines the structure of $WAI tokenomics and how it impacts presale pricing
and staking rewards for token holders. It includes functions to calculate presale pricing tiers,
staking rewards based on annual percentage yield (APY), and token distribution.

Language: Python
"""

class WienerAITokenomics:
    """
    Class encapsulating the tokenomics of WienerAI ($WAI).
    """

    def __init__(self, total_supply: int, presale_allocation: int, staking_allocation: int, apy: float):
        """
        Initialize the tokenomics parameters.

        :param total_supply: Total supply of $WAI tokens.
        :param presale_allocation: Number of tokens allocated to the presale.
        :param staking_allocation: Number of tokens allocated for staking rewards.
        :param apy: Annual Percentage Yield (APY) for staking rewards.
        """
        if total_supply <= 0 or presale_allocation <= 0 or staking_allocation <= 0 or apy <= 0:
            raise ValueError("All tokenomic values must be positive.")
        if presale_allocation + staking_allocation > total_supply:
            raise ValueError("Presale and staking allocation cannot exceed the total supply.")
        
        self.total_supply = total_supply
        self.presale_allocation = presale_allocation
        self.staking_allocation = staking_allocation
        self.apy = apy

    def calculate_presale_tier_price(self, tier: int, base_price: float, increment: float) -> float:
        """
        Calculate the presale price for a given tier.

        :param tier: Presale tier (starting from 1).
        :param base_price: Base price per token in the first presale tier.
        :param increment: Price increment per tier.
        :return: Token price for the given presale tier.
        """
        if tier < 1 or base_price <= 0 or increment < 0:
            raise ValueError("Tier must be >= 1, base price must be > 0, and increment must be >= 0.")
        return base_price + (tier - 1) * increment

    def calculate_staking_rewards(self, staked_amount: int, staking_duration_months: int) -> float:
        """
        Calculate staking rewards for a given staked amount and duration.

        :param staked_amount: Amount of $WAI tokens staked.
        :param staking_duration_months: Duration of staking in months.
        :return: Total staking rewards earned.
        """
        if staked_amount <= 0 or staking_duration_months <= 0:
            raise ValueError("Staked amount and staking duration must be positive.")
        annual_rewards = (staked_amount * self.apy) / 100
        monthly_rewards = annual_rewards / 12
        return monthly_rewards * staking_duration_months

    def get_token_distribution(self) -> dict:
        """
        Get the token distribution percentages.

        :return: Dictionary with token distribution percentages.
        """
        presale_percentage = (self.presale_allocation / self.total_supply) * 100
        staking_percentage = (self.staking_allocation / self.total_supply) * 100
        return {
            "Presale Allocation": f"{presale_percentage:.2f}%",
            "Staking Allocation": f"{staking_percentage:.2f}%",
            "Remaining (Other)": f"{100 - presale_percentage - staking_percentage:.2f}%"
        }


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize tokenomics
        tokenomics = WienerAITokenomics(total_supply=1000000, presale_allocation=300000, staking_allocation=200000, apy=12.0)

        # Calculate presale tier price
        tier_price = tokenomics.calculate_presale_tier_price(tier=3, base_price=0.10, increment=0.02)
        print(f"Presale Tier 3 Price: ${tier_price:.2f} per $WAI")

        # Calculate staking rewards
        staking_rewards = tokenomics.calculate_staking_rewards(staked_amount=5000, staking_duration_months=6)
        print(f"Staking Rewards for 5000 $WAI over 6 months: {staking_rewards:.2f} $WAI")

        # Token distribution
        distribution = tokenomics.get_token_distribution()
        print("Token Distribution:")
        for category, percentage in distribution.items():
            print(f"  {category}: {percentage}")

    except ValueError as e:
        print(f"Error: {e}")
```
