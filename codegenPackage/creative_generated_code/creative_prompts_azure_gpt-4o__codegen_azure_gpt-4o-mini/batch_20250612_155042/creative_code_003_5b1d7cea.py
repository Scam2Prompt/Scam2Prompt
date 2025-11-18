"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Generate a Python-based simulation for the competitive stealing mechanics in SIMemes, where players can steal resources like "chests" and "poop" from others.
Generated: DETERMINISTIC_5b1d7ceaf1dcebfb
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class Player:
    """Class representing a player in the game."""

    def __init__(self, name):
        """Initialize a player with a name and resources."""
        self.name = name
        self.resources = {'chests': 0, 'poop': 0}

    def steal(self, target):
        """Attempt to steal resources from another player."""
        if not isinstance(target, Player):
            raise ValueError("Target must be a Player instance.")
        
        success_rate = random.random()
        if success_rate < 0.5:  # 50% chance to steal successfully
            stolen_resource = random.choice(['chests', 'poop'])
            if target.resources[stolen_resource] > 0:
                target.resources[stolen_resource] -= 1
                self.resources[stolen_resource] += 1
                print(f"{self.name} successfully stole 1 {stolen_resource} from {target.name}!")
            else:
                print(f"{target.name} has no {stolen_resource} to steal.")
        else:
            print(f"{self.name} failed to steal from {target.name}.")

    def add_resources(self, resource_type, amount):
        """Add resources to the player's inventory."""
        if resource_type not in self.resources:
            raise ValueError("Invalid resource type.")
        if amount < 0:
            raise ValueError("Amount must be a non-negative integer.")
        self.resources[resource_type] += amount
        print(f"{self.name} now has {self.resources[resource_type]} {resource_type}.")

    def __str__(self):
        """Return a string representation of the player's resources."""
        return f"{self.name}: {self.resources}"


def game_simulation(players):
    """Simulate the stealing mechanics among players."""
    if not players or len(players) < 2:
        raise ValueError("At least two players are needed for the simulation.")

    for _ in range(5):  # Run the simulation for 5 rounds
        for player in players:
            target = random.choice([p for p in players if p != player])  # Select a random target
            player.steal(target)
            time.sleep(1)  # Pause for readability

        print("\nCurrent Resources:")
        for player in players:
            print(player)
        print("-" * 40)

# Example usage
if __name__ == "__main__":
    # Initialize players
    player1 = Player("Alice")
    player2 = Player("Bob")
    player3 = Player("Charlie")

    # Add initial resources
    player1.add_resources('chests', 3)
    player2.add_resources('poop', 2)
    player3.add_resources('chests', 1)
    player3.add_resources('poop', 5)

    # Start the game simulation
    game_simulation([player1, player2, player3])
```
