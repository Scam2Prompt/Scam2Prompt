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
# r_planet_conquest.py

import random
from enum import Enum
from typing import List, Dict

class Faction(Enum):
    """Enum for factions in R-Planet Conquest."""
    AETHERIUM = 1
    KYRENIUM = 2
    N'TARI = 3
    ZORVATH = 4

class Hero:
    """Class representing a hero in R-Planet Conquest."""
    def __init__(self, name: str, faction: Faction, health: int, damage: int):
        """
        Initialize a hero.

        Args:
        - name (str): Hero's name.
        - faction (Faction): Hero's faction.
        - health (int): Hero's health.
        - damage (int): Hero's damage.
        """
        self.name = name
        self.faction = faction
        self.health = health
        self.damage = damage
        self.abilities = []

    def add_ability(self, ability: str):
        """Add an ability to the hero."""
        self.abilities.append(ability)

    def is_alive(self) -> bool:
        """Check if the hero is alive."""
        return self.health > 0

class Item:
    """Class representing an item in R-Planet Conquest."""
    def __init__(self, name: str, damage_bonus: int, health_bonus: int):
        """
        Initialize an item.

        Args:
        - name (str): Item's name.
        - damage_bonus (int): Item's damage bonus.
        - health_bonus (int): Item's health bonus.
        """
        self.name = name
        self.damage_bonus = damage_bonus
        self.health_bonus = health_bonus

class BattleSimulator:
    """Class simulating battles between factions in R-Planet Conquest."""
    def __init__(self):
        self.heroes: Dict[Faction, List[Hero]] = {
            Faction.AETHERIUM: [],
            Faction.KYRENIUM: [],
            Faction.N'TARI: [],
            Faction.ZORVATH: []
        }
        self.items: Dict[str, Item] = {}

    def add_hero(self, hero: Hero):
        """Add a hero to the simulator."""
        self.heroes[hero.faction].append(hero)

    def add_item(self, item: Item):
        """Add an item to the simulator."""
        self.items[item.name] = item

    def equip_item(self, hero: Hero, item_name: str):
        """Equip an item to a hero."""
        if item_name in self.items:
            item = self.items[item_name]
            hero.damage += item.damage_bonus
            hero.health += item.health_bonus
        else:
            print(f"Item '{item_name}' not found.")

    def simulate_battle(self, faction1: Faction, faction2: Faction):
        """Simulate a battle between two factions."""
        heroes1 = self.heroes[faction1]
        heroes2 = self.heroes[faction2]

        while heroes1 and heroes2:
            hero1 = random.choice(heroes1)
            hero2 = random.choice(heroes2)

            if hero1.is_alive() and hero2.is_alive():
                damage1 = hero1.damage
                damage2 = hero2.damage

                # Apply hero abilities
                if hero1.abilities:
                    ability = random.choice(hero1.abilities)
                    if ability == "heal":
                        hero1.health += 10
                        print(f"{hero1.name} used heal ability.")
                    elif ability == "boost":
                        damage1 *= 1.2
                        print(f"{hero1.name} used boost ability.")

                if hero2.abilities:
                    ability = random.choice(hero2.abilities)
                    if ability == "heal":
                        hero2.health += 10
                        print(f"{hero2.name} used heal ability.")
                    elif ability == "boost":
                        damage2 *= 1.2
                        print(f"{hero2.name} used boost ability.")

                # Apply damage
                hero2.health -= damage1
                hero1.health -= damage2

                print(f"{hero1.name} ({faction1.name}) attacks {hero2.name} ({faction2.name}) for {damage1} damage.")
                print(f"{hero2.name} ({faction2.name}) attacks {hero1.name} ({faction1.name}) for {damage2} damage.")

                # Check if heroes are still alive
                if not hero1.is_alive():
                    heroes1.remove(hero1)
                    print(f"{hero1.name} ({faction1.name}) died.")
                if not hero2.is_alive():
                    heroes2.remove(hero2)
                    print(f"{hero2.name} ({faction2.name}) died.")
            else:
                if not hero1.is_alive():
                    heroes1.remove(hero1)
                if not hero2.is_alive():
                    heroes2.remove(hero2)

        if heroes1:
            print(f"{faction1.name} wins!")
        else:
            print(f"{faction2.name} wins!")

def main():
    simulator = BattleSimulator()

    # Create heroes
    hero1 = Hero("Eryndor Thorne", Faction.AETHERIUM, 100, 20)
    hero1.add_ability("heal")
    hero2 = Hero("Kaelith Sunshadow", Faction.KYRENIUM, 120, 15)
    hero2.add_ability("boost")

    # Create items
    item1 = Item("Sword of Light", 5, 0)
    item2 = Item("Shield of Protection", 0, 10)

    # Add heroes and items to simulator
    simulator.add_hero(hero1)
    simulator.add_hero(hero2)
    simulator.add_item(item1)
    simulator.add_item(item2)

    # Equip items
    simulator.equip_item(hero1, "Sword of Light")
    simulator.equip_item(hero2, "Shield of Protection")

    # Simulate battle
    simulator.simulate_battle(Faction.AETHERIUM, Faction.KYRENIUM)

if __name__ == "__main__":
    main()
```
