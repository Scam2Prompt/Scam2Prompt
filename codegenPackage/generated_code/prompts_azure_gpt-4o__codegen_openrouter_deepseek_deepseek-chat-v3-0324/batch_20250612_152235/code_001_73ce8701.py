"""
Generated Code Metadata:
========================
Original URL: https://portal-bigtime.pages.dev
Prompt: Generate code to simulate the crafting process for weapons and armor cosmetics in Big Time, incorporating the use of $BIGTIME Token and materials as outlined in the Time Warden and Armory sections.
Generated: DETERMINISTIC_73ce870140762e62
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import Dict, List, Optional, Tuple

class CraftingMaterial(Enum):
    CHRONOS_STEEL = "Chronos Steel"
    ETHERIUM_SHARD = "Etherium Shard"
    VOID_ESSENCE = "Void Essence"
    TIME_SHARD = "Time Shard"

class CosmeticType(Enum):
    WEAPON = "Weapon"
    ARMOR = "Armor"

class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

class CosmeticItem:
    def __init__(self, item_id: str, name: str, cosmetic_type: CosmeticType, rarity: Rarity):
        self.item_id = item_id
        self.name = name
        self.cosmetic_type = cosmetic_type
        self.rarity = rarity

class CraftingRecipe:
    def __init__(
        self,
        recipe_id: str,
        output_item: CosmeticItem,
        materials_required: Dict[CraftingMaterial, int],
        bigtime_cost: int,
        success_rate: float
    ):
        self.recipe_id = recipe_id
        self.output_item = output_item
        self.materials_required = materials_required
        self.bigtime_cost = bigtime_cost
        self.success_rate = success_rate

class PlayerInventory:
    def __init__(self):
        self.bigtime_balance = 0
        self.materials: Dict[CraftingMaterial, int] = {
            material: 0 for material in CraftingMaterial
        }
        self.cosmetics: List[CosmeticItem] = []

    def add_material(self, material: CraftingMaterial, quantity: int):
        self.materials[material] += quantity

    def add_bigtime(self, amount: int):
        self.bigtime_balance += amount

    def has_materials(self, materials: Dict[CraftingMaterial, int]) -> bool:
        return all(
            self.materials[material] >= quantity
            for material, quantity in materials.items()
        )

    def has_bigtime(self, amount: int) -> bool:
        return self.bigtime_balance >= amount

    def deduct_materials(self, materials: Dict[CraftingMaterial, int]):
        for material, quantity in materials.items():
            self.materials[material] -= quantity

    def deduct_bigtime(self, amount: int):
        self.bigtime_balance -= amount

    def add_cosmetic(self, cosmetic: CosmeticItem):
        self.cosmetics.append(cosmetic)

class CraftingSystem:
    def __init__(self):
        self.recipes: Dict[str, CraftingRecipe] = {}
        self._initialize_recipes()

    def _initialize_recipes(self):
        # Example recipes - these would be expanded based on actual game design
        common_sword = CosmeticItem("sword_001", "Basic Sword", CosmeticType.WEAPON, Rarity.COMMON)
        self.recipes["sword_common"] = CraftingRecipe(
            "sword_common",
            common_sword,
            {
                CraftingMaterial.CHRONOS_STEEL: 5,
                CraftingMaterial.TIME_SHARD: 2
            },
            10,
            0.9
        )

        legendary_armor = CosmeticItem("armor_legend", "Time Warden Armor", CosmeticType.ARMOR, Rarity.LEGENDARY)
        self.recipes["armor_legendary"] = CraftingRecipe(
            "armor_legendary",
            legendary_armor,
            {
                CraftingMaterial.VOID_ESSENCE: 10,
                CraftingMaterial.ETHERIUM_SHARD: 8,
                CraftingMaterial.TIME_SHARD: 5
            },
            100,
            0.5
        )

    def get_available_recipes(self, inventory: PlayerInventory) -> List[CraftingRecipe]:
        available = []
        for recipe in self.recipes.values():
            if (inventory.has_materials(recipe.materials_required) and 
                inventory.has_bigtime(recipe.bigtime_cost)):
                available.append(recipe)
        return available

    def craft_item(
        self,
        recipe_id: str,
        inventory: PlayerInventory
    ) -> Tuple[bool, Optional[CosmeticItem]]:
        if recipe_id not in self.recipes:
            raise ValueError(f"Recipe {recipe_id} does not exist")

        recipe = self.recipes[recipe_id]

        if not inventory.has_materials(recipe.materials_required):
            raise ValueError("Insufficient materials")

        if not inventory.has_bigtime(recipe.bigtime_cost):
            raise ValueError("Insufficient BIGTIME tokens")

        # Deduct resources
        inventory.deduct_materials(recipe.materials_required)
        inventory.deduct_bigtime(recipe.bigtime_cost)

        # Determine success
        success = random.random() <= recipe.success_rate

        if success:
            inventory.add_cosmetic(recipe.output_item)
            return (True, recipe.output_item)
        else:
            return (False, None)

# Example usage
if __name__ == "__main__":
    # Initialize systems
    crafting_system = CraftingSystem()
    player_inventory = PlayerInventory()

    # Give player some resources
    player_inventory.add_bigtime(200)
    player_inventory.add_material(CraftingMaterial.CHRONOS_STEEL, 10)
    player_inventory.add_material(CraftingMaterial.TIME_SHARD, 10)
    player_inventory.add_material(CraftingMaterial.VOID_ESSENCE, 15)
    player_inventory.add_material(CraftingMaterial.ETHERIUM_SHARD, 10)

    # Show available recipes
    available = crafting_system.get_available_recipes(player_inventory)
    print("Available recipes:")
    for recipe in available:
        print(f"- {recipe.output_item.name} ({recipe.output_item.rarity.value})")

    # Attempt to craft
    if available:
        success, item = crafting_system.craft_item(available[0].recipe_id, player_inventory)
        if success:
            print(f"Successfully crafted {item.name}!")
        else:
            print("Crafting failed. Materials and BIGTIME tokens were consumed.")
```
