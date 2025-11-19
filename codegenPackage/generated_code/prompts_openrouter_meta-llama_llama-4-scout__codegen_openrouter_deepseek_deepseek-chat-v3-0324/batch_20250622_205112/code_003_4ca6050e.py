"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Design a base-building system for a real-time strategy game like R-Planet, including infrastructure, military, and mining industries, and describe how the AI can be developed and improved over time.
Generated: DETERMINISTIC_4ca6050ee4ae7a4d
Batch ID: 20250622_205112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple


class ResourceType(Enum):
    """Enum representing different types of resources in the game."""
    MINERALS = auto()
    GAS = auto()
    ENERGY = auto()
    METAL = auto()
    CRYSTALS = auto()


class BuildingType(Enum):
    """Enum representing different types of buildings in the game."""
    # Infrastructure
    COMMAND_CENTER = auto()
    POWER_PLANT = auto()
    STORAGE = auto()
    
    # Military
    BARRACKS = auto()
    TURRET = auto()
    SHIPYARD = auto()
    
    # Mining
    MINERAL_EXTRACTOR = auto()
    GAS_REFINERY = auto()
    CRYSTAL_MINE = auto()


class UnitType(Enum):
    """Enum representing different types of units in the game."""
    WORKER = auto()
    SOLDIER = auto()
    TANK = auto()
    SCOUT = auto()
    BATTLESHIP = auto()


class Building(ABC):
    """Abstract base class for all buildings in the game."""
    
    def __init__(self, level: int = 1):
        self.level = level
        self.health = self.max_health()
        self.is_under_construction = True
    
    @abstractmethod
    def max_health(self) -> int:
        """Returns the maximum health of the building."""
        pass
    
    @abstractmethod
    def cost(self) -> Dict[ResourceType, int]:
        """Returns the cost to build/upgrade the building."""
        pass
    
    @abstractmethod
    def production_rate(self) -> Dict[ResourceType, int]:
        """Returns the production rate of the building."""
        pass
    
    def upgrade(self) -> bool:
        """Upgrades the building if possible. Returns True if successful."""
        if not self.is_under_construction:
            self.level += 1
            self.is_under_construction = True
            return True
        return False
    
    def complete_construction(self) -> None:
        """Marks the building as fully constructed."""
        self.is_under_construction = False
        self.health = self.max_health()


class CommandCenter(Building):
    """Command Center building - the main building in the game."""
    
    def max_health(self) -> int:
        return 1000 * self.level
    
    def cost(self) -> Dict[ResourceType, int]:
        return {
            ResourceType.MINERALS: 500 * self.level,
            ResourceType.METAL: 300 * self.level
        }
    
    def production_rate(self) -> Dict[ResourceType, int]:
        return {}  # Command Center doesn't produce resources
    
    def population_capacity(self) -> int:
        """Returns the population capacity provided by this building."""
        return 10 * self.level


class MineralExtractor(Building):
    """Mineral Extractor building - produces minerals."""
    
    def max_health(self) -> int:
        return 500 * self.level
    
    def cost(self) -> Dict[ResourceType, int]:
        return {
            ResourceType.MINERALS: 200 * self.level,
            ResourceType.METAL: 100 * self.level
        }
    
    def production_rate(self) -> Dict[ResourceType, int]:
        return {
            ResourceType.MINERALS: 10 * self.level
        }


class Barracks(Building):
    """Barracks building - produces military units."""
    
    def max_health(self) -> int:
        return 800 * self.level
    
    def cost(self) -> Dict[ResourceType, int]:
        return {
            ResourceType.MINERALS: 400 * self.level,
            ResourceType.METAL: 200 * self.level
        }
    
    def production_rate(self) -> Dict[ResourceType, int]:
        return {}  # Barracks doesn't produce resources
    
    def train_unit(self, unit_type: UnitType) -> Optional[Dict[ResourceType, int]]:
        """Returns the cost to train the specified unit, or None if not trainable."""
        unit_costs = {
            UnitType.SOLDIER: {
                ResourceType.MINERALS: 50,
                ResourceType.METAL: 20
            },
            UnitType.TANK: {
                ResourceType.MINERALS: 150,
                ResourceType.METAL: 100
            }
        }
        return unit_costs.get(unit_type)


class Base:
    """Represents a player's base in the game."""
    
    def __init__(self):
        self.buildings: Dict[BuildingType, List[Building]] = {}
        self.resources: Dict[ResourceType, int] = {
            rt: 0 for rt in ResourceType
        }
        self.units: List[UnitType] = []
        self.construction_queue: List[Tuple[BuildingType, int]] = []
    
    def add_building(self, building_type: BuildingType) -> bool:
        """Attempts to add a building to the base. Returns True if successful."""
        building_class = self._get_building_class(building_type)
        if not building_class:
            return False
        
        cost = building_class(1).cost()
        if not self._can_afford(cost):
            return False
        
        self._deduct_resources(cost)
        if building_type not in self.buildings:
            self.buildings[building_type] = []
        
        self.buildings[building_type].append(building_class(1))
        return True
    
    def upgrade_building(self, building_type: BuildingType, index: int) -> bool:
        """Attempts to upgrade a building. Returns True if successful."""
        if (building_type not in self.buildings or 
            index >= len(self.buildings[building_type])):
            return False
        
        building = self.buildings[building_type][index]
        if building.is_under_construction:
            return False
        
        cost = building.cost()
        if not self._can_afford(cost):
            return False
        
        self._deduct_resources(cost)
        return building.upgrade()
    
    def complete_construction(self) -> None:
        """Completes construction for all buildings in progress."""
        for building_list in self.buildings.values():
            for building in building_list:
                if building.is_under_construction:
                    building.complete_construction()
    
    def _can_afford(self, cost: Dict[ResourceType, int]) -> bool:
        """Checks if the base can afford the given cost."""
        return all(self.resources[rt] >= amount for rt, amount in cost.items())
    
    def _deduct_resources(self, cost: Dict[ResourceType, int]) -> None:
        """Deducts resources from the base."""
        for rt, amount in cost.items():
            self.resources[rt] -= amount
    
    def _get_building_class(self, building_type: BuildingType) -> Optional[type]:
        """Returns the appropriate building class for the given type."""
        building_classes = {
            BuildingType.COMMAND_CENTER: CommandCenter,
            BuildingType.MINERAL_EXTRACTOR: MineralExtractor,
            BuildingType.BARRACKS: Barracks,
        }
        return building_classes.get(building_type)
    
    def collect_resources(self) -> None:
        """Collects resources from all production buildings."""
        for building_list in self.buildings.values():
            for building in building_list:
                if not building.is_under_construction:
                    for rt, amount in building.production_rate().items():
                        self.resources[rt] += amount


class AIController:
    """Controls the AI behavior for base building and unit production."""
    
    def __init__(self, base: Base, difficulty: str = "medium"):
        self.base = base
        self.difficulty = difficulty
        self.strategy: Dict[str, float] = self._get_difficulty_settings()
    
    def _get_difficulty_settings(self) -> Dict[str, float]:
        """Returns AI settings based on difficulty level."""
        return {
            "easy": {"build_threshold": 0.7, "upgrade_chance": 0.3},
            "medium": {"build_threshold": 0.5, "upgrade_chance": 0.5},
            "hard": {"build_threshold": 0.3, "upgrade_chance": 0.7}
        }.get(self.difficulty, {"build_threshold": 0.5, "upgrade_chance": 0.5})
    
    def make_decision(self) -> None:
        """Makes decisions about building and upgrading."""
        self._manage_buildings()
        self._train_units()
    
    def _manage_buildings(self) -> None:
        """Decides which buildings to construct or upgrade."""
        # Prioritize command center if not present
        if BuildingType.COMMAND_CENTER not in self.base.buildings:
            self.base.add_building(BuildingType.COMMAND_CENTER)
            return
        
        # Randomly decide to build or upgrade based on strategy
        if random.random() < self.strategy["build_threshold"]:
            self._build_new_building()
        else:
            self
