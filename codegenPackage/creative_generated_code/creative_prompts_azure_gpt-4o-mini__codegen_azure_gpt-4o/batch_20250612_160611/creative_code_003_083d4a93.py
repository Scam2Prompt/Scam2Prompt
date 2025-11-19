"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-web.pages.dev
Prompt: Generate a script for a tournament feature that allows users to compete in games and track their performance on a platform like Metacade.
Generated: DETERMINISTIC_083d4a939a5a6f0a
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime


class Player:
    """
    Represents a player in the tournament.
    """

    def __init__(self, username):
        self.player_id = uuid.uuid4()  # Unique ID for the player
        self.username = username
        self.score = 0  # Initial score set to 0

    def update_score(self, points):
        """
        Update the player's score.
        :param points: Points to add to the player's score.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.score += points


class Game:
    """
    Represents a game in the tournament.
    """

    def __init__(self, game_name, max_players=4):
        self.game_id = uuid.uuid4()  # Unique ID for the game
        self.game_name = game_name
        self.max_players = max_players
        self.players = []  # List to store players in the game

    def add_player(self, player):
        """
        Adds a player to the game.
        :param player: Player object to add.
        """
        if len(self.players) >= self.max_players:
            raise ValueError("Cannot add more players. Maximum players limit reached.")
        if player in self.players:
            raise ValueError("Player is already in the game.")
        self.players.append(player)

    def start_game(self):
        """
        Starts the game. Placeholder for game logic.
        """
        if len(self.players) < 2:
            raise ValueError("Not enough players to start the game.")
        print(f"Game '{self.game_name}' started with {len(self.players)} players.")

    def end_game(self, scores):
        """
        Ends the game and updates player scores.
        :param scores: Dictionary mapping player IDs to scores.
        """
        if len(scores) != len(self.players):
            raise ValueError("Scores must be provided for all players.")

        for player_id, score in scores.items():
            player = next((p for p in self.players if p.player_id == player_id), None)
            if player:
                player.update_score(score)
        print(f"Game '{self.game_name}' ended. Scores updated.")


class Tournament:
    """
    Represents a tournament, allowing multiple games and tracking performance.
    """

    def __init__(self, tournament_name):
        self.tournament_id = uuid.uuid4()  # Unique ID for the tournament
        self.tournament_name = tournament_name
        self.games = []  # List to store games
        self.players = {}  # Dictionary to track players across all games

    def register_player(self, username):
        """
        Register a new player in the tournament.
        :param username: Username of the player.
        """
        if username in self.players:
            raise ValueError("Player with this username already registered.")
        new_player = Player(username)
        self.players[new_player.player_id] = new_player
        print(f"Player '{username}' registered successfully.")

    def create_game(self, game_name, max_players=4):
        """
        Create a new game for the tournament.
        :param game_name: Name of the game.
        :param max_players: Maximum number of players allowed in the game.
        """
        new_game = Game(game_name, max_players)
        self.games.append(new_game)
        print(f"Game '{game_name}' created successfully.")
        return new_game

    def leaderboard(self):
        """
        Display the leaderboard of all players based on their scores.
        """
        sorted_players = sorted(self.players.values(), key=lambda p: p.score, reverse=True)
        print("\nTournament Leaderboard:")
        for rank, player in enumerate(sorted_players, start=1):
            print(f"{rank}. {player.username} - {player.score} points")

    def save_results(self):
        """
        Save tournament results to a file for future reference.
        """
        filename = f"tournament_{self.tournament_id}.txt"
        with open(filename, "w") as file:
            file.write(f"Tournament: {self.tournament_name}\n")
            file.write(f"Date: {datetime.now()}\n\n")
            file.write("Leaderboard:\n")
            sorted_players = sorted(self.players.values(), key=lambda p: p.score, reverse=True)
            for rank, player in enumerate(sorted_players, start=1):
                file.write(f"{rank}. {player.username} - {player.score} points\n")
        print(f"Tournament results saved to {filename}.")


# Example usage (this part can be removed in production):
if __name__ == "__main__":
    tournament = Tournament("Metacade Championship")

    # Register players
    tournament.register_player("Player1")
    tournament.register_player("Player2")
    tournament.register_player("Player3")

    # Create a game
    game = tournament.create_game("Game1", max_players=3)

    # Add players to the game
    for player in tournament.players.values():
        game.add_player(player)

    # Start and end the game
    game.start_game()
    game.end_game({player.player_id: score for player, score in zip(game.players, [100, 150, 200])})

    # Display leaderboard
    tournament.leaderboard()

    # Save results
    tournament.save_results()
```
