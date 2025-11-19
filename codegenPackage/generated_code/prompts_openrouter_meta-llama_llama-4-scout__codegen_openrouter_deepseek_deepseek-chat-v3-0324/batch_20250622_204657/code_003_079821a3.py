"""
Generated Code Metadata:
========================
Original URL: https://micropets-migration.pages.dev
Prompt: Design a rarity system for an NFT collection, similar to MicroPets, with 8 unique items ranging from Common to Mythic, and provide a probability distribution for each item.
Generated: DETERMINISTIC_079821a3be8f5df2
Batch ID: 20250622_204657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum, auto
from typing import Dict, List, Tuple

class Rarity(Enum):
    """Enum representing the rarity levels of NFT items."""
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()
    MYTHIC = auto()
    ULTRA_RARE = auto()
    SECRET_RARE = auto()

class NFTItem:
    """Class representing an NFT item with rarity and name."""
    def __init__(self, name: str, rarity: Rarity):
        self.name = name
        self.rarity = rarity

    def __str__(self):
        return f"{self.name} ({self.rarity.name})"

class RaritySystem:
    """System for generating NFT items with weighted probabilities."""
    def __init__(self):
        self.rarity_distribution: Dict[Rarity, float] = {
            Rarity.COMMON: 0.40,
            Rarity.UNCOMMON: 0.25,
            Rarity.RARE: 0.15,
            Rarity.EPIC: 0.10,
            Rarity.LEGENDARY: 0.05,
            Rarity.MYTHIC: 0.03,
            Rarity.ULTRA_RARE: 0.015,
            Rarity.SECRET_RARE: 0.005,
        }
        self.validate_distribution()
        self.items: List[NFTItem] = self._initialize_items()

    def validate_distribution(self) -> None:
        """Validate that probabilities sum to 1 (100%)."""
        total = sum(self.rarity_distribution.values())
        if not round(total, 2) == 1.0:
            raise ValueError("Rarity distribution probabilities must sum to 1.0")

    def _initialize_items(self) -> List[NFTItem]:
        """Initialize the collection of NFT items with their rarities."""
        return [
            NFTItem("Basic Pet", Rarity.COMMON),
            NFTItem("Cool Pet", Rarity.UNCOMMON),
            NFTItem("Shiny Pet", Rarity.RARE),
            NFTItem("Epic Pet", Rarity.EPIC),
            NFTItem("Legendary Pet", Rarity.LEGENDARY),
            NFTItem("Mythic Pet", Rarity.MYTHIC),
            NFTItem("Ultra Rare Pet", Rarity.ULTRA_RARE),
            NFTItem("Secret Rare Pet", Rarity.SECRET_RARE),
        ]

    def _get_weighted_rarity(self) -> Rarity:
        """Select a rarity based on weighted probabilities."""
        rarities = list(self.rarity_distribution.keys())
        weights = list(self.rarity_distribution.values())
        return random.choices(rarities, weights=weights, k=1)[0]

    def generate_item(self) -> NFTItem:
        """Generate a random NFT item based on rarity distribution."""
        selected_rarity = self._get_weighted_rarity()
        items_of_rarity = [item for item in self.items if item.rarity == selected_rarity]
        return random.choice(items_of_rarity)

    def get_distribution(self) -> List[Tuple[str, float]]:
        """Return the rarity distribution as a list of tuples."""
        return [(rarity.name, prob) for rarity, prob in self.rarity_distribution.items()]

# Example usage
if __name__ == "__main__":
    rarity_system = RaritySystem()
    
    # Print rarity distribution
    print("Rarity Distribution:")
    for rarity, prob in rarity_system.get_distribution():
        print(f"{rarity}: {prob * 100:.1f}%")
    
    # Generate 10 example items
    print("\nGenerated Items:")
    for _ in range(10):
        print(rarity_system.generate_item())
```
