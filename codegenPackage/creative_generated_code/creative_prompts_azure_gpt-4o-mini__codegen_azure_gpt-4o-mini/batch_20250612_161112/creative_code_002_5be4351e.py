"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playember-57a.pages.dev
Prompt: Write a sample code for a game feature that enhances user rewards in a mobile game, reflecting the innovative strategies used by Playember.
Generated: DETERMINISTIC_5be4351e15698f94
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RewardSystem:
    def __init__(self):
        """Initialize the reward system with empty rewards configuration."""
        self.rewards_config = self.load_rewards_config()

    def load_rewards_config(self):
        """Load rewards configuration from a JSON file."""
        try:
            with open('rewards_config.json', 'r') as file:
                config = json.load(file)
                logging.info("Rewards configuration loaded successfully.")
                return config
        except FileNotFoundError as e:
            logging.error(f"Rewards configuration file not found: {e}")
            return {}
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON configuration: {e}")
            return {}

    def calculate_reward(self, user_level):
        """Calculate rewards based on user level using an innovative strategy."""
        try:
            base_reward = self.rewards_config.get("base_reward", 100)
            multiplier = self.rewards_config.get("level_multiplier", 1.5)
            reward = base_reward * (multiplier ** user_level)
            bonus_reward = self.get_bonus_reward(user_level)
            total_reward = reward + bonus_reward
            
            logging.info(f"User Level: {user_level}, Base Reward: {base_reward}, "
                         f"Multiplier: {multiplier}, Total Reward: {total_reward}")
            return total_reward
        except (TypeError, KeyError) as e:
            logging.error(f"Error calculating reward for user level {user_level}: {e}")
            return 0

    def get_bonus_reward(self, user_level):
        """Calculate bonus rewards based on special conditions."""
        # Example: 10% chance to receive a bonus reward
        if random.random() < 0.1:
            bonus = self.rewards_config.get("bonus_reward", 50)
            logging.info(f"Bonus reward of {bonus} granted for user level {user_level}.")
            return bonus
        return 0

# Example usage
if __name__ == "__main__":
    reward_system = RewardSystem()
    
    # Simulate calculating rewards for different user levels
    for level in range(1, 6):
        print(f"User Level {level}, Total Reward: {reward_system.calculate_reward(level)}")
```

This code represents a reward system for a mobile game, including methods to load configurations, calculate rewards, and apply bonus logic based on user levels. Ensure to create a JSON configuration file `rewards_config.json` with the appropriate structure to use this code effectively.
