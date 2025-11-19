"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Create a program to model the behavior of individual sprinklers activating based on proximity to a fire, as explained by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_83db976dabc35c39
Batch ID: 20250612_153224
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
from typing import List

class Fire:
    """Class representing a fire with a position."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_position(self) -> tuple:
        """Returns the position of the fire."""
        return self.x, self.y


class Sprinkler:
    """Class representing an individual sprinkler."""
    def __init__(self, id: int, x: float, y: float, activation_radius: float):
        self.id = id
        self.x = x
        self.y = y
        self.activation_radius = activation_radius
        self.active = False

    def check_activation(self, fire: Fire) -> None:
        """Checks if the sprinkler should activate based on the fire's position."""
        fire_x, fire_y = fire.get_position()
        distance = self.calculate_distance(fire_x, fire_y)

        if distance <= self.activation_radius:
            self.activate()
        else:
            self.deactivate()

    def calculate_distance(self, fire_x: float, fire_y: float) -> float:
        """Calculates the distance from the sprinkler to the fire."""
        return ((self.x - fire_x) ** 2 + (self.y - fire_y) ** 2) ** 0.5

    def activate(self) -> None:
        """Activates the sprinkler."""
        if not self.active:
            self.active = True
            print(f"Sprinkler {self.id} activated.")

    def deactivate(self) -> None:
        """Deactivates the sprinkler."""
        if self.active:
            self.active = False
            print(f"Sprinkler {self.id} deactivated.")


class SprinklerSystem:
    """Class representing a system of sprinklers."""
    def __init__(self, sprinklers: List[Sprinkler]):
        self.sprinklers = sprinklers

    def simulate_fire(self, fire: Fire) -> None:
        """Simulates the sprinklers responding to a fire."""
        for sprinkler in self.sprinklers:
            sprinkler.check_activation(fire)


def main():
    """Main function to run the sprinkler simulation."""
    # Create a list of sprinklers with random positions
    sprinklers = [Sprinkler(id=i, x=random.uniform(0, 100), y=random.uniform(0, 100), activation_radius=20) for i in range(5)]
    
    # Create a fire at a random position
    fire = Fire(x=random.uniform(0, 100), y=random.uniform(0, 100))

    print("Fire is at position:", fire.get_position())
    
    # Simulate the sprinkler system responding to the fire
    sprinkler_system = SprinklerSystem(sprinklers)
    sprinkler_system.simulate_fire(fire)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
