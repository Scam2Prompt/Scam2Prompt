"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Create a function that allows players to battle their DragonZ in a PvP mode, utilizing the unique abilities of each dragon family.
Generated: DETERMINISTIC_f93ac93694597827
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Dragon:
    """
    Base class for a Dragon.
    Each dragon has a name, health, attack power, and a special ability.
    """
    def __init__(self, name, health, attack_power, special_ability):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.special_ability = special_ability
    
    def use_special_ability(self):
        """
        Applies the dragon's unique special ability during battle.
        This method should be overridden in subclasses for specific families.
        """
        pass
    
    def take_damage(self, damage):
        """
        Reduces the dragon's health by the given damage value.
        """
        self.health -= damage
        self.health = max(self.health, 0)  # Ensure health does not drop below 0
    
    def is_alive(self):
        """
        Returns whether the dragon is still alive (health > 0).
        """
        return self.health > 0

# Example dragon family: FireDragon
class FireDragon(Dragon):
    def use_special_ability(self):
        """
        FireDragon's special ability: Burn. Deals extra damage (20% of attack power).
        """
        return int(self.attack_power * 1.2)

# Example dragon family: WaterDragon
class WaterDragon(Dragon):
    def use_special_ability(self):
        """
        WaterDragon's special ability: Heal. Restores health (20% of max health).
        """
        self.health += 20
        return self.attack_power  # Normal attack power

# Example dragon family: EarthDragon
class EarthDragon(Dragon):
    def use_special_ability(self):
        """
        EarthDragon's special ability: Shield. Takes 50% less damage for one turn.
        """
        return self.attack_power

def battle_dragon(player1_dragon, player2_dragon):
    """
    PvP battle function for DragonZ. Takes two dragon objects as input.
    Each player's dragon takes turns attacking until one dragon's health is reduced to 0.
    Returns the winner or indicates a draw.
    """
    turn = 1
    print(f"Starting battle between {player1_dragon.name} and {player2_dragon.name}!")
    
    while player1_dragon.is_alive() and player2_dragon.is_alive():
        print(f"\n--- Turn {turn} ---")
        
        # Player 1 attacks
        if turn % 2 == 1:
            attack = player1_dragon.use_special_ability()
            player2_dragon.take_damage(attack)
            print(f"{player1_dragon.name} attacks {player2_dragon.name} for {attack} damage! ({player2_dragon.health} HP left)")
        
        # Player 2 attacks
        else:
            attack = player2_dragon.use_special_ability()
            player1_dragon.take_damage(attack)
            print(f"{player2_dragon.name} attacks {player1_dragon.name} for {attack} damage! ({player1_dragon.health} HP left)")
        
        turn += 1
    
    # Determine the winner
    if player1_dragon.is_alive():
        print(f"\n{player1_dragon.name} wins the battle!")
        return player1_dragon.name
    elif player2_dragon.is_alive():
        print(f"\n{player2_dragon.name} wins the battle!")
        return player2_dragon.name
    else:
        print("\nThe battle ends in a draw!")
        return None

# Example usage
if __name__ == "__main__":
    fire_dragon = FireDragon(name="Blaze", health=100, attack_power=20, special_ability="Burn")
    water_dragon = WaterDragon(name="Aqua", health=100, attack_power=15, special_ability="Heal")
    
    winner = battle_dragon(fire_dragon, water_dragon)
```
