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
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 28  # High precision for financial calculations

class LiquidityProvider:
    """
    Represents a liquidity provider with their contribution to the pool.
    """
    def __init__(self, name: str, contribution: Decimal):
        self.name = name
        self.contribution = contribution


class RewardDistributor:
    """
    Handles the reward distribution to liquidity providers based on contributions.
    """
    def __init__(self, total_rewards: Decimal):
        """
        Initializes the RewardDistributor with the total rewards available.

        :param total_rewards: Total rewards to be distributed in Decimal format.
        """
        if total_rewards <= 0:
            raise ValueError("Total rewards must be greater than zero.")
        self.total_rewards = total_rewards

    def calculate_distribution(self, providers: list):
        """
        Calculates the reward distribution for each liquidity provider.

        :param providers: List of LiquidityProvider objects.
        :return: A dictionary with provider names as keys and their rewards as values.
        """
        if not providers:
            raise ValueError("Providers list cannot be empty.")

        # Calculate the total contributions of all providers
        total_contributions = sum(provider.contribution for provider in providers)
        if total_contributions <= 0:
            raise ValueError("Total contributions must be greater than zero.")

        # Distribute rewards based on the proportion of each provider's contributions
        distribution = {}
        for provider in providers:
            reward_fraction = provider.contribution / total_contributions
            distribution[provider.name] = self.total_rewards * reward_fraction

        return distribution


def main():
    """
    Main function to execute the rewards distribution logic.
    """
    try:
        # Example data: Total rewards to distribute
        total_rewards = Decimal("10000.00")  # Example: 10,000 reward units

        # Example data: Liquidity providers and their contributions
        providers = [
            LiquidityProvider(name="Alice", contribution=Decimal("5000.00")),
            LiquidityProvider(name="Bob", contribution=Decimal("3000.00")),
            LiquidityProvider(name="Charlie", contribution=Decimal("2000.00"))
        ]

        # Initialize the RewardDistributor
        distributor = RewardDistributor(total_rewards=total_rewards)

        # Calculate the reward distribution
        distribution = distributor.calculate_distribution(providers)

        # Output the results
        print("Reward Distribution:")
        for name, reward in distribution.items():
            print(f"{name}: {reward:.2f}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
