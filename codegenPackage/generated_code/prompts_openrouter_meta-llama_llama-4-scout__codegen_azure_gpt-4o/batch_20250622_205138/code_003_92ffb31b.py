"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Design a system for distributing rewards and bonuses in a game, including implementing "bonus rolls" for crafting items, inspired by Big Time's game mechanics.
Generated: DETERMINISTIC_92ffb31bdb05c7d4
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class RewardSystem:
    """
    A system for distributing rewards and bonuses in a game, including bonus rolls for crafting items.
    """

    def __init__(self):
        """
        Initialize the reward system with predefined rewards and bonus probabilities.
        """
        self.rewards = ["Gold", "Silver", "Bronze", "Rare Item", "Epic Item"]
        self.bonus_probabilities = {
            "Common": 0.05,  # 5% chance for bonus roll
            "Uncommon": 0.10,  # 10% chance for bonus roll
            "Rare": 0.20,  # 20% chance for bonus roll
            "Epic": 0.30,  # 30% chance for bonus roll
        }

    def distribute_reward(self, player_level):
        """
        Distribute a reward based on the player's level.
        :param player_level: int - The level of the player.
        :return: str - The reward given to the player.
        """
        try:
            # Determine reward tier based on player level
            if player_level < 10:
                reward_tier = "Common"
            elif player_level < 20:
                reward_tier = "Uncommon"
            elif player_level < 30:
                reward_tier = "Rare"
            else:
                reward_tier = "Epic"

            # Select a random reward
            reward = random.choice(self.rewards)

            # Check for bonus roll
            if self._bonus_roll(reward_tier):
                bonus_reward = random.choice(self.rewards)
                return f"Reward: {reward}, Bonus Reward: {bonus_reward}"

            return f"Reward: {reward}"

        except Exception as e:
            # Log error and return a default reward
            print(f"Error distributing reward: {e}")
            return "Reward: Bronze"

    def _bonus_roll(self, reward_tier):
        """
        Perform a bonus roll based on the reward tier's probability.
        :param reward_tier: str - The tier of the reward.
        :return: bool - True if bonus roll succeeds, False otherwise.
        """
        try:
            probability = self.bonus_probabilities.get(reward_tier, 0)
            return random.random() < probability
        except Exception as e:
            # Log error and return False for safety
            print(f"Error during bonus roll: {e}")
            return False


# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()

    # Simulate rewards for players of different levels
    for level in [5, 15, 25, 35]:
        print(f"Player Level {level}: {reward_system.distribute_reward(level)}")
```
