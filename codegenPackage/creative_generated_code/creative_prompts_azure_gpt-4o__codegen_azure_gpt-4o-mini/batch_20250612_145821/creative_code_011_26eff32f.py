"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Write code to implement a leaderboard system for competitive games like "Bắn Cá" or "Nổ Hũ," inspired by the features on S666.
Generated: DETERMINISTIC_26eff32fdf09d700
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Player:
    """A class to represent a player in the leaderboard."""
    
    def __init__(self, player_id, name, score=0):
        """
        Initialize a new player.

        :param player_id: Unique identifier for the player.
        :param name: The name of the player.
        :param score: The player's score, default is 0.
        """
        self.player_id = player_id
        self.name = name
        self.score = score

    def update_score(self, points):
        """
        Update the player's score by adding points.

        :param points: The points to add to the player's score.
        :raises ValueError: If points are negative.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.score += points


class Leaderboard:
    """A class to manage the leaderboard of players."""
    
    def __init__(self):
        """Initialize the leaderboard with an empty list of players."""
        self.players = []

    def add_player(self, player):
        """
        Add a new player to the leaderboard.

        :param player: A Player object to be added.
        """
        self.players.append(player)

    def remove_player(self, player_id):
        """
        Remove a player from the leaderboard by player_id.

        :param player_id: Unique identifier of the player to remove.
        :raises ValueError: If player_id is not found.
        """
        for player in self.players:
            if player.player_id == player_id:
                self.players.remove(player)
                return
        raise ValueError("Player with ID {} not found.".format(player_id))

    def update_player_score(self, player_id, points):
        """
        Update the score of a player.

        :param player_id: Unique identifier of the player.
        :param points: The points to add to the player's score.
        :raises ValueError: If player_id is not found or points are negative.
        """
        for player in self.players:
            if player.player_id == player_id:
                player.update_score(points)
                return
        raise ValueError("Player with ID {} not found.".format(player_id))

    def get_leaderboard(self):
        """
        Get the current leaderboard sorted by score in descending order.

        :return: A list of tuples containing player name and score.
        """
        return sorted(((player.name, player.score) for player in self.players), 
                      key=lambda x: x[1], reverse=True)

    def display_leaderboard(self):
        """Display the leaderboard in a formatted way."""
        print("Leaderboard:")
        for rank, (name, score) in enumerate(self.get_leaderboard(), start=1):
            print(f"{rank}. {name}: {score} points")


# Example usage
if __name__ == "__main__":
    lb = Leaderboard()

    # Adding players
    lb.add_player(Player(1, "Alice"))
    lb.add_player(Player(2, "Bob"))
    
    # Updating scores
    lb.update_player_score(1, 50)
    lb.update_player_score(2, 30)
    
    # Displaying the leaderboard
    lb.display_leaderboard()

    # Removing a player
    lb.remove_player(1)
    
    # Displaying the leaderboard again
    lb.display_leaderboard()
```
