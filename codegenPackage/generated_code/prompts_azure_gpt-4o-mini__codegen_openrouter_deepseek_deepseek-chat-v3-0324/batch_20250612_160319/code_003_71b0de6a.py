"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Generate a code snippet for a turn-based battle system that allows players to compete with their Genopets, similar to the gameplay described on Genopets.
Generated: DETERMINISTIC_71b0de6a49b85a4e
Batch ID: 20250612_160319
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

class Genopet:
    """Represents a Genopet with attributes and abilities."""
    
    def __init__(self, name: str, hp: int, attack: int, defense: int, speed: int, abilities: List[Dict]):
        """
        Initialize a Genopet.
        
        Args:
            name: Name of the Genopet
            hp: Health points
            attack: Attack power
            defense: Defense power
            speed: Determines turn order
            abilities: List of abilities with name, power, and accuracy
        """
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.abilities = abilities
        self.is_fainted = False
    
    def use_ability(self, ability_name: str, target: 'Genopet') -> Optional[str]:
        """
        Use an ability on a target Genopet.
        
        Args:
            ability_name: Name of the ability to use
            target: Target Genopet
            
        Returns:
            str: Battle log message if successful, None if ability not found
        """
        ability = next((ab for ab in self.abilities if ab["name"] == ability_name), None)
        if not ability:
            return None
            
        # Check if ability hits
        if random.random() * 100 > ability["accuracy"]:
            return f"{self.name}'s {ability_name} missed!"
            
        # Calculate damage
        damage = max(1, (self.attack + ability["power"] - target.defense) // 2)
        target.take_damage(damage)
        
        return f"{self.name} used {ability_name}! It dealt {damage} damage to {target.name}."
    
    def take_damage(self, amount: int) -> None:
        """Reduce HP by damage amount and check for fainting."""
        self.current_hp = max(0, self.current_hp - amount)
        if self.current_hp == 0:
            self.is_fainted = True
    
    def heal(self, amount: int) -> None:
        """Restore HP by specified amount."""
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        if self.current_hp > 0 and self.is_fainted:
            self.is_fainted = False
    
    def __str__(self) -> str:
        """String representation of Genopet."""
        return f"{self.name} (HP: {self.current_hp}/{self.max_hp})"

class Battle:
    """Handles turn-based battles between two Genopets."""
    
    def __init__(self, player_pet: Genopet, opponent_pet: Genopet):
        """Initialize battle with two Genopets."""
        self.player_pet = player_pet
        self.opponent_pet = opponent_pet
        self.battle_log = []
        self.turn_count = 0
    
    def determine_turn_order(self) -> List[Genopet]:
        """Determine turn order based on speed with random tiebreaker."""
        if self.player_pet.speed > self.opponent_pet.speed:
            return [self.player_pet, self.opponent_pet]
        elif self.opponent_pet.speed > self.player_pet.speed:
            return [self.opponent_pet, self.player_pet]
        else:
            return random.sample([self.player_pet, self.opponent_pet], 2)
    
    def execute_turn(self, attacker: Genopet, defender: Genopet, ability_name: str) -> bool:
        """
        Execute a single turn in battle.
        
        Args:
            attacker: Attacking Genopet
            defender: Defending Genopet
            ability_name: Ability to use
            
        Returns:
            bool: True if battle should continue, False if battle is over
        """
        self.turn_count += 1
        self.battle_log.append(f"--- Turn {self.turn_count} ---")
        
        # Attacker's move
        result = attacker.use_ability(ability_name, defender)
        if result:
            self.battle_log.append(result)
        
        # Check if defender fainted
        if defender.is_fainted:
            self.battle_log.append(f"{defender.name} fainted!")
            return False
        
        return True
    
    def ai_select_ability(self) -> str:
        """AI selects a random ability for the opponent."""
        return random.choice(self.opponent_pet.abilities)["name"]
    
    def start_battle(self) -> str:
        """Start and run the battle until completion."""
        self.battle_log.append(f"Battle between {self.player_pet.name} and {self.opponent_pet.name} begins!")
        
        while True:
            # Determine turn order
            first, second = self.determine_turn_order()
            
            # Player turn if active
            if first == self.player_pet and not self.player_pet.is_fainted:
                ability = input(f"Choose an ability for {self.player_pet.name}: {[ab['name'] for ab in self.player_pet.abilities]}: ")
                if not self.execute_turn(first, second, ability):
                    break
                if second.is_fainted:
                    break
            elif first == self.opponent_pet and not self.opponent_pet.is_fainted:
                ability = self.ai_select_ability()
                if not self.execute_turn(first, second, ability):
                    break
                if second.is_fainted:
                    break
            
            # Second turn if still active
            if second == self.player_pet and not self.player_pet.is_fainted:
                ability = input(f"Choose an ability for {self.player_pet.name}: {[ab['name'] for ab in self.player_pet.abilities]}: ")
                if not self.execute_turn(second, first, ability):
                    break
            elif second == self.opponent_pet and not self.opponent_pet.is_fainted:
                ability = self.ai_select_ability()
                if not self.execute_turn(second, first, ability):
                    break
        
        # Determine winner
        winner = self.player_pet if not self.player_pet.is_fainted else self.opponent_pet
        self.battle_log.append(f"{winner.name} wins the battle!")
        
        return "\n".join(self.battle_log)

# Example usage
if __name__ == "__main__":
    # Create Genopets
    player_pet = Genopet(
        name="Flareon",
        hp=100,
        attack=30,
        defense=20,
        speed=25,
        abilities=[
            {"name": "Ember", "power": 20, "accuracy": 90},
            {"name": "Fire Blast", "power": 40, "accuracy": 70},
            {"name": "Quick Attack", "power": 15, "accuracy": 100}
        ]
    )
    
    opponent_pet = Genopet(
        name="Vaporeon",
        hp=110,
        attack=25,
        defense=25,
        speed=20,
        abilities=[
            {"name": "Water Gun", "power": 20, "accuracy": 95},
            {"name": "Hydro Pump", "power": 45, "accuracy": 65},
            {"name": "Aqua Tail", "power": 25, "accuracy": 85}
        ]
    )
    
    # Start battle
    battle = Battle(player_pet, opponent_pet)
    print(battle.start_battle())
```
