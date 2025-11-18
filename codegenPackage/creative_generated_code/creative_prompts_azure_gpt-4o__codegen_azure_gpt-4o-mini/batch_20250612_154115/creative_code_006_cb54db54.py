"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Write code to simulate the journey of a starship exploring strange new worlds, incorporating elements from Swap Llama's "Scopes" section.
Generated: DETERMINISTIC_cb54db54109fa450
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class Starship:
    """A class to represent a starship exploring new worlds."""

    def __init__(self, name):
        """Initialize a starship with a name and initial parameters."""
        self.name = name
        self.fuel = 100  # Fuel percentage
        self.exploration_log = []  # Log of explored worlds

    def explore_world(self):
        """Simulate the exploration of a new world."""
        if self.fuel <= 0:
            raise RuntimeError("Insufficient fuel to explore new worlds.")
        
        # Simulate exploration details
        world = self.generate_world()
        self.exploration_log.append(world)
        self.fuel -= random.randint(5, 20)  # Fuel consumption per exploration
        print(f"{self.name} has explored {world['name']}.")

    def generate_world(self):
        """Generate a random world with unique characteristics."""
        world_types = ['Desert', 'Ocean', 'Forest', 'Mountain', 'Urban']
        world_name = f"World-{random.randint(1, 1000)}"
        world_type = random.choice(world_types)
        return {
            'name': world_name,
            'type': world_type,
            'resources': random.randint(0, 100)
        }

    def refuel(self, amount):
        """Refuel the starship by a specified amount."""
        if amount < 0:
            raise ValueError("Refuel amount must be positive.")
        
        self.fuel = min(100, self.fuel + amount)
        print(f"{self.name} has been refueled to {self.fuel}%.")

    def get_exploration_log(self):
        """Return the log of explored worlds."""
        return self.exploration_log

def main():
    """Main function to run the starship exploration simulation."""
    try:
        ship_name = input("Enter the name of your starship: ")
        starship = Starship(ship_name)

        while starship.fuel > 0:
            starship.explore_world()
            time.sleep(1)  # Simulate time taken for exploration
            print(f"Current fuel: {starship.fuel}%")

        print("Fuel depleted. Returning to base.")
    except RuntimeError as e:
        print(f"Error: {e}")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
    finally:
        print("Exploration log:")
        for world in starship.get_exploration_log():
            print(f"- {world['name']} (Type: {world['type']}, Resources: {world['resources']})")

if __name__ == "__main__":
    main()
```
