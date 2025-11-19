"""
Generated Code Metadata:
========================
Original URL: https://embersft.costhentic.com
Prompt: Create a rarity tier system for NFTs, like Embers, using a programming language of your choice, that takes into account the 150 traits and 1/1 rare Embers.
Generated: DETERMINISTIC_bfbc58ff92a82320
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class RarityTier(Enum):
    """Rarity tiers for Embers NFTs"""
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5
    MYTHIC = 6
    ULTRA_RARE = 7
    ONE_OF_ONE = 8

class Ember:
    """Represents an Ember NFT"""
    def __init__(self, id: int, traits: List[str]):
        """
        Initializes an Ember NFT

        Args:
        id (int): Unique identifier for the Ember
        traits (List[str]): List of traits for the Ember
        """
        self.id = id
        self.traits = traits

class RaritySystem:
    """Manages the rarity tier system for Embers NFTs"""
    def __init__(self):
        self.rarity_distribution = {
            RarityTier.COMMON: 0.4,
            RarityTier.UNCOMMON: 0.3,
            RarityTier.RARE: 0.15,
            RarityTier.EPIC: 0.075,
            RarityTier.LEGENDARY: 0.025,
            RarityTier.MYTHIC: 0.01,
            RarityTier.ULTRA_RARE: 0.005,
            RarityTier.ONE_OF_ONE: 0.001
        }
        self.trait_rarity = self.calculate_trait_rarity()

    def calculate_trait_rarity(self) -> Dict[str, float]:
        """
        Calculates the rarity of each trait

        Returns:
        Dict[str, float]: A dictionary mapping traits to their rarity
        """
        # For simplicity, assume each trait has an equal chance of being selected
        # In a real-world scenario, this would be calculated based on historical data
        num_traits = 150
        trait_rarity = {}
        for i in range(num_traits):
            trait_rarity[f"Trait {i}"] = 1 / num_traits
        return trait_rarity

    def determine_rarity_tier(self, ember: Ember) -> RarityTier:
        """
        Determines the rarity tier of an Ember NFT

        Args:
        ember (Ember): The Ember NFT to determine the rarity tier for

        Returns:
        RarityTier: The rarity tier of the Ember NFT
        """
        # Calculate the total rarity of the Ember based on its traits
        total_rarity = sum(self.trait_rarity[trait] for trait in ember.traits)

        # Map the total rarity to a rarity tier
        rand = 0
        cumulative_prob = 0
        for tier, prob in self.rarity_distribution.items():
            cumulative_prob += prob
            if rand < cumulative_prob:
                return tier

        # Default to COMMON if no tier is selected
        return RarityTier.COMMON

    def generate_ember(self) -> Ember:
        """
        Generates a new Ember NFT with a random set of traits

        Returns:
        Ember: The generated Ember NFT
        """
        import random
        num_traits = 150
        traits = random.sample([f"Trait {i}" for i in range(num_traits)], random.randint(1, num_traits))
        return Ember(1, traits)

    def assign_rarity_tier(self, ember: Ember) -> RarityTier:
        """
        Assigns a rarity tier to an Ember NFT

        Args:
        ember (Ember): The Ember NFT to assign a rarity tier to

        Returns:
        RarityTier: The assigned rarity tier
        """
        if len(ember.traits) == 0:
            raise ValueError("Ember must have at least one trait")

        # 1/1 rare Embers are always ONE_OF_ONE
        if ember.id == 1:
            return RarityTier.ONE_OF_ONE

        return self.determine_rarity_tier(ember)

def main():
    rarity_system = RaritySystem()
    ember = rarity_system.generate_ember()
    print(f"Ember {ember.id} has traits: {ember.traits}")
    rarity_tier = rarity_system.assign_rarity_tier(ember)
    print(f"Ember {ember.id} has rarity tier: {rarity_tier.name}")

if __name__ == "__main__":
    main()
```
