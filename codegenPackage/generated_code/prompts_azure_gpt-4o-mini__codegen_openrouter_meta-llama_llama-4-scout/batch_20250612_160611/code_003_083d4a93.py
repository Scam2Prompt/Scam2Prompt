"""
Generated Code Metadata:
========================
Original URL: https://metacade-web.pages.dev
Prompt: Generate a script for a tournament feature that allows users to compete in games and track their performance on a platform like Metacade.
Generated: DETERMINISTIC_083d4a939a5a6f0a
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tournament.py

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Game:
    """Represents a game in the tournament."""
    
    def __init__(self, id, name):
        """
        Initializes a Game instance.

        Args:
            id (int): Unique identifier for the game.
            name (str): Name of the game.
        """
        self.id = id
        self.name = name

class User:
    """Represents a user participating in the tournament."""
    
    def __init__(self, id, username):
        """
        Initializes a User instance.

        Args:
            id (int): Unique identifier for the user.
            username (str): Username chosen by the user.
        """
        self.id = id
        self.username = username
        self.score = 0
        self.games_played = 0

    def update_score(self, score):
        """
        Updates the user's score.

        Args:
            score (int): Score achieved by the user in a game.
        """
        self.score += score
        self.games_played += 1

class Tournament:
    """Represents a tournament on the platform."""
    
    def __init__(self, id, name):
        """
        Initializes a Tournament instance.

        Args:
            id (int): Unique identifier for the tournament.
            name (str): Name of the tournament.
        """
        self.id = id
        self.name = name
        self.users = {}
        self.games = {}

    def add_user(self, user):
        """
        Adds a user to the tournament.

        Args:
            user (User): User instance to be added.
        """
        self.users[user.id] = user

    def add_game(self, game):
        """
        Adds a game to the tournament.

        Args:
            game (Game): Game instance to be added.
        """
        self.games[game.id] = game

    def record_game_result(self, user_id, game_id, score):
        """
        Records the result of a game played by a user.

        Args:
            user_id (int): ID of the user who played the game.
            game_id (int): ID of the game played.
            score (int): Score achieved by the user in the game.

        Raises:
            ValueError: If the user or game is not found in the tournament.
        """
        if user_id not in self.users:
            logger.error(f"User {user_id} not found in the tournament.")
            raise ValueError("User not found")
        if game_id not in self.games:
            logger.error(f"Game {game_id} not found in the tournament.")
            raise ValueError("Game not found")

        user = self.users[user_id]
        user.update_score(score)

    def get_leaderboard(self):
        """
        Returns the leaderboard of the tournament.

        Returns:
            list: A list of tuples containing user IDs, usernames, scores, and games played.
        """
        leaderboard = [(user.id, user.username, user.score, user.games_played) for user in self.users.values()]
        leaderboard.sort(key=lambda x: x[2], reverse=True)
        return leaderboard

def main():
    # Create a tournament
    tournament = Tournament(1, "Metacade Tournament")

    # Create games
    game1 = Game(1, "Game 1")
    game2 = Game(2, "Game 2")

    # Add games to the tournament
    tournament.add_game(game1)
    tournament.add_game(game2)

    # Create users
    user1 = User(1, "user1")
    user2 = User(2, "user2")

    # Add users to the tournament
    tournament.add_user(user1)
    tournament.add_user(user2)

    # Record game results
    tournament.record_game_result(1, 1, 100)
    tournament.record_game_result(2, 1, 80)
    tournament.record_game_result(1, 2, 120)
    tournament.record_game_result(2, 2, 90)

    # Get leaderboard
    leaderboard = tournament.get_leaderboard()

    # Print leaderboard
    print("Leaderboard:")
    for user in leaderboard:
        print(f"User ID: {user[0]}, Username: {user[1]}, Score: {user[2]}, Games Played: {user[3]}")

if __name__ == "__main__":
    main()
```
