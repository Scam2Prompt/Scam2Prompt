"""
Generated Code Metadata:
========================
Original URL: https://register-stormwarfarecom.pages.dev
Prompt: Develop a system for generating legendary hero cards with unique abilities and attributes, inspired by Storm Warfare's 100 Legendary Heroes.
Generated: DETERMINISTIC_1d98638c49b6c06b
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from dataclasses import dataclass

# Enum for hero roles
class HeroRole(Enum):
    """Enum for hero roles."""
    WARRIOR = 1
    MAGE = 2
    ARCHER = 3
    ASSASSIN = 4

# Enum for ability types
class AbilityType(Enum):
    """Enum for ability types."""
    ATTACK = 1
    DEFENSE = 2
    SUPPORT = 3

# Dataclass for hero abilities
@dataclass
class Ability:
    """Dataclass for hero abilities."""
    name: str
    ability_type: AbilityType
    effect: str
    value: int

# Dataclass for legendary heroes
@dataclass
class LegendaryHero:
    """Dataclass for legendary heroes."""
    name: str
    role: HeroRole
    abilities: list[Ability]
    attributes: dict[str, int]

# Class for generating legendary heroes
class LegendaryHeroGenerator:
    """Class for generating legendary heroes."""

    def __init__(self):
        self.roles = list(HeroRole)
        self.ability_types = list(AbilityType)
        self.attribute_names = ["strength", "intelligence", "agility", "vitality"]

    def generate_hero_name(self) -> str:
        """Generate a random hero name."""
        adjectives = ["Brave", "Fearless", "Legendary", "Mighty", "Valiant"]
        nouns = ["Warrior", "Mage", "Archer", "Assassin", "Champion"]
        return f"{random.choice(adjectives)} {random.choice(nouns)}"

    def generate_ability(self) -> Ability:
        """Generate a random ability."""
        ability_names = {
            AbilityType.ATTACK: ["Attack Boost", "Critical Strike", "Damage Increase"],
            AbilityType.DEFENSE: ["Shield", "Defense Boost", "Damage Reduction"],
            AbilityType.SUPPORT: ["Healing", "Speed Boost", "Mana Regeneration"]
        }
        ability_name = random.choice(ability_names[random.choice(self.ability_types)])
        ability_type = next(at for at in self.ability_types if ability_name in ability_names[at])
        effect = random.choice(["Increases", "Decreases", "Restores"]) + f" {random.randint(1, 10)} {self.get_attribute_name()}"
        value = random.randint(1, 10)
        return Ability(ability_name, ability_type, effect, value)

    def generate_attributes(self) -> dict[str, int]:
        """Generate random attributes."""
        return {attr: random.randint(1, 10) for attr in self.attribute_names}

    def get_attribute_name(self) -> str:
        """Get a random attribute name."""
        return random.choice(self.attribute_names)

    def generate_legendary_hero(self) -> LegendaryHero:
        """Generate a legendary hero."""
        try:
            hero_name = self.generate_hero_name()
            role = random.choice(self.roles)
            abilities = [self.generate_ability() for _ in range(random.randint(2, 4))]
            attributes = self.generate_attributes()
            return LegendaryHero(hero_name, role, abilities, attributes)
        except Exception as e:
            print(f"Error generating legendary hero: {e}")
            return None

# Example usage
if __name__ == "__main__":
    generator = LegendaryHeroGenerator()
    legendary_hero = generator.generate_legendary_hero()
    if legendary_hero:
        print(f"Name: {legendary_hero.name}")
        print(f"Role: {legendary_hero.role.name}")
        print("Abilities:")
        for ability in legendary_hero.abilities:
            print(f"- {ability.name} ({ability.ability_type.name}): {ability.effect} by {ability.value}")
        print("Attributes:")
        for attribute, value in legendary_hero.attributes.items():
            print(f"- {attribute.capitalize()}: {value}")
```
