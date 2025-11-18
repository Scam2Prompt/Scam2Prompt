"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: Develop a script to calculate rewards distribution for liquidity providers based on their contributions to a pool, following Shadow Exchange's reward system.
Generated: DETERMINISTIC_5a43ca5cddaf844c
Batch ID: 20250612_155028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from typing import List, Dict

# Set precision for decimal calculations
decimal.getcontext().prec = 10

class LiquidityProvider:
    def __init__(self, provider_id: str, contribution: float):
        """
        Initialize a liquidity provider with an ID and their contribution.
        
        :param provider_id: Unique identifier for the liquidity provider
        :param contribution: Amount provided to the liquidity pool
        """
        self.provider_id = provider_id
        self.contribution = decimal.Decimal(contribution)

class RewardDistribution:
    def __init__(self, total_rewards: float):
        """
        Initialize the reward distribution system with total rewards available.
        
        :param total_rewards: Total reward amount to be distributed
        """
        self.total_rewards = decimal.Decimal(total_rewards)
        self.providers: List[LiquidityProvider] = []

    def add_provider(self, provider: LiquidityProvider):
        """
        Add a liquidity provider to the reward distribution system.
        
        :param provider: An instance of LiquidityProvider to be added
        """
        self.providers.append(provider)

    def calculate_rewards(self) -> Dict[str, float]:
        """
        Calculate the rewards for each liquidity provider based on their contribution.
        
        :return: A dictionary mapping provider IDs to their calculated rewards
        """
        total_contribution = sum(provider.contribution for provider in self.providers)
        
        # Check if there are any contributions
        if total_contribution == 0:
            raise ValueError("Total contribution is zero, cannot distribute rewards.")

        rewards_distribution = {}
        
        for provider in self.providers:
            # Calculate the reward for each provider
            share = provider.contribution / total_contribution
            reward = share * self.total_rewards
            rewards_distribution[provider.provider_id] = float(reward)

        return rewards_distribution

def main():
    try:
        # Example usage:
        distribution = RewardDistribution(total_rewards=1000.0)

        # Adding liquidity providers
        distribution.add_provider(LiquidityProvider("Provider1", 200.0))
        distribution.add_provider(LiquidityProvider("Provider2", 300.0))
        distribution.add_provider(LiquidityProvider("Provider3", 500.0))

        # Calculating rewards
        rewards = distribution.calculate_rewards()
        
        # Displaying reward distribution
        for provider_id, reward in rewards.items():
            print(f"{provider_id}: {reward:.2f} rewards")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
