"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: Generate code for a leaderboard system that ranks players based on the number of coins collected in a game like Khaby Lame Coin.
Generated: DETERMINISTIC_e034a48b23098c1f
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Leaderboard System
-------------------
A Python implementation of a leaderboard system that ranks players based on the number of coins collected in a game.
The system supports adding players, updating their coin counts, retrieving the top players, and displaying rankings.
"""

from typing import List, Tuple

class Leaderboard:
    def __init__(self):
        """
        Initialize the leaderboard with an empty dictionary to store player scores.
        """
        self.scores = {}  # Dictionary to store player names and their coin counts

    def add_player(self, player_name: str):
        """
        Add a new player to the leaderboard with an initial score of 0.
        
        :param player_name: Name of the player to add.
        :raises ValueError: If the player already exists in the leaderboard.
        """
        if player_name in self.scores:
            raise ValueError(f"Player '{player_name}' already exists in the leaderboard.")
        self.scores[player_name] = 0

    def update_score(self, player_name: str, coins: int):
        """
        Update the coin count for an existing player. If the player is not found, raise an error.
        
        :param player_name: Name of the player whose score is to be updated.
        :param coins: Number of coins to add to the player's score (must be non-negative).
        :raises ValueError: If the player does not exist or if coins is negative.
        """
        if player_name not in self.scores:
            raise ValueError(f"Player '{player_name}' does not exist in the leaderboard.")
        if coins < 0:
            raise ValueError("Coins must be a non-negative number.")
        self.scores[player_name] += coins

    def get_top_players(self, top_n: int) -> List[Tuple[str, int]]:
        """
        Retrieve the top N players sorted by their coin counts in descending order.
        
        :param top_n: Number of top players to fetch.
        :return: A list of tuples containing player names and their scores.
        """
        if top_n <= 0:
            raise ValueError("The number of top players must be greater than 0.")
        # Sort players by score in descending order and retrieve the top N
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[:top_n]

    def display_leaderboard(self):
        """
        Display the entire leaderboard sorted by coin counts in descending order.
        """
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        print("Leaderboard:")
        print("------------")
        for rank, (player_name, coins) in enumerate(sorted_scores, start=1):
            print(f"{rank}. {player_name} - {coins} coins")


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players
    leaderboard.add_player("Alice")
    leaderboard.add_player("Bob")
    leaderboard.add_player("Charlie")
    
    # Updating scores
    leaderboard.update_score("Alice", 100)
    leaderboard.update_score("Bob", 150)
    leaderboard.update_score("Charlie", 120)
    
    # Display the leaderboard
    leaderboard.display_leaderboard()
    
    # Fetch top 2 players
    top_players = leaderboard.get_top_players(2)
    print("\nTop Players:")
    for player, score in top_players:
        print(f"{player} - {score} coins")
```
