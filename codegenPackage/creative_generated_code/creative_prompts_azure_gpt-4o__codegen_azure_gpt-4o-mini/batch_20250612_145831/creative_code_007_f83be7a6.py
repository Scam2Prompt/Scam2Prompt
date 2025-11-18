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

class Player:
    """Represents a player in the play-to-earn model."""
    
    def __init__(self, player_id):
        """
        Initialize a new player with an ID and no rewards.
        
        Args:
            player_id (str): Unique identifier for the player.
        """
        self.player_id = player_id
        self.activity_score = 0
        self.rewards = 0.0

    def perform_activity(self):
        """
        Simulates a player's activity, which increases their activity score.
        The activity score is a random value between 1 and 10.
        """
        activity_gain = random.randint(1, 10)
        self.activity_score += activity_gain
        print(f"Player {self.player_id} performed an activity, gaining {activity_gain} points.")

    def calculate_rewards(self):
        """
        Calculates rewards based on the player's activity score.
        Rewards are calculated as 0.1 times the activity score.
        """
        reward_multiplier = 0.1
        self.rewards = self.activity_score * reward_multiplier
        print(f"Player {self.player_id}'s rewards calculated: {self.rewards:.2f}")

    def reset_activity(self):
        """Resets the player's activity score for a new round."""
        self.activity_score = 0
        print(f"Player {self.player_id}'s activity score reset.")

def simulate_play_to_earn(num_players, num_activities):
    """
    Simulates the play-to-earn model for a specified number of players and activities.
    
    Args:
        num_players (int): Number of players participating in the simulation.
        num_activities (int): Number of activities each player will perform.
    
    Returns:
        list: A list of tuples containing player IDs and their corresponding rewards.
    """
    players = [Player(player_id=f'Player_{i+1}') for i in range(num_players)]
    results = []

    for activity in range(num_activities):
        print(f"\n--- Activity Round {activity + 1} ---")
        for player in players:
            player.perform_activity()

    for player in players:
        player.calculate_rewards()
        results.append((player.player_id, player.rewards))
        player.reset_activity()

    return results

if __name__ == "__main__":
    try:
        # Number of players and activities to simulate
        num_players = 5
        num_activities = 3

        # Run the simulation
        final_results = simulate_play_to_earn(num_players, num_activities)
        print("\n--- Final Rewards ---")
        for player_id, reward in final_results:
            print(f"{player_id}: {reward:.2f} rewards")
    
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
