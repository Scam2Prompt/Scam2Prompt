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
from typing import List, Dict

# Base class for all buildings
class Building:
    def __init__(self, name: str, level: int = 1):
        self.name = name
        self.level = level

    def upgrade(self):
        """Upgrade the building to the next level."""
        self.level += 1
        print(f"{self.name} upgraded to level {self.level}.")

    def get_info(self) -> Dict:
        """Return building information."""
        return {"name": self.name, "level": self.level}


# Infrastructure building
class Infrastructure(Building):
    def __init__(self, name: str, level: int = 1, capacity: int = 100):
        super().__init__(name, level)
        self.capacity = capacity

    def upgrade(self):
        """Upgrade infrastructure and increase capacity."""
        super().upgrade()
        self.capacity += 50  # Increase capacity with each upgrade

    def get_info(self) -> Dict:
        info = super().get_info()
        info["capacity"] = self.capacity
        return info


# Military building
class Military(Building):
    def __init__(self, name: str, level: int = 1, unit_capacity: int = 10):
        super().__init__(name, level)
        self.unit_capacity = unit_capacity

    def upgrade(self):
        """Upgrade military building and increase unit capacity."""
        super().upgrade()
        self.unit_capacity += 5  # Increase unit capacity with each upgrade

    def get_info(self) -> Dict:
        info = super().get_info()
        info["unit_capacity"] = self.unit_capacity
        return info


# Mining building
class Mining(Building):
    def __init__(self, name: str, level: int = 1, resource_rate: int = 10):
        super().__init__(name, level)
        self.resource_rate = resource_rate

    def upgrade(self):
        """Upgrade mining building and increase resource rate."""
        super().upgrade()
        self.resource_rate += 5  # Increase resource rate with each upgrade

    def get_info(self) -> Dict:
        info = super().get_info()
        info["resource_rate"] = self.resource_rate
        return info


# Base class to manage all buildings
class Base:
    def __init__(self):
        self.buildings: List[Building] = []

    def add_building(self, building: Building):
        """Add a new building to the base."""
        self.buildings.append(building)
        print(f"{building.name} added to the base.")

    def upgrade_building(self, building_name: str):
        """Upgrade a specific building by name."""
        for building in self.buildings:
            if building.name == building_name:
                building.upgrade()
                return
        print(f"Building {building_name} not found.")

    def get_base_info(self) -> List[Dict]:
        """Get information about all buildings in the base."""
        return [building.get_info() for building in self.buildings]


# AI system for managing the base
class BaseAI:
    def __init__(self, base: Base):
        self.base = base

    def prioritize_upgrades(self):
        """AI logic to prioritize building upgrades."""
        # Example: Prioritize mining buildings first, then infrastructure, then military
        mining_buildings = [b for b in self.base.buildings if isinstance(b, Mining)]
        infrastructure_buildings = [b for b in self.base.buildings if isinstance(b, Infrastructure)]
        military_buildings = [b for b in self.base.buildings if isinstance(b, Military)]

        for building in mining_buildings + infrastructure_buildings + military_buildings:
            building.upgrade()

    def add_random_building(self):
        """AI logic to add a random building to the base."""
        building_types = [Infrastructure, Military, Mining]
        building_type = random.choice(building_types)
        building_name = f"{building_type.__name__} {len(self.base.buildings) + 1}"
        new_building = building_type(name=building_name)
        self.base.add_building(new_building)

    def improve_over_time(self):
        """Simulate AI improvement over time."""
        # Example: AI learns to balance upgrades better
        print("AI is improving its strategy...")
        self.prioritize_upgrades()


# Example usage
if __name__ == "__main__":
    # Create a base
    my_base = Base()

    # Add initial buildings
    my_base.add_building(Infrastructure(name="Town Hall"))
    my_base.add_building(Military(name="Barracks"))
    my_base.add_building(Mining(name="Gold Mine"))

    # Display base info
    print("Initial Base Info:", my_base.get_base_info())

    # Create AI to manage the base
    base_ai = BaseAI(base=my_base)

    # AI adds a random building
    base_ai.add_random_building()

    # AI prioritizes upgrades
    base_ai.prioritize_upgrades()

    # Display updated base info
    print("Updated Base Info:", my_base.get_base_info())

    # Simulate AI improvement
    base_ai.improve_over_time()

    # Display final base info
    print("Final Base Info:", my_base.get_base_info())
```
