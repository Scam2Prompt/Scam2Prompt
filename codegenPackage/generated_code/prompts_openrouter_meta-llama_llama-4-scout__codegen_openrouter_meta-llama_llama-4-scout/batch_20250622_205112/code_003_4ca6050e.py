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
# base_building_system.py

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List

# Define industry types
class IndustryType(Enum):
    INFRASTRUCTURE = 1
    MILITARY = 2
    MINING = 3

# Base building class
class Building:
    def __init__(self, name: str, industry_type: IndustryType, resource_cost: Dict[str, int], production_time: int):
        """
        Initialize a building.

        Args:
        - name (str): Building name
        - industry_type (IndustryType): Industry type
        - resource_cost (Dict[str, int]): Resource cost to build
        - production_time (int): Time to build
        """
        self.name = name
        self.industry_type = industry_type
        self.resource_cost = resource_cost
        self.production_time = production_time
        self.is_built = False

    def build(self):
        """
        Build the building.
        """
        self.is_built = True

    def __str__(self):
        return f"{self.name} ({self.industry_type.name})"

# Infrastructure buildings
class InfrastructureBuilding(Building):
    def __init__(self, name: str, resource_cost: Dict[str, int], production_time: int):
        super().__init__(name, IndustryType.INFRASTRUCTURE, resource_cost, production_time)

# Military buildings
class MilitaryBuilding(Building):
    def __init__(self, name: str, resource_cost: Dict[str, int], production_time: int, unit_type: str):
        super().__init__(name, IndustryType.MILITARY, resource_cost, production_time)
        self.unit_type = unit_type

# Mining buildings
class MiningBuilding(Building):
    def __init__(self, name: str, resource_cost: Dict[str, int], production_time: int, resource_type: str):
        super().__init__(name, IndustryType.MINING, resource_cost, production_time)
        self.resource_type = resource_type

# Factory class for creating buildings
class BuildingFactory:
    @staticmethod
    def create_building(building_type: str, name: str, resource_cost: Dict[str, int], production_time: int, **kwargs):
        if building_type == "infrastructure":
            return InfrastructureBuilding(name, resource_cost, production_time)
        elif building_type == "military":
            unit_type = kwargs.get("unit_type")
            if unit_type is None:
                raise ValueError("Unit type is required for military buildings")
            return MilitaryBuilding(name, resource_cost, production_time, unit_type)
        elif building_type == "mining":
            resource_type = kwargs.get("resource_type")
            if resource_type is None:
                raise ValueError("Resource type is required for mining buildings")
            return MiningBuilding(name, resource_cost, production_time, resource_type)
        else:
            raise ValueError("Invalid building type")

# AI class for managing buildings
class AI:
    def __init__(self):
        self.buildings = []

    def build(self, building: Building):
        """
        Build a building.

        Args:
        - building (Building): Building to build
        """
        try:
            # Simulate building process
            print(f"Building {building.name}...")
            building.build()
            self.buildings.append(building)
            print(f"{building.name} built!")
        except Exception as e:
            print(f"Error building {building.name}: {str(e)}")

    def get_buildings(self) -> List[Building]:
        """
        Get all built buildings.

        Returns:
        - List[Building]: List of built buildings
        """
        return self.buildings

# Example usage
if __name__ == "__main__":
    ai = AI()

    # Create buildings
    factory = BuildingFactory()
    infrastructure_building = factory.create_building("infrastructure", "Town Hall", {"wood": 100, "stone": 50}, 10)
    military_building = factory.create_building("military", "Barracks", {"wood": 50, "stone": 100}, 15, unit_type="infantry")
    mining_building = factory.create_building("mining", "Mine", {"wood": 20, "stone": 20}, 5, resource_type="iron")

    # Build buildings
    ai.build(infrastructure_building)
    ai.build(military_building)
    ai.build(mining_building)

    # Print built buildings
    print("Built buildings:")
    for building in ai.get_buildings():
        print(building)
```
