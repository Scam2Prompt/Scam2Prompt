"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Create a Python program to simulate planetary exploration in Stellar Crop, generating random "keşfedilmemiş gezegen türleri" with unique resources and challenges.
Generated: DETERMINISTIC_a6192ebc62143d72
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

class Planet:
    """
    A class to represent a planet with unique properties.

    Attributes:
        name (str): The name of the planet.
        resource_type (str): The type of resource found on the planet.
        challenge_type (str): The type of challenge present on the planet.
    """

    def __init__(self, name: str, resource_type: str, challenge_type: str):
        self.name = name
        self.resource_type = resource_type
        self.challenge_type = challenge_type

    def __str__(self):
        return (f"Planet Name: {self.name}\n"
                f"Resource Type: {self.resource_type}\n"
                f"Challenge Type: {self.challenge_type}")

class PlanetGenerator:
    """
    A class to generate random planets with unique resources and challenges.

    Attributes:
        resource_types (list): A list of possible resource types.
        challenge_types (list): A list of possible challenge types.
    """

    def __init__(self):
        self.resource_types = [
            "Rare Minerals", "Water Ice", "Ancient Artifacts", 
            "Alien Flora", "Energy Crystals"
        ]
        self.challenge_types = [
            "Intense Radiation", "Extreme Weather", 
            "Hostile Wildlife", "Toxic Atmosphere", 
            "Geological Instability"
        ]

    def generate_random_planet(self) -> Planet:
        """Generates and returns a random Planet instance."""
        name = self._generate_planet_name()
        resource_type = random.choice(self.resource_types)
        challenge_type = random.choice(self.challenge_types)
        return Planet(name, resource_type, challenge_type)

    def _generate_planet_name(self) -> str:
        """Generates a random planet name."""
        adjectives = ["Mysterious", "Ancient", "Forgotten", "Barren", "Lush"]
        planets = ["Zeta", "Alpha", "Beta", "Gamma", "Delta"]
        return f"{random.choice(adjectives)} {random.choice(planets)}"

def save_planets_to_file(planets: list, filename: str) -> None:
    """Saves a list of planets to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump([planet.__dict__ for planet in planets], file, indent=4)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    """Main function to simulate planetary exploration."""
    planet_generator = PlanetGenerator()
    planets = []

    # Generate a specified number of random planets
    number_of_planets = 5
    for _ in range(number_of_planets):
        new_planet = planet_generator.generate_random_planet()
        planets.append(new_planet)
        print(new_planet)
        print("-" * 40)

    # Save the generated planets to a file
    save_planets_to_file(planets, 'planets.json')

if __name__ == "__main__":
    main()
```
