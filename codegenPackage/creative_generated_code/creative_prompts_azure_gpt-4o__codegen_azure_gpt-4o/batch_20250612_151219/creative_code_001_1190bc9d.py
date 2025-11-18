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

class PetNFT:
    """
    Class representing a MicroPets NFT with rarity and minting probabilities.
    """
    def __init__(self, name, rarity, minting_chance):
        """
        Initialize a PetNFT instance.
        :param name: Name of the pet (e.g., 'Phoenix Evolved').
        :param rarity: Rarity level of the pet (e.g., 'Legendary').
        :param minting_chance: Probability of minting this pet in percentage (e.g., 0.5 for 0.5%).
        """
        self.name = name
        self.rarity = rarity
        self.minting_chance = minting_chance

def mint_pet():
    """
    Simulates the minting process for MicroPets NFTs.
    :return: The name and rarity of the minted pet.
    """
    pets = [
        PetNFT("Phoenix Evolved", "Legendary", 0.5),
        PetNFT("Dragon Warrior", "Epic", 1.5),
        PetNFT("Shadow Wolf", "Rare", 5),
        PetNFT("Golden Retriever", "Uncommon", 15),
        PetNFT("Playful Cat", "Common", 78)
    ]

    # Calculate cumulative distribution for minting chances
    cumulative_chance = 0
    cumulative_distribution = []
    for pet in pets:
        cumulative_chance += pet.minting_chance
        cumulative_distribution.append(cumulative_chance)

    # Ensure chances sum to 100% (normalization check)
    assert cumulative_chance == 100, "Minting chances must sum up to 100%."

    # Generate a random number between 0 and 100 to simulate minting chance
    random_roll = random.uniform(0, 100)

    # Determine which pet was minted based on random roll
    for pet, upper_bound in zip(pets, cumulative_distribution):
        if random_roll <= upper_bound:
            return f"Minted Pet: {pet.name} ({pet.rarity})"

    # Fallback for unexpected errors
    return "Error: Unable to mint pet."

def main():
    """
    Main function to simulate the minting process multiple times.
    """
    try:
        print("Starting MicroPets NFT Minting Simulation...")
        for _ in range(10):  # Simulate minting 10 pets
            result = mint_pet()
            print(result)
    except Exception as e:
        print(f"An error occurred during minting: {e}")

if __name__ == "__main__":
    main()
```
