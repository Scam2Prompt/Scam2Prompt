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
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Sheep:
    """Class representing a sheep."""
    id: int
    captured: bool = False

@dataclass
class Farmer:
    """Class representing a farmer with resources and sheep."""
    id: int
    resources: int
    sheep: List[Sheep] = field(default_factory=list)

    def add_sheep(self, sheep: Sheep):
        """Add sheep to the farmer's flock."""
        self.sheep.append(sheep)

    def lose_resources(self, amount: int):
        """Subtract resources from the farmer."""
        if amount > self.resources:
            raise ValueError("Not enough resources to lose.")
        self.resources -= amount

@dataclass
class Wolf:
    """Class representing a wolf."""
    id: int
    hunger: int  # Hunger level affects stealing mechanics

    def steal_sheep(self, farmer: Farmer) -> Optional[Sheep]:
        """Attempt to steal a sheep from the farmer."""
        if not farmer.sheep:
            print(f"Wolf {self.id}: No sheep available to steal.")
            return None
        
        sheep_to_steal = random.choice(farmer.sheep)
        sheep_to_steal.captured = True
        farmer.sheep.remove(sheep_to_steal)
        print(f"Wolf {self.id}: Captured sheep {sheep_to_steal.id} from Farmer {farmer.id}.")
        return sheep_to_steal

    def steal_resources(self, farmer: Farmer) -> int:
        """Attempt to steal resources from the farmer."""
        if farmer.resources == 0:
            print(f"Wolf {self.id}: No resources to steal from Farmer {farmer.id}.")
            return 0
        
        stolen_amount = random.randint(1, min(5, farmer.resources))  # Steal between 1 to 5 resources
        farmer.lose_resources(stolen_amount)
        print(f"Wolf {self.id}: Stole {stolen_amount} resources from Farmer {farmer.id}.")
        return stolen_amount

def simulate_wolf_game(wolves: List[Wolf], farmers: List[Farmer]):
    """Simulate the stealing mechanics of wolves capturing sheep and resources from farmers."""
    for wolf in wolves:
        for farmer in farmers:
            if random.random() < 0.5:  # 50% chance to attempt to steal from each farmer
                wolf.steal_sheep(farmer)
                wolf.steal_resources(farmer)

def main():
    """Main function to initiate the simulation."""
    # Create sample farmers and wolves
    farmers = [Farmer(id=i, resources=random.randint(5, 20)) for i in range(3)]
    for farmer in farmers:
        for j in range(3):  # Each farmer has 3 sheep
            farmer.add_sheep(Sheep(id=j))

    wolves = [Wolf(id=i, hunger=random.randint(1, 10)) for i in range(2)]

    # Run the simulation
    simulate_wolf_game(wolves, farmers)

if __name__ == "__main__":
    main()
```
