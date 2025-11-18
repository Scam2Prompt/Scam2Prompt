"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micropets-migration.pages.dev
Prompt: Write a program to simulate the ranking and leveling-up process for MicroPets NFTs based on their rarity and multiplier attributes.
Generated: DETERMINISTIC_2121e55916e55b3c
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class MicroPet:
    """
    Represents a MicroPet NFT with attributes for rarity, multiplier, and level.
    """

    def __init__(self, name, rarity, multiplier):
        """
        Initialize a MicroPet object.
        
        :param name: Name of the MicroPet (string)
        :param rarity: Rarity level of the MicroPet (string, e.g., "Common", "Rare", "Epic", "Legendary")
        :param multiplier: Multiplier associated with the MicroPet (float)
        """
        self.name = name
        self.rarity = rarity
        self.multiplier = multiplier
        self.level = 1  # Default starting level
        self.experience = 0  # Starting experience points

    def add_experience(self, points):
        """
        Adds experience points to the MicroPet and handles level-ups.
        
        :param points: Number of experience points to add (int)
        """
        self.experience += points

        # Define experience thresholds for leveling up
        experience_thresholds = {
            1: 100,  # Level 1 -> Level 2 requires 100 XP
            2: 300,  # Level 2 -> Level 3 requires 300 XP
            3: 600,  # Level 3 -> Level 4 requires 600 XP
            # Add more thresholds if needed
        }

        while self.level in experience_thresholds and self.experience >= experience_thresholds[self.level]:
            self.level_up()

    def level_up(self):
        """
        Handles the leveling-up process for the MicroPet.
        """
        self.level += 1
        print(f"{self.name} has leveled up! New level: {self.level}")

    def __str__(self):
        """
        Returns a string representation of the MicroPet.
        """
        return f"MicroPet(name={self.name}, rarity={self.rarity}, multiplier={self.multiplier}, level={self.level}, experience={self.experience})"


def rank_micro_pets(micro_pets):
    """
    Ranks a list of MicroPets based on their rarity and multiplier attributes.

    :param micro_pets: List of MicroPet objects
    :return: List of MicroPet objects sorted by rank
    """
    # Define rarity ranking
    rarity_order = {
        "Common": 1,
        "Uncommon": 2,
        "Rare": 3,
        "Epic": 4,
        "Legendary": 5,
    }

    try:
        # Sort MicroPets primarily by rarity and secondarily by multiplier (descending order)
        sorted_pets = sorted(
            micro_pets,
            key=lambda pet: (rarity_order.get(pet.rarity, 0), pet.multiplier),
            reverse=True,
        )
        return sorted_pets
    except Exception as e:
        print(f"Error during ranking: {e}")
        return []


def simulate_micro_pets():
    """
    Simulates the ranking and leveling-up process for a collection of MicroPets.
    """
    # Create MicroPets
    pets = [
        MicroPet("Fluffy", "Rare", 2.5),
        MicroPet("Sparky", "Legendary", 4.0),
        MicroPet("Mittens", "Common", 1.2),
        MicroPet("Shadow", "Epic", 3.0),
    ]

    # Add experience points to simulate leveling up
    pets[0].add_experience(150)  # Fluffy gains experience
    pets[1].add_experience(100)  # Sparky gains experience
    pets[2].add_experience(50)   # Mittens gains experience
    pets[3].add_experience(300)  # Shadow gains experience

    # Rank MicroPets
    ranked_pets = rank_micro_pets(pets)

    # Display results
    print("Ranked MicroPets:")
    for pet in ranked_pets:
        print(pet)


if __name__ == "__main__":
    try:
        simulate_micro_pets()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
