"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Write a Python script that simulates survival scenarios for characters stranded on an island, incorporating elements from "The Cannibals" project, such as resource management and alliance creation.
Generated: DETERMINISTIC_843adf42dc6dd973
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional

class Character:
    """Represents a character stranded on the island."""
    
    def __init__(self, name: str):
        self.name = name
        self.resources: Dict[str, int] = {'food': 0, 'water': 0}
        self.allies: List['Character'] = []
        self.is_alive: bool = True

    def gather_resources(self, food: int, water: int):
        """Simulate gathering resources."""
        if not self.is_alive:
            raise ValueError(f"{self.name} is not alive and cannot gather resources.")
        self.resources['food'] += food
        self.resources['water'] += water
        print(f"{self.name} gathered {food} food and {water} water.")

    def form_alliance(self, other: 'Character'):
        """Form an alliance with another character."""
        if other not in self.allies and other.is_alive:
            self.allies.append(other)
            other.allies.append(self)  # Mutual alliance
            print(f"{self.name} formed an alliance with {other.name}.")

    def consume_resources(self):
        """Consume resources to survive."""
        if not self.is_alive:
            raise ValueError(f"{self.name} is not alive and cannot consume resources.")
        
        if self.resources['food'] > 0 and self.resources['water'] > 0:
            self.resources['food'] -= 1
            self.resources['water'] -= 1
            print(f"{self.name} consumed 1 food and 1 water.")
        else:
            self.is_alive = False
            print(f"{self.name} has died due to lack of resources.")

class Island:
    """Represents the island where characters are stranded."""
    
    def __init__(self):
        self.characters: List[Character] = []

    def add_character(self, character: Character):
        """Add a character to the island."""
        self.characters.append(character)
        print(f"{character.name} has arrived on the island.")

    def simulate_day(self):
        """Simulate a day on the island for all characters."""
        for character in self.characters:
            if character.is_alive:
                food_gathered = random.randint(0, 3)  # Random food gathered
                water_gathered = random.randint(0, 3)  # Random water gathered
                character.gather_resources(food_gathered, water_gathered)
                character.consume_resources()

def main():
    """Main function to run the survival simulation."""
    island = Island()
    
    # Create characters
    characters = [Character(name=f"Survivor {i}") for i in range(1, 6)]
    
    # Add characters to the island
    for character in characters:
        island.add_character(character)

    # Simulate multiple days
    for day in range(1, 11):  # Simulate 10 days
        print(f"\n--- Day {day} ---")
        island.simulate_day()

    # Display final status of characters
    for character in characters:
        status = "alive" if character.is_alive else "dead"
        print(f"{character.name} is {status} with resources: {character.resources}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
