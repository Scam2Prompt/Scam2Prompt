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
import random
from typing import Dict, List, Optional, Tuple

class Sheep:
    """Represents a Sheep in the game."""
    def __init__(self, sheep_id: int, wool: int = 0):
        self.sheep_id = sheep_id
        self.wool = wool
    
    def __repr__(self) -> str:
        return f"Sheep(id={self.sheep_id}, wool={self.wool})"

class Farmer:
    """Represents a Farmer in the game."""
    def __init__(self, farmer_id: int, resources: Dict[str, int] = None):
        self.farmer_id = farmer_id
        self.resources = resources if resources else {"wheat": 0, "wood": 0}
    
    def __repr__(self) -> str:
        return f"Farmer(id={self.farmer_id}, resources={self.resources})"

class Wolf:
    """Represents a Wolf in the game."""
    def __init__(self, wolf_id: int, strength: int = 10):
        self.wolf_id = wolf_id
        self.strength = strength
        self.captured_sheep: List[Sheep] = []
        self.stolen_resources: Dict[str, int] = {"wheat": 0, "wood": 0}
    
    def __repr__(self) -> str:
        return f"Wolf(id={self.wolf_id}, strength={self.strength}, captured_sheep={len(self.captured_sheep)}, stolen_resources={self.stolen_resources})"

class WolfGame:
    """Models the Wolf Game mechanics including stealing from Sheep and Farmers."""
    def __init__(self):
        self.sheep: Dict[int, Sheep] = {}
        self.farmers: Dict[int, Farmer] = {}
        self.wolves: Dict[int, Wolf] = {}
        self.next_id = 1
    
    def add_sheep(self, wool: int = 0) -> Sheep:
        """Add a new Sheep to the game."""
        sheep = Sheep(self.next_id, wool)
        self.sheep[self.next_id] = sheep
        self.next_id += 1
        return sheep
    
    def add_farmer(self, resources: Dict[str, int] = None) -> Farmer:
        """Add a new Farmer to the game."""
        farmer = Farmer(self.next_id, resources)
        self.farmers[self.next_id] = farmer
        self.next_id += 1
        return farmer
    
    def add_wolf(self, strength: int = 10) -> Wolf:
        """Add a new Wolf to the game."""
        wolf = Wolf(self.next_id, strength)
        self.wolves[self.next_id] = wolf
        self.next_id += 1
        return wolf
    
    def wolf_attack_sheep(self, wolf_id: int, sheep_id: int) -> bool:
        """
        A Wolf attempts to capture a Sheep.
        Returns True if successful, False otherwise.
        """
        if wolf_id not in self.wolves or sheep_id not in self.sheep:
            return False
        
        wolf = self.wolves[wolf_id]
        sheep = self.sheep[sheep_id]
        
        # Base success chance is 50%, modified by wolf strength
        success_chance = 0.5 + (wolf.strength / 100)
        success_chance = min(max(success_chance, 0.1), 0.9)  # Clamp between 10% and 90%
        
        if random.random() < success_chance:
            wolf.captured_sheep.append(sheep)
            del self.sheep[sheep_id]
            return True
        return False
    
    def wolf_steal_from_farmer(self, wolf_id: int, farmer_id: int) -> Dict[str, int]:
        """
        A Wolf attempts to steal resources from a Farmer.
        Returns the stolen resources.
        """
        if wolf_id not in self.wolves or farmer_id not in self.farmers:
            return {}
        
        wolf = self.wolves[wolf_id]
        farmer = self.farmers[farmer_id]
        
        stolen = {}
        for resource, amount in farmer.resources.items():
            # Wolf can steal up to 50% of each resource
            steal_amount = max(1, int(amount * 0.5 * (wolf.strength / 10)))
            steal_amount = min(steal_amount, amount)
            
            stolen[resource] = steal_amount
            farmer.resources[resource] -= steal_amount
            wolf.stolen_resources[resource] += steal_amount
        
        return stolen
    
    def get_wolf_stats(self, wolf_id: int) -> Optional[Dict[str, int]]:
        """Get statistics for a specific Wolf."""
        if wolf_id not in self.wolves:
            return None
        
        wolf = self.wolves[wolf_id]
        return {
            "wolf_id": wolf.wolf_id,
            "strength": wolf.strength,
            "captured_sheep": len(wolf.captured_sheep),
            "stolen_resources": wolf.stolen_resources
        }
    
    def get_all_wolf_stats(self) -> List[Dict[str, int]]:
        """Get statistics for all Wolves."""
        return [self.get_wolf_stats(wolf_id) for wolf_id in self.wolves]

# Example usage
if __name__ == "__main__":
    game = WolfGame()
    
    # Add some entities
    for _ in range(5):
        game.add_sheep(wool=random.randint(1, 10))
    
    for _ in range(3):
        game.add_farmer({"wheat": random.randint(10, 50), "wood": random.randint(5, 30)})
    
    wolf1 = game.add_wolf(strength=15)
    wolf2 = game.add_wolf(strength=8)
    
    # Simulate some attacks
    for sheep_id in list(game.sheep.keys()):
        game.wolf_attack_sheep(wolf1.wolf_id, sheep_id)
    
    for farmer_id in game.farmers:
        game.wolf_steal_from_farmer(wolf2.wolf_id, farmer_id)
    
    # Print results
    print("Wolf 1 stats:", game.get_wolf_stats(wolf1.wolf_id))
    print("Wolf 2 stats:", game.get_wolf_stats(wolf2.wolf_id))
```
