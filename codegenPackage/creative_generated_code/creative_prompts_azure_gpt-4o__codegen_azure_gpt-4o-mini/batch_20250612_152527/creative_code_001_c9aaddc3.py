"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-xai-games.pages.dev
Prompt: Generate a script that calculates the reward success multiplier based on the esXAI staking tiers (Bronze, Silver, Gold, Platinum, Diamond) as outlined on the Xai Staking webpage.
Generated: DETERMINISTIC_c9aaddc3c33548ec
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingTier:
    """Class representing a staking tier and its reward multiplier."""

    def __init__(self, name: str, multiplier: float):
        """
        Initializes a new StakingTier.

        :param name: The name of the staking tier.
        :param multiplier: The reward multiplier for this tier.
        """
        self.name = name
        self.multiplier = multiplier


class RewardCalculator:
    """Class to calculate the reward success multiplier based on staking tiers."""

    def __init__(self):
        """Initializes the RewardCalculator with predefined tiers."""
        self.tiers = {
            "Bronze": StakingTier("Bronze", 1.0),
            "Silver": StakingTier("Silver", 1.5),
            "Gold": StakingTier("Gold", 2.0),
            "Platinum": StakingTier("Platinum", 2.5),
            "Diamond": StakingTier("Diamond", 3.0),
        }

    def get_multiplier(self, tier_name: str) -> float:
        """
        Gets the reward multiplier for a given staking tier.

        :param tier_name: The name of the staking tier.
        :return: The reward multiplier for the specified tier.
        :raises ValueError: If the tier name is invalid.
        """
        try:
            tier = self.tiers[tier_name]
            return tier.multiplier
        except KeyError:
            raise ValueError(f"Invalid staking tier: '{tier_name}'. Valid tiers are {list(self.tiers.keys())}.")

    def calculate_reward(self, tier_name: str, base_reward: float) -> float:
        """
        Calculates the total reward based on the staking tier and base reward.

        :param tier_name: The name of the staking tier.
        :param base_reward: The base reward amount.
        :return: The calculated total reward based on the tier multiplier.
        :raises ValueError: If the tier name is invalid.
        """
        multiplier = self.get_multiplier(tier_name)
        return base_reward * multiplier


def main():
    """Main function to demonstrate the reward calculation."""
    try:
        # Example usage of the RewardCalculator
        calculator = RewardCalculator()

        # Define a base reward amount
        base_reward = 100.0  # Example base reward

        # Specify the desired staking tier
        tier_name = "Gold"  # Change this to test other tiers

        # Calculate the total reward
        total_reward = calculator.calculate_reward(tier_name, base_reward)
        
        print(f"The total reward for tier '{tier_name}' is: {total_reward:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
