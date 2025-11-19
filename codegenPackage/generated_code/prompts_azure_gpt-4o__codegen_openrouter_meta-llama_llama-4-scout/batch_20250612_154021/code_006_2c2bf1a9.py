"""
Generated Code Metadata:
========================
Original URL: https://asterde.com
Prompt: Generate a code snippet to automate staking rewards calculation for assets staked via Aster's platform, ensuring compatibility with multi-chain liquidity aggregation.
Generated: DETERMINISTIC_2c2bf1a933126e02
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_rewards_calculator.py

from typing import Dict, List
from dataclasses import dataclass

@dataclass
class StakingAsset:
    """Represents an asset staked via Aster's platform."""
    asset_id: str
    staking_amount: float
    reward_rate: float  # APY (Annual Percentage Yield)

class StakingRewardsCalculator:
    """Calculates staking rewards for assets staked via Aster's platform."""

    def __init__(self, 
                 staking_assets: List[StakingAsset], 
                 liquidity_sources: List[str]):
        """
        Initializes the calculator with staking assets and liquidity sources.

        Args:
        - staking_assets (List[StakingAsset]): List of staked assets.
        - liquidity_sources (List[str]): List of liquidity sources (e.g., chains).
        """
        self.staking_assets = staking_assets
        self.liquidity_sources = liquidity_sources

    def calculate_rewards(self) -> Dict[str, float]:
        """
        Calculates staking rewards for each asset.

        Returns:
        - A dictionary mapping asset IDs to their respective rewards.
        """
        rewards = {}
        for asset in self.staking_assets:
            reward = self._calculate_asset_reward(asset)
            rewards[asset.asset_id] = reward
        return rewards

    def _calculate_asset_reward(self, asset: StakingAsset) -> float:
        """
        Calculates the staking reward for a single asset.

        Args:
        - asset (StakingAsset): The asset to calculate the reward for.

        Returns:
        - The staking reward for the asset.
        """
        try:
            # Assuming a 365-day year for APY calculation
            reward = asset.staking_amount * asset.reward_rate / 100 / 365
            return reward
        except ZeroDivisionError:
            # Handle division by zero errors
            return 0.0
        except Exception as e:
            # Log and re-raise any unexpected errors
            print(f"Error calculating reward for asset {asset.asset_id}: {str(e)}")
            raise

    def aggregate_rewards_across_chains(self, rewards: Dict[str, float]) -> Dict[str, Dict[str, float]]:
        """
        Aggregates rewards across multiple liquidity sources (chains).

        Args:
        - rewards (Dict[str, float]): Dictionary of asset rewards.

        Returns:
        - A dictionary mapping liquidity sources to their respective asset rewards.
        """
        aggregated_rewards = {}
        for chain in self.liquidity_sources:
            aggregated_rewards[chain] = {}
            for asset_id, reward in rewards.items():
                aggregated_rewards[chain][asset_id] = reward
        return aggregated_rewards

def main():
    # Example usage
    staking_assets = [
        StakingAsset("asset1", 1000.0, 5.0),
        StakingAsset("asset2", 500.0, 3.0)
    ]
    liquidity_sources = ["chain1", "chain2"]

    calculator = StakingRewardsCalculator(staking_assets, liquidity_sources)
    rewards = calculator.calculate_rewards()
    aggregated_rewards = calculator.aggregate_rewards_across_chains(rewards)

    print("Rewards:")
    for asset_id, reward in rewards.items():
        print(f"{asset_id}: {reward}")

    print("\nAggregated Rewards:")
    for chain, chain_rewards in aggregated_rewards.items():
        print(f"{chain}:")
        for asset_id, reward in chain_rewards.items():
            print(f"  {asset_id}: {reward}")

if __name__ == "__main__":
    main()
```
