"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thecannibals.xyz
Prompt: Write a Python script that simulates survival scenarios for characters stranded on an island, incorporating elements from "The Cannibals" project, such as resource management and alliance creation.
Generated: DETERMINISTIC_843adf42dc6dd973
Batch ID: 20250612_160507
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

class Character:
    """Class representing a character on the island."""
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.resources = {
            "food": 0,
            "water": 0,
            "shelter": 0
        }
        self.alliances = []

    def gather_resources(self):
        """Gathers random resources."""
        gathered_food = random.randint(0, 10)
        gathered_water = random.randint(0, 5)
        gathered_shelter = random.randint(0, 3)

        self.resources["food"] += gathered_food
        self.resources["water"] += gathered_water
        self.resources["shelter"] += gathered_shelter

        print(f"{self.name} gathered: {gathered_food} food, {gathered_water} water, {gathered_shelter} shelter.")

    def form_alliance(self, other_character):
        """Forms an alliance with another character."""
        if other_character not in self.alliances:
            self.alliances.append(other_character)
            other_character.alliances.append(self)
            print(f"{self.name} formed an alliance with {other_character.name}.")
        else:
            print(f"{self.name} is already allied with {other_character.name}.")

    def survive_day(self):
        """Simulates a day of survival, checking resources and health."""
        food_needed = 5
        water_needed = 3
        
        if self.resources["food"] < food_needed:
            self.health -= 10
            print(f"{self.name} didn't have enough food. Health is now {self.health}.")
        else:
            self.resources["food"] -= food_needed

        if self.resources["water"] < water_needed:
            self.health -= 5
            print(f"{self.name} didn't have enough water. Health is now {self.health}.")
        else:
            self.resources["water"] -= water_needed

        if self.health <= 0:
            print(f"{self.name} has starved or dehydrated to death.")

class Island:
    """Class representing the island with characters and game logic."""
    
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        """Adds a character to the island."""
        self.characters.append(character)

    def simulate_day(self):
        """Simulates a day on the island for all characters."""
        for character in self.characters:
            character.gather_resources()
            character.survive_day()

    def save_state(self, filename):
        """Saves the current state of the island to a file."""
        state = {
            "characters": [
                {
                    "name": character.name,
                    "health": character.health,
                    "resources": character.resources,
                    "alliances": [ally.name for ally in character.alliances]
                } for character in self.characters
            ]
        }
        with open(filename, 'w') as f:
            json.dump(state, f)
        print("Game state saved.")

# Example usage
if __name__ == "__main__":
    island = Island()

    # Create characters
    alice = Character("Alice")
    bob = Character("Bob")
    charlie = Character("Charlie")

    # Add characters to the island
    island.add_character(alice)
    island.add_character(bob)
    island.add_character(charlie)

    # Form alliances
    alice.form_alliance(bob)

    # Simulate a week on the island
    for _ in range(7):
        island.simulate_day()

    # Save the game state
    island.save_state("island_state.json")
```
