"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hbpufeng.com
Prompt: Write code to implement a reward and punishment system in a multiplayer game, inspired by 盛煌娱乐's reference to game mechanics in "blood-c."
Generated: DETERMINISTIC_0c3353ccec3af457
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Player:
    """
    Represents a player in the game.
    Attributes:
        player_id (str): Unique identifier for the player.
        score (int): Current score of the player.
        rewards (list): List of rewards collected by the player.
        punishments (list): List of punishments received by the player.
    """
    def __init__(self, player_id):
        self.player_id = player_id
        self.score = 0
        self.rewards = []
        self.punishments = []

    def apply_reward(self, reward):
        """
        Apply a reward to the player.
        Args:
            reward (dict): Contains information about the reward (e.g., {'name': 'Gold Coin', 'points': 10}).
        """
        if not isinstance(reward, dict) or 'name' not in reward or 'points' not in reward:
            logging.error("Invalid reward format. Expected a dictionary with 'name' and 'points' keys.")
            return
        self.score += reward['points']
        self.rewards.append(reward['name'])
        logging.info(f"Player {self.player_id} received reward: {reward['name']}, Points: {reward['points']}")

    def apply_punishment(self, punishment):
        """
        Apply a punishment to the player.
        Args:
            punishment (dict): Contains information about the punishment (e.g., {'name': 'Time Penalty', 'points': -5}).
        """
        if not isinstance(punishment, dict) or 'name' not in punishment or 'points' not in punishment:
            logging.error("Invalid punishment format. Expected a dictionary with 'name' and 'points' keys.")
            return
        self.score += punishment['points']
        self.punishments.append(punishment['name'])
        logging.info(f"Player {self.player_id} received punishment: {punishment['name']}, Points: {punishment['points']}")

    def get_status(self):
        """
        Get the current status of the player.
        Returns:
            dict: Contains player's score, rewards, and punishments.
        """
        return {
            'player_id': self.player_id,
            'score': self.score,
            'rewards': self.rewards,
            'punishments': self.punishments
        }


class Game:
    """
    Represents the multiplayer game, managing players and their rewards/punishments.
    """
    def __init__(self):
        self.players = {}

    def add_player(self, player_id):
        """
        Add a new player to the game.
        Args:
            player_id (str): Unique identifier for the player.
        """
        if player_id in self.players:
            logging.warning(f"Player {player_id} already exists.")
        else:
            self.players[player_id] = Player(player_id)
            logging.info(f"Player {player_id} added to the game.")

    def issue_reward(self, player_id, reward):
        """
        Issue a reward to a specific player.
        Args:
            player_id (str): Identifier of the player.
            reward (dict): Contains information about the reward.
        """
        player = self.players.get(player_id)
        if player:
            player.apply_reward(reward)
        else:
            logging.error(f"Player {player_id} does not exist. Cannot issue reward.")

    def issue_punishment(self, player_id, punishment):
        """
        Issue a punishment to a specific player.
        Args:
            player_id (str): Identifier of the player.
            punishment (dict): Contains information about the punishment.
        """
        player = self.players.get(player_id)
        if player:
            player.apply_punishment(punishment)
        else:
            logging.error(f"Player {player_id} does not exist. Cannot issue punishment.")

    def get_player_status(self, player_id):
        """
        Retrieve the status of a specific player.
        Args:
            player_id (str): Identifier of the player.
        Returns:
            dict: Player status or None if not found.
        """
        player = self.players.get(player_id)
        if player:
            return player.get_status()
        else:
            logging.error(f"Player {player_id} does not exist.")
            return None

# Example usage
if __name__ == '__main__':
    game = Game()
    game.add_player('Player1')
    game.add_player('Player2')

    game.issue_reward('Player1', {'name': 'Gold Coin', 'points': 10})
    game.issue_punishment('Player1', {'name': 'Time Penalty', 'points': -5})

    status = game.get_player_status('Player1')
    if status:
        logging.info(f"Status of Player1: {status}")
```
