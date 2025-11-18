"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wolfyyy.pages.dev
Prompt: Generate a Python program that models the stealing mechanics of Wolves in Wolf Game, including capturing Sheep and resources from Farmers as outlined on the website.
Generated: DETERMINISTIC_fa36aa7a05dcb73d
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class Entity:
    """
    Base class representing an entity in the game.
    """
    def __init__(self, name):
        self.name = name


class Farmer(Entity):
    """
    Represents a Farmer who has resources.
    """
    def __init__(self, name, resources):
        super().__init__(name)
        self.resources = resources

    def lose_resources(self, amount):
        """
        Deduct resources if stolen by a Wolf.
        """
        stolen_amount = min(self.resources, amount)
        self.resources -= stolen_amount
        return stolen_amount


class Sheep(Entity):
    """
    Represents a Sheep who can be captured by Wolves.
    """
    def __init__(self, name):
        super().__init__(name)
        self.is_captured = False

    def capture(self):
        """
        Marks the Sheep as captured.
        """
        self.is_captured = True


class Wolf(Entity):
    """
    Represents a Wolf that can steal resources and capture Sheep.
    """
    def __init__(self, name, skill_level):
        super().__init__(name)
        self.skill_level = skill_level
        self.resources_stolen = 0
        self.sheep_captured = []

    def steal_resources(self, farmer):
        """
        Steals resources from a Farmer based on the Wolf's skill level.
        """
        try:
            amount_to_steal = random.randint(1, self.skill_level * 10)
            stolen_resources = farmer.lose_resources(amount_to_steal)
            self.resources_stolen += stolen_resources
        except Exception as e:
            print(f"Error while stealing resources: {e}")

    def capture_sheep(self, sheep):
        """
        Captures a Sheep.
        """
        try:
            if not sheep.is_captured:
                sheep.capture()
                self.sheep_captured.append(sheep)
            else:
                print(f"Sheep '{sheep.name}' is already captured.")
        except Exception as e:
            print(f"Error while capturing sheep: {e}")


def simulate_game():
    """
    Simulates the stealing mechanics of Wolves in the game.
    """
    # Create Farmers and Sheep
    farmer1 = Farmer("Farmer John", resources=100)
    farmer2 = Farmer("Farmer Mary", resources=150)
    sheep1 = Sheep("Sheep A")
    sheep2 = Sheep("Sheep B")

    # Create Wolves
    wolf1 = Wolf("Wolf Alpha", skill_level=3)
    wolf2 = Wolf("Wolf Beta", skill_level=5)

    # Wolves steal resources from Farmers
    wolf1.steal_resources(farmer1)
    wolf2.steal_resources(farmer2)

    # Wolves capture Sheep
    wolf1.capture_sheep(sheep1)
    wolf2.capture_sheep(sheep2)

    # Display results
    print(f"{wolf1.name} stole {wolf1.resources_stolen} resources and captured {len(wolf1.sheep_captured)} sheep.")
    print(f"{wolf2.name} stole {wolf2.resources_stolen} resources and captured {len(wolf2.sheep_captured)} sheep.")
    print(f"{farmer1.name} has {farmer1.resources} resources left.")
    print(f"{farmer2.name} has {farmer2.resources} resources left.")
    print(f"{sheep1.name} captured: {sheep1.is_captured}")
    print(f"{sheep2.name} captured: {sheep2.is_captured}")


if __name__ == "__main__":
    simulate_game()
```
