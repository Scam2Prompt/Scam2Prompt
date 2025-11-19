"""
Generated Code Metadata:
========================
Original URL: https://rascalsnft.web.app
Prompt: What are the best practices for creating a rarity system for NFTs, based on the utilities described in the Rascals NFT project?
Generated: DETERMINISTIC_2aab6d45ac9cbd32
Batch ID: 20250612_155351
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
from typing import Dict, List, Optional, Tuple
import random

class RarityTier(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

class NFTAttribute:
    def __init__(self, name: str, values: Dict[str, float]):
        """
        Initialize an NFT attribute with possible values and their weights.
        
        Args:
            name: Name of the attribute (e.g., "Background")
            values: Dictionary of value: weight pairs (e.g., {"Red": 0.5, "Blue": 0.3})
        """
        self.name = name
        self.values = values
        self._normalize_weights()
    
    def _normalize_weights(self):
        """Normalize weights to sum to 1.0"""
        total = sum(self.values.values())
        self.values = {k: v/total for k, v in self.values.items()}
    
    def get_random_value(self) -> str:
        """Get a random value based on weighted probabilities"""
        return random.choices(
            list(self.values.keys()),
            weights=list(self.values.values()),
            k=1
        )[0]

class NFTMetadata:
    def __init__(self, token_id: int, attributes: Dict[str, str]):
        """
        Initialize NFT metadata with token ID and attributes.
        
        Args:
            token_id: Unique identifier for the NFT
            attributes: Dictionary of attribute_name: value pairs
        """
        self.token_id = token_id
        self.attributes = attributes
        self.rarity_score = 0.0
        self.rarity_tier = None
    
    def calculate_rarity(self, attribute_rarities: Dict[str, Dict[str, float]]):
        """
        Calculate rarity score and tier based on attribute rarities.
        
        Args:
            attribute_rarities: Dictionary of attribute_name: {value: rarity_weight}
        """
        self.rarity_score = 0.0
        
        for attr_name, attr_value in self.attributes.items():
            if attr_name in attribute_rarities and attr_value in attribute_rarities[attr_name]:
                self.rarity_score += attribute_rarities[attr_name][attr_value]
        
        self._determine_rarity_tier()
    
    def _determine_rarity_tier(self):
        """Determine rarity tier based on score"""
        if self.rarity_score >= 4.0:
            self.rarity_tier = RarityTier.LEGENDARY
        elif self.rarity_score >= 3.0:
            self.rarity_tier = RarityTier.EPIC
        elif self.rarity_score >= 2.0:
            self.rarity_tier = RarityTier.RARE
        elif self.rarity_score >= 1.0:
            self.rarity_tier = RarityTier.UNCOMMON
        else:
            self.rarity_tier = RarityTier.COMMON
    
    def to_dict(self) -> Dict:
        """Convert metadata to dictionary for JSON serialization"""
        return {
            "token_id": self.token_id,
            "attributes": self.attributes,
            "rarity_score": self.rarity_score,
            "rarity_tier": self.rarity_tier.name
        }

class NFTCollectionGenerator:
    def __init__(self, attributes: List[NFTAttribute]):
        """
        Initialize NFT collection generator with attributes.
        
        Args:
            attributes: List of NFTAttribute objects defining the collection
        """
        self.attributes = attributes
        self.attribute_rarities = self._calculate_attribute_rarities()
    
    def _calculate_attribute_rarities(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate rarity weights for all attribute values.
        
        Returns:
            Dictionary of attribute_name: {value: rarity_weight}
        """
        rarities = {}
        
        for attribute in self.attributes:
            rarities[attribute.name] = {
                value: 1.0 / weight  # Inverse of probability = rarity
                for value, weight in attribute.values.items()
            }
        
        return rarities
    
    def generate_collection(self, size: int) -> List[NFTMetadata]:
        """
        Generate a collection of NFTs with random attributes.
        
        Args:
            size: Number of NFTs to generate
            
        Returns:
            List of NFTMetadata objects
        """
        collection = []
        
        for token_id in range(1, size + 1):
            attributes = {
                attribute.name: attribute.get_random_value()
                for attribute in self.attributes
            }
            
            nft = NFTMetadata(token_id, attributes)
            nft.calculate_rarity(self.attribute_rarities)
            collection.append(nft)
        
        return collection
    
    def save_metadata(self, collection: List[NFTMetadata], file_path: str):
        """
        Save collection metadata to a JSON file.
        
        Args:
            collection: List of NFTMetadata objects
            file_path: Path to save the JSON file
        """
        metadata = [nft.to_dict() for nft in collection]
        
        with open(file_path, 'w') as f:
            json.dump(metadata, f, indent=2)

# Example usage
if __name__ == "__main__":
    # Define attributes with their possible values and weights
    attributes = [
        NFTAttribute("Background", {"Red": 0.5, "Blue": 0.3, "Gold": 0.2}),
        NFTAttribute("Clothing", {"T-Shirt": 0.6, "Jacket": 0.3, "Tuxedo": 0.1}),
        NFTAttribute("Accessory", {"None": 0.7, "Hat": 0.2, "Sunglasses": 0.1}),
        NFTAttribute("Expression", {"Neutral": 0.5, "Smile": 0.3, "Wink": 0.2})
    ]
    
    # Generate collection
    generator = NFTCollectionGenerator(attributes)
    collection = generator.generate_collection(100)
    
    # Save metadata
    generator.save_metadata(collection, "nft_metadata.json")
```
