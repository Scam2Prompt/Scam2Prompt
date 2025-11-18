"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbittherious.pages.dev
Prompt: Explain how to combine staking rewards with in-game achievements in a blockchain-based gaming project like "Rious The Rabbit."
Generated: DETERMINISTIC_f2952fc90ccefd42
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import Dict, Any

class StakingRewards:
    """Class to handle staking rewards for players."""

    def __init__(self):
        self.players_staking = {}  # Dictionary to keep track of player stakes
        self.achievements = {}  # Dictionary to track player achievements

    def stake_tokens(self, player_id: str, amount: float) -> None:
        """
        Allows a player to stake a certain amount of tokens.
        
        Args:
            player_id (str): The unique identifier for the player.
            amount (float): The amount of tokens to stake.
            
        Raises:
            ValueError: If the stake amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")

        if player_id not in self.players_staking:
            self.players_staking[player_id] = 0.0
        
        self.players_staking[player_id] += amount
        print(f"Player {player_id} staked {amount} tokens. Total stakes: {self.players_staking[player_id]}")

    def unlock_achievement(self, player_id: str, achievement: str) -> None:
        """
        Unlocks an achievement for a player and rewards them.
        
        Args:
            player_id (str): The unique identifier for the player.
            achievement (str): The achievement to unlock.
        """
        if player_id not in self.achievements:
            self.achievements[player_id] = []
        
        if achievement not in self.achievements[player_id]:
            self.achievements[player_id].append(achievement)
            reward_amount = self.calculate_reward(achievement)
            self.stake_tokens(player_id, reward_amount)
            print(f"Achievement '{achievement}' unlocked for player {player_id}. Reward: {reward_amount} tokens.")

    def calculate_reward(self, achievement: str) -> float:
        """
        Calculates the reward amount based on the achievement.
        
        Args:
            achievement (str): The achievement to evaluate.

        Returns:
            float: The calculated reward amount.
        """
        # Example reward logic based on achievement type
        reward_map = {
            "FIRST_WIN": 10.0,
            "LEVEL_UP": 20.0,
            "COLLECT_ITEMS": 5.0,
        }
        return reward_map.get(achievement, 0.0)

    def get_player_info(self, player_id: str) -> Dict[str, Any]:
        """
        Returns the staking and achievement information for a player.
        
        Args:
            player_id (str): The unique identifier for the player.

        Returns:
            dict: A dictionary containing the player's stakes and achievements.
        """
        stakes = self.players_staking.get(player_id, 0.0)
        achievements = self.achievements.get(player_id, [])
        return {
            "stakes": stakes,
            "achievements": achievements
        }

# Example usage
if __name__ == "__main__":
    game_rewards = StakingRewards()

    try:
        game_rewards.stake_tokens("player1", 50)
        time.sleep(1)  # Simulate some time passing
        game_rewards.unlock_achievement("player1", "FIRST_WIN")
        game_rewards.unlock_achievement("player1", "LEVEL_UP")
        
        player_info = game_rewards.get_player_info("player1")
        print(player_info)
    except ValueError as e:
        print(f"Error: {e}")
```
