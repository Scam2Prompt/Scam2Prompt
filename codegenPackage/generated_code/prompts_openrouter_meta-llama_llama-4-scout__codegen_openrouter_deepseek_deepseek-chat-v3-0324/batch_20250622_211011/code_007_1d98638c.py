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
from typing import Dict, List, Optional
from dataclasses import dataclass
import json
import uuid

class HeroClass(Enum):
    WARRIOR = "Warrior"
    MAGE = "Mage"
    ROGUE = "Rogue"
    RANGER = "Ranger"
    CLERIC = "Cleric"
    MONK = "Monk"

class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

@dataclass
class Ability:
    name: str
    description: str
    cooldown: int
    effect_strength: float

@dataclass
class HeroCard:
    id: str
    name: str
    hero_class: HeroClass
    rarity: Rarity
    health: int
    attack: int
    defense: int
    speed: int
    abilities: List[Ability]
    
    def to_dict(self) -> Dict:
        """Convert HeroCard to a dictionary for serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "hero_class": self.hero_class.value,
            "rarity": self.rarity.value,
            "health": self.health,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "abilities": [
                {
                    "name": ability.name,
                    "description": ability.description,
                    "cooldown": ability.cooldown,
                    "effect_strength": ability.effect_strength
                } for ability in self.abilities
            ]
        }

class HeroGenerator:
    """Generates random legendary hero cards with unique abilities and attributes."""
    
    # Predefined lists for name generation
    FIRST_NAMES = ["Aelar", "Bryn", "Cael", "Dain", "Eira", "Fael", "Gwyn", "Hael", "Iris", "Jora"]
    LAST_NAMES = ["Stormborn", "Fireheart", "Shadowstep", "Moonwhisper", "Ironfist", "Lightbringer", "Duskblade", "Frostvein", "Thunderclap", "Starweaver"]
    
    # Ability templates by class
    ABILITY_TEMPLATES = {
        HeroClass.WARRIOR: [
            ("Whirlwind Strike", "Deals damage to all enemies", 3, 1.2),
            ("Shield Bash", "Stuns the target", 4, 1.0),
            ("Battle Cry", "Increases attack of all allies", 5, 1.5)
        ],
        HeroClass.MAGE: [
            ("Fireball", "Deals fire damage to target", 2, 1.8),
            ("Ice Nova", "Freezes nearby enemies", 4, 1.2),
            ("Arcane Shield", "Absorbs damage", 3, 1.0)
        ],
        HeroClass.ROGUE: [
            ("Backstab", "Deals critical damage from behind", 3, 2.0),
            ("Poison Dart", "Applies poison over time", 2, 0.5),
            ("Shadowmeld", "Becomes invisible", 4, 0.0)
        ],
        HeroClass.RANGER: [
            ("Multi-Shot", "Hits multiple targets", 3, 1.2),
            ("Piercing Arrow", "Ignores armor", 4, 1.5),
            ("Call of the Wild", "Summons a beast companion", 5, 1.0)
        ],
        HeroClass.CLERIC: [
            ("Heal", "Restores health to target", 2, 1.5),
            ("Divine Light", "Removes debuffs", 3, 0.0),
            ("Holy Smite", "Deals damage to undead", 4, 2.0)
        ],
        HeroClass.MONK: [
            ("Flying Kick", "Knocks back the target", 3, 1.2),
            ("Meditate", "Restores energy", 4, 1.0),
            ("Pressure Point", "Stuns the target", 5, 1.5)
        ]
    }
    
    @staticmethod
    def generate_name() -> str:
        """Generate a random hero name."""
        return f"{random.choice(HeroGenerator.FIRST_NAMES)} {random.choice(HeroGenerator.LAST_NAMES)}"
    
    @staticmethod
    def generate_abilities(hero_class: HeroClass) -> List[Ability]:
        """Generate random abilities for a hero based on their class."""
        templates = HeroGenerator.ABILITY_TEMPLATES[hero_class]
        num_abilities = random.randint(2, 3)
        selected = random.sample(templates, num_abilities)
        return [Ability(name, desc, cd, eff) for name, desc, cd, eff in selected]
    
    @staticmethod
    def generate_stats(rarity: Rarity) -> Dict[str, int]:
        """Generate base stats based on rarity."""
        base = {
            "health": random.randint(50, 100),
            "attack": random.randint(5, 20),
            "defense": random.randint(5, 20),
            "speed": random.randint(5, 20)
        }
        
        # Apply rarity multipliers
        multiplier = {
            Rarity.COMMON: 1.0,
            Rarity.UNCOMMON: 1.2,
            Rarity.RARE: 1.5,
            Rarity.EPIC: 1.8,
            Rarity.LEGENDARY: 2.2
        }[rarity]
        
        return {stat: int(value * multiplier) for stat, value in base.items()}
    
    @classmethod
    def generate_hero(cls, rarity: Rarity = Rarity.LEGENDARY) -> HeroCard:
        """Generate a random legendary hero card."""
        hero_class = random.choice(list(HeroClass))
        name = cls.generate_name()
        stats = cls.generate_stats(rarity)
        abilities = cls.generate_abilities(hero_class)
        
        return HeroCard(
            id=str(uuid.uuid4()),
            name=name,
            hero_class=hero_class,
            rarity=rarity,
            health=stats["health"],
            attack=stats["attack"],
            defense=stats["defense"],
            speed=stats["speed"],
            abilities=abilities
        )

class HeroCardSystem:
    """System for managing and generating hero cards."""
    
    def __init__(self):
        self.generator = HeroGenerator()
    
    def generate_heroes(self, count: int = 1, rarity: Optional[Rarity] = None) -> List[HeroCard]:
        """Generate multiple hero cards."""
        if count <= 0:
            raise ValueError("Count must be positive")
        
        rarity = rarity or Rarity.LEGENDARY
        return [self.generator.generate_hero(rarity) for _ in range(count)]
    
    def save_to_file(self, heroes: List[HeroCard], filename: str) -> None:
        """Save hero cards to a JSON file."""
        if not filename.endswith('.json'):
            filename += '.json'
        
        with open(filename, 'w') as f:
            json.dump([hero.to_dict() for hero in heroes], f, indent=2)
    
    def load_from_file(self, filename: str) -> List[HeroCard]:
        """Load hero cards from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return [
                    HeroCard(
                        id=hero_data["id"],
                        name=hero_data["name"],
                        hero_class=HeroClass(hero_data["hero_class"]),
                        rarity=Rarity(hero_data["rarity"]),
                        health=hero_data["health"],
                        attack=hero_data["attack"],
                        defense=hero_data["defense"],
                        speed=hero_data["speed"],
                        abilities=[
                            Ability(
                                name=ability["name"],
                                description=ability["description"],
                                cooldown=ability["cooldown"],
                                effect_strength=ability["effect_strength"]
                            ) for ability in hero_data["abilities"]
                        ]
                    ) for hero_data in data
                ]
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
        except KeyError as e:
            raise ValueError(f"Missing required field: {e}")

# Example usage
if __name__ == "__main__":
    try:
        system = HeroCardSystem()
        heroes = system.generate_heroes(count=5)
        system.save_to_file(heroes, "legendary_heroes.json")
        print("Successfully generated and saved 5 legendary heroes!")
    except Exception as e:
        print(f"Error: {e}")
```
