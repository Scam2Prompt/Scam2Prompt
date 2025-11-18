"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flipperzerobase-presales.pages.dev
Prompt: Write code to implement a feature that tracks player progress and rewards in an NFT treasure hunt game, inspired by Flipper Zero's gameplay mechanics.
Generated: DETERMINISTIC_4b8b9bf2b8b3854f
Batch ID: 20250612_145616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime


class Player:
    """
    Represents a player in the NFT treasure hunt game.
    """

    def __init__(self, player_id, username):
        self.player_id = player_id
        self.username = username
        self.progress = 0  # Tracks player progress (0-100%)
        self.rewards = []  # List of rewards collected

    def update_progress(self, new_progress):
        """
        Update the player's progress in the game.
        :param new_progress: Float value representing the new progress percentage.
        """
        if not (0 <= new_progress <= 100):
            raise ValueError("Progress value must be between 0 and 100.")
        self.progress = new_progress

    def add_reward(self, reward):
        """
        Add a new reward to the player's rewards.
        :param reward: Dictionary containing reward details.
        """
        if not isinstance(reward, dict) or 'name' not in reward or 'timestamp' not in reward:
            raise ValueError("Reward must be a dictionary with 'name' and 'timestamp' keys.")
        self.rewards.append(reward)

    def to_dict(self):
        """
        Convert player data to a dictionary format for serialization.
        """
        return {
            'player_id': self.player_id,
            'username': self.username,
            'progress': self.progress,
            'rewards': self.rewards
        }


class TreasureHuntGame:
    """
    Manages the logic for the NFT treasure hunt game.
    """

    def __init__(self, data_file='game_data.json'):
        self.players = {}  # Dictionary to store players by their ID
        self.data_file = data_file
        self.load_game_data()

    def add_player(self, player_id, username):
        """
        Add a new player to the game.
        :param player_id: Unique identifier for the player.
        :param username: Username of the player.
        """
        if player_id in self.players:
            raise ValueError(f"Player with ID {player_id} already exists.")
        self.players[player_id] = Player(player_id, username)

    def update_player_progress(self, player_id, new_progress):
        """
        Update a player's progress in the game.
        :param player_id: Unique identifier for the player.
        :param new_progress: Float value representing the new progress percentage.
        """
        if player_id not in self.players:
            raise ValueError(f"Player with ID {player_id} does not exist.")
        self.players[player_id].update_progress(new_progress)

    def reward_player(self, player_id, reward_name):
        """
        Reward a player with a new reward item.
        :param player_id: Unique identifier for the player.
        :param reward_name: Name of the reward to give.
        """
        if player_id not in self.players:
            raise ValueError(f"Player with ID {player_id} does not exist.")
        reward = {
            'name': reward_name,
            'timestamp': datetime.now().isoformat()
        }
        self.players[player_id].add_reward(reward)

    def save_game_data(self):
        """
        Save the current game state to a JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                data = {player_id: player.to_dict() for player_id, player in self.players.items()}
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving game data: {e}")

    def load_game_data(self):
        """
        Load game data from a JSON file.
        """
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for player_id, player_data in data.items():
                    player = Player(
                        player_id=player_data['player_id'],
                        username=player_data['username']
                    )
                    player.progress = player_data['progress']
                    player.rewards = player_data['rewards']
                    self.players[player_id] = player
        except FileNotFoundError:
            # No game data exists yet, this is fine.
            pass
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading game data: {e}")

    def get_player_data(self, player_id):
        """
        Retrieve the data for a specific player.
        :param player_id: Unique identifier for the player.
        :return: Dictionary containing the player's data.
        """
        if player_id not in self.players:
            raise ValueError(f"Player with ID {player_id} does not exist.")
        return self.players[player_id].to_dict()


# Example usage (uncomment to test the functionality):
# game = TreasureHuntGame()
# game.add_player("player1", "Alice")
# game.update_player_progress("player1", 50.0)
# game.reward_player("player1", "Golden NFT")
# game.save_game_data()
```
