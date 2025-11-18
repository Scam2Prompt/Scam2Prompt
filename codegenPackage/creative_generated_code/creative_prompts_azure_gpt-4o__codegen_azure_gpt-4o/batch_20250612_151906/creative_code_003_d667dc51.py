"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-io.web.app
Prompt: Create a tokenomics model in Python for a utility token like Everlodge's $ELDG, including calculations for presale stages, bonuses, and rewards distribution.
Generated: DETERMINISTIC_d667dc51b8d2d462
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class TokenomicsModel:
    """
    A tokenomics model for a utility token, including presale stages, bonuses, 
    and rewards distribution calculations.
    """
    def __init__(self, total_supply: int):
        """
        Initializes the tokenomics model.
        
        :param total_supply: Total supply of the token in units.
        """
        self.total_supply = total_supply
        self.presale_stages = []
        self.bonus_tiers = []
        self.rewards_pool = 0
        self.allocated_supply = 0  # Tracks the allocated tokens during presale and rewards

    def add_presale_stage(self, stage_name: str, allocation_percentage: float, price_per_token: float):
        """
        Adds a presale stage with allocation percentage and token price.
        
        :param stage_name: Name of the presale stage.
        :param allocation_percentage: Percentage of total supply allocated for this stage.
        :param price_per_token: Price per token for this stage.
        """
        # Validate inputs
        if allocation_percentage <= 0 or allocation_percentage > 100:
            raise ValueError("Allocation percentage must be between 0 and 100.")
        if price_per_token <= 0:
            raise ValueError("Price per token must be positive.")
        
        allocation = math.floor((allocation_percentage / 100) * self.total_supply)
        if self.allocated_supply + allocation > self.total_supply:
            raise ValueError("Allocation exceeds total supply.")
        
        self.presale_stages.append({
            "stage_name": stage_name,
            "allocation": allocation,
            "price_per_token": price_per_token
        })
        self.allocated_supply += allocation

    def add_bonus_tier(self, tier_name: str, purchase_threshold: int, bonus_percentage: float):
        """
        Adds a bonus tier for presale purchases.
        
        :param tier_name: Name of the bonus tier.
        :param purchase_threshold: Minimum number of tokens purchased to qualify for the bonus.
        :param bonus_percentage: Bonus percentage of purchased tokens.
        """
        if purchase_threshold <= 0:
            raise ValueError("Purchase threshold must be positive.")
        if bonus_percentage < 0 or bonus_percentage > 100:
            raise ValueError("Bonus percentage must be between 0 and 100.")
        
        self.bonus_tiers.append({
            "tier_name": tier_name,
            "purchase_threshold": purchase_threshold,
            "bonus_percentage": bonus_percentage
        })

    def allocate_rewards_pool(self, allocation_percentage: float):
        """
        Allocates a percentage of the total supply to the rewards pool.
        
        :param allocation_percentage: Percentage of total supply allocated for rewards.
        """
        if allocation_percentage <= 0 or allocation_percentage > 100:
            raise ValueError("Allocation percentage must be between 0 and 100.")
        
        allocation = math.floor((allocation_percentage / 100) * self.total_supply)
        if self.allocated_supply + allocation > self.total_supply:
            raise ValueError("Allocation exceeds total supply.")
        
        self.rewards_pool += allocation
        self.allocated_supply += allocation

    def calculate_bonus(self, tokens_purchased: int):
        """
        Calculates the bonus tokens based on the purchase amount and bonus tiers.
        
        :param tokens_purchased: Number of tokens purchased.
        :return: Total bonus tokens earned.
        """
        bonus_tokens = 0
        for tier in self.bonus_tiers:
            if tokens_purchased >= tier["purchase_threshold"]:
                bonus_tokens += math.floor((tier["bonus_percentage"] / 100) * tokens_purchased)
        return bonus_tokens

    def get_summary(self):
        """
        Provides a summary of the tokenomics model.
        
        :return: Dictionary containing the summary details.
        """
        return {
            "total_supply": self.total_supply,
            "allocated_supply": self.allocated_supply,
            "remaining_supply": self.total_supply - self.allocated_supply,
            "presale_stages": self.presale_stages,
            "bonus_tiers": self.bonus_tiers,
            "rewards_pool": self.rewards_pool
        }

# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the tokenomics model with a total supply of 1,000,000 tokens
        tokenomics = TokenomicsModel(total_supply=1_000_000)

        # Add presale stages
        tokenomics.add_presale_stage(stage_name="Stage 1", allocation_percentage=30, price_per_token=0.01)
        tokenomics.add_presale_stage(stage_name="Stage 2", allocation_percentage=20, price_per_token=0.02)

        # Add bonus tiers
        tokenomics.add_bonus_tier(tier_name="Bronze", purchase_threshold=500, bonus_percentage=5)
        tokenomics.add_bonus_tier(tier_name="Silver", purchase_threshold=1000, bonus_percentage=10)
        tokenomics.add_bonus_tier(tier_name="Gold", purchase_threshold=5000, bonus_percentage=20)

        # Allocate rewards pool
        tokenomics.allocate_rewards_pool(allocation_percentage=10)

        # Calculate bonus for a sample purchase
        tokens_purchased = 1200
        bonus = tokenomics.calculate_bonus(tokens_purchased)
        print(f"Tokens purchased: {tokens_purchased}, Bonus tokens: {bonus}")

        # Get and print summary
        summary = tokenomics.get_summary()
        print("Tokenomics Summary:", summary)

    except Exception as e:
        print(f"Error: {e}")
```
