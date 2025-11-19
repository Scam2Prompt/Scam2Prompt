"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Generate code to implement a crafting system, like the one in Big Time, where players can craft and upgrade items using materials and $BIGTIME tokens.
Generated: DETERMINISTIC_2290cd76ae5b7e7d
Batch ID: 20250622_211405
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
from enum import Enum

class CraftingError(Exception):
    """Base exception for crafting system errors."""
    pass

class InsufficientMaterialsError(CraftingError):
    """Raised when player doesn't have enough materials."""
    pass

class InsufficientTokensError(CraftingError):
    """Raised when player doesn't have enough tokens."""
    pass

class ItemRarity(Enum):
    """Enum representing item rarity levels."""
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

class ItemType(Enum):
    """Enum representing item types."""
    WEAPON = 1
    ARMOR = 2
    ACCESSORY = 3
    CONSUMABLE = 4

class Material:
    """Class representing a crafting material."""
    def __init__(self, material_id: str, name: str, description: str):
        self.material_id = material_id
        self.name = name
        self.description = description

class Item:
    """Class representing an in-game item."""
    def __init__(
        self,
        item_id: str,
        name: str,
        item_type: ItemType,
        rarity: ItemRarity,
        stats: Dict[str, float],
        level: int = 1
    ):
        self.item_id = item_id
        self.name = name
        self.item_type = item_type
        self.rarity = rarity
        self.stats = stats
        self.level = level

    def upgrade(self):
        """Upgrade the item's level and stats."""
        self.level += 1
        for stat in self.stats:
            self.stats[stat] *= 1.2  # 20% increase per level

class Recipe:
    """Class representing a crafting recipe."""
    def __init__(
        self,
        recipe_id: str,
        output_item: Item,
        materials_required: Dict[str, int],  # material_id: quantity
        token_cost: float,
        upgrade: bool = False
    ):
        self.recipe_id = recipe_id
        self.output_item = output_item
        self.materials_required = materials_required
        self.token_cost = token_cost
        self.is_upgrade = upgrade

class PlayerInventory:
    """Class representing a player's inventory."""
    def __init__(self):
        self.items: List[Item] = []
        self.materials: Dict[str, int] = {}  # material_id: quantity
        self.tokens: float = 0.0

    def add_item(self, item: Item):
        """Add an item to the inventory."""
        self.items.append(item)

    def remove_item(self, item_id: str) -> bool:
        """Remove an item from the inventory."""
        for i, item in enumerate(self.items):
            if item.item_id == item_id:
                self.items.pop(i)
                return True
        return False

    def add_material(self, material_id: str, quantity: int):
        """Add materials to the inventory."""
        if material_id in self.materials:
            self.materials[material_id] += quantity
        else:
            self.materials[material_id] = quantity

    def remove_material(self, material_id: str, quantity: int) -> bool:
        """Remove materials from the inventory if available."""
        if material_id not in self.materials or self.materials[material_id] < quantity:
            return False
        self.materials[material_id] -= quantity
        return True

    def add_tokens(self, amount: float):
        """Add tokens to the inventory."""
        self.tokens += amount

    def spend_tokens(self, amount: float) -> bool:
        """Spend tokens if available."""
        if self.tokens < amount:
            return False
        self.tokens -= amount
        return True

class CraftingSystem:
    """Main crafting system class."""
    def __init__(self):
        self.recipes: Dict[str, Recipe] = {}
        self.materials: Dict[str, Material] = {}

    def register_material(self, material: Material):
        """Register a new material in the system."""
        self.materials[material.material_id] = material

    def register_recipe(self, recipe: Recipe):
        """Register a new recipe in the system."""
        self.recipes[recipe.recipe_id] = recipe

    def craft_item(
        self,
        player_inventory: PlayerInventory,
        recipe_id: str,
        target_item_id: Optional[str] = None
    ) -> Item:
        """
        Craft or upgrade an item using a recipe.
        
        Args:
            player_inventory: The player's inventory
            recipe_id: ID of the recipe to use
            target_item_id: For upgrades, the ID of item to upgrade (None for new crafts)
        
        Returns:
            The crafted/upgraded item
        
        Raises:
            CraftingError: If crafting fails
        """
        if recipe_id not in self.recipes:
            raise CraftingError(f"Recipe {recipe_id} not found")

        recipe = self.recipes[recipe_id]

        # Check if this is an upgrade and validate target item
        if recipe.is_upgrade:
            if not target_item_id:
                raise CraftingError("Upgrade requires target item ID")
            
            target_item = next(
                (item for item in player_inventory.items if item.item_id == target_item_id),
                None
            )
            if not target_item:
                raise CraftingError(f"Item {target_item_id} not found in inventory")

        # Check material requirements
        for material_id, quantity in recipe.materials_required.items():
            if material_id not in player_inventory.materials:
                raise InsufficientMaterialsError(f"Missing material {material_id}")
            if player_inventory.materials[material_id] < quantity:
                raise InsufficientMaterialsError(
                    f"Insufficient quantity of material {material_id}"
                )

        # Check token requirements
        if not player_inventory.spend_tokens(recipe.token_cost):
            raise InsufficientTokensError("Insufficient tokens")

        # Deduct materials
        for material_id, quantity in recipe.materials_required.items():
            player_inventory.remove_material(material_id, quantity)

        # Handle crafting vs upgrading
        if recipe.is_upgrade:
            target_item.upgrade()
            return target_item
        else:
            player_inventory.add_item(recipe.output_item)
            return recipe.output_item

    def load_from_json(self, materials_file: str, recipes_file: str):
        """
        Load materials and recipes from JSON files.
        
        Args:
            materials_file: Path to materials JSON file
            recipes_file: Path to recipes JSON file
        """
        # Load materials
        with open(materials_file, 'r') as f:
            materials_data = json.load(f)
            for mat_data in materials_data:
                material = Material(
                    material_id=mat_data['id'],
                    name=mat_data['name'],
                    description=mat_data['description']
                )
                self.register_material(material)

        # Load recipes
        with open(recipes_file, 'r') as f:
            recipes_data = json.load(f)
            for rec_data in recipes_data:
                item_type = ItemType[rec_data['output_item']['type'].upper()]
                rarity = ItemRarity[rec_data['output_item']['rarity'].upper()]
                
                output_item = Item(
                    item_id=rec_data['output_item']['id'],
                    name=rec_data['output_item']['name'],
                    item_type=item_type,
                    rarity=rarity,
                    stats=rec_data['output_item']['stats']
                )
                
                recipe = Recipe(
                    recipe_id=rec_data['id'],
                    output_item=output_item,
                    materials_required=rec_data['materials_required'],
                    token_cost=rec_data['token_cost'],
                    upgrade=rec_data.get('upgrade', False)
                )
                self.register_recipe(recipe)
```
