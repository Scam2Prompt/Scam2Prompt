"""
Generated Code Metadata:
========================
Original URL: https://swap.depillama.com
Prompt: Write code to simulate the journey of a starship exploring strange new worlds, incorporating elements from Swap Llama's "Scopes" section.
Generated: DETERMINISTIC_cb54db54109fa450
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# starship_journey.py

class Starship:
    """Represents a starship exploring the galaxy."""

    def __init__(self, name, fuel_capacity, current_fuel):
        """
        Initializes a Starship object.

        Args:
            name (str): The name of the starship.
            fuel_capacity (float): The maximum fuel capacity of the starship.
            current_fuel (float): The current fuel level of the starship.
        """
        self.name = name
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel
        self.explored_worlds = []

    def explore_world(self, world_name):
        """
        Simulates the starship exploring a new world.

        Args:
            world_name (str): The name of the world to explore.

        Raises:
            ValueError: If the starship does not have enough fuel to explore.
        """
        if self.current_fuel <= 0:
            raise ValueError("Not enough fuel to explore")

        # Consume fuel for exploration
        self.current_fuel -= 10
        if self.current_fuel < 0:
            self.current_fuel = 0

        self.explored_worlds.append(world_name)
        print(f"{self.name} has explored {world_name}")

    def refuel(self, amount):
        """
        Refuels the starship.

        Args:
            amount (float): The amount of fuel to add.

        Raises:
            ValueError: If the refuel amount is negative.
        """
        if amount < 0:
            raise ValueError("Refuel amount cannot be negative")

        self.current_fuel = min(self.fuel_capacity, self.current_fuel + amount)
        print(f"{self.name} has refueled {amount} units")

    def status(self):
        """Prints the current status of the starship."""
        print(f"{self.name}'s Status:")
        print(f"Fuel: {self.current_fuel}/{self.fuel_capacity}")
        print(f"Explored Worlds: {', '.join(self.explored_worlds)}")


class Galaxy:
    """Represents a galaxy with multiple star systems."""

    def __init__(self):
        self.star_systems = {}

    def add_star_system(self, name, description):
        """
        Adds a star system to the galaxy.

        Args:
            name (str): The name of the star system.
            description (str): A brief description of the star system.
        """
        self.star_systems[name] = description

    def explore_star_system(self, starship, system_name):
        """
        Simulates a starship exploring a star system.

        Args:
            starship (Starship): The starship exploring the system.
            system_name (str): The name of the star system to explore.

        Raises:
            KeyError: If the star system does not exist.
        """
        if system_name not in self.star_systems:
            raise KeyError("Star system does not exist")

        print(f"Exploring {system_name}...")
        starship.explore_world(system_name)
        print(f"Discovered: {self.star_systems[system_name]}")


def main():
    galaxy = Galaxy()
    galaxy.add_star_system("Andromeda", "A distant galaxy with uncharted worlds")
    galaxy.add_star_system("Rigel", "A star system with habitable planets")

    starship = Starship("Aurora", 1000, 1000)

    try:
        galaxy.explore_star_system(starship, "Andromeda")
        starship.status()

        starship.refuel(-100)  # Test error handling

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

    try:
        starship.explore_world("Test World")
        starship.explore_world("Test World 2")
        starship.status()

        galaxy.explore_star_system(starship, "Non-existent System")  # Test error handling

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
