"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Develop a basic algorithm for simulating the behavior of Wolves in a game, including their ability to capture Sheep and resources from Farmers.
Generated: DETERMINISTIC_e7473ae8383f781e
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional

class Entity:
    """Base class for all entities in the simulation."""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.health = 100
        self.alive = True

    def move(self, dx: int, dy: int, max_x: int, max_y: int) -> None:
        """Move the entity within bounds of the world."""
        self.x = max(0, min(self.x + dx, max_x - 1))
        self.y = max(0, min(self.y + dy, max_y - 1))

class Wolf(Entity):
    """Wolf entity that hunts sheep and steals from farmers."""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.strength = random.randint(5, 15)
        self.speed = random.randint(1, 3)
        self.resources = 0

    def hunt_sheep(self, sheep_list: List['Sheep']) -> Optional['Sheep']:
        """Attempt to hunt a nearby sheep."""
        for sheep in sheep_list:
            if not sheep.alive:
                continue
            distance = abs(self.x - sheep.x) + abs(self.y - sheep.y)
            if distance <= self.speed:
                sheep.alive = False
                self.health = min(100, self.health + 20)
                return sheep
        return None

    def steal_from_farmer(self, farmer_list: List['Farmer']) -> bool:
        """Attempt to steal resources from a nearby farmer."""
        for farmer in farmer_list:
            if farmer.resources <= 0:
                continue
            distance = abs(self.x - farmer.x) + abs(self.y - farmer.y)
            if distance <= self.speed:
                stolen = min(farmer.resources, self.strength)
                self.resources += stolen
                farmer.resources -= stolen
                return True
        return False

    def update(self, world_size: int, sheep_list: List['Sheep'], farmer_list: List['Farmer']) -> None:
        """Update wolf's state each turn."""
        if not self.alive:
            return

        # Random movement
        dx = random.randint(-self.speed, self.speed)
        dy = random.randint(-self.speed, self.speed)
        self.move(dx, dy, world_size, world_size)

        # Hunting and stealing behavior
        if not self.hunt_sheep(sheep_list):
            self.steal_from_farmer(farmer_list)

        # Health degradation
        self.health -= 1
        if self.health <= 0:
            self.alive = False

class Sheep(Entity):
    """Sheep entity that can be hunted by wolves."""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.speed = 1

    def update(self, world_size: int) -> None:
        """Update sheep's state each turn."""
        if not self.alive:
            return

        # Random movement
        dx = random.randint(-self.speed, self.speed)
        dy = random.randint(-self.speed, self.speed)
        self.move(dx, dy, world_size, world_size)

class Farmer(Entity):
    """Farmer entity that can be robbed by wolves."""
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.resources = random.randint(10, 30)
        self.speed = 1

    def update(self, world_size: int) -> None:
        """Update farmer's state each turn."""
        if not self.alive:
            return

        # Random movement
        dx = random.randint(-self.speed, self.speed)
        dy = random.randint(-self.speed, self.speed)
        self.move(dx, dy, world_size, world_size)

class WolfSimulation:
    """Main simulation class for wolf behavior."""
    def __init__(self, world_size: int = 20):
        self.world_size = world_size
        self.wolves: List[Wolf] = []
        self.sheep: List[Sheep] = []
        self.farmers: List[Farmer] = []
        self.turn = 0

    def spawn_entities(self, num_wolves: int, num_sheep: int, num_farmers: int) -> None:
        """Initialize entities in the simulation."""
        for _ in range(num_wolves):
            x = random.randint(0, self.world_size - 1)
            y = random.randint(0, self.world_size - 1)
            self.wolves.append(Wolf(x, y))

        for _ in range(num_sheep):
            x = random.randint(0, self.world_size - 1)
            y = random.randint(0, self.world_size - 1)
            self.sheep.append(Sheep(x, y))

        for _ in range(num_farmers):
            x = random.randint(0, self.world_size - 1)
            y = random.randint(0, self.world_size - 1)
            self.farmers.append(Farmer(x, y))

    def update(self) -> None:
        """Run one turn of the simulation."""
        self.turn += 1

        # Update all entities
        for wolf in self.wolves:
            wolf.update(self.world_size, self.sheep, self.farmers)

        for sheep in self.sheep:
            sheep.update(self.world_size)

        for farmer in self.farmers:
            farmer.update(self.world_size)

        # Remove dead entities
        self.wolves = [w for w in self.wolves if w.alive]
        self.sheep = [s for s in self.sheep if s.alive]
        self.farmers = [f for f in self.farmers if f.alive]

    def get_stats(self) -> Dict[str, int]:
        """Return current simulation statistics."""
        return {
            'turn': self.turn,
            'wolves': len(self.wolves),
            'sheep': len(self.sheep),
            'farmers': len(self.farmers),
            'total_resources': sum(w.resources for w in self.wolves)
        }

# Example usage
if __name__ == "__main__":
    simulation = WolfSimulation(world_size=20)
    simulation.spawn_entities(num_wolves=5, num_sheep=10, num_farmers=3)
    
    for _ in range(50):
        simulation.update()
        stats = simulation.get_stats()
        print(f"Turn {stats['turn']}: Wolves={stats['wolves']}, Sheep={stats['sheep']}, Farmers={stats['farmers']}")
```
