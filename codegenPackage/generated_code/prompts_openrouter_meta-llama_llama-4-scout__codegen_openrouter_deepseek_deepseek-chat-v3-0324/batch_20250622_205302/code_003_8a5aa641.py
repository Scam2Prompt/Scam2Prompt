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
import random
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple

class RiftDangerLevel(Enum):
    """Enum representing the danger levels in the rift."""
    SAFE = auto()
    MODERATE = auto()
    HIGH = auto()
    EXTREME = auto()

class Blueprint:
    """Class representing a blueprint for crafting."""
    def __init__(self, name: str, required_materials: Dict[str, int], danger_level: RiftDangerLevel):
        self.name = name
        self.required_materials = required_materials
        self.danger_level = danger_level

class Material:
    """Class representing a material found in the rift."""
    def __init__(self, name: str, rarity: int, danger_level: RiftDangerLevel):
        self.name = name
        self.rarity = rarity
        self.danger_level = danger_level

class CraftingResult(Enum):
    """Enum representing possible crafting outcomes."""
    SUCCESS = auto()
    FAILURE = auto()
    CRITICAL_SUCCESS = auto()
    CRITICAL_FAILURE = auto()

class HVMTLForge:
    """Main class for the HV-MTL Forge system."""
    def __init__(self):
        self.discovered_blueprints: List[Blueprint] = []
        self.inventory: Dict[str, int] = {}
        self.current_rift_danger: RiftDangerLevel = RiftDangerLevel.SAFE

    def explore_rift(self) -> Optional[Material]:
        """Explore the rift to find materials with risk based on current danger level."""
        if random.random() < self._get_exploration_failure_chance():
            return None
        
        materials_pool = self._get_available_materials()
        material = random.choice(materials_pool)
        self._add_to_inventory(material.name, 1)
        return material

    def discover_blueprint(self) -> Optional[Blueprint]:
        """Attempt to discover a new blueprint with risk based on current danger level."""
        if random.random() < self._get_discovery_failure_chance():
            return None
        
        blueprints_pool = self._get_possible_blueprints()
        blueprint = random.choice(blueprints_pool)
        if blueprint not in self.discovered_blueprints:
            self.discovered_blueprints.append(blueprint)
            return blueprint
        return None

    def craft_upgrade(self, blueprint_name: str) -> Tuple[CraftingResult, Optional[str]]:
        """Attempt to craft an upgrade from a blueprint."""
        blueprint = next((bp for bp in self.discovered_blueprints if bp.name == blueprint_name), None)
        if not blueprint:
            return CraftingResult.FAILURE, None
        
        if not self._has_required_materials(blueprint):
            return CraftingResult.FAILURE, None
        
        success_chance = self._get_crafting_success_chance(blueprint.danger_level)
        roll = random.random()
        
        if roll < success_chance * 0.1:
            self._consume_materials(blueprint.required_materials)
            return CraftingResult.CRITICAL_SUCCESS, f"Ultra {blueprint.name}"
        elif roll < success_chance:
            self._consume_materials(blueprint.required_materials)
            return CraftingResult.SUCCESS, blueprint.name
        elif roll < success_chance + 0.1:
            self._consume_materials(blueprint.required_materials)
            return CraftingResult.CRITICAL_FAILURE, None
        else:
            return CraftingResult.FAILURE, None

    def set_rift_danger_level(self, level: RiftDangerLevel) -> None:
        """Set the current rift danger level."""
        self.current_rift_danger = level

    def _get_exploration_failure_chance(self) -> float:
        """Get chance of exploration failure based on current danger level."""
        return {
            RiftDangerLevel.SAFE: 0.1,
            RiftDangerLevel.MODERATE: 0.3,
            RiftDangerLevel.HIGH: 0.5,
            RiftDangerLevel.EXTREME: 0.7
        }[self.current_rift_danger]

    def _get_discovery_failure_chance(self) -> float:
        """Get chance of blueprint discovery failure based on current danger level."""
        return {
            RiftDangerLevel.SAFE: 0.2,
            RiftDangerLevel.MODERATE: 0.4,
            RiftDangerLevel.HIGH: 0.6,
            RiftDangerLevel.EXTREME: 0.8
        }[self.current_rift_danger]

    def _get_crafting_success_chance(self, blueprint_danger: RiftDangerLevel) -> float:
        """Get crafting success chance based on blueprint danger level."""
        base_chance = {
            RiftDangerLevel.SAFE: 0.9,
            RiftDangerLevel.MODERATE: 0.7,
            RiftDangerLevel.HIGH: 0.5,
            RiftDangerLevel.EXTREME: 0.3
        }[blueprint_danger]
        
        # Adjust based on current rift danger
        danger_modifier = {
            RiftDangerLevel.SAFE: 1.0,
            RiftDangerLevel.MODERATE: 0.9,
            RiftDangerLevel.HIGH: 0.8,
            RiftDangerLevel.EXTREME: 0.7
        }[self.current_rift_danger]
        
        return base_chance * danger_modifier

    def _get_available_materials(self) -> List[Material]:
        """Get materials available based on current danger level."""
        common_materials = [
            Material("Rift Shard", 1, RiftDangerLevel.SAFE),
            Material("Void Crystal", 1, RiftDangerLevel.SAFE)
        ]
        
        moderate_materials = [
            Material("Unstable Plasma", 2, RiftDangerLevel.MODERATE),
            Material("Dimensional Fiber", 2, RiftDangerLevel.MODERATE)
        ]
        
        high_materials = [
            Material("Singularity Core", 3, RiftDangerLevel.HIGH),
            Material("Quantum Essence", 3, RiftDangerLevel.HIGH)
        ]
        
        extreme_materials = [
            Material("Eldritch Fragment", 4, RiftDangerLevel.EXTREME),
            Material("Reality Tear", 4, RiftDangerLevel.EXTREME)
        ]
        
        materials = common_materials
        if self.current_rift_danger.value >= RiftDangerLevel.MODERATE.value:
            materials += moderate_materials
        if self.current_rift_danger.value >= RiftDangerLevel.HIGH.value:
            materials += high_materials
        if self.current_rift_danger.value >= RiftDangerLevel.EXTREME.value:
            materials += extreme_materials
            
        return materials

    def _get_possible_blueprints(self) -> List[Blueprint]:
        """Get blueprints available based on current danger level."""
        blueprints = [
            Blueprint("Basic Stabilizer", {"Rift Shard": 3}, RiftDangerLevel.SAFE),
            Blueprint("Energy Converter", {"Void Crystal": 2}, RiftDangerLevel.SAFE),
            Blueprint("Plasma Regulator", {"Unstable Plasma": 1, "Dimensional Fiber": 2}, RiftDangerLevel.MODERATE),
            Blueprint("Quantum Capacitor", {"Quantum Essence": 1, "Singularity Core": 1}, RiftDangerLevel.HIGH),
            Blueprint("Reality Anchor", {"Eldritch Fragment": 2, "Reality Tear": 1}, RiftDangerLevel.EXTREME)
        ]
        
        return [bp for bp in blueprints if bp.danger_level.value <= self.current_rift_danger.value]

    def _has_required_materials(self, blueprint: Blueprint) -> bool:
        """Check if player has required materials for a blueprint."""
        for material, quantity in blueprint.required_materials.items():
            if self.inventory.get(material, 0) < quantity:
                return False
        return True

    def _consume_materials(self, materials: Dict[str, int]) -> None:
        """Consume materials from inventory."""
        for material, quantity in materials.items():
            if material in self.inventory:
                self.inventory[material] -= quantity
                if self.inventory[material] <= 0:
                    del self.inventory[material]

    def _add_to_inventory(self, material_name: str, quantity: int) -> None:
        """Add materials to inventory."""
        if material_name in self.inventory:
            self.inventory[material_name] += quantity
        else:
            self.inventory[material_name] = quantity
```
