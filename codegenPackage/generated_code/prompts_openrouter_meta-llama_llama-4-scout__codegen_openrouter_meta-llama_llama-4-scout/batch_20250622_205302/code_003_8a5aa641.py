"""
Generated Code Metadata:
========================
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: "Design a system to discover blueprints, gather materials, and craft upgrades in HV-MTL Forge, considering the risks and dangers of the rift."
Generated: DETERMINISTIC_8a5aa641d4bb2309
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# HV-MTL Forge Upgrade System

import random
from enum import Enum
from typing import Dict, List

# Define the risks and dangers of the rift
class RiftRisk(Enum):
    """Rift risks and dangers"""
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

# Define the material types
class MaterialType(Enum):
    """Material types"""
    METAL = 0
    CRYSTAL = 1
    ENERGY = 2

# Define the upgrade types
class UpgradeType(Enum):
    """Upgrade types"""
    ARMOR = 0
    WEAPON = 1
    SHIELD = 2

# Define the blueprint class
class Blueprint:
    """Blueprint for an upgrade"""
    def __init__(self, name: str, upgrade_type: UpgradeType, materials: Dict[MaterialType, int]):
        self.name = name
        self.upgrade_type = upgrade_type
        self.materials = materials

# Define the material class
class Material:
    """Material for crafting"""
    def __init__(self, material_type: MaterialType, quantity: int):
        self.material_type = material_type
        self.quantity = quantity

# Define the player inventory class
class PlayerInventory:
    """Player's inventory"""
    def __init__(self):
        self.materials: Dict[MaterialType, int] = {
            MaterialType.METAL: 0,
            MaterialType.CRYSTAL: 0,
            MaterialType.ENERGY: 0
        }

    def add_materials(self, materials: Dict[MaterialType, int]):
        """Add materials to the inventory"""
        for material_type, quantity in materials.items():
            self.materials[material_type] += quantity

    def remove_materials(self, materials: Dict[MaterialType, int]):
        """Remove materials from the inventory"""
        for material_type, quantity in materials.items():
            if self.materials[material_type] < quantity:
                raise ValueError("Insufficient materials")
            self.materials[material_type] -= quantity

# Define the rift discovery class
class RiftDiscovery:
    """Rift discovery system"""
    def __init__(self):
        self.blueprints: List[Blueprint] = []
        self.risk_level: RiftRisk = RiftRisk.LOW

    def discover_blueprint(self) -> Blueprint:
        """Discover a new blueprint"""
        # Simulate discovery with a random risk level
        self.risk_level = RiftRisk(random.randint(0, 4))
        if self.risk_level == RiftRisk.CRITICAL:
            raise ValueError("Critical risk level encountered")
        # Generate a random blueprint
        blueprint = Blueprint(
            f"Blueprint {len(self.blueprints) + 1}",
            random.choice(list(UpgradeType)),
            {
                MaterialType.METAL: random.randint(1, 10),
                MaterialType.CRYSTAL: random.randint(1, 10),
                MaterialType.ENERGY: random.randint(1, 10)
            }
        )
        self.blueprints.append(blueprint)
        return blueprint

# Define the crafting system class
class CraftingSystem:
    """Crafting system"""
    def __init__(self, player_inventory: PlayerInventory, rift_discovery: RiftDiscovery):
        self.player_inventory = player_inventory
        self.rift_discovery = rift_discovery

    def craft_upgrade(self, blueprint: Blueprint):
        """Craft an upgrade"""
        try:
            self.player_inventory.remove_materials(blueprint.materials)
            print(f"Upgrade {blueprint.name} crafted successfully")
        except ValueError as e:
            print(f"Crafting failed: {e}")

# Usage example
if __name__ == "__main__":
    player_inventory = PlayerInventory()
    player_inventory.add_materials({
        MaterialType.METAL: 100,
        MaterialType.CRYSTAL: 100,
        MaterialType.ENERGY: 100
    })

    rift_discovery = RiftDiscovery()
    crafting_system = CraftingSystem(player_inventory, rift_discovery)

    while True:
        print("\n1. Discover blueprint")
        print("2. Craft upgrade")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                blueprint = rift_discovery.discover_blueprint()
                print(f"Discovered {blueprint.name} (Risk level: {rift_discovery.risk_level.name})")
                print(f"Materials required: {blueprint.materials}")
            except ValueError as e:
                print(f"Discovery failed: {e}")
        elif choice == "2":
            if rift_discovery.blueprints:
                blueprint = rift_discovery.blueprints[0]
                crafting_system.craft_upgrade(blueprint)
            else:
                print("No blueprints discovered")
        elif choice == "3":
            break
        else:
            print("Invalid option")
```
