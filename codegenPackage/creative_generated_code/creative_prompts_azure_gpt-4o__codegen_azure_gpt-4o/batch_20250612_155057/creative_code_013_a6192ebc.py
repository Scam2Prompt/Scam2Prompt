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

# Define constants for the simulation
PLANET_TYPES = ["Rocky", "Gas Giant", "Ice", "Ocean", "Volcanic", "Desert", "Forest"]
RESOURCES = ["Iron", "Gold", "Hydrogen", "Water", "Silicon", "Uranium", "Carbon"]
CHALLENGES = ["Extreme Heat", "Extreme Cold", "Radiation Storms", "Toxic Atmosphere", "High Gravity", "Low Gravity", "Meteor Showers"]

class Planet:
    """
    Class representing a randomly generated planet with unique properties.
    """
    def __init__(self, name):
        self.name = name
        self.type = random.choice(PLANET_TYPES)
        self.resources = random.sample(RESOURCES, random.randint(1, 3))
        self.challenges = random.sample(CHALLENGES, random.randint(1, 2))
    
    def __str__(self):
        """
        String representation of the planet details.
        """
        return (f"Planet Name: {self.name}\n"
                f"Type: {self.type}\n"
                f"Resources: {', '.join(self.resources)}\n"
                f"Challenges: {', '.join(self.challenges)}\n")

def generate_planet_name():
    """
    Generate a unique name for a planet using random letters and numbers.
    """
    prefix = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3))
    suffix = ''.join(random.choices("0123456789", k=3))
    return f"{prefix}-{suffix}"

def simulate_exploration(num_planets):
    """
    Simulate the exploration of a given number of planets.

    Parameters:
        num_planets (int): Number of planets to generate and explore.
    
    Returns:
        list: A list of Planet objects representing the explored planets.
    """
    if num_planets <= 0:
        raise ValueError("Number of planets must be greater than zero.")
    
    planets = []
    for _ in range(num_planets):
        name = generate_planet_name()
        planet = Planet(name)
        planets.append(planet)
    return planets

def main():
    """
    Main function to run the planetary exploration simulation.
    """
    try:
        print("Welcome to Stellar Crop: Planetary Exploration Simulator!")
        num_planets = int(input("Enter the number of planets to explore: "))
        
        planets = simulate_exploration(num_planets)
        print("\nExploration Results:")
        for planet in planets:
            print(planet)
            print("-" * 40)
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
