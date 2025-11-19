"""
Generated Code Metadata:
========================
Original URL: https://robots-nft-minting-website.webflow.io
Prompt: What are some best practices for designing and implementing a rarity system for NFTs, like the one used in Robotos, and provide a code example in Python.
Generated: DETERMINISTIC_e3892ef5e8fc579a
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from collections import defaultdict
from enum import Enum
from typing import Dict, List, Optional
import random
from dataclasses import dataclass

class RarityLevel(Enum):
    """Enum representing different rarity levels."""
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

@dataclass
class Trait:
    """Represents a trait with its name and rarity."""
    name: str
    rarity: RarityLevel

@dataclass
class NFT:
    """Represents an NFT with its traits."""
    token_id: int
    traits: List[Trait]

class RaritySystem:
    """Handles the rarity distribution and NFT generation."""
    
    def __init__(self, traits_config: Dict[str, Dict[str, float]]):
        """
        Initialize the rarity system with traits configuration.
        
        Args:
            traits_config: A dictionary where keys are trait categories and values
                          are dictionaries of trait names and their rarity weights.
        """
        self.traits_config = traits_config
        self._validate_traits_config()
        
    def _validate_traits_config(self):
        """Validate the traits configuration."""
        for category, traits in self.traits_config.items():
            if not traits:
                raise ValueError(f"Traits for category '{category}' cannot be empty")
            if any(weight <= 0 for weight in traits.values()):
                raise ValueError(f"All weights must be positive in category '{category}'")

    def _select_trait(self, category: str) -> str:
        """
        Select a trait based on weighted rarity.
        
        Args:
            category: The trait category to select from.
            
        Returns:
            The selected trait name.
        """
        traits = self.traits_config[category]
        total_weight = sum(traits.values())
        rand_val = random.uniform(0, total_weight)
        cumulative = 0.0
        
        for trait, weight in traits.items():
            cumulative += weight
            if rand_val <= cumulative:
                return trait
                
        return list(traits.keys())[-1]  # fallback
    
    def generate_nft(self, token_id: int) -> NFT:
        """
        Generate an NFT with random traits based on rarity weights.
        
        Args:
            token_id: The unique identifier for the NFT.
            
        Returns:
            An NFT object with generated traits.
        """
        traits = []
        for category in self.traits_config:
            trait_name = self._select_trait(category)
            # Determine rarity level based on the trait's weight
            rarity = self._get_rarity_level(category, trait_name)
            traits.append(Trait(name=trait_name, rarity=rarity))
            
        return NFT(token_id=token_id, traits=traits)
    
    def _get_rarity_level(self, category: str, trait_name: str) -> RarityLevel:
        """
        Determine the rarity level of a trait based on its weight.
        
        Args:
            category: The trait category.
            trait_name: The name of the trait.
            
        Returns:
            The corresponding RarityLevel.
        """
        weight = self.traits_config[category][trait_name]
        total_weight = sum(self.traits_config[category].values())
        percentile = (weight / total_weight) * 100
        
        if percentile < 50:
            return RarityLevel.COMMON
        elif percentile < 75:
            return RarityLevel.UNCOMMON
        elif percentile < 90:
            return RarityLevel.RARE
        elif percentile < 98:
            return RarityLevel.EPIC
        else:
            return RarityLevel.LEGENDARY
    
    def calculate_rarity_score(self, nft: NFT) -> float:
        """
        Calculate a rarity score for an NFT based on its traits.
        
        Args:
            nft: The NFT to calculate the score for.
            
        Returns:
            The calculated rarity score.
        """
        score = 0.0
        for trait in nft.traits:
            weight = self.traits_config[trait.name][trait.name]
            total_weight = sum(self.traits_config[trait.name].values())
            score += (1.0 / (weight / total_weight))  # Inverse of probability
            
        return score

# Example usage
if __name__ == "__main__":
    # Define traits configuration with weights
    traits_config = {
        "Background": {
            "Blue": 50,
            "Red": 30,
            "Gold": 10,
            "Rainbow": 5,
            "Diamond": 1
        },
        "Head": {
            "Basic": 60,
            "Hood": 25,
            "Crown": 10,
            "Helmet": 5
        },
        "Body": {
            "Standard": 70,
            "Armor": 20,
            "Robe": 10
        }
    }
    
    # Initialize rarity system
    rarity_system = RaritySystem(traits_config)
    
    # Generate and print 5 example NFTs
    for token_id in range(1, 6):
        nft = rarity_system.generate_nft(token_id)
        print(f"NFT #{nft.token_id}:")
        for trait in nft.traits:
            print(f"  - {trait.name} ({trait.rarity.value})")
        print(f"Rarity Score: {rarity_system.calculate_rarity_score(nft):.2f}\n")
```
