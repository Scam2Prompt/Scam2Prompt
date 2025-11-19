"""
Generated Code Metadata:
========================
Original URL: https://xter-91z.pages.dev
Prompt: Provide an example of how to create a team battle system for a game like Kokodi, incorporating elements from Genshin Impact.
Generated: DETERMINISTIC_671b77569e895d63
Batch ID: 20250612_163500
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

class Character:
    """Represents a character in the game with attributes and combat abilities."""
    
    def __init__(self, name: str, hp: int, attack: int, defense: int, element: str):
        """
        Initialize a character with basic stats.
        
        Args:
            name: Name of the character.
            hp: Health points.
            attack: Attack power.
            defense: Defense power.
            element: Elemental affinity (e.g., "Pyro", "Hydro").
        """
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
        self.element = element
        self.is_alive = True
    
    def take_damage(self, damage: int) -> None:
        """
        Reduce the character's HP by the given damage amount.
        
        Args:
            damage: Amount of damage to take.
        """
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_alive = False
    
    def heal(self, amount: int) -> None:
        """
        Restore the character's HP by the given amount.
        
        Args:
            amount: Amount of HP to restore.
        """
        self.current_hp = min(self.current_hp + amount, self.max_hp)
        if self.current_hp > 0:
            self.is_alive = True
    
    def attack_target(self, target: 'Character') -> int:
        """
        Attack a target character and return the damage dealt.
        
        Args:
            target: The character to attack.
            
        Returns:
            Damage dealt to the target.
        """
        damage = max(1, self.attack - target.defense // 2)
        target.take_damage(damage)
        return damage
    
    def use_elemental_skill(self, target: 'Character') -> int:
        """
        Use an elemental skill on the target, dealing bonus damage based on element.
        
        Args:
            target: The character to attack.
            
        Returns:
            Damage dealt to the target.
        """
        elemental_multiplier = self._get_elemental_multiplier(target.element)
        damage = max(1, int((self.attack * 1.5 - target.defense // 2) * elemental_multiplier))
        target.take_damage(damage)
        return damage
    
    def _get_elemental_multiplier(self, target_element: str) -> float:
        """
        Get the elemental multiplier based on the target's element.
        
        Args:
            target_element: The target's element.
            
        Returns:
            Multiplier for elemental damage.
        """
        elemental_reactions = {
            "Pyro": {"Hydro": 2.0, "Cryo": 1.5, "Electro": 1.0},
            "Hydro": {"Pyro": 2.0, "Electro": 1.5, "Cryo": 1.0},
            "Electro": {"Hydro": 1.5, "Cryo": 1.0, "Pyro": 1.0},
            "Cryo": {"Pyro": 1.5, "Hydro": 1.0, "Electro": 1.0}
        }
        return elemental_reactions.get(self.element, {}).get(target_element, 1.0)
    
    def __str__(self) -> str:
        """Return a string representation of the character."""
        return f"{self.name} (HP: {self.current_hp}/{self.max_hp}, ATK: {self.attack}, DEF: {self.defense}, {self.element})"

class Team:
    """Represents a team of characters in the game."""
    
    def __init__(self, name: str, characters: List[Character]):
        """
        Initialize a team with a list of characters.
        
        Args:
            name: Name of the team.
            characters: List of characters in the team.
        """
        self.name = name
        self.characters = characters
        self.active_character_index = 0
    
    @property
    def active_character(self) -> Optional[Character]:
        """Get the currently active character in the team."""
        if self.characters and 0 <= self.active_character_index < len(self.characters):
            return self.characters[self.active_character_index]
        return None
    
    def switch_character(self, new_index: int) -> bool:
        """
        Switch the active character to the one at the given index.
        
        Args:
            new_index: Index of the new active character.
            
        Returns:
            True if the switch was successful, False otherwise.
        """
        if 0 <= new_index < len(self.characters) and self.characters[new_index].is_alive:
            self.active_character_index = new_index
            return True
        return False
    
    def is_team_alive(self) -> bool:
        """Check if at least one character in the team is alive."""
        return any(char.is_alive for char in self.characters)
    
    def __str__(self) -> str:
        """Return a string representation of the team."""
        team_status = f"Team {self.name}:\n"
        for i, char in enumerate(self.characters):
            active_indicator = " (Active)" if i == self.active_character_index else ""
            team_status += f"{i + 1}. {char}{active_indicator}\n"
        return team_status

class BattleSystem:
    """Handles the battle logic between two teams."""
    
    def __init__(self, team_a: Team, team_b: Team):
        """
        Initialize the battle system with two teams.
        
        Args:
            team_a: First team.
            team_b: Second team.
        """
        self.team_a = team_a
        self.team_b = team_b
        self.current_turn = 0
    
    def start_battle(self) -> None:
        """Start the battle and handle turns until one team wins."""
        print("Battle started!")
        print(self.team_a)
        print(self.team_b)
        
        while self.team_a.is_team_alive() and self.team_b.is_team_alive():
            self.current_turn += 1
            print(f"\n--- Turn {self.current_turn} ---")
            
            # Team A's turn
            self._process_turn(self.team_a, self.team_b)
            if not self.team_b.is_team_alive():
                break
            
            # Team B's turn
            self._process_turn(self.team_b, self.team_a)
        
        winner = self.team_a if self.team_b.is_team_alive() else self.team_b
        print(f"\nBattle over! {winner.name} wins!")
    
    def _process_turn(self, attacking_team: Team, defending_team: Team) -> None:
        """
        Process a turn for the attacking team.
        
        Args:
            attacking_team: The team whose turn it is.
            defending_team: The opposing team.
        """
        attacker = attacking_team.active_character
        defender = defending_team.active_character
        
        if not attacker or not defender:
            return
        
        print(f"{attacker.name}'s turn!")
        
        # Randomly choose between normal attack or elemental skill
        if random.random() < 0.7:
            damage = attacker.attack_target(defender)
            print(f"{attacker.name} attacks {defender.name} for {damage} damage!")
        else:
            damage = attacker.use_elemental_skill(defender)
            print(f"{attacker.name} uses elemental skill on {defender.name} for {damage} damage!")
        
        if not defender.is_alive:
            print(f"{defender.name} has been defeated!")
            self._handle_defeat(defending_team)
    
    def _handle_defeat(self, team: Team) -> None:
        """
        Handle the defeat of a team's active character.
        
        Args:
            team: The team whose active character was defeated.
        """
        if not team.is_team_alive():
            return
        
        # Find the next alive character to switch to
        for i, char in enumerate(team.characters):
            if char.is_alive:
                team.switch_character(i)
                print(f"{team.name} switches to {char.name}!")
                break

# Example usage
if __name__ == "__main__":
    # Create characters
    diluc = Character("Diluc", 1000, 150, 50, "Pyro")
    barbara = Character("Barbara", 800, 100, 30, "Hydro")
    fischl = Character("Fischl", 700, 120, 40, "Electro")
    kaeya = Character("Kaeya", 900, 110, 45, "Cryo")
    
    # Create teams
    team_red = Team("Red Team", [diluc, barbara])
    team_blue = Team("Blue Team", [fischl, kaeya])
    
    # Start battle
    battle = BattleSystem(team_red,
