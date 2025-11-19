"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Create a Python program to simulate planetary exploration in Stellar Crop, generating random "keşfedilmemiş gezegen türleri" with unique resources and challenges.
Generated: DETERMINISTIC_a6192ebc62143d72
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json

class Planet:
    """Class representing a planet with unique resources and challenges."""
    
    def __init__(self, name, resources, challenges):
        self.name = name
        self.resources = resources
        self.challenges = challenges

    def to_dict(self):
        """Convert the planet object to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'resources': self.resources,
            'challenges': self.challenges
        }

def generate_random_planet():
    """Generate a random planet with unique resources and challenges."""
    planet_names = ["Zyphor", "Klyntar", "Vortan", "Xelthar", "Qyron"]
    resources = ["Water", "Minerals", "Gases", "Organic Life", "Rare Metals"]
    challenges = ["Extreme Weather", "High Radiation", "Hostile Lifeforms", "Lack of Resources", "Geological Instability"]

    name = random.choice(planet_names)
    unique_resources = random.sample(resources, k=random.randint(1, len(resources)))
    unique_challenges = random.sample(challenges, k=random.randint(1, len(challenges)))

    return Planet(name, unique_resources, unique_challenges)

def save_planets_to_file(planets, filename):
    """Save the list of planets to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump([planet.to_dict() for planet in planets], file, indent=4)
    except IOError as e:
        print(f"Error saving planets to file: {e}")

def main():
    """Main function to simulate planetary exploration."""
    num_planets = 5  # Number of planets to generate
    planets = []

    for _ in range(num_planets):
        planet = generate_random_planet()
        planets.append(planet)

    # Save generated planets to a file
    save_planets_to_file(planets, 'planets.json')

    # Output the generated planets
    for planet in planets:
        print(f"Planet Name: {planet.name}")
        print(f"Resources: {', '.join(planet.resources)}")
        print(f"Challenges: {', '.join(planet.challenges)}")
        print("-" * 40)

if __name__ == "__main__":
    main()
```
