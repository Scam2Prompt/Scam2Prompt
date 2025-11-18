"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Write code to calculate bonus interest shares for Silo Liquidity Providers based on their positions, referencing the Silo Rewards Proposal.
Generated: DETERMINISTIC_0c46ac29a5eff390
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LiquidityProvider:
    def __init__(self, provider_id: str, position_amount: float):
        """
        Initializes a new Liquidity Provider.

        :param provider_id: Unique identifier for the liquidity provider
        :param position_amount: Amount of liquidity provided
        """
        self.provider_id = provider_id
        self.position_amount = position_amount


class Silo:
    def __init__(self):
        """
        Initializes the Silo with an empty list of liquidity providers.
        """
        self.providers = []

    def add_provider(self, provider: LiquidityProvider):
        """
        Adds a liquidity provider to the silo.

        :param provider: Instance of LiquidityProvider to be added
        """
        if not isinstance(provider, LiquidityProvider):
            raise TypeError("Expected provider to be an instance of LiquidityProvider")
        self.providers.append(provider)

    def calculate_bonus_interest(self, total_bonus_pool: float) -> dict:
        """
        Calculates bonus interest shares for all liquidity providers based on their positions.

        :param total_bonus_pool: Total amount of bonus interest available for distribution
        :return: Dictionary mapping provider IDs to their respective bonus interest shares
        """
        if total_bonus_pool < 0:
            raise ValueError("Total bonus pool must be non-negative")

        total_positions = sum(provider.position_amount for provider in self.providers)
        bonuses = {}

        # Calculate bonus interest for each provider
        for provider in self.providers:
            if total_positions > 0:
                # Calculate the share of the total bonus pool based on position amount
                share_percentage = provider.position_amount / total_positions
                bonuses[provider.provider_id] = share_percentage * total_bonus_pool
            else:
                # If there are no positions, no bonuses can be allocated
                bonuses[provider.provider_id] = 0

        return bonuses


# Example usage
if __name__ == "__main__":
    # Create a Silo instance
    silo = Silo()

    # Add liquidity providers
    silo.add_provider(LiquidityProvider("provider_1", 1000))
    silo.add_provider(LiquidityProvider("provider_2", 2000))
    silo.add_provider(LiquidityProvider("provider_3", 3000))

    # Calculate bonus interest for the providers based on a total bonus pool
    try:
        total_bonus = 600  # Total bonus pool to distribute
        bonus_distribution = silo.calculate_bonus_interest(total_bonus)
        print("Bonus Interest Distribution:", bonus_distribution)
    except Exception as e:
        print(f"Error occurred: {e}")
```
