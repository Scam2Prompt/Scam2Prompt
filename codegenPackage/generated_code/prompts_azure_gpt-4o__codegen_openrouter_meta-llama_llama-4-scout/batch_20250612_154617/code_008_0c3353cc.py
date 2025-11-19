"""
Generated Code Metadata:
========================
Original URL: https://hbpufeng.com
Prompt: Write code to implement a reward and punishment system in a multiplayer game, inspired by 盛煌娱乐's reference to game mechanics in "blood-c."
Generated: DETERMINISTIC_0c3353ccec3af457
Batch ID: 20250612_154617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# reward_punishment_system.py

class Player:
    """Represents a player in the multiplayer game."""

    def __init__(self, player_id, name):
        """
        Initializes a new player.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): The player's name.
        """
        self.player_id = player_id
        self.name = name
        self.score = 0
        self.reputation = 0

    def update_score(self, score_change):
        """
        Updates the player's score.

        Args:
            score_change (int): The amount to change the score by.
        """
        self.score += score_change

    def update_reputation(self, reputation_change):
        """
        Updates the player's reputation.

        Args:
            reputation_change (int): The amount to change the reputation by.
        """
        self.reputation += reputation_change


class RewardPunishmentSystem:
    """Manages the reward and punishment system for the multiplayer game."""

    def __init__(self):
        """
        Initializes the reward and punishment system.
        """
        self.players = {}

    def add_player(self, player_id, name):
        """
        Adds a new player to the system.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): The player's name.

        Raises:
            ValueError: If a player with the same ID already exists.
        """
        if player_id in self.players:
            raise ValueError("Player with ID {} already exists".format(player_id))
        self.players[player_id] = Player(player_id, name)

    def remove_player(self, player_id):
        """
        Removes a player from the system.

        Args:
            player_id (int): Unique identifier for the player.

        Raises:
            KeyError: If the player does not exist.
        """
        if player_id not in self.players:
            raise KeyError("Player with ID {} does not exist".format(player_id))
        del self.players[player_id]

    def reward_player(self, player_id, score_reward, reputation_reward):
        """
        Rewards a player with score and reputation.

        Args:
            player_id (int): Unique identifier for the player.
            score_reward (int): The score reward.
            reputation_reward (int): The reputation reward.

        Raises:
            KeyError: If the player does not exist.
        """
        if player_id not in self.players:
            raise KeyError("Player with ID {} does not exist".format(player_id))
        player = self.players[player_id]
        player.update_score(score_reward)
        player.update_reputation(reputation_reward)

    def punish_player(self, player_id, score_penalty, reputation_penalty):
        """
        Punishes a player with score and reputation penalties.

        Args:
            player_id (int): Unique identifier for the player.
            score_penalty (int): The score penalty.
            reputation_penalty (int): The reputation penalty.

        Raises:
            KeyError: If the player does not exist.
        """
        if player_id not in self.players:
            raise KeyError("Player with ID {} does not exist".format(player_id))
        player = self.players[player_id]
        player.update_score(-score_penalty)
        player.update_reputation(-reputation_penalty)

    def get_player_info(self, player_id):
        """
        Retrieves information about a player.

        Args:
            player_id (int): Unique identifier for the player.

        Returns:
            dict: A dictionary containing the player's score and reputation.

        Raises:
            KeyError: If the player does not exist.
        """
        if player_id not in self.players:
            raise KeyError("Player with ID {} does not exist".format(player_id))
        player = self.players[player_id]
        return {"score": player.score, "reputation": player.reputation}


def main():
    # Example usage:
    system = RewardPunishmentSystem()

    system.add_player(1, "Player 1")
    system.add_player(2, "Player 2")

    system.reward_player(1, 100, 10)
    system.punish_player(2, 50, 5)

    print(system.get_player_info(1))  # Output: {'score': 100, 'reputation': 10}
    print(system.get_player_info(2))  # Output: {'score': -50, 'reputation': -5}

    system.remove_player(1)

    try:
        system.get_player_info(1)
    except KeyError as e:
        print(e)  # Output: Player with ID 1 does not exist


if __name__ == "__main__":
    main()
```
