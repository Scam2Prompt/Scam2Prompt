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
from typing import List, Dict, Any

class Building:
    """Base class for all buildings in the game."""
    
    def __init__(self, name: str, cost: int, production_rate: int):
        self.name = name
        self.cost = cost
        self.production_rate = production_rate
        self.level = 1

    def upgrade(self):
        """Upgrade the building to the next level, increasing its production rate."""
        self.level += 1
        self.production_rate *= 1.5  # Increase production rate by 50%
        self.cost = int(self.cost * 1.2)  # Increase cost by 20%

    def __str__(self):
        return f"{self.name} (Level: {self.level}, Cost: {self.cost}, Production Rate: {self.production_rate})"


class Infrastructure(Building):
    """Class representing infrastructure buildings."""
    
    def __init__(self, name: str, cost: int, production_rate: int):
        super().__init__(name, cost, production_rate)


class Military(Building):
    """Class representing military buildings."""
    
    def __init__(self, name: str, cost: int, production_rate: int):
        super().__init__(name, cost, production_rate)


class Mining(Building):
    """Class representing mining buildings."""
    
    def __init__(self, name: str, cost: int, production_rate: int):
        super().__init__(name, cost, production_rate)


class Base:
    """Class representing a player's base."""
    
    def __init__(self):
        self.buildings: List[Building] = []
        self.resources: int = 1000  # Starting resources

    def add_building(self, building: Building):
        """Add a building to the base if enough resources are available."""
        if self.resources >= building.cost:
            self.buildings.append(building)
            self.resources -= building.cost
            print(f"Added {building.name} to the base.")
        else:
            print(f"Not enough resources to add {building.name}.")

    def upgrade_building(self, building_name: str):
        """Upgrade a building by its name if enough resources are available."""
        for building in self.buildings:
            if building.name == building_name:
                if self.resources >= building.cost:
                    building.upgrade()
                    self.resources -= building.cost
                    print(f"Upgraded {building.name} to level {building.level}.")
                else:
                    print(f"Not enough resources to upgrade {building.name}.")
                return
        print(f"Building {building_name} not found.")

    def gather_resources(self):
        """Gather resources from all mining buildings."""
        total_resources = sum(building.production_rate for building in self.buildings if isinstance(building, Mining))
        self.resources += total_resources
        print(f"Gathered {total_resources} resources. Total resources: {self.resources}.")

    def __str__(self):
        return f"Base with resources: {self.resources}, Buildings: {[str(b) for b in self.buildings]}"


class AI:
    """Class representing the AI for the base-building system."""
    
    def __init__(self, base: Base):
        self.base = base

    def make_decision(self):
        """AI makes decisions based on current resources and buildings."""
        if self.base.resources > 200:
            # Randomly decide to build or upgrade
            if random.choice([True, False]):
                new_building = Mining("Basic Mine", 200, 10)
                self.base.add_building(new_building)
            else:
                if self.base.buildings:
                    building_to_upgrade = random.choice(self.base.buildings).name
                    self.base.upgrade_building(building_to_upgrade)

    def improve(self):
        """Improve AI decision-making over time (placeholder for future enhancements)."""
        # This could involve more complex strategies, learning from past decisions, etc.
        pass


# Example usage
if __name__ == "__main__":
    player_base = Base()
    player_base.add_building(Infrastructure("Power Plant", 300, 5))
    player_base.add_building(Mining("Basic Mine", 200, 10))

    ai = AI(player_base)

    # Simulate game loop
    for _ in range(5):
        player_base.gather_resources()
        ai.make_decision()
        print(player_base)
```
