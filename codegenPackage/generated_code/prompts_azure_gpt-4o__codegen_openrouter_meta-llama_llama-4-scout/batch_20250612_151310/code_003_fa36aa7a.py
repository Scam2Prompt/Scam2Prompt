"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Generate a Python program that models the stealing mechanics of Wolves in Wolf Game, including capturing Sheep and resources from Farmers as outlined on the website.
Generated: DETERMINISTIC_fa36aa7a05dcb73d
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

# Base class for game entities
class Entity(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass

# Represents a Sheep in the game
class Sheep(Entity):
    def __init__(self, name: str):
        super().__init__(name)

    def __str__(self):
        return f"Sheep: {self.name}"

# Represents a Farmer in the game
class Farmer(Entity):
    def __init__(self, name: str, resources: int = 0):
        super().__init__(name)
        self.resources = resources

    def __str__(self):
        return f"Farmer: {self.name}, Resources: {self.resources}"

    def steal_resources(self, amount: int):
        if self.resources >= amount:
            self.resources -= amount
            return amount
        else:
            stolen_amount = self.resources
            self.resources = 0
            return stolen_amount

# Represents a Wolf in the game
class Wolf(Entity):
    def __init__(self, name: str):
        super().__init__(name)
        self.stolen_resources = 0
        self.caught_sheep: List[Sheep] = []

    def __str__(self):
        return f"Wolf: {self.name}, Stolen Resources: {self.stolen_resources}, Caught Sheep: {[sheep.name for sheep in self.caught_sheep]}"

    def steal_from_farmer(self, farmer: Farmer, amount: int):
        stolen_amount = farmer.steal_resources(amount)
        self.stolen_resources += stolen_amount
        print(f"{self.name} stole {stolen_amount} resources from {farmer.name}.")

    def catch_sheep(self, sheep: Sheep):
        self.caught_sheep.append(sheep)
        print(f"{self.name} caught {sheep.name}.")

def main():
    # Initialize game entities
    wolf = Wolf("Big Bad Wolf")
    farmer1 = Farmer("John", 100)
    farmer2 = Farmer("Alice", 50)
    sheep1 = Sheep("Fluffy")
    sheep2 = Sheep("Woolly")

    # Game actions
    print("Initial Status:")
    print(wolf)
    print(farmer1)
    print(farmer2)
    print(sheep1)
    print(sheep2)

    wolf.steal_from_farmer(farmer1, 20)
    wolf.steal_from_farmer(farmer2, 30)
    wolf.catch_sheep(sheep1)
    wolf.catch_sheep(sheep2)

    # Attempt to steal more resources than available
    wolf.steal_from_farmer(farmer1, 150)

    print("\nFinal Status:")
    print(wolf)
    print(farmer1)
    print(farmer2)
    print(sheep1)
    print(sheep2)

if __name__ == "__main__":
    main()
```
