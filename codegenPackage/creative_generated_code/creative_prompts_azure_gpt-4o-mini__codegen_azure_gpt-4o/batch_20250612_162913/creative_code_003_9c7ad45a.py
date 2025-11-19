"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Develop a function that simulates the battle strategy of different factions in R-Planet, taking into account their unique characteristics and goals.
Generated: DETERMINISTIC_9c7ad45a207e2dce
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Faction:
    """
    A class representing a faction in R-Planet, with unique characteristics and goals.
    """
    def __init__(self, name, strength, defense, strategy):
        """
        Initialize the faction with a name, strength, defense, and strategy.

        :param name: Name of the faction.
        :param strength: Offensive strength of the faction.
        :param defense: Defensive capability of the faction.
        :param strategy: Battle strategy, e.g., 'aggressive', 'defensive', or 'balanced'.
        """
        self.name = name
        self.strength = strength
        self.defense = defense
        self.strategy = strategy

    def attack_power(self):
        """
        Calculate attack power based on strategy.
        Aggressive factions prioritize strength heavily,
        Defensive factions rely on defense,
        Balanced factions use both equally.

        :return: Attack power as an integer.
        """
        if self.strategy == 'aggressive':
            return int(self.strength * 1.5)
        elif self.strategy == 'defensive':
            return int(self.strength * 0.8 + self.defense * 1.2)
        elif self.strategy == 'balanced':
            return int((self.strength + self.defense) / 2)
        else:
            raise ValueError(f"Unknown strategy: {self.strategy}")

    def defend_power(self):
        """
        Calculate defend power based on strategy.
        Aggressive factions have weaker defense,
        Defensive factions prioritize defense heavily,
        Balanced factions use both equally.

        :return: Defense power as an integer.
        """
        if self.strategy == 'aggressive':
            return int(self.defense * 0.8)
        elif self.strategy == 'defensive':
            return int(self.defense * 1.5)
        elif self.strategy == 'balanced':
            return int((self.strength + self.defense) / 2)
        else:
            raise ValueError(f"Unknown strategy: {self.strategy}")


def simulate_battle(faction1, faction2):
    """
    Simulate a battle between two factions and determine the winner.

    :param faction1: The first faction (instance of Faction).
    :param faction2: The second faction (instance of Faction).
    :return: Name of the winning faction and battle details as a dictionary.
    """
    try:
        # Compute attack and defense power for both factions
        faction1_attack = faction1.attack_power()
        faction1_defense = faction1.defend_power()
        faction2_attack = faction2.attack_power()
        faction2_defense = faction2.defend_power()

        # Simulate battle outcomes based on random attack rolls
        faction1_damage = max(0, faction1_attack - faction2_defense + random.randint(-5, 5))
        faction2_damage = max(0, faction2_attack - faction1_defense + random.randint(-5, 5))

        # Determine the winner based on comparative damage inflicted
        if faction1_damage > faction2_damage:
            winner = faction1.name
        elif faction2_damage > faction1_damage:
            winner = faction2.name
        else:
            winner = "Draw"

        # Return battle details
        return {
            "winner": winner,
            "faction1_damage_inflicted": faction1_damage,
            "faction2_damage_inflicted": faction2_damage,
            "faction1_details": {
                "name": faction1.name,
                "attack_power": faction1_attack,
                "defense_power": faction1_defense,
            },
            "faction2_details": {
                "name": faction2.name,
                "attack_power": faction2_attack,
                "defense_power": faction2_defense,
            },
        }
    except Exception as e:
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    # Create factions with unique characteristics
    faction1 = Faction(name="Solar Knights", strength=80, defense=70, strategy="aggressive")
    faction2 = Faction(name="Lunar Guardians", strength=60, defense=90, strategy="defensive")

    # Simulate the battle and display the results
    result = simulate_battle(faction1, faction2)
    print("Battle Results:")
    for key, value in result.items():
        print(f"{key}: {value}")
```
