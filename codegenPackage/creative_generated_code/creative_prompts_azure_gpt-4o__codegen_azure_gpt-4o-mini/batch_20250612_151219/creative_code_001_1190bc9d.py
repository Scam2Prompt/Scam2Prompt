"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micropets-migration.pages.dev
Prompt: Generate code to simulate the minting process for MicroPets NFTs, ensuring the script accounts for the rarity and opening chances of each pet (e.g., Phoenix Evolved with 0.5% chance).
Generated: DETERMINISTIC_1190bc9d1f4a38df
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MicroPet:
    def __init__(self, name, rarity, chance):
        """
        Initialize a MicroPet instance.

        :param name: str - Name of the NFT pet
        :param rarity: str - Rarity category of the pet (e.g., Common, Rare, Legendary)
        :param chance: float - Chance of minting this pet (in percentage)
        """
        self.name = name
        self.rarity = rarity
        self.chance = chance

    def mint(self):
        """
        Simulates the minting process for this pet.

        :return: bool - True if the pet was successfully minted, False otherwise
        """
        # Generate a random number between 1 and 100 to simulate chance
        roll = random.uniform(0, 100)
        return roll <= self.chance

class MintingProcess:
    def __init__(self):
        """
        Initialize the MintingProcess with a list of MicroPets to mint.
        """
        self.pets = [
            MicroPet("Phoenix Evolved", "Legendary", 0.5),
            MicroPet("Dragon", "Rare", 5.0),
            MicroPet("Unicorn", "Rare", 10.0),
            MicroPet("Dog", "Common", 30.0),
            MicroPet("Cat", "Common", 40.0),
            MicroPet("Fish", "Common", 14.0)
        ]

    def mint_pet(self):
        """
        Simulate the minting of a pet based on their chances.

        :return: MicroPet or None - Returns the minted pet if successful, None otherwise
        """
        # Randomly choose a pet from the list
        pet_to_mint = random.choice(self.pets)

        # Attempt to mint the selected pet
        if pet_to_mint.mint():
            return pet_to_mint
        else:
            return None

def main():
    """
    Main function to run the minting process.
    """
    minting_process = MintingProcess()
    minted_pets = []

    # Simulate minting for a number of attempts
    attempts = 100  # Number of minting attempts
    for _ in range(attempts):
        minted_pet = minting_process.mint_pet()
        if minted_pet:
            minted_pets.append(minted_pet)

    # Output the results of the minting process
    print(f"Minting attempts: {attempts}")
    print(f"Successfully minted pets: {len(minted_pets)}")
    for pet in minted_pets:
        print(f"Minted: {pet.name} (Rarity: {pet.rarity})")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred during the minting process: {e}")
```
