"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Create a program to model the behavior of individual sprinklers activating based on proximity to a fire, as explained by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_83db976dabc35c39
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class Fire:
    """
    Represents a fire with a specific location (x, y).
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Sprinkler:
    """
    Represents a sprinkler with a specific location (x, y) and activation radius.
    """
    def __init__(self, x, y, activation_radius):
        self.x = x
        self.y = y
        self.activation_radius = activation_radius
        self.is_activated = False  # Tracks whether the sprinkler is activated

    def check_activation(self, fire):
        """
        Checks if the sprinkler should activate based on its proximity to the fire.
        """
        distance = math.sqrt((self.x - fire.x) ** 2 + (self.y - fire.y) ** 2)
        if distance <= self.activation_radius:
            self.activate()

    def activate(self):
        """
        Activates the sprinkler.
        """
        self.is_activated = True
        print(f"Sprinkler at ({self.x}, {self.y}) activated.")


class SprinklerSystem:
    """
    Represents a system of sprinklers and models their behavior when a fire occurs.
    """
    def __init__(self):
        self.sprinklers = []

    def add_sprinkler(self, sprinkler):
        """
        Adds a sprinkler to the system.
        """
        self.sprinklers.append(sprinkler)

    def respond_to_fire(self, fire):
        """
        Activates sprinklers based on their proximity to the fire.
        """
        print(f"Fire detected at ({fire.x}, {fire.y}). Evaluating sprinklers...")
        for sprinkler in self.sprinklers:
            sprinkler.check_activation(fire)

    def display_status(self):
        """
        Displays the status of all sprinklers in the system.
        """
        for sprinkler in self.sprinklers:
            status = "Activated" if sprinkler.is_activated else "Inactive"
            print(f"Sprinkler at ({sprinkler.x}, {sprinkler.y}): {status}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create a sprinkler system
        system = SprinklerSystem()

        # Add sprinklers to the system
        system.add_sprinkler(Sprinkler(0, 0, 5))
        system.add_sprinkler(Sprinkler(5, 5, 5))
        system.add_sprinkler(Sprinkler(10, 10, 5))

        # Create a fire at a specific location
        fire = Fire(3, 3)

        # Respond to the fire
        system.respond_to_fire(fire)

        # Display the status of sprinklers
        system.display_status()

    except Exception as e:
        print(f"An error occurred: {e}")
```
