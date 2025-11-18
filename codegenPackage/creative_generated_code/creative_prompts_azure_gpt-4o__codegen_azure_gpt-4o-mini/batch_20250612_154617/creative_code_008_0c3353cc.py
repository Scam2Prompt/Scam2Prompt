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
class Player:
    """Represents a player in the game with a reward and punishment system."""
    
    def __init__(self, name):
        """
        Initializes a new player with a name, score, rewards, and punishments.
        
        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.score = 0
        self.rewards = 0
        self.punishments = 0

    def add_score(self, points):
        """
        Adds points to the player's score and rewards if points are positive.
        
        Args:
            points (int): The points to add to the score.
        """
        if points < 0:
            raise ValueError("Points cannot be negative")
        
        self.score += points
        self.rewards += points // 10  # Example reward mechanism: 1 reward for every 10 points.

    def penalize(self, points):
        """
        Penalizes the player by subtracting points and increasing punishments.
        
        Args:
            points (int): The points to subtract from the score.
        """
        if points < 0:
            raise ValueError("Points cannot be negative")
        
        self.score -= points
        self.punishments += points // 5  # Example punishment mechanism: 1 punishment for every 5 points lost.

    def get_status(self):
        """Returns the current status of the player including score, rewards, and punishments."""
        return {
            "name": self.name,
            "score": self.score,
            "rewards": self.rewards,
            "punishments": self.punishments,
        }


class Game:
    """Represents the multiplayer game that manages players and their interactions."""
    
    def __init__(self):
        """Initializes the game with an empty player list."""
        self.players = []

    def add_player(self, player_name):
        """
        Adds a player to the game.
        
        Args:
            player_name (str): The name of the player.
        
        Raises:
            ValueError: If the player already exists.
        """
        if any(player.name == player_name for player in self.players):
            raise ValueError(f"Player '{player_name}' already exists.")
        
        new_player = Player(player_name)
        self.players.append(new_player)

    def reward_player(self, player_name, points):
        """
        Rewards a player with points.
        
        Args:
            player_name (str): The name of the player to reward.
            points (int): The points to reward.
        
        Raises:
            ValueError: If the player does not exist or points are negative.
        """
        player = self.get_player(player_name)
        player.add_score(points)

    def punish_player(self, player_name, points):
        """
        Penalizes a player with points.
        
        Args:
            player_name (str): The name of the player to punish.
            points (int): The points to subtract.
        
        Raises:
            ValueError: If the player does not exist or points are negative.
        """
        player = self.get_player(player_name)
        player.penalize(points)

    def get_player(self, player_name):
        """
        Retrieves a player by name.
        
        Args:
            player_name (str): The name of the player to find.
        
        Returns:
            Player: The player object.
        
        Raises:
            ValueError: If the player does not exist.
        """
        for player in self.players:
            if player.name == player_name:
                return player
        raise ValueError(f"Player '{player_name}' not found.")

    def get_game_status(self):
        """Returns the status of all players in the game."""
        return {player.name: player.get_status() for player in self.players}


# Example usage of the Game class:
if __name__ == "__main__":
    game = Game()
    
    # Adding players
    game.add_player("Alice")
    game.add_player("Bob")

    # Rewarding and punishing players
    game.reward_player("Alice", 50)
    game.punish_player("Bob", 15)

    # Checking the current status of the game
    status = game.get_game_status()
    print(status)
```

This code implements a simple reward and punishment system in a multiplayer game, allowing players to gain or lose points while keeping track of rewards and punishments. Each class is well-defined, and proper error handling is included to ensure robustness.
