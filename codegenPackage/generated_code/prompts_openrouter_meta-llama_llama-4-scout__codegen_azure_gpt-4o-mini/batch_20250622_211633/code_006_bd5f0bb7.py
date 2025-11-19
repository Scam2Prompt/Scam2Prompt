"""
Generated Code Metadata:
========================
Original URL: https://jellyesports.web.app
Prompt: "Explain the rarity system in Jelly Esports and provide a code example for implementing a rarity-based staking strategy."
Generated: DETERMINISTIC_bd5f0bb707190116
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class Rarity:
    """Class to represent the rarity of an item."""
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

class Item:
    """Class to represent an item with a rarity."""
    def __init__(self, name: str, rarity: Rarity):
        self.name = name
        self.rarity = rarity

class RaritySystem:
    """Class to manage the rarity system and staking strategy."""
    
    def __init__(self):
        self.rarities: List[Rarity] = []
        self.items: List[Item] = []
    
    def add_rarity(self, name: str, weight: int):
        """Add a new rarity to the system."""
        if weight <= 0:
            raise ValueError("Weight must be a positive integer.")
        self.rarities.append(Rarity(name, weight))
    
    def add_item(self, name: str, rarity_name: str):
        """Add a new item with a specified rarity."""
        rarity = self.get_rarity_by_name(rarity_name)
        if rarity is None:
            raise ValueError(f"Rarity '{rarity_name}' does not exist.")
        self.items.append(Item(name, rarity))
    
    def get_rarity_by_name(self, name: str) -> Rarity:
        """Retrieve a rarity by its name."""
        for rarity in self.rarities:
            if rarity.name == name:
                return rarity
        return None
    
    def stake_item(self, item_name: str) -> str:
        """Stake an item based on its rarity."""
        item = self.get_item_by_name(item_name)
        if item is None:
            raise ValueError(f"Item '{item_name}' does not exist.")
        
        # Simulate staking based on rarity
        stake_success = random.choices(
            [True, False],
            weights=[item.rarity.weight, 100 - item.rarity.weight],
            k=1
        )[0]
        
        return f"Staking {'succeeded' if stake_success else 'failed'} for item '{item.name}' with rarity '{item.rarity.name}'."
    
    def get_item_by_name(self, name: str) -> Item:
        """Retrieve an item by its name."""
        for item in self.items:
            if item.name == name:
                return item
        return None

# Example usage
if __name__ == "__main__":
    rarity_system = RaritySystem()
    
    # Adding rarities
    rarity_system.add_rarity("Common", 70)
    rarity_system.add_rarity("Rare", 20)
    rarity_system.add_rarity("Epic", 9)
    rarity_system.add_rarity("Legendary", 1)
    
    # Adding items
    rarity_system.add_item("Sword of Valor", "Epic")
    rarity_system.add_item("Shield of Courage", "Rare")
    
    # Staking items
    try:
        print(rarity_system.stake_item("Sword of Valor"))
        print(rarity_system.stake_item("Shield of Courage"))
    except ValueError as e:
        print(f"Error: {e}")
```
