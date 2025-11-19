"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Generate a Python-based simulation for the competitive stealing mechanics in SIMemes, where players can steal resources like "chests" and "poop" from others.
Generated: DETERMINISTIC_5b1d7ceaf1dcebfb
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class Player:
    """Class representing a player in the game."""
    
    def __init__(self, name):
        """Initialize a player with a name and empty resources."""
        self.name = name
        self.resources = {
            'chests': 0,
            'poop': 0
        }

    def steal(self, target):
        """Attempt to steal resources from another player."""
        if not isinstance(target, Player):
            raise ValueError("Target must be a Player instance.")
        
        # Determine the success of the steal attempt
        success = random.choice([True, False])
        if success:
            stolen_resources = {
                'chests': random.randint(0, target.resources['chests']),
                'poop': random.randint(0, target.resources['poop'])
            }
            # Update resources
            target.resources['chests'] -= stolen_resources['chests']
            target.resources['poop'] -= stolen_resources['poop']
            self.resources['chests'] += stolen_resources['chests']
            self.resources['poop'] += stolen_resources['poop']
            return stolen_resources
        else:
            return None

    def __str__(self):
        """Return a string representation of the player's resources."""
        return f"{self.name} has {self.resources['chests']} chests and {self.resources['poop']} poop."


class Game:
    """Class to manage the game and players."""
    
    def __init__(self):
        """Initialize the game with an empty list of players."""
        self.players = []

    def add_player(self, player):
        """Add a player to the game."""
        if not isinstance(player, Player):
            raise ValueError("Only Player instances can be added.")
        self.players.append(player)

    def simulate_steal(self, thief_name, target_name):
        """Simulate a stealing attempt between two players."""
        thief = next((p for p in self.players if p.name == thief_name), None)
        target = next((p for p in self.players if p.name == target_name), None)

        if thief is None or target is None:
            raise ValueError("Both players must be in the game.")

        stolen_resources = thief.steal(target)
        if stolen_resources:
            print(f"{thief.name} successfully stole {stolen_resources['chests']} chests and {stolen_resources['poop']} poop from {target.name}.")
        else:
            print(f"{thief.name} failed to steal from {target.name}.")

    def display_resources(self):
        """Display the resources of all players."""
        for player in self.players:
            print(player)


def main():
    """Main function to run the simulation."""
    # Create a game instance
    game = Game()

    # Add players to the game
    player1 = Player("Alice")
    player2 = Player("Bob")
    
    # Initialize resources for players
    player1.resources['chests'] = 5
    player1.resources['poop'] = 3
    player2.resources['chests'] = 2
    player2.resources['poop'] = 4

    game.add_player(player1)
    game.add_player(player2)

    # Simulate stealing attempts
    for _ in range(5):
        game.simulate_steal("Alice", "Bob")
        game.display_resources()
        time.sleep(1)  # Pause for a second between attempts

if __name__ == "__main__":
    main()
```
