"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Describe the process of crafting visually distinct armor pieces using the Armory in Big Time.
Generated: DETERMINISTIC_8cc80607ff0440c1
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# armor_crafting.py

import random
from enum import Enum
from typing import List, Dict, Optional

class ArmorType(Enum):
    """Enum representing different types of armor pieces."""
    HELMET = "Helmet"
    CHEST = "Chest"
    GAUNTLETS = "Gauntlets"
    GREAVES = "Greaves"
    BOOTS = "Boots"

class Material(Enum):
    """Enum representing different crafting materials."""
    IRON = "Iron"
    STEEL = "Steel"
    OBSIDIAN = "Obsidian"
    CRYSTAL = "Crystal"
    VOIDSTONE = "Voidstone"

class Rarity(Enum):
    """Enum representing different rarity levels."""
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

class ArmorPiece:
    """Class representing a crafted armor piece."""
    
    def __init__(self, armor_type: ArmorType, material: Material, rarity: Rarity, visual_traits: Dict[str, str]):
        """
        Initialize an armor piece.
        
        Args:
            armor_type: Type of armor (Helmet, Chest, etc.)
            material: Material used for crafting
            rarity: Rarity level of the armor
            visual_traits: Dictionary of visual traits (colors, patterns, etc.)
        """
        self.armor_type = armor_type
        self.material = material
        self.rarity = rarity
        self.visual_traits = visual_traits
    
    def __str__(self) -> str:
        """Return a string representation of the armor piece."""
        return (f"{self.rarity.value} {self.material.value} {self.armor_type.value}\n"
                f"Visual Traits: {', '.join(f'{k}: {v}' for k, v in self.visual_traits.items())}")

class Armory:
    """Class representing the Armory crafting system in Big Time."""
    
    def __init__(self):
        """Initialize the Armory with available materials and visual traits."""
        self.available_materials = list(Material)
        self.visual_traits_db = {
            "color": ["Red", "Blue", "Green", "Gold", "Silver", "Black", "White"],
            "pattern": ["Striped", "Dotted", "Swirl", "Geometric", "None"],
            "glow": ["None", "Faint", "Moderate", "Intense"],
            "engraving": ["None", "Simple", "Complex", "Mythical"]
        }
    
    def _generate_visual_traits(self, rarity: Rarity) -> Dict[str, str]:
        """
        Generate random visual traits based on rarity.
        
        Args:
            rarity: Rarity level that influences trait generation
            
        Returns:
            Dictionary of visual traits
        """
        traits = {}
        
        # Higher rarity means more/better traits
        trait_count = {
            Rarity.COMMON: 1,
            Rarity.UNCOMMON: 2,
            Rarity.RARE: 3,
            Rarity.EPIC: 4,
            Rarity.LEGENDARY: 5
        }.get(rarity, 1)
        
        # Select random traits
        available_trait_types = list(self.visual_traits_db.keys())
        selected_trait_types = random.sample(available_trait_types, min(trait_count, len(available_trait_types)))
        
        for trait_type in selected_trait_types:
            possible_values = self.visual_traits_db[trait_type]
            
            # Higher rarity gets better options (later in the list)
            if rarity == Rarity.LEGENDARY:
                possible_values = possible_values[-3:]
            elif rarity == Rarity.EPIC:
                possible_values = possible_values[-2:]
            
            traits[trait_type] = random.choice(possible_values)
        
        return traits
    
    def _determine_rarity(self, material: Material) -> Rarity:
        """
        Determine the rarity based on material used.
        
        Args:
            material: Material used for crafting
            
        Returns:
            Rarity level
        """
        rarity_chances = {
            Material.IRON: [0.6, 0.3, 0.1, 0.0, 0.0],
            Material.STEEL: [0.4, 0.4, 0.2, 0.0, 0.0],
            Material.OBSIDIAN: [0.2, 0.3, 0.3, 0.2, 0.0],
            Material.CRYSTAL: [0.1, 0.2, 0.3, 0.3, 0.1],
            Material.VOIDSTONE: [0.0, 0.1, 0.2, 0.3, 0.4]
        }
        
        chances = rarity_chances.get(material, rarity_chances[Material.IRON])
        return random.choices(list(Rarity), weights=chances, k=1)[0]
    
    def craft_armor(self, armor_type: ArmorType, material: Material) -> Optional[ArmorPiece]:
        """
        Craft an armor piece with the given type and material.
        
        Args:
            armor_type: Type of armor to craft
            material: Material to use for crafting
            
        Returns:
            Crafted ArmorPiece or None if crafting failed
        """
        if armor_type not in ArmorType or material not in Material:
            return None
            
        try:
            rarity = self._determine_rarity(material)
            visual_traits = self._generate_visual_traits(rarity)
            
            return ArmorPiece(armor_type, material, rarity, visual_traits)
        except Exception as e:
            print(f"Error during crafting: {e}")
            return None
    
    def craft_random_armor(self) -> ArmorPiece:
        """
        Craft a random armor piece with random type and material.
        
        Returns:
            Crafted ArmorPiece
        """
        armor_type = random.choice(list(ArmorType))
        material = random.choice(self.available_materials)
        return self.craft_armor(armor_type, material)

# Example usage
if __name__ == "__main__":
    armory = Armory()
    
    # Craft a specific armor piece
    helmet = armory.craft_armor(ArmorType.HELMET, Material.CRYSTAL)
    if helmet:
        print("--- Crafted Helmet ---")
        print(helmet)
    
    # Craft a random armor piece
    random_armor = armory.craft_random_armor()
    if random_armor:
        print("\n--- Random Crafted Armor ---")
        print(random_armor)
```
