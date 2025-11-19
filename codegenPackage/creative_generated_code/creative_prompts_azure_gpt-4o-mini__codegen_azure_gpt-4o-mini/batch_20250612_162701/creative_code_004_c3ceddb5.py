"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellar-datagrid.xyz
Prompt: Illustrate how to implement a leaderboard feature for poker tournaments in a casino app, drawing on the competitive elements highlighted in the Royal Joker experience.
Generated: DETERMINISTIC_c3ceddb538c4153e
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

class Player:
    """Class representing a player in the poker tournament."""
    
    def __init__(self, player_id, name):
        """
        Initialize a new player.
        
        :param player_id: Unique identifier for the player
        :param name: The name of the player
        """
        self.player_id = player_id
        self.name = name
        self.score = 0

    def update_score(self, points):
        """
        Update the player's score.
        
        :param points: Points to add to the player's score
        """
        if points < 0:
            raise ValueError("Points must be non-negative")
        self.score += points

class Leaderboard:
    """Class representing a leaderboard for the poker tournament."""
    
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.players = {}

    def add_player(self, player):
        """
        Add a player to the leaderboard.
        
        :param player: An instance of Player
        """
        if player.player_id in self.players:
            raise ValueError("Player already exists in the leaderboard")
        self.players[player.player_id] = player

    def update_player_score(self, player_id, points):
        """
        Update the score of an existing player.
        
        :param player_id: Unique identifier for the player
        :param points: Points to add to the player's score
        """
        if player_id not in self.players:
            raise ValueError("Player not found in the leaderboard")
        self.players[player_id].update_score(points)

    def get_leaderboard(self):
        """
        Retrieve the current leaderboard sorted by score.
        
        :return: List of tuples (player_id, player_name, score) sorted by score
        """
        return sorted(
            [(player.player_id, player.name, player.score) for player in self.players.values()],
            key=lambda x: x[2], 
            reverse=True
        )

    def display_leaderboard(self):
        """Print the leaderboard in a formatted way."""
        print("Leaderboard:")
        for idx, (player_id, name, score) in enumerate(self.get_leaderboard(), start=1):
            print(f"{idx}. {name} (ID: {player_id}) - Score: {score}")

# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Create players
    player1 = Player(1, "Alice")
    player2 = Player(2, "Bob")
    player3 = Player(3, "Charlie")

    # Add players to leaderboard
    leaderboard.add_player(player1)
    leaderboard.add_player(player2)
    leaderboard.add_player(player3)

    # Update scores
    leaderboard.update_player_score(1, 10)
    leaderboard.update_player_score(2, 15)
    leaderboard.update_player_score(3, 5)

    # Display the leaderboard
    leaderboard.display_leaderboard()
```
