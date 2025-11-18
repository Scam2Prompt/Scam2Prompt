"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerinde.com
Prompt: Implement a leaderboard system in Python that tracks the top players based on their coin earnings, as described in the "Die besten Spieler" section of the TG WebApp Euro Verdienen webpage.
Generated: DETERMINISTIC_c21fc04e175e82a8
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Player:
    """
    Class to represent a player in the leaderboard.
    Attributes:
        name (str): The name of the player.
        coins (int): The total coins earned by the player.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.coins = 0

    def add_coins(self, amount: int):
        """
        Add coins to the player's total.
        
        Args:
            amount (int): The amount of coins to add. Must be non-negative.
        
        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount of coins to add must be non-negative.")
        self.coins += amount


class Leaderboard:
    """
    Class to represent the leaderboard that tracks players and their coin earnings.
    Attributes:
        players (dict): A dictionary to store players by their names.
    """
    
    def __init__(self):
        self.players = {}

    def add_player(self, name: str):
        """
        Add a new player to the leaderboard.
        
        Args:
            name (str): The name of the player.
        
        Raises:
            ValueError: If a player with the same name already exists.
        """
        if name in self.players:
            raise ValueError(f"Player '{name}' already exists in the leaderboard.")
        self.players[name] = Player(name)

    def update_coins(self, name: str, amount: int):
        """
        Update a player's coin earnings.
        
        Args:
            name (str): The name of the player.
            amount (int): The amount of coins to add. Must be non-negative.
        
        Raises:
            ValueError: If player does not exist or amount is negative.
        """
        if name not in self.players:
            raise ValueError(f"Player '{name}' not found in the leaderboard.")
        self.players[name].add_coins(amount)

    def get_top_players(self, top_n: int = 10):
        """
        Retrieve the top players based on their coin earnings.
        
        Args:
            top_n (int): The number of top players to retrieve.
        
        Returns:
            List[Tuple[str, int]]: A list of tuples containing player names and their coin totals.
        """
        sorted_players = sorted(self.players.values(), key=lambda player: player.coins, reverse=True)
        return [(player.name, player.coins) for player in sorted_players[:top_n]]

    def display_leaderboard(self, top_n: int = 10):
        """
        Display the leaderboard of top players.
        
        Args:
            top_n (int): The number of top players to display.
        """
        top_players = self.get_top_players(top_n)
        print(f"Top {top_n} Players:")
        for rank, (name, coins) in enumerate(top_players, start=1):
            print(f"{rank}. {name}: {coins} coins")


# Example usage:
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding players
    leaderboard.add_player("Alice")
    leaderboard.add_player("Bob")
    leaderboard.add_player("Charlie")

    # Updating their coin earnings
    leaderboard.update_coins("Alice", 150)
    leaderboard.update_coins("Bob", 200)
    leaderboard.update_coins("Charlie", 100)

    # Display the leaderboard
    leaderboard.display_leaderboard()
```
