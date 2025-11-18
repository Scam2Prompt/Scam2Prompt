"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soonverse.pages.dev
Prompt: Write a function in Python to simulate the play-to-earn model described in SoonVerse, including calculations for rewards based on player activity.
Generated: DETERMINISTIC_f83be7a6c593f996
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class PlayToEarnModel:
    """
    A class that simulates the play-to-earn model for a game.
    Players earn rewards based on their activity and engagement levels.
    """

    def __init__(self, base_reward_per_action: float = 0.1, max_daily_actions: int = 100):
        """
        Initializes the play-to-earn model.
        
        :param base_reward_per_action: The base reward (e.g., in tokens) given per action performed.
        :param max_daily_actions: The maximum number of actions a player can perform per day.
        """
        self.base_reward_per_action = base_reward_per_action
        self.max_daily_actions = max_daily_actions

    def calculate_rewards(self, player_activity: dict) -> dict:
        """
        Calculates the daily rewards for players based on their activity.
        
        :param player_activity: A dictionary where keys are player IDs and values are the number of actions performed by the player in a day.
                                Example: {"player_1": 80, "player_2": 120}
        :return: A dictionary where keys are player IDs and values are the rewards they earned.
        """
        player_rewards = {}

        for player_id, actions in player_activity.items():
            try:
                # Cap actions at the maximum allowed daily actions
                actions_capped = min(actions, self.max_daily_actions)

                # Calculate rewards based on capped actions
                reward = actions_capped * self.base_reward_per_action
                
                # Store the calculated reward for the player
                player_rewards[player_id] = reward

            except Exception as e:
                # Log error and set reward to 0 for the player
                print(f"Error calculating rewards for player {player_id}: {e}")
                player_rewards[player_id] = 0
        
        return player_rewards

    def simulate_daily_activity(self, num_players: int) -> dict:
        """
        Simulates daily activity for a given number of players.
        
        :param num_players: The number of players in the simulation.
        :return: A dictionary with simulated player activity.
        """
        simulated_activity = {}
        
        for player_id in range(1, num_players + 1):
            # Randomize the number of actions performed by each player (between 0 and 150)
            simulated_actions = random.randint(0, 150)
            simulated_activity[f"player_{player_id}"] = simulated_actions
        
        return simulated_activity


# Example usage
if __name__ == "__main__":
    # Initialize the play-to-earn model
    play_to_earn = PlayToEarnModel(base_reward_per_action=0.2, max_daily_actions=100)
    
    # Simulate daily activity for 10 players
    daily_activity = play_to_earn.simulate_daily_activity(num_players=10)
    print("Simulated Player Activity:", daily_activity)
    
    # Calculate rewards based on the simulated activity
    rewards = play_to_earn.calculate_rewards(daily_activity)
    print("Calculated Player Rewards:", rewards)
```
