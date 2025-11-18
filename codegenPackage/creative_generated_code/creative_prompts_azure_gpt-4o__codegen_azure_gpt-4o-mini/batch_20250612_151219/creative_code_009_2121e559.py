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
class MicroPet:
    """
    A class to represent a MicroPet NFT.

    Attributes
    ----------
    name : str
        the name of the MicroPet
    rarity : str
        the rarity of the MicroPet (e.g., 'Common', 'Rare', 'Epic', 'Legendary')
    multiplier : float
        the multiplier for leveling up based on rarity
    level : int
        the current level of the MicroPet

    Methods
    -------
    level_up():
        Increases the MicroPet's level based on its rarity multiplier.
    rank():
        Returns the rank of the MicroPet based on its rarity.
    """

    rarity_multipliers = {
        'Common': 1.0,
        'Rare': 1.5,
        'Epic': 2.0,
        'Legendary': 3.0
    }

    def __init__(self, name, rarity):
        """
        Constructs all the necessary attributes for the MicroPet object.

        Parameters
        ----------
        name : str
            the name of the MicroPet
        rarity : str
            the rarity of the MicroPet
        """
        self.name = name
        self.rarity = rarity
        self.multiplier = self.rarity_multipliers.get(rarity, 1.0)
        self.level = 1

    def level_up(self):
        """
        Increases the MicroPet's level based on its rarity multiplier and logs the level-up.
        """
        try:
            previous_level = self.level
            self.level += 1
            print(f"{self.name} leveled up from {previous_level} to {self.level}!")
        except Exception as e:
            print(f"An error occurred while leveling up: {e}")

    def rank(self):
        """
        Returns the rank of the MicroPet based on its rarity.

        Returns
        -------
        str
            The rank of the MicroPet
        """
        return self.rarity

    
def simulate_ranking_and_leveling_up(pets):
    """
    Simulates the ranking and leveling-up process for a list of MicroPets.

    Parameters
    ----------
    pets : list
        A list of MicroPet objects
    """
    for pet in pets:
        try:
            print(f"--- Processing {pet.name} ---")
            print(f"Initial Level: {pet.level}, Rarity: {pet.rank()}")
            pet.level_up()
            print(f"New Level: {pet.level}, Multiplier: {pet.multiplier}\n")
        except Exception as e:
            print(f"An error occurred while processing {pet.name}: {e}")


if __name__ == "__main__":
    # Create a list of MicroPets
    pets = [
        MicroPet("Fluffy", "Common"),
        MicroPet("Spike", "Rare"),
        MicroPet("Whiskers", "Epic"),
        MicroPet("Shadow", "Legendary"),
    ]
    
    # Simulate the ranking and leveling-up process
    simulate_ranking_and_leveling_up(pets)
```
