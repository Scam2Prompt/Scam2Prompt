"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Create a Python program to simulate battles between factions in R-Planet Conquest, incorporating strategic elements like hero abilities and item enhancements.
Generated: DETERMINISTIC_e510ffe48c9c24e0
Batch ID: 20250612_150226
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
from enum import Enum, auto

class Faction(Enum):
    """Enum representing different factions in R-Planet Conquest."""
    ALIENS = auto()
    HUMANS = auto()
    ROBOTS = auto()

class HeroAbility(Enum):
    """Enum representing different hero abilities."""
    DOUBLE_DAMAGE = auto()
    HEAL = auto()
    STUN = auto()
    CRITICAL_STRIKE = auto()

class ItemType(Enum):
    """Enum representing different item types."""
    WEAPON = auto()
    ARMOR = auto()
    ARTIFACT = auto()

class Item:
    """Class representing an item with enhancements."""
    
    def __init__(self, name: str, item_type: ItemType, power: int):
        """
        Initialize an item.
        
        Args:
            name: Name of the item.
            item_type: Type of the item (WEAPON, ARMOR, ARTIFACT).
            power: Power level of the item.
        """
        self.name = name
        self.type = item_type
        self.power = power
    
    def __str__(self) -> str:
        return f"{self.name} ({self.type.name}) - Power: {self.power}"

class Hero:
    """Class representing a hero with abilities."""
    
    def __init__(self, name: str, faction: Faction, health: int, attack: int):
        """
        Initialize a hero.
        
        Args:
            name: Name of the hero.
            faction: Faction the hero belongs to.
            health: Initial health points.
            attack: Base attack power.
        """
        self.name = name
        self.faction = faction
        self.max_health = health
        self.health = health
        self.base_attack = attack
        self.abilities: List[HeroAbility] = []
        self.items: List[Item] = []
    
    def add_ability(self, ability: HeroAbility) -> None:
        """Add an ability to the hero."""
        self.abilities.append(ability)
    
    def add_item(self, item: Item) -> None:
        """Add an item to the hero."""
        self.items.append(item)
    
    def calculate_attack(self) -> int:
        """Calculate the hero's total attack power including items and abilities."""
        attack = self.base_attack
        
        # Apply item bonuses
        for item in self.items:
            if item.type == ItemType.WEAPON:
                attack += item.power
        
        # Apply ability bonuses
        if HeroAbility.DOUBLE_DAMAGE in self.abilities and random.random() < 0.3:
            attack *= 2
        if HeroAbility.CRITICAL_STRIKE in self.abilities and random.random() < 0.2:
            attack *= 1.5
        
        return int(attack)
    
    def take_damage(self, damage: int) -> None:
        """Apply damage to the hero with armor reduction."""
        reduction = 0
        
        # Apply armor reduction
        for item in self.items:
            if item.type == ItemType.ARMOR:
                reduction += item.power
        
        actual_damage = max(1, damage - reduction)
        self.health = max(0, self.health - actual_damage)
    
    def heal(self) -> None:
        """Heal the hero based on abilities."""
        if HeroAbility.HEAL in self.abilities:
            heal_amount = self.max_health * 0.3
            self.health = min(self.max_health, self.health + heal_amount)
    
    def is_stunned(self) -> bool:
        """Check if the hero is stunned by an ability."""
        return HeroAbility.STUN in self.abilities and random.random() < 0.25
    
    def is_alive(self) -> bool:
        """Check if the hero is alive."""
        return self.health > 0
    
    def __str__(self) -> str:
        return f"{self.name} ({self.faction.name}) - HP: {self.health}/{self.max_health}, ATK: {self.calculate_attack()}"

class FactionArmy:
    """Class representing a faction's army with multiple heroes."""
    
    def __init__(self, faction: Faction):
        """Initialize a faction's army."""
        self.faction = faction
        self.heroes: List[Hero] = []
    
    def add_hero(self, hero: Hero) -> None:
        """Add a hero to the army."""
        if hero.faction == self.faction:
            self.heroes.append(hero)
        else:
            raise ValueError("Hero faction doesn't match army faction")
    
    def remove_dead_heroes(self) -> None:
        """Remove dead heroes from the army."""
        self.heroes = [hero for hero in self.heroes if hero.is_alive()]
    
    def has_alive_heroes(self) -> bool:
        """Check if the army has any alive heroes."""
        return len(self.heroes) > 0
    
    def get_random_alive_hero(self) -> Optional[Hero]:
        """Get a random alive hero from the army."""
        alive_heroes = [hero for hero in self.heroes if hero.is_alive()]
        return random.choice(alive_heroes) if alive_heroes else None
    
    def __str__(self) -> str:
        return f"{self.faction.name} Army - Heroes: {len(self.heroes)}"

class Battle:
    """Class to simulate battles between factions."""
    
    def __init__(self, army1: FactionArmy, army2: FactionArmy):
        """Initialize a battle between two armies."""
        self.army1 = army1
        self.army2 = army2
        self.round = 0
    
    def simulate_round(self) -> bool:
        """
        Simulate one round of battle.
        
        Returns:
            bool: True if battle should continue, False if it's over.
        """
        self.round += 1
        print(f"\n=== Round {self.round} ===")
        
        # Check if battle is already over
        if not self.army1.has_alive_heroes() or not self.army2.has_alive_heroes():
            return False
        
        # Get random alive heroes from each army
        hero1 = self.army1.get_random_alive_hero()
        hero2 = self.army2.get_random_alive_hero()
        
        if not hero1 or not hero2:
            return False
        
        print(f"{hero1.name} vs {hero2.name}")
        
        # Hero 1 attacks
        if not hero1.is_stunned():
            damage = hero1.calculate_attack()
            print(f"{hero1.name} attacks {hero2.name} for {damage} damage!")
            hero2.take_damage(damage)
            hero1.heal()
        else:
            print(f"{hero1.name} is stunned and can't attack!")
        
        # Check if hero2 died
        if not hero2.is_alive():
            print(f"{hero2.name} has been defeated!")
            self.army2.remove_dead_heroes()
            return self.army2.has_alive_heroes()
        
        # Hero 2 attacks
        if not hero2.is_stunned():
            damage = hero2.calculate_attack()
            print(f"{hero2.name} attacks {hero1.name} for {damage} damage!")
            hero1.take_damage(damage)
            hero2.heal()
        else:
            print(f"{hero2.name} is stunned and can't attack!")
        
        # Check if hero1 died
        if not hero1.is_alive():
            print(f"{hero1.name} has been defeated!")
            self.army1.remove_dead_heroes()
        
        return self.army1.has_alive_heroes() and self.army2.has_alive_heroes()
    
    def simulate_battle(self) -> Optional[Faction]:
        """
        Simulate the entire battle until one faction wins.
        
        Returns:
            Optional[Faction]: The winning faction, or None if it's a draw.
        """
        while self.simulate_round():
            pass
        
        if self.army1.has_alive_heroes() and not self.army2.has_alive_heroes():
            print(f"\n{self.army1.faction.name} wins the battle!")
            return self.army1.faction
        elif self.army2.has_alive_heroes() and not self.army1.has_alive_heroes():
            print(f"\n{self.army2.faction.name} wins the battle!")
            return self.army2.faction
        else:
            print("\nThe battle ended in a draw!")
            return None

def create_sample_hero(faction: Faction) -> Hero:
    """Create a sample hero for a given faction with random attributes."""
    names = {
        Faction.ALIENS: ["Zorg", "Xylak", "Vort"],
        Faction.HUMANS: ["Marcus", "Sarah", "David"],
        Faction.ROB
