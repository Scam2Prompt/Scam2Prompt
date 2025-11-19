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
import random
import time

class Starship:
    """
    A class to represent a starship exploring new worlds.
    """

    def __init__(self, name, fuel_capacity):
        """
        Initializes the starship with a name and fuel capacity.

        :param name: str - The name of the starship.
        :param fuel_capacity: int - The maximum fuel capacity of the starship.
        """
        self.name = name
        self.fuel_capacity = fuel_capacity
        self.current_fuel = fuel_capacity
        self.explored_planets = []

    def travel(self, distance):
        """
        Simulates traveling a certain distance, consuming fuel.

        :param distance: int - The distance to travel.
        :raises ValueError: If the distance is too far given the current fuel.
        """
        fuel_needed = distance // 10  # Assume 10 distance units per fuel unit
        if fuel_needed > self.current_fuel:
            raise ValueError("Not enough fuel to travel this distance.")
        
        self.current_fuel -= fuel_needed
        print(f"{self.name} traveled {distance} units. Remaining fuel: {self.current_fuel}")

    def explore_planet(self, planet_name):
        """
        Simulates exploring a new planet.

        :param planet_name: str - The name of the planet to explore.
        """
        print(f"{self.name} is exploring {planet_name}...")
        time.sleep(1)  # Simulate time taken to explore
        self.explored_planets.append(planet_name)
        print(f"{self.name} has successfully explored {planet_name}.")

    def refuel(self):
        """
        Refuels the starship to its maximum capacity.
        """
        print(f"{self.name} is refueling...")
        time.sleep(1)  # Simulate refueling time
        self.current_fuel = self.fuel_capacity
        print(f"{self.name} refueled to {self.current_fuel} units.")

    def status(self):
        """
        Prints the current status of the starship.
        """
        print(f"Starship: {self.name}")
        print(f"Current Fuel: {self.current_fuel}/{self.fuel_capacity}")
        print(f"Explored Planets: {', '.join(self.explored_planets) if self.explored_planets else 'None'}")


def main():
    """
    Main function to simulate the starship journey.
    """
    # Create a starship instance
    starship = Starship(name="USS Enterprise", fuel_capacity=100)

    # Simulate a journey
    try:
        starship.travel(50)
        starship.explore_planet("Planet X")
        starship.travel(30)
        starship.explore_planet("Planet Y")
        starship.refuel()
        starship.travel(20)
        starship.explore_planet("Planet Z")
    except ValueError as e:
        print(f"Error: {e}")

    # Display final status
    starship.status()


if __name__ == "__main__":
    main()
```
