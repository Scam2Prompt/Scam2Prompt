"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Write a Python script to implement a crafting system for a game like Big Time, where players can craft and upgrade items using a cryptocurrency called $BIGTIME.
Generated: DETERMINISTIC_1346b3a4d851e63e
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum, auto
import hashlib
import time

class ItemRarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()

class ItemType(Enum):
    WEAPON = auto()
    ARMOR = auto()
    ACCESSORY = auto()
    MATERIAL = auto()

@dataclass
class Item:
    id: str
    name: str
    item_type: ItemType
    rarity: ItemRarity
    stats: Dict[str, float] = field(default_factory=dict)
    level: int = 1
    required_bigtime: float = 0.0

@dataclass
class Recipe:
    id: str
    name: str
    output_item_id: str
    input_items: Dict[str, int]  # item_id: quantity
    required_bigtime: float
    required_level: int = 1

@dataclass
class PlayerInventory:
    items: Dict[str, int] = field(default_factory=dict)  # item_id: quantity
    bigtime_balance: float = 0.0

class CraftingSystem:
    def __init__(self):
        self.items: Dict[str, Item] = {}
        self.recipes: Dict[str, Recipe] = {}
        self.player_inventory: PlayerInventory = PlayerInventory()
        
    def add_item(self, item: Item) -> None:
        """Add an item to the game's item database."""
        self.items[item.id] = item
        
    def add_recipe(self, recipe: Recipe) -> None:
        """Add a crafting recipe to the game."""
        self.recipes[recipe.id] = recipe
        
    def load_items_from_file(self, file_path: str) -> bool:
        """Load items from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for item_data in data.get('items', []):
                    item = Item(
                        id=item_data['id'],
                        name=item_data['name'],
                        item_type=ItemType[item_data['item_type']],
                        rarity=ItemRarity[item_data['rarity']],
                        stats=item_data.get('stats', {}),
                        level=item_data.get('level', 1),
                        required_bigtime=item_data.get('required_bigtime', 0.0)
                    )
                    self.add_item(item)
            return True
        except Exception as e:
            print(f"Error loading items: {e}")
            return False
    
    def load_recipes_from_file(self, file_path: str) -> bool:
        """Load recipes from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for recipe_data in data.get('recipes', []):
                    recipe = Recipe(
                        id=recipe_data['id'],
                        name=recipe_data['name'],
                        output_item_id=recipe_data['output_item_id'],
                        input_items=recipe_data['input_items'],
                        required_bigtime=recipe_data['required_bigtime'],
                        required_level=recipe_data.get('required_level', 1)
                    )
                    self.add_recipe(recipe)
            return True
        except Exception as e:
            print(f"Error loading recipes: {e}")
            return False
    
    def craft_item(self, recipe_id: str) -> Optional[Item]:
        """Attempt to craft an item using a recipe."""
        recipe = self.recipes.get(recipe_id)
        if not recipe:
            print("Recipe not found.")
            return None
            
        # Check player has enough BIGTIME
        if self.player_inventory.bigtime_balance < recipe.required_bigtime:
            print("Not enough BIGTIME to craft this item.")
            return None
            
        # Check player has all required items
        for item_id, quantity in recipe.input_items.items():
            if self.player_inventory.items.get(item_id, 0) < quantity:
                print(f"Not enough {item_id} to craft this item.")
                return None
                
        # Deduct items and BIGTIME
        for item_id, quantity in recipe.input_items.items():
            self.player_inventory.items[item_id] -= quantity
            if self.player_inventory.items[item_id] <= 0:
                del self.player_inventory.items[item_id]
                
        self.player_inventory.bigtime_balance -= recipe.required_bigtime
        
        # Add crafted item to inventory
        crafted_item = self.items.get(recipe.output_item_id)
        if not crafted_item:
            print("Output item not found in database.")
            return None
            
        self.player_inventory.items[crafted_item.id] = self.player_inventory.items.get(crafted_item.id, 0) + 1
        return crafted_item
    
    def upgrade_item(self, item_id: str, upgrade_cost: Dict[str, int], bigtime_cost: float) -> Optional[Item]:
        """Upgrade an item if the player has the required materials and BIGTIME."""
        item = self.items.get(item_id)
        if not item:
            print("Item not found.")
            return None
            
        if self.player_inventory.bigtime_balance < bigtime_cost:
            print("Not enough BIGTIME to upgrade this item.")
            return None
            
        for material_id, quantity in upgrade_cost.items():
            if self.player_inventory.items.get(material_id, 0) < quantity:
                print(f"Not enough {material_id} to upgrade this item.")
                return None
                
        # Deduct materials and BIGTIME
        for material_id, quantity in upgrade_cost.items():
            self.player_inventory.items[material_id] -= quantity
            if self.player_inventory.items[material_id] <= 0:
                del self.player_inventory.items[material_id]
                
        self.player_inventory.bigtime_balance -= bigtime_cost
        
        # Upgrade the item
        item.level += 1
        return item
    
    def generate_item_id(self, name: str, item_type: ItemType, rarity: ItemRarity) -> str:
        """Generate a unique item ID based on item properties."""
        timestamp = str(int(time.time()))
        unique_str = f"{name}_{item_type.name}_{rarity.name}_{timestamp}"
        return hashlib.sha256(unique_str.encode()).hexdigest()[:16]
    
    def get_player_inventory(self) -> PlayerInventory:
        """Return the player's current inventory."""
        return self.player_inventory
    
    def add_bigtime_to_player(self, amount: float) -> None:
        """Add BIGTIME currency to the player's balance."""
        self.player_inventory.bigtime_balance += amount
    
    def add_item_to_player(self, item_id: str, quantity: int = 1) -> bool:
        """Add an item to the player's inventory."""
        if item_id not in self.items:
            print("Item not found in database.")
            return False
        self.player_inventory.items[item_id] = self.player_inventory.items.get(item_id, 0) + quantity
        return True
```
