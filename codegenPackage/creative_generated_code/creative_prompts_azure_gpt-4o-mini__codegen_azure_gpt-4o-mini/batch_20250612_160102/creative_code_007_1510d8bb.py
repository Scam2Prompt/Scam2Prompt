"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.volarisgames.top
Prompt: What are the key features of the Volarian Heist game, and how can I implement Tap2Earn mechanics in my own game?
Generated: DETERMINISTIC_1510d8bbd2f1aa23
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VolarianHeistGame:
    """
    A class to represent the Volarian Heist game with key features and mechanics.
    """

    def __init__(self):
        """
        Initializes the game with default values and features.
        """
        self.players = {}
        self.tap2earn_enabled = False
        self.total_earnings = 0.0

    def add_player(self, player_id: str):
        """
        Adds a new player to the game.

        Args:
            player_id (str): Unique identifier for the player.
        """
        if player_id in self.players:
            raise ValueError(f"Player ID {player_id} already exists.")
        
        self.players[player_id] = {
            "earnings": 0.0,
            "tap_count": 0
        }
        print(f"Player {player_id} added.")

    def enable_tap2earn(self):
        """
        Enables the Tap2Earn mechanic for the game.
        """
        self.tap2earn_enabled = True
        print("Tap2Earn mechanic has been enabled.")

    def tap(self, player_id: str):
        """
        Records a tap action from the player and updates their earnings.

        Args:
            player_id (str): Unique identifier for the player.
        
        Raises:
            ValueError: If the player ID is not found or if Tap2Earn is not enabled.
        """
        if not self.tap2earn_enabled:
            raise ValueError("Tap2Earn mechanic is not enabled.")
        
        if player_id not in self.players:
            raise ValueError(f"Player ID {player_id} does not exist.")

        # Increment the tap count and calculate earnings
        self.players[player_id]["tap_count"] += 1
        earnings = self.calculate_earnings(self.players[player_id]["tap_count"])
        self.players[player_id]["earnings"] += earnings
        self.total_earnings += earnings
        
        print(f"Player {player_id} tapped. Current earnings: {self.players[player_id]['earnings']:.2f}")

    def calculate_earnings(self, tap_count: int) -> float:
        """
        Calculates earnings based on the number of taps.

        Args:
            tap_count (int): Number of taps made by the player.

        Returns:
            float: Calculated earnings for the current tap count.
        """
        # Example earning formula: $0.10 per tap
        return tap_count * 0.10

    def get_player_summary(self, player_id: str) -> dict:
        """
        Returns the summary of a player's earnings and tap count.

        Args:
            player_id (str): Unique identifier for the player.

        Returns:
            dict: Summary of the player's earnings and tap count.
        
        Raises:
            ValueError: If the player ID is not found.
        """
        if player_id not in self.players:
            raise ValueError(f"Player ID {player_id} does not exist.")
        
        return {
            "player_id": player_id,
            "earnings": self.players[player_id]["earnings"],
            "tap_count": self.players[player_id]["tap_count"]
        }

    def get_total_earnings(self) -> float:
        """
        Returns the total earnings of all players in the game.

        Returns:
            float: Total earnings of all players.
        """
        return self.total_earnings


# Example Usage
if __name__ == "__main__":
    game = VolarianHeistGame()
    game.add_player("player1")
    game.enable_tap2earn()

    try:
        game.tap("player1")
        print(game.get_player_summary("player1"))
    except ValueError as e:
        print(f"Error: {e}")
```
