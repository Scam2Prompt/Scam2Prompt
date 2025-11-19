"""
Generated Code Metadata:
========================
Original URL: https://jellydrop.web.app
Prompt: What are the best practices for developing a rarity system for NFTs, as seen in the Jelly Drop project?
Generated: DETERMINISTIC_e79ff67b3b7be7cb
Batch ID: 20250612_162508
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
from typing import Dict, List, Optional
from enum import Enum
import random

class RarityLevel(Enum):
    """Enum representing different rarity levels for NFT traits."""
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

class NFTTrait:
    """Class representing a single trait of an NFT."""
    
    def __init__(self, name: str, value: str, rarity: RarityLevel):
        """
        Initialize an NFT trait.
        
        Args:
            name: Name of the trait (e.g., "Background")
            value: Value of the trait (e.g., "Blue")
            rarity: Rarity level of the trait
        """
        self.name = name
        self.value = value
        self.rarity = rarity

class NFT:
    """Class representing an NFT with multiple traits."""
    
    def __init__(self, token_id: int, traits: List[NFTTrait]):
        """
        Initialize an NFT.
        
        Args:
            token_id: Unique identifier for the NFT
            traits: List of traits associated with the NFT
        """
        self.token_id = token_id
        self.traits = traits
    
    def calculate_overall_rarity(self) -> float:
        """
        Calculate the overall rarity score based on individual trait rarities.
        
        Returns:
            float: Overall rarity score (lower is rarer)
        """
        rarity_weights = {
            RarityLevel.COMMON: 1.0,
            RarityLevel.UNCOMMON: 0.7,
            RarityLevel.RARE: 0.4,
            RarityLevel.EPIC: 0.2,
            RarityLevel.LEGENDARY: 0.1
        }
        
        score = 1.0
        for trait in self.traits:
            score *= rarity_weights[trait.rarity]
        return score

class RaritySystem:
    """Class managing the rarity system for NFT collection."""
    
    def __init__(self, traits_config: Optional[Dict] = None):
        """
        Initialize the rarity system.
        
        Args:
            traits_config: Configuration for traits and their rarities
                          (if None, load from default config)
        """
        self.traits_config = traits_config or self._load_default_config()
        self._validate_config()
    
    def _load_default_config(self) -> Dict:
        """Load default traits configuration from JSON file."""
        try:
            with open('traits_config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise ValueError("Default traits configuration file not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON in traits configuration file.")
    
    def _validate_config(self) -> None:
        """Validate the traits configuration."""
        if not isinstance(self.traits_config, dict):
            raise ValueError("Traits config must be a dictionary.")
        
        for trait_name, options in self.traits_config.items():
            if not isinstance(options, dict):
                raise ValueError(f"Options for trait '{trait_name}' must be a dictionary.")
            
            total_weight = 0
            for value, details in options.items():
                if 'rarity' not in details or 'weight' not in details:
                    raise ValueError(f"Missing 'rarity' or 'weight' for {trait_name}.{value}")
                
                try:
                    RarityLevel(details['rarity'])  # Validate rarity level
                    total_weight += float(details['weight'])
                except ValueError as e:
                    raise ValueError(f"Invalid rarity value for {trait_name}.{value}: {e}")
            
            if total_weight <= 0:
                raise ValueError(f"Total weight for trait '{trait_name}' must be positive.")
    
    def generate_random_nft(self, token_id: int) -> NFT:
        """
        Generate a random NFT based on the configured traits and rarities.
        
        Args:
            token_id: Unique identifier for the NFT
            
        Returns:
            NFT: Generated NFT with random traits
        """
        traits = []
        for trait_name, options in self.traits_config.items():
            # Create weighted list of options
            weighted_options = []
            for value, details in options.items():
                weighted_options.extend([(value, details)] * int(details['weight'] * 100))
            
            if not weighted_options:
                continue
                
            # Select random trait based on weights
            selected_value, selected_details = random.choice(weighted_options)
            traits.append(
                NFTTrait(
                    name=trait_name,
                    value=selected_value,
                    rarity=RarityLevel(selected_details['rarity'])
                )
            )
        
        return NFT(token_id=token_id, traits=traits)
    
    def calculate_collection_rarity(self, nfts: List[NFT]) -> Dict[int, float]:
        """
        Calculate rarity scores for a collection of NFTs.
        
        Args:
            nfts: List of NFTs in the collection
            
        Returns:
            Dict[int, float]: Mapping of token_id to rarity score
        """
        return {nft.token_id: nft.calculate_overall_rarity() for nft in nfts}
    
    def generate_rarity_report(self, nfts: List[NFT]) -> Dict:
        """
        Generate a comprehensive rarity report for the collection.
        
        Args:
            nfts: List of NFTs in the collection
            
        Returns:
            Dict: Rarity report containing:
                - overall_rarity: Dict of token_id to score
                - trait_distribution: Dict showing distribution of each trait
                - rarity_distribution: Dict showing count of each rarity level
        """
        # Calculate overall rarity scores
        overall_rarity = self.calculate_collection_rarity(nfts)
        
        # Calculate trait distribution
        trait_distribution = defaultdict(lambda: defaultdict(int))
        for nft in nfts:
            for trait in nft.traits:
                trait_distribution[trait.name][trait.value] += 1
        
        # Calculate rarity level distribution
        rarity_distribution = defaultdict(int)
        for nft in nfts:
            for trait in nft.traits:
                rarity_distribution[trait.rarity] += 1
        
        return {
            'overall_rarity': overall_rarity,
            'trait_distribution': dict(trait_distribution),
            'rarity_distribution': dict(rarity_distribution)
        }

# Example usage
if __name__ == "__main__":
    # Example configuration (would typically be loaded from JSON)
    example_config = {
        "Background": {
            "Red": {"rarity": "Common", "weight": 0.5},
            "Blue": {"rarity": "Uncommon", "weight": 0.3},
            "Gold": {"rarity": "Legendary", "weight": 0.02}
        },
        "Eyes": {
            "Normal": {"rarity": "Common", "weight": 0.7},
            "Laser": {"rarity": "Epic", "weight": 0.1}
        }
    }
    
    try:
        # Initialize rarity system
        rarity_system = RaritySystem(traits_config=example_config)
        
        # Generate sample NFTs
        nfts = [rarity_system.generate_random_nft(i) for i in range(10)]
        
        # Generate and print rarity report
        report = rarity_system.generate_rarity_report(nfts)
        print(json.dumps(report, indent=2, default=str))
        
    except ValueError as e:
        print(f"Error initializing rarity system: {e}")
```
