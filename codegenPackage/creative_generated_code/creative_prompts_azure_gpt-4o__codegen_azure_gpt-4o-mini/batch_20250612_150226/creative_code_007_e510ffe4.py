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
    """Class representing a hero in the battle."""
    
    def __init__(self, name, health, attack, ability, ability_power):
        """Initialize the hero with basic attributes."""
        self.name = name
        self.health = health
        self.attack = attack
        self.ability = ability
        self.ability_power = ability_power

    def use_ability(self, enemy):
        """Use the hero's ability on the enemy."""
        print(f"{self.name} uses {self.ability}!")
        damage = self.ability_power
        enemy.take_damage(damage)

    def take_damage(self, damage):
        """Reduce the hero's health by the damage taken."""
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health left: {self.health}")

    def is_alive(self):
        """Check if the hero is still alive."""
        return self.health > 0


class Item:
    """Class representing an item that can enhance a hero's abilities."""
    
    def __init__(self, name, attack_bonus, health_bonus):
        """Initialize the item with attack and health bonuses."""
        self.name = name
        self.attack_bonus = attack_bonus
        self.health_bonus = health_bonus

    def apply(self, hero):
        """Apply the item's effects to the hero."""
        hero.attack += self.attack_bonus
        hero.health += self.health_bonus
        print(f"{hero.name} uses {self.name} - Attack: {hero.attack}, Health: {hero.health}")


class Battle:
    """Class to simulate a battle between two factions of heroes."""
    
    def __init__(self, heroes1, heroes2):
        """Initialize the battle with two factions of heroes."""
        self.heroes1 = heroes1
        self.heroes2 = heroes2
        self.turn = 0

    def simulate(self):
        """Run the battle simulation until one faction is defeated."""
        while self.heroes1 and self.heroes2:
            self.turn += 1
            print(f"\n--- Turn {self.turn} ---")
            self.battle_round()
            self.clean_up()

        winner = "Faction 1" if self.heroes1 else "Faction 2"
        print(f"{winner} wins the battle!")

    def battle_round(self):
        """Conduct a round of battle between the two factions."""
        for hero1, hero2 in zip(self.heroes1, self.heroes2):
            if hero1.is_alive() and hero2.is_alive():
                self.fight(hero1, hero2)

    def fight(self, hero1, hero2):
        """Fight between two heroes."""
        print(f"{hero1.name} attacks {hero2.name}!")
        hero2.take_damage(hero1.attack)
        
        if hero2.is_alive():
            print(f"{hero2.name} retaliates!")
            hero1.take_damage(hero2.attack)

    def clean_up(self):
        """Remove defeated heroes from the factions."""
        self.heroes1 = [hero for hero in self.heroes1 if hero.is_alive()]
        self.heroes2 = [hero for hero in self.heroes2 if hero.is_alive()]


# Example Usage

if __name__ == "__main__":
    # Create heroes for the first faction
    hero_a = Hero(name="Warrior A", health=100, attack=15, ability="Sword Slash", ability_power=25)
    hero_b = Hero(name="Mage A", health=80, attack=10, ability="Fireball", ability_power=30)

    # Create heroes for the second faction
    hero_c = Hero(name="Warrior B", health=90, attack=12, ability="Shield Bash", ability_power=20)
    hero_d = Hero(name="Mage B", health=70, attack=14, ability="Lightning Strike", ability_power=35)

    # Create items
    item1 = Item(name="Health Potion", attack_bonus=0, health_bonus=20)
    item2 = Item(name="Strength Elixir", attack_bonus=5, health_bonus=0)

    # Apply items to heroes
    item1.apply(hero_a)
    item2.apply(hero_c)

    # Set up the battle
    battle = Battle(heroes1=[hero_a, hero_b], heroes2=[hero_c, hero_d])
    
    # Start the battle simulation
    battle.simulate()
```
