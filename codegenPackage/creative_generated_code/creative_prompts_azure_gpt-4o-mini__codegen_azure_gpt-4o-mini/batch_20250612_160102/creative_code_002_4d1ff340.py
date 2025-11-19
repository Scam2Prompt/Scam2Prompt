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
import json
from typing import List, Dict

class RewardSystem:
    def __init__(self):
        """Initialize the Reward System with a base reward structure."""
        self.base_rewards = {
            "win": 10,
            "lose": 0,
            "draw": 5,
        }
        self.players = {}

    def register_player(self, player_id: str) -> None:
        """Register a new player in the reward system."""
        if player_id in self.players:
            raise ValueError(f"Player '{player_id}' already registered.")
        self.players[player_id] = {"points": 0, "games_played": 0}
        print(f"Player '{player_id}' registered successfully.")

    def record_game_result(self, player_id: str, result: str) -> None:
        """Record the result of a game for a player."""
        if player_id not in self.players:
            raise ValueError(f"Player '{player_id}' not found.")
        
        if result not in self.base_rewards:
            raise ValueError(f"Invalid game result: '{result}'. Expected one of {list(self.base_rewards.keys())}.")

        # Update player's points and games played
        reward = self.base_rewards[result]
        self.players[player_id]["points"] += reward
        self.players[player_id]["games_played"] += 1
        print(f"Game result '{result}' recorded for player '{player_id}'. Reward: {reward} points.")

    def get_player_info(self, player_id: str) -> Dict:
        """Retrieve the information of a specific player."""
        if player_id not in self.players:
            raise ValueError(f"Player '{player_id}' not found.")
        return self.players[player_id]

    def get_leaderboard(self) -> List[Dict]:
        """Return a leaderboard sorted by points."""
        leaderboard = sorted(self.players.items(), key=lambda item: item[1]['points'], reverse=True)
        return [{"player_id": player_id, "points": info["points"], "games_played": info["games_played"]} for player_id, info in leaderboard]

    def save_to_file(self, filename: str) -> None:
        """Save the current state of the reward system to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.players, file, indent=4)
            print(f"Data saved to '{filename}' successfully.")
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the state of the reward system from a JSON file."""
        try:
            with open(filename, 'r') as file:
                self.players = json.load(file)
            print(f"Data loaded from '{filename}' successfully.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from file: {e}")

# Example usage:
if __name__ == "__main__":
    reward_system = RewardSystem()
    
    # Register players
    try:
        reward_system.register_player("player1")
        reward_system.register_player("player2")
        
        # Record game results
        reward_system.record_game_result("player1", "win")
        reward_system.record_game_result("player2", "lose")
        reward_system.record_game_result("player1", "draw")

        # Get player info and leaderboard
        print(reward_system.get_player_info("player1"))
        print(reward_system.get_leaderboard())

        # Save and load data
        reward_system.save_to_file("reward_system_data.json")
        reward_system.load_from_file("reward_system_data.json")

    except ValueError as e:
        print(f"Error: {e}")
```
