"""
Generated Code Metadata:
========================
Original URL: https://stepn-walkin.com
Prompt: Create a Python program that simulates the leveling-up process in STEPN, incorporating the recommended point allocation strategies from the blog.
Generated: DETERMINISTIC_dea9e518281d4cd0
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Player:
    """
    A class to represent a player in the STEPN leveling-up simulation.
    """

    def __init__(self, name, level=1, points=0):
        """
        Initializes a new player with a name, level, and points.

        :param name: str - The name of the player.
        :param level: int - The current level of the player (default is 1).
        :param points: int - The current points of the player (default is 0).
        """
        self.name = name
        self.level = level
        self.points = points

    def allocate_points(self, points_allocation):
        """
        Allocates points to the player based on the provided allocation strategy.

        :param points_allocation: dict - A dictionary with point allocation strategies.
        :raises ValueError: If the total points allocated exceeds available points.
        """
        total_allocation = sum(points_allocation.values())
        if total_allocation > self.points:
            raise ValueError("Total allocation exceeds available points.")

        for attribute, points in points_allocation.items():
            if points < 0:
                raise ValueError(f"Points allocated for {attribute} cannot be negative.")
            setattr(self, attribute, getattr(self, attribute, 0) + points)
            self.points -= points

    def level_up(self):
        """
        Levels up the player, increasing their level and resetting points.
        """
        self.level += 1
        self.points = 0
        print(f"{self.name} leveled up to level {self.level}!")

    def earn_points(self, points):
        """
        Increases the player's points.

        :param points: int - The number of points to earn.
        """
        if points < 0:
            raise ValueError("Points earned cannot be negative.")
        self.points += points
        print(f"{self.name} earned {points} points. Total points: {self.points}")

def simulate_leveling_up(player, rounds=5):
    """
    Simulates the leveling-up process for a player over a number of rounds.

    :param player: Player - The player to simulate for.
    :param rounds: int - The number of rounds to simulate (default is 5).
    """
    for round_number in range(1, rounds + 1):
        print(f"\n--- Round {round_number} ---")
        points_earned = random.randint(10, 50)  # Simulate earning points
        player.earn_points(points_earned)

        # Example point allocation strategy
        allocation_strategy = {
            'speed': random.randint(0, player.points),
            'endurance': random.randint(0, player.points),
            'luck': player.points  # Allocate remaining points to luck
        }

        try:
            player.allocate_points(allocation_strategy)
        except ValueError as e:
            print(f"Error during point allocation: {e}")

        # Level up if points reach a threshold
        if player.points >= 100:  # Example threshold for leveling up
            player.level_up()

if __name__ == "__main__":
    # Create a player instance
    player_name = input("Enter the player's name: ")
    player = Player(name=player_name)

    # Start the leveling-up simulation
    simulate_leveling_up(player)
```
