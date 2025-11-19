"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Design a simulation-based game like Parallel Colony, where players can interact with their avatars and make decisions that impact the game world.
Generated: DETERMINISTIC_17ff3cc2514f9df7
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# parallel_colony.py

import random
import time
from typing import List, Dict

class Avatar:
    """Represents a player's avatar in the game."""

    def __init__(self, name: str, energy: int = 100):
        """
        Initializes an Avatar object.

        Args:
            name (str): The avatar's name.
            energy (int): The avatar's initial energy level. Defaults to 100.
        """
        self.name = name
        self.energy = energy
        self.happiness = 50

    def is_alive(self) -> bool:
        """Checks if the avatar is alive (energy > 0)."""
        return self.energy > 0

    def update_energy(self, change: int):
        """Updates the avatar's energy level."""
        self.energy += change
        if self.energy < 0:
            self.energy = 0

    def update_happiness(self, change: int):
        """Updates the avatar's happiness level."""
        self.happiness += change
        if self.happiness < 0:
            self.happiness = 0
        elif self.happiness > 100:
            self.happiness = 100


class Colony:
    """Represents a player's colony in the game."""

    def __init__(self, name: str):
        """
        Initializes a Colony object.

        Args:
            name (str): The colony's name.
        """
        self.name = name
        self.resources: Dict[str, int] = {"food": 100, "water": 100, "materials": 100}
        self.avatars: List[Avatar] = []

    def add_avatar(self, avatar: Avatar):
        """Adds an avatar to the colony."""
        self.avatars.append(avatar)

    def update_resources(self, resource: str, change: int):
        """Updates the colony's resources."""
        if resource in self.resources:
            self.resources[resource] += change
            if self.resources[resource] < 0:
                self.resources[resource] = 0

    def is_resource_available(self, resource: str, amount: int) -> bool:
        """Checks if the colony has enough resources."""
        return self.resources[resource] >= amount


class Game:
    """Represents the game world."""

    def __init__(self):
        """Initializes a Game object."""
        self.colonies: List[Colony] = []
        self.current_colony: Colony = None

    def create_colony(self, name: str) -> Colony:
        """
        Creates a new colony.

        Args:
            name (str): The colony's name.

        Returns:
            Colony: The newly created colony.
        """
        colony = Colony(name)
        self.colonies.append(colony)
        return colony

    def switch_colony(self, colony: Colony):
        """Switches to a different colony."""
        if colony in self.colonies:
            self.current_colony = colony

    def simulate_day(self):
        """Simulates a day in the game."""
        if self.current_colony:
            # Update resources
            self.current_colony.update_resources("food", -10)
            self.current_colony.update_resources("water", -5)

            # Update avatars' energy and happiness
            for avatar in self.current_colony.avatars:
                avatar.update_energy(-5)
                avatar.update_happiness(random.randint(-10, 10))

            # Check for avatar deaths
            self.current_colony.avatars = [avatar for avatar in self.current_colony.avatars if avatar.is_alive()]


def main():
    game = Game()

    # Create a new colony
    colony = game.create_colony("My Colony")
    game.switch_colony(colony)

    # Create avatars
    avatar1 = Avatar("John")
    avatar2 = Avatar("Jane")
    colony.add_avatar(avatar1)
    colony.add_avatar(avatar2)

    # Game loop
    while True:
        print("\n--- Colony Status ---")
        print(f"Resources: {colony.resources}")
        print(f"Avatars: {[avatar.name for avatar in colony.avatars]}")

        print("\n--- Actions ---")
        print("1. Simulate day")
        print("2. Add resource")
        print("3. Create avatar")
        print("4. Switch colony")
        print("5. Exit")

        action = input("Choose an action: ")

        if action == "1":
            game.simulate_day()
            time.sleep(1)
        elif action == "2":
            resource = input("Enter resource (food, water, materials): ")
            amount = int(input("Enter amount: "))
            colony.update_resources(resource, amount)
        elif action == "3":
            name = input("Enter avatar name: ")
            avatar = Avatar(name)
            colony.add_avatar(avatar)
        elif action == "4":
            # Switch colony (not implemented)
            pass
        elif action == "5":
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
```
