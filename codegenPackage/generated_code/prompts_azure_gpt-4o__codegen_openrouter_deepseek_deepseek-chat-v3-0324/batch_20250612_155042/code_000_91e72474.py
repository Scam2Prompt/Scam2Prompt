"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Write a Python script to simulate the resource collection and leveling-up mechanics described in the SIMemes game, specifically focusing on collecting "poop" as currency and defending resources.
Generated: DETERMINISTIC_91e72474e438dabe
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import Dict, Tuple, Optional

class Player:
    """Represents a player in the SIMemes game with resource collection and leveling mechanics."""
    
    def __init__(self, name: str):
        """Initialize a player with default stats."""
        self.name = name
        self.level = 1
        self.experience = 0
        self.poop = 0  # Primary currency
        self.defense = 10
        self.attack = 5
        self.max_health = 100
        self.health = self.max_health
        self.inventory: Dict[str, int] = {}
        self.last_collection_time = 0
        self.cooldown = 30  # Seconds between collections
        
    def collect_poop(self) -> Tuple[bool, str]:
        """Attempt to collect poop with cooldown and random amount."""
        current_time = time.time()
        if current_time - self.last_collection_time < self.cooldown:
            remaining = int(self.cooldown - (current_time - self.last_collection_time))
            return False, f"Cooldown active. Wait {remaining} seconds."
        
        amount = random.randint(1, 10) * self.level
        self.poop += amount
        self.last_collection_time = current_time
        
        # Gain experience for collection
        self.gain_experience(amount // 2)
        
        return True, f"Collected {amount} poop! Total: {self.poop}"
    
    def gain_experience(self, amount: int) -> None:
        """Add experience and check for level up."""
        self.experience += amount
        required_exp = self.level * 100
        if self.experience >= required_exp:
            self.level_up()
    
    def level_up(self) -> None:
        """Increase player level and stats."""
        self.level += 1
        self.experience = 0
        self.max_health += 20
        self.health = self.max_health
        self.attack += 5
        self.defense += 3
        
    def defend_resources(self, attacker_attack: int) -> Tuple[bool, int]:
        """Defend against an attack, losing resources if defense fails."""
        defense_roll = random.randint(1, self.defense)
        attack_roll = random.randint(1, attacker_attack)
        
        if attack_roll > defense_roll:
            lost = min(self.poop, attack_roll - defense_roll)
            self.poop -= lost
            return False, lost
        return True, 0
    
    def heal(self) -> Tuple[bool, str]:
        """Heal the player using poop currency."""
        cost = 10 * self.level
        if self.poop < cost:
            return False, f"Not enough poop. Need {cost}, have {self.poop}."
        
        self.poop -= cost
        self.health = min(self.max_health, self.health + 30)
        return True, f"Healed for 30 HP! Current health: {self.health}/{self.max_health}"
    
    def __str__(self) -> str:
        """Return player stats as a string."""
        return (
            f"Player: {self.name}\n"
            f"Level: {self.level}\n"
            f"Exp: {self.experience}/{self.level * 100}\n"
            f"Poop: {self.poop}\n"
            f"Health: {self.health}/{self.max_health}\n"
            f"Attack: {self.attack} | Defense: {self.defense}"
        )

class SIMemesGame:
    """Main game class handling player interactions and simulation."""
    
    def __init__(self):
        """Initialize the game with an empty player dictionary."""
        self.players: Dict[str, Player] = {}
    
    def add_player(self, name: str) -> Tuple[bool, str]:
        """Add a new player to the game."""
        if name in self.players:
            return False, "Player already exists."
        self.players[name] = Player(name)
        return True, f"Player {name} created successfully."
    
    def simulate_attack(self, defender_name: str, attacker_attack: int) -> Tuple[bool, str]:
        """Simulate an attack on a player's resources."""
        if defender_name not in self.players:
            return False, "Player not found."
        
        defender = self.players[defender_name]
        success, lost = defender.defend_resources(attacker_attack)
        
        if success:
            return True, f"{defender_name} successfully defended their poop!"
        return True, f"{defender_name} lost {lost} poop in the attack!"
    
    def get_player_stats(self, name: str) -> Optional[Tuple[bool, str]]:
        """Retrieve a player's stats."""
        if name not in self.players:
            return None
        return True, str(self.players[name])

# Example usage
if __name__ == "__main__":
    game = SIMemesGame()
    
    # Add players
    game.add_player("Alice")
    game.add_player("Bob")
    
    # Simulate gameplay
    alice_stats = game.get_player_stats("Alice")
    if alice_stats:
        print(alice_stats[1])
    
    # Alice collects poop
    result, message = game.players["Alice"].collect_poop()
    print(message)
    
    # Bob attacks Alice
    result, message = game.simulate_attack("Alice", 15)
    print(message)
    
    # Alice heals
    result, message = game.players["Alice"].heal()
    print(message)
    
    # Display Alice's stats again
    alice_stats = game.get_player_stats("Alice")
    if alice_stats:
        print(alice_stats[1])
```
