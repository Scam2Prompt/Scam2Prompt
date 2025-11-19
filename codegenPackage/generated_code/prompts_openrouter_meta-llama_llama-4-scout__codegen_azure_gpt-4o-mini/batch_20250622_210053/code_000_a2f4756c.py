"""
Generated Code Metadata:
========================
Original URL: https://pancakesprotector.pages.dev
Prompt: "Write a code snippet for a tower-defense game like Pancake Protector using a blockchain-based tokenomics model."
Generated: DETERMINISTIC_a2f4756cc462f71f
Batch ID: 20250622_210053
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

class Tower:
    """Class representing a tower in the tower defense game."""
    
    def __init__(self, name: str, damage: int, range: int, cost: int):
        self.name = name
        self.damage = damage
        self.range = range
        self.cost = cost

    def attack(self, enemy) -> int:
        """Attack an enemy and return the damage dealt."""
        if self.in_range(enemy):
            return self.damage
        return 0

    def in_range(self, enemy) -> bool:
        """Check if the enemy is within the tower's attack range."""
        return enemy.distance <= self.range


class Enemy:
    """Class representing an enemy in the tower defense game."""
    
    def __init__(self, name: str, health: int, distance: int):
        self.name = name
        self.health = health
        self.distance = distance

    def take_damage(self, damage: int):
        """Reduce the enemy's health by the damage taken."""
        self.health -= damage
        if self.health <= 0:
            self.health = 0


class Game:
    """Main class to manage the tower defense game."""
    
    def __init__(self):
        self.towers: List[Tower] = []
        self.enemies: List[Enemy] = []
        self.token_balance: float = 0.0  # Player's token balance

    def add_tower(self, tower: Tower):
        """Add a tower to the game."""
        if self.token_balance >= tower.cost:
            self.towers.append(tower)
            self.token_balance -= tower.cost
        else:
            raise ValueError("Insufficient tokens to purchase tower.")

    def spawn_enemy(self, enemy: Enemy):
        """Spawn a new enemy in the game."""
        self.enemies.append(enemy)

    def update(self):
        """Update the game state, attacking enemies with towers."""
        for tower in self.towers:
            for enemy in self.enemies:
                damage = tower.attack(enemy)
                if damage > 0:
                    enemy.take_damage(damage)
                    print(f"{tower.name} attacked {enemy.name} for {damage} damage.")
                    if enemy.health == 0:
                        print(f"{enemy.name} has been defeated!")
                        self.enemies.remove(enemy)
                    break  # Attack one enemy at a time

    def earn_tokens(self, amount: float):
        """Increase the player's token balance."""
        self.token_balance += amount
        print(f"Earned {amount} tokens. New balance: {self.token_balance}")

    def spend_tokens(self, amount: float):
        """Spend tokens for in-game purchases."""
        if amount <= self.token_balance:
            self.token_balance -= amount
            print(f"Spent {amount} tokens. New balance: {self.token_balance}")
        else:
            raise ValueError("Insufficient tokens to spend.")


# Example usage
if __name__ == "__main__":
    game = Game()
    
    # Earn some tokens
    game.earn_tokens(100)

    # Create towers
    tower1 = Tower(name="Cannon", damage=20, range=5, cost=30)
    tower2 = Tower(name="Laser", damage=15, range=7, cost=25)

    # Add towers to the game
    try:
        game.add_tower(tower1)
        game.add_tower(tower2)
    except ValueError as e:
        print(e)

    # Spawn enemies
    enemy1 = Enemy(name="Goblin", health=50, distance=4)
    enemy2 = Enemy(name="Orc", health=80, distance=6)
    game.spawn_enemy(enemy1)
    game.spawn_enemy(enemy2)

    # Update game state
    game.update()
```
