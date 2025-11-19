"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Generate code to simulate crafting weapons and armor cosmetics in Big Time using $BIGTIME tokens and materials, including functionality for upgrading items through the Forge and Armory.
Generated: DETERMINISTIC_73b665545a32727c
Batch ID: 20250612_150316
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

class Rarity(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

class ItemType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    COSMETIC = "cosmetic"

class MaterialType(Enum):
    METAL = "metal"
    GEM = "gem"
    CLOTH = "cloth"
    LEATHER = "leather"
    ESSENCE = "essence"

class Item:
    def __init__(
        self,
        item_id: str,
        name: str,
        item_type: ItemType,
        rarity: Rarity,
        stats: Dict[str, float],
        materials_cost: Dict[MaterialType, int],
        bigtime_cost: int,
        level: int = 1
    ):
        self.item_id = item_id
        self.name = name
        self.item_type = item_type
        self.rarity = rarity
        self.stats = stats
        self.materials_cost = materials_cost
        self.bigtime_cost = bigtime_cost
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.rarity.name}) - Lvl {self.level}"

class PlayerInventory:
    def __init__(self):
        self.bigtime_balance = 0
        self.materials = {material: 0 for material in MaterialType}
        self.items: List[Item] = []

    def add_bigtime(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Cannot add negative BIGTIME")
        self.bigtime_balance += amount

    def add_material(self, material: MaterialType, amount: int) -> None:
        if amount < 0:
            raise ValueError("Cannot add negative materials")
        self.materials[material] += amount

    def has_resources(self, item: Item) -> bool:
        if self.bigtime_balance < item.bigtime_cost:
            return False
        
        for material, cost in item.materials_cost.items():
            if self.materials[material] < cost:
                return False
        
        return True

    def spend_resources(self, item: Item) -> None:
        if not self.has_resources(item):
            raise ValueError("Insufficient resources")
        
        self.bigtime_balance -= item.bigtime_cost
        for material, cost in item.materials_cost.items():
            self.materials[material] -= cost

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item: Item) -> None:
        if item not in self.items:
            raise ValueError("Item not in inventory")
        self.items.remove(item)

class CraftingSystem:
    def __init__(self):
        self.weapon_templates = self._load_weapon_templates()
        self.armor_templates = self._load_armor_templates()
        self.cosmetic_templates = self._load_cosmetic_templates()

    def _load_weapon_templates(self) -> List[Dict]:
        return [
            {
                "name": "Iron Sword",
                "rarity": Rarity.COMMON,
                "stats": {"damage": 10, "speed": 1.0},
                "materials": {MaterialType.METAL: 5, MaterialType.LEATHER: 2},
                "bigtime_cost": 50
            },
            {
                "name": "Dragon Blade",
                "rarity": Rarity.LEGENDARY,
                "stats": {"damage": 50, "speed": 1.5},
                "materials": {MaterialType.METAL: 20, MaterialType.GEM: 10, MaterialType.ESSENCE: 5},
                "bigtime_cost": 500
            }
        ]

    def _load_armor_templates(self) -> List[Dict]:
        return [
            {
                "name": "Leather Armor",
                "rarity": Rarity.COMMON,
                "stats": {"defense": 5, "health": 20},
                "materials": {MaterialType.LEATHER: 10, MaterialType.CLOTH: 5},
                "bigtime_cost": 40
            },
            {
                "name": "Dragon Plate",
                "rarity": Rarity.LEGENDARY,
                "stats": {"defense": 30, "health": 100},
                "materials": {MaterialType.METAL: 30, MaterialType.GEM: 15, MaterialType.ESSENCE: 10},
                "bigtime_cost": 600
            }
        ]

    def _load_cosmetic_templates(self) -> List[Dict]:
        return [
            {
                "name": "Hero's Cape",
                "rarity": Rarity.RARE,
                "stats": {"style": 15},
                "materials": {MaterialType.CLOTH: 8, MaterialType.GEM: 3},
                "bigtime_cost": 200
            }
        ]

    def _generate_item_id(self) -> str:
        return f"item_{random.randint(1000, 9999)}"

    def craft_item(
        self,
        item_type: ItemType,
        rarity: Optional[Rarity] = None,
        inventory: Optional[PlayerInventory] = None
    ) -> Item:
        templates = []
        if item_type == ItemType.WEAPON:
            templates = self.weapon_templates
        elif item_type == ItemType.ARMOR:
            templates = self.armor_templates
        elif item_type == ItemType.COSMETIC:
            templates = self.cosmetic_templates
        else:
            raise ValueError("Invalid item type")

        if rarity:
            templates = [t for t in templates if t["rarity"] == rarity]
            if not templates:
                raise ValueError(f"No templates available for {rarity.name} {item_type.value}")

        template = random.choice(templates)
        
        item = Item(
            item_id=self._generate_item_id(),
            name=template["name"],
            item_type=item_type,
            rarity=template["rarity"],
            stats=template["stats"],
            materials_cost=template["materials"],
            bigtime_cost=template["bigtime_cost"]
        )

        if inventory:
            if not inventory.has_resources(item):
                raise ValueError("Insufficient resources to craft item")
            inventory.spend_resources(item)
            inventory.add_item(item)

        return item

class UpgradeSystem:
    def __init__(self):
        self.upgrade_cost_multiplier = 1.5
        self.stat_increase_per_level = 0.2

    def calculate_upgrade_cost(self, item: Item) -> Tuple[Dict[MaterialType, int], int]:
        materials_cost = {
            material: int(cost * self.upgrade_cost_multiplier ** (item.level - 1))
            for material, cost in item.materials_cost.items()
        }
        bigtime_cost = int(item.bigtime_cost * self.upgrade_cost_multiplier ** (item.level - 1))
        return materials_cost, bigtime_cost

    def upgrade_item(self, item: Item, inventory: PlayerInventory) -> Item:
        materials_cost, bigtime_cost = self.calculate_upgrade_cost(item)
        
        temp_item = Item(
            item_id=item.item_id,
            name=item.name,
            item_type=item.item_type,
            rarity=item.rarity,
            stats=item.stats.copy(),
            materials_cost=materials_cost,
            bigtime_cost=bigtime_cost,
            level=item.level
        )

        if not inventory.has_resources(temp_item):
            raise ValueError("Insufficient resources to upgrade item")

        inventory.spend_resources(temp_item)
        
        # Apply stat increases
        for stat in item.stats:
            item.stats[stat] *= (1 + self.stat_increase_per_level)
        
        item.level += 1
        return item

class BigTimeCraftingSimulator:
    def __init__(self):
        self.inventory = PlayerInventory()
        self.crafting_system = CraftingSystem()
        self.upgrade_system = UpgradeSystem()

    def initialize_player(self, bigtime: int, materials: Dict[MaterialType, int]) -> None:
        self.inventory.add_bigtime(bigtime)
        for material, amount in materials.items():
            self.inventory.add_material(material, amount)

    def craft_item_menu(self) -> None:
        print("\nCrafting Menu:")
        print("1. Weapon")
        print("2. Armor")
        print("3. Cosmetic")
        print("4. Back")
        
        choice = input("Select item type to craft: ")
        try:
            choice = int(choice)
            if choice == 1:
                self._craft_item_of_type(ItemType.WEAPON)
            elif choice == 2:
                self._craft_item_of_type(ItemType.ARMOR)
            elif choice == 3:
                self._craft_item_of
