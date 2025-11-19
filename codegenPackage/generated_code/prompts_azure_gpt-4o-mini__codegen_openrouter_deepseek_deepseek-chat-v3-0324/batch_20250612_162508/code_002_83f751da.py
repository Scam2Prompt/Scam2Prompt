"""
Generated Code Metadata:
========================
Original URL: https://ejelly.web.app
Prompt: What are the best practices for creating a rarity system for NFTs like the 1/1 Jelly Drop mentioned on ejelly.web.app?
Generated: DETERMINISTIC_83f751daeeab28cf
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional
from enum import Enum
from dataclasses import dataclass
import json

class Rarity(Enum):
    """Enum representing different rarity levels."""
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"
    ONE_OF_ONE = "1/1"

@dataclass
class NFT:
    """Data class representing an NFT with rarity attributes."""
    id: str
    name: str
    rarity: Rarity
    attributes: Dict[str, str]

class RaritySystem:
    """Class to handle NFT rarity distribution and generation."""
    
    def __init__(self, rarity_weights: Optional[Dict[Rarity, float]] = None):
        """
        Initialize the rarity system with optional custom weights.
        Default weights are provided if none are specified.
        """
        self.rarity_weights = rarity_weights or {
            Rarity.COMMON: 0.5,
            Rarity.UNCOMMON: 0.3,
            Rarity.RARE: 0.15,
            Rarity.EPIC: 0.04,
            Rarity.LEGENDARY: 0.009,
            Rarity.ONE_OF_ONE: 0.001
        }
        self._validate_weights()
        
    def _validate_weights(self):
        """Validate that rarity weights sum to approximately 1."""
        total = sum(self.rarity_weights.values())
        if not 0.99 <= total <= 1.01:
            raise ValueError(f"Rarity weights must sum to 1 (current sum: {total})")
    
    def generate_nft(self, nft_id: str, name: str, attributes: Dict[str, str]) -> NFT:
        """
        Generate an NFT with a random rarity based on configured weights.
        
        Args:
            nft_id: Unique identifier for the NFT
            name: Name of the NFT
            attributes: Dictionary of NFT attributes
            
        Returns:
            Generated NFT with assigned rarity
        """
        rarity = self._select_rarity()
        return NFT(id=nft_id, name=name, rarity=rarity, attributes=attributes)
    
    def _select_rarity(self) -> Rarity:
        """Select a rarity level based on configured weights."""
        rand_val = random.random()
        cumulative = 0.0
        
        for rarity, weight in self.rarity_weights.items():
            cumulative += weight
            if rand_val <= cumulative:
                return rarity
        
        return Rarity.COMMON  # fallback
    
    def generate_one_of_one(self, nft_id: str, name: str, attributes: Dict[str, str]) -> NFT:
        """
        Generate a guaranteed 1/1 NFT.
        
        Args:
            nft_id: Unique identifier for the NFT
            name: Name of the NFT
            attributes: Dictionary of NFT attributes
            
        Returns:
            Generated 1/1 NFT
        """
        return NFT(id=nft_id, name=name, rarity=Rarity.ONE_OF_ONE, attributes=attributes)
    
    def get_rarity_distribution(self, nfts: List[NFT]) -> Dict[Rarity, int]:
        """
        Calculate the distribution of rarities in a collection of NFTs.
        
        Args:
            nfts: List of NFTs to analyze
            
        Returns:
            Dictionary mapping rarity levels to counts
        """
        distribution = {rarity: 0 for rarity in Rarity}
        for nft in nfts:
            distribution[nft.rarity] += 1
        return distribution

# Example usage
if __name__ == "__main__":
    # Initialize rarity system
    rarity_system = RaritySystem()
    
    # Generate a collection of NFTs
    nft_collection = []
    for i in range(1000):
        nft = rarity_system.generate_nft(
            nft_id=f"nft_{i}",
            name=f"Jelly #{i}",
            attributes={"color": random.choice(["red", "blue", "green"]), "pattern": "striped"}
        )
        nft_collection.append(nft)
    
    # Add a special 1/1 NFT
    one_of_one = rarity_system.generate_one_of_one(
        nft_id="nft_special",
        name="Ultra Rare Jelly",
        attributes={"color": "rainbow", "pattern": "unique"}
    )
    nft_collection.append(one_of_one)
    
    # Get rarity distribution
    distribution = rarity_system.get_rarity_distribution(nft_collection)
    print("Rarity Distribution:")
    for rarity, count in distribution.items():
        print(f"{rarity.value}: {count}")
    
    # Save collection to JSON
    with open("nft_collection.json", "w") as f:
        json.dump([nft.__dict__ for nft in nft_collection], f, indent=2, default=str)
```
