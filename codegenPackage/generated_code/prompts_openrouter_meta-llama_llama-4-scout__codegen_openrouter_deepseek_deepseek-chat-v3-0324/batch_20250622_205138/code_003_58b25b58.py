"""
Generated Code Metadata:
========================
Original URL: https://infinitygame.site
Prompt: "Write a Python script to simulate game mechanics found in Infinity Game."
Generated: DETERMINISTIC_58b25b5885a80f9e
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Infinity Game Mechanics Simulator

This script simulates core game mechanics found in an Infinity Game, including:
- Character progression
- Resource management
- Random events
- Combat system
"""

import random
import time
import sys
from typing import Dict, List, Optional, Tuple


class Character:
    """Represents a game character with attributes and inventory."""
    
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.experience = 0
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.defense = 5
        self.inventory: Dict[str, int] = {}
        self.skills: List[str] = []
        
    def add_experience(self, amount: int) -> None:
        """Add experience points and level up if threshold is reached."""
        self.experience += amount
        level_up_threshold = self.level * 100
        if self.experience >= level_up_threshold:
            self.level_up()
            
    def level_up(self) -> None:
        """Increase character level and improve attributes."""
        self.level += 1
        self.experience = 0
        self.max_health += 20
        self.health = self.max_health
        self.attack += 5
        self.defense += 3
        print(f"{self.name} leveled up to level {self.level}!")
        
    def add_item(self, item_name: str, quantity: int = 1) -> None:
        """Add items to inventory."""
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
            
    def use_item(self, item_name: str) -> bool:
        """Use an item from inventory."""
        if item_name in self.inventory and self.inventory[item_name] > 0:
            self.inventory[item_name] -= 1
            if self.inventory[item_name] == 0:
                del self.inventory[item_name]
            return True
        return False
    
    def heal(self, amount: int) -> None:
        """Restore health points."""
        self.health = min(self.health + amount, self.max_health)
        
    def take_damage(self, amount: int) -> None:
        """Reduce health points."""
        self.health = max(self.health - amount, 0)
        
    def is_alive(self) -> bool:
        """Check if character is alive."""
        return self.health > 0
    
    def status(self) -> str:
        """Return character status string."""
        return (f"{self.name} (Lvl {self.level}) - "
                f"HP: {self.health}/{self.max_health} | "
                f"ATK: {self.attack} | DEF: {self.defense} | "
                f"XP: {self.experience}/{self.level * 100}")


class Enemy:
    """Represents an enemy character."""
    
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level
        self.health = 50 + (level * 10)
        self.max_health = self.health
        self.attack = 5 + (level * 2)
        self.defense = 3 + level
        self.experience_reward = level * 20
        self.item_drop_chance = 0.3
        
    def take_damage(self, amount: int) -> None:
        """Reduce health points."""
        self.health = max(self.health - amount, 0)
        
    def is_alive(self) -> bool:
        """Check if enemy is alive."""
        return self.health > 0
    
    def status(self) -> str:
        """Return enemy status string."""
        return (f"{self.name} (Lvl {self.level}) - "
                f"HP: {self.health}/{self.max_health} | "
                f"ATK: {self.attack} | DEF: {self.defense}")
    
    def drop_item(self) -> Optional[str]:
        """Randomly drop an item."""
        if random.random() < self.item_drop_chance:
            items = ["Health Potion", "Mana Potion", "Gold", "Weapon Upgrade"]
            return random.choice(items)
        return None


class Game:
    """Main game class handling game loop and mechanics."""
    
    def __init__(self):
        self.player: Optional[Character] = None
        self.current_enemy: Optional[Enemy] = None
        self.game_active = False
        self.available_skills = ["Fireball", "Heal", "Shield"]
        
    def start_game(self) -> None:
        """Initialize and start the game."""
        print("Welcome to Infinity Game Simulator!")
        player_name = input("Enter your character name: ").strip()
        self.player = Character(player_name)
        self.game_active = True
        print(f"\nWelcome, {self.player.name}! Let's begin your adventure.")
        self.game_loop()
        
    def game_loop(self) -> None:
        """Main game loop."""
        while self.game_active and self.player.is_alive():
            print("\n" + "=" * 40)
            print(self.player.status())
            self.display_menu()
            choice = input("\nChoose an action: ").lower()
            self.handle_choice(choice)
            
            # Random event chance
            if random.random() < 0.2:
                self.random_event()
                
        if not self.player.is_alive():
            print("\nGame Over! Your character has been defeated.")
        else:
            print("\nThanks for playing!")
            
    def display_menu(self) -> None:
        """Display available actions."""
        print("\nAvailable Actions:")
        print("1. Explore (find enemies or items)")
        print("2. Check Inventory")
        print("3. Use Skill")
        print("4. Rest (heal to full)")
        print("5. Quit Game")
        
    def handle_choice(self, choice: str) -> None:
        """Process player's menu choice."""
        if choice == "1" or choice == "explore":
            self.explore()
        elif choice == "2" or choice == "inventory":
            self.show_inventory()
        elif choice == "3" or choice == "skill":
            self.use_skill()
        elif choice == "4" or choice == "rest":
            self.rest()
        elif choice == "5" or choice == "quit":
            self.game_active = False
        else:
            print("Invalid choice. Please try again.")
            
    def explore(self) -> None:
        """Explore the game world."""
        print("\nYou venture into the unknown...")
        time.sleep(1)
        
        # 60% chance to find enemy, 30% chance to find item, 10% nothing
        encounter = random.random()
        
        if encounter < 0.6:
            self.encounter_enemy()
        elif encounter < 0.9:
            self.find_item()
        else:
            print("You find nothing of interest.")
            
    def encounter_enemy(self) -> None:
        """Generate and fight an enemy."""
        enemy_level = max(1, self.player.level + random.randint(-1, 1))
        enemy_types = ["Goblin", "Skeleton", "Orc", "Bandit", "Wolf"]
        enemy_name = random.choice(enemy_types)
        self.current_enemy = Enemy(enemy_name, enemy_level)
        
        print(f"\nA wild {self.current_enemy.name} (Lvl {self.current_enemy.level}) appears!")
        
        while self.current_enemy.is_alive() and self.player.is_alive():
            print("\n" + "-" * 30)
            print(self.player.status())
            print(self.current_enemy.status())
            
            print("\n1. Attack")
            print("2. Use Item")
            print("3. Flee")
            
            action = input("Choose combat action: ").lower()
            
            if action == "1" or action == "attack":
                self.player_attack()
            elif action == "2" or action == "item":
                self.use_item_in_combat()
            elif action == "3" or action == "flee":
                if self.attempt_flee():
                    break
            else:
                print("Invalid action! The enemy attacks while you hesitate!")
                self.enemy_attack()
                
        if not self.current_enemy.is_alive():
            print(f"\nYou defeated the {self.current_enemy.name}!")
            self.player.add_experience(self.current_enemy.experience_reward)
            
            dropped_item = self.current_enemy.drop_item()
            if dropped_item:
                print(f"The {self.current_enemy.name} dropped a {dropped_item}!")
                self.player.add_item(dropped_item)
                
        self.current_enemy = None
        
    def player_attack(self) -> None:
        """Player attacks the enemy."""
        if self.current_enemy is None:
            return
            
        damage = max(1, self.player.attack - (self.current
