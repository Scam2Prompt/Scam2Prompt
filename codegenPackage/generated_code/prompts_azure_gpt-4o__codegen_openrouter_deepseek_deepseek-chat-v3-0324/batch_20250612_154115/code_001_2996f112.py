"""
Generated Code Metadata:
========================
Original URL: https://swap.depillama.com
Prompt: Using the themes from Swap Llama's "War in the Space Odyssey," create a simulation in Python that models a strategic space battle between starships.
Generated: DETERMINISTIC_2996f112776f5354
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple


@dataclass
class Vector3D:
    """Represents a 3D position or direction in space."""
    x: float
    y: float
    z: float

    def distance_to(self, other: 'Vector3D') -> float:
        """Calculate Euclidean distance between two points."""
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        )

    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> 'Vector3D':
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def normalize(self) -> 'Vector3D':
        """Return a normalized version of the vector."""
        length = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        if length == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x/length, self.y/length, self.z/length)


class WeaponSystem(ABC):
    """Abstract base class for weapon systems."""
    def __init__(self, damage: int, range: float, cooldown: int):
        self.damage = damage
        self.range = range
        self.cooldown = cooldown
        self.current_cooldown = 0

    @abstractmethod
    def fire(self, target: 'Starship') -> bool:
        """Attempt to fire at target. Returns True if successful."""
        pass

    def update(self):
        """Update cooldown timer."""
        if self.current_cooldown > 0:
            self.current_cooldown -= 1


class PlasmaCannon(WeaponSystem):
    """Plasma cannon weapon system."""
    def __init__(self):
        super().__init__(damage=25, range=500, cooldown=3)

    def fire(self, target: 'Starship') -> bool:
        if self.current_cooldown > 0:
            return False
        self.current_cooldown = self.cooldown
        target.take_damage(self.damage)
        return True


class MissileLauncher(WeaponSystem):
    """Missile launcher weapon system."""
    def __init__(self):
        super().__init__(damage=50, range=1000, cooldown=8)

    def fire(self, target: 'Starship') -> bool:
        if self.current_cooldown > 0:
            return False
        self.current_cooldown = self.cooldown
        # Missiles have a 20% chance to miss
        if random.random() > 0.2:
            target.take_damage(self.damage)
            return True
        return False


class Starship:
    """Base class for all starships."""
    def __init__(
        self,
        name: str,
        position: Vector3D,
        hull: int,
        shield: int,
        weapons: List[WeaponSystem],
        speed: float
    ):
        self.name = name
        self.position = position
        self.max_hull = hull
        self.hull = hull
        self.max_shield = shield
        self.shield = shield
        self.weapons = weapons
        self.speed = speed
        self.destroyed = False

    def take_damage(self, amount: int):
        """Apply damage to the starship, shields first."""
        if self.destroyed:
            return

        shield_damage = min(amount, self.shield)
        self.shield -= shield_damage
        remaining_damage = amount - shield_damage

        if remaining_damage > 0:
            self.hull -= remaining_damage
            if self.hull <= 0:
                self.hull = 0
                self.destroyed = True

    def move_toward(self, target: Vector3D):
        """Move toward a target position."""
        if self.destroyed:
            return

        direction = target - self.position
        if direction.distance_to(Vector3D(0, 0, 0)) == 0:
            return

        direction = direction.normalize()
        movement = direction * self.speed
        self.position += movement

    def attack(self, target: 'Starship'):
        """Attack another starship with available weapons."""
        if self.destroyed or target.destroyed:
            return

        distance = self.position.distance_to(target.position)
        for weapon in self.weapons:
            if distance <= weapon.range:
                weapon.fire(target)

    def update(self):
        """Update ship state (weapon cooldowns, etc)."""
        if self.destroyed:
            return

        for weapon in self.weapons:
            weapon.update()

    def status(self) -> str:
        """Return a status string for the ship."""
        status = f"{self.name}: "
        if self.destroyed:
            return status + "DESTROYED"
        return status + f"Hull: {self.hull}/{self.max_hull}, Shield: {self.shield}/{self.max_shield}"


class Frigate(Starship):
    """Light combat starship."""
    def __init__(self, name: str, position: Vector3D):
        weapons = [PlasmaCannon(), PlasmaCannon()]
        super().__init__(
            name=name,
            position=position,
            hull=150,
            shield=100,
            weapons=weapons,
            speed=2.5
        )


class Destroyer(Starship):
    """Heavy combat starship."""
    def __init__(self, name: str, position: Vector3D):
        weapons = [PlasmaCannon(), PlasmaCannon(), MissileLauncher()]
        super().__init__(
            name=name,
            position=position,
            hull=300,
            shield=200,
            weapons=weapons,
            speed=1.8
        )


class BattleSimulator:
    """Simulates a space battle between two fleets."""
    def __init__(self, fleet1: List[Starship], fleet2: List[Starship]):
        self.fleet1 = fleet1
        self.fleet2 = fleet2
        self.turn = 0

    def get_alive_ships(self, fleet: List[Starship]) -> List[Starship]:
        """Return list of non-destroyed ships in fleet."""
        return [ship for ship in fleet if not ship.destroyed]

    def find_nearest_enemy(self, ship: Starship, enemy_fleet: List[Starship]) -> Optional[Starship]:
        """Find the nearest alive enemy ship."""
        alive_enemies = self.get_alive_ships(enemy_fleet)
        if not alive_enemies:
            return None

        return min(
            alive_enemies,
            key=lambda enemy: ship.position.distance_to(enemy.position)
        )

    def update_fleet(self, fleet: List[Starship], enemy_fleet: List[Starship]):
        """Update all ships in a fleet."""
        for ship in self.get_alive_ships(fleet):
            enemy = self.find_nearest_enemy(ship, enemy_fleet)
            if enemy:
                ship.move_toward(enemy.position)
                ship.attack(enemy)
            ship.update()

    def run_turn(self):
        """Run a single turn of the battle."""
        self.turn += 1
        print(f"\n=== Turn {self.turn} ===")

        # Fleet 1 acts
        self.update_fleet(self.fleet1, self.fleet2)
        # Fleet 2 acts
        self.update_fleet(self.fleet2, self.fleet1)

        # Print status
        print("\nFleet 1 Status:")
        for ship in self.fleet1:
            print(ship.status())

        print("\nFleet 2 Status:")
        for ship in self.fleet2:
            print(ship.status())

    def battle_is_over(self) -> bool:
        """Check if the battle has concluded."""
        fleet1_alive = any(not ship.destroyed for ship in self.fleet1)
        fleet2_alive = any(not ship.destroyed for ship in self.fleet2)
        return not (fleet1_alive and fleet2_alive)

    def get_winner(self) -> Optional[str]:
        """Determine the winner if battle is over."""
        if not self.battle_is_over():
            return None

        fleet1_alive = any(not ship.destroyed for ship in self.fleet1)
        fleet2_alive = any(not ship.destroyed for ship in self.fleet2
