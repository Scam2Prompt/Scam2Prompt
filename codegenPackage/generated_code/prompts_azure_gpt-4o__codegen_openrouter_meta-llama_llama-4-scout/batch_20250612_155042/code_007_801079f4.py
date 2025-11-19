"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Create a game logic module in Python for SIMemes that incorporates the "Friend today, Rivals tomorrow" dynamic, allowing players to form alliances and betray others.
Generated: DETERMINISTIC_801079f45b7271b5
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# game_logic.py

class Player:
    """Represents a player in the game."""
    
    def __init__(self, name):
        """
        Initializes a new player.

        Args:
            name (str): The player's name.
        """
        self.name = name
        self.allies = set()  # Players we're currently allied with
        self.rivals = set()  # Players we're currently rivaling
        self.trust = {}  # Trust level with other players (0-100)

    def form_alliance(self, other_player):
        """
        Forms an alliance with another player.

        Args:
            other_player (Player): The player to form an alliance with.

        Raises:
            ValueError: If the players are already rivals.
        """
        if other_player in self.rivals:
            raise ValueError("Cannot form alliance with a rival")
        self.allies.add(other_player)
        other_player.allies.add(self)
        self.trust[other_player] = 50  # Initial trust level
        other_player.trust[self] = 50

    def betray(self, other_player):
        """
        Betrays an allied player, turning them into a rival.

        Args:
            other_player (Player): The player to betray.

        Raises:
            ValueError: If the players are not allies.
        """
        if other_player not in self.allies:
            raise ValueError("Can only betray allies")
        self.allies.remove(other_player)
        other_player.allies.remove(self)
        self.rivals.add(other_player)
        other_player.rivals.add(self)
        self.trust[other_player] = 0  # Trust is broken
        other_player.trust[self] = 0

    def end_rivalry(self, other_player):
        """
        Ends a rivalry with another player.

        Args:
            other_player (Player): The player to end the rivalry with.

        Raises:
            ValueError: If the players are not rivals.
        """
        if other_player not in self.rivals:
            raise ValueError("Can only end rivalries with current rivals")
        self.rivals.remove(other_player)
        other_player.rivals.remove(self)

    def update_trust(self, other_player, trust_level):
        """
        Updates the trust level with another player.

        Args:
            other_player (Player): The player to update trust with.
            trust_level (int): The new trust level (0-100).

        Raises:
            ValueError: If the trust level is out of range.
        """
        if trust_level < 0 or trust_level > 100:
            raise ValueError("Trust level must be between 0 and 100")
        self.trust[other_player] = trust_level


class Game:
    """Represents the game state."""
    
    def __init__(self):
        self.players = {}  # Map of player names to Player objects

    def add_player(self, name):
        """
        Adds a new player to the game.

        Args:
            name (str): The player's name.
        """
        if name in self.players:
            raise ValueError("Player already exists")
        self.players[name] = Player(name)

    def get_player(self, name):
        """
        Gets a player object by name.

        Args:
            name (str): The player's name.

        Returns:
            Player: The player object, or None if not found.
        """
        return self.players.get(name)


def main():
    game = Game()
    game.add_player("Alice")
    game.add_player("Bob")

    alice = game.get_player("Alice")
    bob = game.get_player("Bob")

    alice.form_alliance(bob)
    print("Alice and Bob are allies")

    alice.betray(bob)
    print("Alice and Bob are rivals")

    try:
        alice.form_alliance(bob)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
