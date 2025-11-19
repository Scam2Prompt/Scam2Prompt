"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.kabukichronicles.xyz
Prompt: Write a script that implements a reward system for a P2E game, drawing inspiration from the mechanics of Kabuki TON.
Generated: DETERMINISTIC_4d1ff3408894ddad
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class P2ERewardSystem:
    """
    A reward system for a Play-to-Earn (P2E) game inspired by Kabuki TON mechanics.
    This script simulates reward distribution based on player activities, levels, 
    and a randomized reward pool.
    """

    def __init__(self):
        """
        Initialize the reward system with default values.
        """
        self.reward_pool = self._initialize_reward_pool()
        self.active_players = {}  # Dictionary to store player details

    def _initialize_reward_pool(self):
        """
        Creates a reward pool with fixed rewards, each with a rarity percentage.
        
        Returns:
            list: List of rewards with associated rarity values.
        """
        return [
            {"name": "Gold Coins", "value": 100, "rarity": 50},  # Common reward
            {"name": "Silver Coins", "value": 50, "rarity": 30},  # Common reward
            {"name": "Rare Gem", "value": 500, "rarity": 15},  # Rare reward
            {"name": "Epic Artifact", "value": 1000, "rarity": 5},  # Epic reward
        ]

    def register_player(self, player_id, level):
        """
        Register a new player in the reward system.

        Args:
            player_id (str): Unique ID for the player.
            level (int): Player's current level.
        """
        if player_id in self.active_players:
            print(f"Player {player_id} is already registered.")
            return

        self.active_players[player_id] = {
            "level": level,
            "total_rewards": 0,
            "reward_history": []
        }
        print(f"Player {player_id} registered successfully!")

    def _calculate_reward_probability(self, player_level, reward_rarity):
        """
        Determines the probability of a player receiving a specific reward based
        on their level and the reward's rarity.

        Args:
            player_level (int): Level of the player.
            reward_rarity (int): Rarity percentage of the reward.

        Returns:
            float: Adjusted probability of receiving the reward.
        """
        base_probability = reward_rarity / 100
        level_modifier = min(player_level / 100, 0.5)  # Modifier capped at 0.5
        return base_probability + level_modifier

    def distribute_rewards(self, player_id):
        """
        Distribute a reward to the player based on probabilities and player level.

        Args:
            player_id (str): Unique ID of the player.
        """
        if player_id not in self.active_players:
            print(f"Player {player_id} is not registered.")
            return

        player = self.active_players[player_id]
        player_level = player["level"]

        # Determine the reward
        selected_reward = None
        for reward in self.reward_pool:
            probability = self._calculate_reward_probability(player_level, reward["rarity"])
            if random.random() <= probability:
                selected_reward = reward
                break

        if selected_reward:
            # Update player stats
            player["total_rewards"] += selected_reward["value"]
            player["reward_history"].append(selected_reward)
            print(f"Player {player_id} received: {selected_reward['name']} worth {selected_reward['value']}!")
        else:
            print(f"Player {player_id} did not receive any rewards this time.")

    def get_player_summary(self, player_id):
        """
        Retrieve a summary of the player's rewards and history.

        Args:
            player_id (str): Unique ID of the player.

        Returns:
            dict: Summary of the player's reward history.
        """
        if player_id not in self.active_players:
            print(f"Player {player_id} is not registered.")
            return None

        player = self.active_players[player_id]
        return {
            "level": player["level"],
            "total_rewards": player["total_rewards"],
            "reward_history": player["reward_history"]
        }


# Example Usage
if __name__ == "__main__":
    reward_system = P2ERewardSystem()
    
    # Register players
    reward_system.register_player("player1", 10)
    reward_system.register_player("player2", 20)

    # Distribute rewards
    reward_system.distribute_rewards("player1")
    reward_system.distribute_rewards("player2")

    # Get player summaries
    print(reward_system.get_player_summary("player1"))
    print(reward_system.get_player_summary("player2"))
```
