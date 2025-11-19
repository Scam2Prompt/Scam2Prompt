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
import math

class Sprinkler:
    """
    Represents a fire sprinkler with properties and behavior.
    """

    def __init__(self, x, y, activation_radius):
        """
        Initializes a new sprinkler.

        Args:
            x (float): The x-coordinate of the sprinkler.
            y (float): The y-coordinate of the sprinkler.
            activation_radius (float): The radius within which the sprinkler activates.
        """
        self.x = x
        self.y = y
        self.activation_radius = activation_radius
        self.is_active = False

    def distance_to_fire(self, fire_x, fire_y):
        """
        Calculates the distance from the sprinkler to a fire.

        Args:
            fire_x (float): The x-coordinate of the fire.
            fire_y (float): The y-coordinate of the fire.

        Returns:
            float: The Euclidean distance from the sprinkler to the fire.
        """
        return math.sqrt((self.x - fire_x) ** 2 + (self.y - fire_y) ** 2)

    def update_status(self, fire_x, fire_y):
        """
        Updates the sprinkler's status based on proximity to a fire.

        Args:
            fire_x (float): The x-coordinate of the fire.
            fire_y (float): The y-coordinate of the fire.
        """
        distance = self.distance_to_fire(fire_x, fire_y)
        if distance <= self.activation_radius and not self.is_active:
            self.is_active = True
            print(f"Sprinkler at ({self.x}, {self.y}) activated.")
        elif distance > self.activation_radius and self.is_active:
            self.is_active = False
            print(f"Sprinkler at ({self.x}, {self.y}) deactivated.")


class FireSprinklerSystem:
    """
    Represents a system of fire sprinklers.
    """

    def __init__(self):
        """
        Initializes a new fire sprinkler system.
        """
        self.sprinklers = []

    def add_sprinkler(self, sprinkler):
        """
        Adds a sprinkler to the system.

        Args:
            sprinkler (Sprinkler): The sprinkler to add.
        """
        self.sprinklers.append(sprinkler)

    def update_sprinkler_status(self, fire_x, fire_y):
        """
        Updates the status of all sprinklers in the system based on proximity to a fire.

        Args:
            fire_x (float): The x-coordinate of the fire.
            fire_y (float): The y-coordinate of the fire.
        """
        for sprinkler in self.sprinklers:
            sprinkler.update_status(fire_x, fire_y)


def main():
    try:
        # Create a fire sprinkler system
        system = FireSprinklerSystem()

        # Create and add sprinklers to the system
        system.add_sprinkler(Sprinkler(0, 0, 5))
        system.add_sprinkler(Sprinkler(10, 0, 3))
        system.add_sprinkler(Sprinkler(5, 5, 4))

        # Simulate a fire at different locations
        print("Simulating fire at (2, 2):")
        system.update_sprinkler_status(2, 2)

        print("\nSimulating fire at (8, 1):")
        system.update_sprinkler_status(8, 1)

        print("\nSimulating fire at (6, 6):")
        system.update_sprinkler_status(6, 6)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
