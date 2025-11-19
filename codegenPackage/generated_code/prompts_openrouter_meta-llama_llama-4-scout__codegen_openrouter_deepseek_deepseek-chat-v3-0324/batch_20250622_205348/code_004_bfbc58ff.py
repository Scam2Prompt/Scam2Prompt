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
import random
from typing import List, Dict, Optional
from enum import Enum, auto

class RarityTier(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()
    MYTHIC = auto()  # For 1/1 traits

class Trait:
    def __init__(self, name: str, rarity: RarityTier):
        self.name = name
        self.rarity = rarity

class Ember:
    def __init__(self, traits: List[Trait]):
        self.traits = traits
        self.rarity_score = self._calculate_rarity_score()
        self.tier = self._determine_tier()

    def _calculate_rarity_score(self) -> float:
        """Calculate rarity score based on trait rarities."""
        score = 0.0
        for trait in self.traits:
            if trait.rarity == RarityTier.COMMON:
                score += 1
            elif trait.rarity == RarityTier.UNCOMMON:
                score += 2
            elif trait.rarity == RarityTier.RARE:
                score += 3
            elif trait.rarity == RarityTier.EPIC:
                score += 5
            elif trait.rarity == RarityTier.LEGENDARY:
                score += 8
            elif trait.rarity == RarityTier.MYTHIC:
                score += 20  # Significant boost for 1/1 traits
        return score

    def _determine_tier(self) -> RarityTier:
        """Determine overall tier based on rarity score."""
        if any(trait.rarity == RarityTier.MYTHIC for trait in self.traits):
            return RarityTier.MYTHIC
        
        if self.rarity_score >= 15:
            return RarityTier.LEGENDARY
        elif self.rarity_score >= 10:
            return RarityTier.EPIC
        elif self.rarity_score >= 6:
            return RarityTier.RARE
        elif self.rarity_score >= 3:
            return RarityTier.UNCOMMON
        else:
            return RarityTier.COMMON

class EmberGenerator:
    def __init__(self, traits_db: List[Trait]):
        self.traits_db = traits_db
        self._validate_traits_db()

    def _validate_traits_db(self):
        """Validate traits database contains required fields."""
        if not self.traits_db:
            raise ValueError("Traits database cannot be empty")
        for trait in self.traits_db:
            if not isinstance(trait, Trait):
                raise ValueError("All traits must be instances of Trait class")

    def generate_ember(self, num_traits: int = 5) -> Ember:
        """Generate a random Ember with specified number of traits."""
        if num_traits <= 0:
            raise ValueError("Number of traits must be positive")
        
        selected_traits = random.sample(self.traits_db, min(num_traits, len(self.traits_db)))
        return Ember(selected_traits)

    def generate_with_1of1(self, num_traits: int = 5) -> Optional[Ember]:
        """Generate an Ember with a 1/1 trait if available."""
        mythic_traits = [trait for trait in self.traits_db if trait.rarity == RarityTier.MYTHIC]
        if not mythic_traits:
            return None
        
        mythic_trait = random.choice(mythic_traits)
        other_traits = [trait for trait in self.traits_db if trait != mythic_trait]
        
        if num_traits <= 1:
            selected_traits = [mythic_trait]
        else:
            selected_other_traits = random.sample(other_traits, num_traits - 1)
            selected_traits = [mythic_trait] + selected_other_traits
        
        return Ember(selected_traits)

def load_traits_from_config(config: List[Dict]) -> List[Trait]:
    """Load traits from configuration data."""
    traits = []
    for trait_data in config:
        try:
            trait = Trait(
                name=trait_data['name'],
                rarity=RarityTier[trait_data['rarity'].upper()]
            )
            traits.append(trait)
        except KeyError as e:
            raise ValueError(f"Invalid trait configuration: {str(e)}")
    return traits

# Example usage
if __name__ == "__main__":
    # Example configuration for traits
    example_config = [
        {"name": "Fire Aura", "rarity": "COMMON"},
        {"name": "Ice Core", "rarity": "UNCOMMON"},
        {"name": "Electric Pulse", "rarity": "RARE"},
        {"name": "Golden Flame", "rarity": "EPIC"},
        {"name": "Dragon Heart", "rarity": "LEGENDARY"},
        {"name": "Phoenix Feather", "rarity": "MYTHIC"},
        # ... 150 total traits
    ]
    
    try:
        traits_db = load_traits_from_config(example_config)
        generator = EmberGenerator(traits_db)
        
        # Generate a random Ember
        ember = generator.generate_ember()
        print(f"Generated Ember with tier: {ember.tier.name}")
        
        # Try to generate an Ember with 1/1 trait
        special_ember = generator.generate_with_1of1()
        if special_ember:
            print(f"Generated 1/1 Ember with tier: {special_ember.tier.name}")
        else:
            print("No 1/1 traits available in the database")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
