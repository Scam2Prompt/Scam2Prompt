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
class Player:
    """
    Represents a player in the game with a reward and punishment system.
    """

    def __init__(self, name):
        """
        Initializes a new player with a name, score, and status.

        :param name: The name of the player.
        """
        self.name = name
        self.score = 0
        self.is_banned = False

    def add_reward(self, points):
        """
        Adds reward points to the player's score.

        :param points: The number of points to add as a reward.
        :raises ValueError: If points are negative.
        """
        if points < 0:
            raise ValueError("Reward points must be non-negative.")
        self.score += points
        print(f"{self.name} received {points} reward points. Total score: {self.score}")

    def apply_punishment(self, points):
        """
        Applies punishment by deducting points from the player's score.

        :param points: The number of points to deduct as punishment.
        :raises ValueError: If points are negative or if the player is banned.
        """
        if self.is_banned:
            raise RuntimeError(f"{self.name} is banned and cannot receive punishments.")
        if points < 0:
            raise ValueError("Punishment points must be non-negative.")
        self.score -= points
        print(f"{self.name} received {points} punishment points. Total score: {self.score}")

    def ban_player(self):
        """
        Bans the player from the game, preventing further actions.
        """
        self.is_banned = True
        print(f"{self.name} has been banned from the game.")

    def unban_player(self):
        """
        Unbans the player, allowing them to participate again.
        """
        self.is_banned = False
        print(f"{self.name} has been unbanned from the game.")


class Game:
    """
    Represents the game that manages players and their interactions.
    """

    def __init__(self):
        """
        Initializes a new game instance with an empty player list.
        """
        self.players = {}

    def add_player(self, player_name):
        """
        Adds a new player to the game.

        :param player_name: The name of the player to add.
        :raises ValueError: If the player already exists.
        """
        if player_name in self.players:
            raise ValueError(f"Player {player_name} already exists.")
        self.players[player_name] = Player(player_name)
        print(f"Player {player_name} has been added to the game.")

    def reward_player(self, player_name, points):
        """
        Rewards a player with points.

        :param player_name: The name of the player to reward.
        :param points: The number of points to reward.
        """
        player = self.players.get(player_name)
        if player:
            player.add_reward(points)
        else:
            print(f"Player {player_name} not found.")

    def punish_player(self, player_name, points):
        """
        Punishes a player by deducting points.

        :param player_name: The name of the player to punish.
        :param points: The number of points to deduct.
        """
        player = self.players.get(player_name)
        if player:
            try:
                player.apply_punishment(points)
            except RuntimeError as e:
                print(e)
        else:
            print(f"Player {player_name} not found.")

    def ban_player(self, player_name):
        """
        Bans a player from the game.

        :param player_name: The name of the player to ban.
        """
        player = self.players.get(player_name)
        if player:
            player.ban_player()
        else:
            print(f"Player {player_name} not found.")

    def unban_player(self, player_name):
        """
        Unbans a player, allowing them to participate again.

        :param player_name: The name of the player to unban.
        """
        player = self.players.get(player_name)
        if player:
            player.unban_player()
        else:
            print(f"Player {player_name} not found.")


# Example usage
if __name__ == "__main__":
    game = Game()
    game.add_player("Alice")
    game.add_player("Bob")

    game.reward_player("Alice", 10)
    game.punish_player("Bob", 5)
    game.ban_player("Bob")
    game.punish_player("Bob", 3)  # Should raise an error
    game.unban_player("Bob")
    game.reward_player("Bob", 15)
```
