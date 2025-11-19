"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Write code to calculate bonus interest shares for Silo Liquidity Providers based on their positions, referencing the Silo Rewards Proposal.
Generated: DETERMINISTIC_0c46ac29a5eff390
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

class SiloLiquidityProvider:
    def __init__(self, id: int, position: float):
        """
        Initialize a Silo Liquidity Provider.

        Args:
        id (int): Unique identifier for the liquidity provider.
        position (float): The liquidity provider's position.
        """
        self.id = id
        self.position = position

class SiloRewardsCalculator:
    def __init__(self, total_rewards: float, total_positions: float):
        """
        Initialize a Silo Rewards Calculator.

        Args:
        total_rewards (float): The total rewards to be distributed.
        total_positions (float): The total positions of all liquidity providers.
        """
        self.total_rewards = total_rewards
        self.total_positions = total_positions

    def calculate_bonus_interest_shares(self, liquidity_providers: List[SiloLiquidityProvider]) -> Dict[int, float]:
        """
        Calculate bonus interest shares for Silo Liquidity Providers.

        Args:
        liquidity_providers (List[SiloLiquidityProvider]): A list of liquidity providers.

        Returns:
        Dict[int, float]: A dictionary mapping liquidity provider IDs to their bonus interest shares.

        Raises:
        ValueError: If the total positions of all liquidity providers is zero.
        """
        if self.total_positions == 0:
            raise ValueError("Total positions of all liquidity providers cannot be zero.")

        bonus_interest_shares = {}
        for provider in liquidity_providers:
            # Calculate the bonus interest share for the current liquidity provider
            bonus_interest_share = (provider.position / self.total_positions) * self.total_rewards
            bonus_interest_shares[provider.id] = bonus_interest_share

        return bonus_interest_shares

def main():
    try:
        # Example usage
        liquidity_providers = [
            SiloLiquidityProvider(1, 1000),
            SiloLiquidityProvider(2, 2000),
            SiloLiquidityProvider(3, 3000),
        ]

        total_rewards = 10000
        total_positions = sum(provider.position for provider in liquidity_providers)

        calculator = SiloRewardsCalculator(total_rewards, total_positions)
        bonus_interest_shares = calculator.calculate_bonus_interest_shares(liquidity_providers)

        print("Bonus Interest Shares:")
        for provider_id, share in bonus_interest_shares.items():
            print(f"Provider {provider_id}: {share}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
