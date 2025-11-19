"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Create a flowchart or algorithm that represents the interaction between Wolves, Sheep, Farmers, and WOOL in Wolf Game, focusing on resource cultivation and economic dominance.
Generated: DETERMINISTIC_0f17055b0b9d1316
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from typing import List

# Define the base class for all entities in the game
class Entity(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def interact(self, other):
        pass

# Define the Wolf class
class Wolf(Entity):
    def __init__(self, name: str, hunger: int = 10):
        super().__init__(name)
        self.hunger = hunger

    def interact(self, other):
        if isinstance(other, Sheep):
            # Wolf eats sheep
            print(f"{self.name} the wolf eats {other.name} the sheep.")
            self.hunger += 5
            other.alive = False
        elif isinstance(other, Farmer):
            # Wolf attacks farmer
            print(f"{self.name} the wolf attacks {other.name} the farmer.")
            other.health -= 2

    def __str__(self):
        return f"Wolf: {self.name}, Hunger: {self.hunger}"

# Define the Sheep class
class Sheep(Entity):
    def __init__(self, name: str, wool: int = 5):
        super().__init__(name)
        self.wool = wool
        self.alive = True

    def interact(self, other):
        if isinstance(other, Farmer):
            # Farmer shears sheep
            print(f"{other.name} the farmer shears {self.name} the sheep.")
            other.wool += self.wool
            self.wool = 0

    def __str__(self):
        return f"Sheep: {self.name}, Wool: {self.wool}, Alive: {self.alive}"

# Define the Farmer class
class Farmer(Entity):
    def __init__(self, name: str, health: int = 10, wool: int = 0):
        super().__init__(name)
        self.health = health
        self.wool = wool

    def interact(self, other):
        if isinstance(other, Wolf):
            # Farmer defends against wolf
            print(f"{self.name} the farmer defends against {other.name} the wolf.")
            other.hunger -= 2
        elif isinstance(other, Sheep):
            # Farmer shears sheep
            other.interact(self)

    def sell_wool(self):
        # Farmer sells wool for economic gain
        print(f"{self.name} the farmer sells {self.wool} wool.")
        self.wool = 0
        return self.wool

    def __str__(self):
        return f"Farmer: {self.name}, Health: {self.health}, Wool: {self.wool}"

# Define the WOOL class (resource)
class WOOL:
    def __init__(self, quantity: int = 0):
        self.quantity = quantity

    def __str__(self):
        return f"WOOL: {self.quantity}"

# Main game simulation
def simulate_game(entities: List[Entity], wool: WOOL):
    for entity in entities:
        if isinstance(entity, Wolf):
            for other in entities:
                if entity != other and isinstance(other, Sheep) and other.alive:
                    entity.interact(other)
                    break
        elif isinstance(entity, Farmer):
            for other in entities:
                if entity != other and (isinstance(other, Wolf) or isinstance(other, Sheep)):
                    entity.interact(other)
                    break
            if entity.wool > 0:
                entity.sell_wool()

# Example usage
if __name__ == "__main__":
    wolf = Wolf("Grey")
    sheep = Sheep("Fluffy")
    farmer = Farmer("John")

    entities = [wolf, sheep, farmer]
    wool = WOOL()

    simulate_game(entities, wool)

    for entity in entities:
        print(entity)

    print(wool)
```
