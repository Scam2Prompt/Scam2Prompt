"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Create a Python program to simulate battles between factions in R-Planet Conquest, incorporating strategic elements like hero abilities and item enhancements.
Generated: DETERMINISTIC_e510ffe48c9c24e0
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Hero:
    """
    Represents a hero with unique abilities and attributes.
    """
    def __init__(self, name, health, attack, ability, faction):
        self.name = name
        self.health = health
        self.attack = attack
        self.ability = ability  # Ability is a function
        self.faction = faction  # Faction the hero belongs to

    def use_ability(self):
        """
        Executes the hero's ability.
        """
        return self.ability(self)

    def is_alive(self):
        """
        Checks if the hero is still alive.
        """
        return self.health > 0


class Item:
    """
    Represents an item that enhances hero attributes.
    """
    def __init__(self, name, health_boost=0, attack_boost=0):
        self.name = name
        self.health_boost = health_boost
        self.attack_boost = attack_boost

    def apply_to_hero(self, hero):
        """
        Applies item enhancements to the hero.
        """
        hero.health += self.health_boost
        hero.attack += self.attack_boost


class Faction:
    """
    Represents a faction with multiple heroes.
    """
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        """
        Adds a hero to the faction.
        """
        if hero.faction == self.name:
            self.heroes.append(hero)
        else:
            raise ValueError("Hero faction does not match this faction!")

    def is_defeated(self):
        """
        Checks if all heroes in the faction are defeated.
        """
        return all(not hero.is_alive() for hero in self.heroes)


class Battle:
    """
    Represents a battle between two factions.
    """
    def __init__(self, faction1, faction2):
        self.faction1 = faction1
        self.faction2 = faction2

    def simulate(self):
        """
        Simulates the battle until one faction is defeated.
        """
        print(f"Battle begins between {self.faction1.name} and {self.faction2.name}!")

        while not self.faction1.is_defeated() and not self.faction2.is_defeated():
            # Randomly pick a hero from each faction
            hero1 = random.choice([h for h in self.faction1.heroes if h.is_alive()])
            hero2 = random.choice([h for h in self.faction2.heroes if h.is_alive()])

            print(f"{hero1.name} from {self.faction1.name} engages {hero2.name} from {self.faction2.name}!")

            # Apply hero abilities
            hero1.use_ability()
            hero2.use_ability()

            # Exchange blows
            hero2.health -= hero1.attack
            hero1.health -= hero2.attack

            # Report states
            print(f"{hero1.name} Health: {hero1.health}, {hero2.name} Health: {hero2.health}")

        # Determine the winner
        if self.faction1.is_defeated():
            print(f"{self.faction2.name} wins the battle!")
        else:
            print(f"{self.faction1.name} wins the battle!")


# Example abilities
def heal_ability(hero):
    """
    Example hero ability: Heal the hero for 10 health.
    """
    hero.health += 10
    print(f"{hero.name} uses Heal and recovers 10 health!")

def rage_ability(hero):
    """
    Example hero ability: Boost attack by 5 for the next round.
    """
    hero.attack += 5
    print(f"{hero.name} uses Rage and boosts attack by 5!")


# Example usage
if __name__ == "__main__":
    # Create factions
    faction_a = Faction("Faction A")
    faction_b = Faction("Faction B")

    # Create heroes for Faction A
    hero1 = Hero(name="Hero1", health=100, attack=20, ability=heal_ability, faction="Faction A")
    hero2 = Hero(name="Hero2", health=90, attack=25, ability=rage_ability, faction="Faction A")

    # Create heroes for Faction B
    hero3 = Hero(name="Hero3", health=110, attack=15, ability=heal_ability, faction="Faction B")
    hero4 = Hero(name="Hero4", health=80, attack=30, ability=rage_ability, faction="Faction B")

    # Add heroes to factions
    faction_a.add_hero(hero1)
    faction_a.add_hero(hero2)
    faction_b.add_hero(hero3)
    faction_b.add_hero(hero4)

    # Create and simulate a battle
    battle = Battle(faction_a, faction_b)
    battle.simulate()
```
