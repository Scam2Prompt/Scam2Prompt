"""
Generated Code Metadata:
========================
Original URL: https://register-stormwarfarecom.pages.dev
Prompt: Provide an example of how to design a unique Commander ability system for a card game, inspired by the features in Storm Warfare.
Generated: DETERMINISTIC_ff9e678c3e0118a8
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List, Dict, Optional

class CommanderAbilityType(Enum):
    """Enum representing different types of commander abilities."""
    PASSIVE = auto()
    ACTIVE = auto()
    TRIGGERED = auto()

class AbilityEffect(ABC):
    """Abstract base class for commander ability effects."""
    @abstractmethod
    def apply(self, game_state: Dict) -> Dict:
        """Apply the ability effect to the game state."""
        pass

class DamageEffect(AbilityEffect):
    """Concrete effect that deals damage to targets."""
    def __init__(self, damage_amount: int, target_type: str):
        self.damage_amount = damage_amount
        self.target_type = target_type  # e.g., "enemy", "ally", "all"
    
    def apply(self, game_state: Dict) -> Dict:
        """Apply damage to specified targets."""
        targets = game_state.get(self.target_type, [])
        for target in targets:
            target["health"] -= self.damage_amount
        return game_state

class HealEffect(AbilityEffect):
    """Concrete effect that heals targets."""
    def __init__(self, heal_amount: int, target_type: str):
        self.heal_amount = heal_amount
        self.target_type = target_type
    
    def apply(self, game_state: Dict) -> Dict:
        """Apply healing to specified targets."""
        targets = game_state.get(self.target_type, [])
        for target in targets:
            target["health"] += self.heal_amount
        return game_state

class CommanderAbility:
    """Class representing a commander's ability."""
    def __init__(
        self,
        name: str,
        ability_type: CommanderAbilityType,
        cooldown: int,
        effects: List[AbilityEffect],
        description: str = ""
    ):
        self.name = name
        self.type = ability_type
        self.cooldown = cooldown
        self.current_cooldown = 0
        self.effects = effects
        self.description = description
    
    def is_ready(self) -> bool:
        """Check if ability is ready to use."""
        return self.current_cooldown <= 0
    
    def trigger(self, game_state: Dict) -> Optional[Dict]:
        """Trigger the ability if ready."""
        if not self.is_ready():
            return None
        
        for effect in self.effects:
            game_state = effect.apply(game_state)
        
        self.current_cooldown = self.cooldown
        return game_state
    
    def update_cooldown(self):
        """Update cooldown counter."""
        if self.current_cooldown > 0:
            self.current_cooldown -= 1

class Commander:
    """Class representing a commander with abilities."""
    def __init__(self, name: str, abilities: List[CommanderAbility]):
        self.name = name
        self.abilities = {ability.name: ability for ability in abilities}
    
    def get_ability(self, name: str) -> Optional[CommanderAbility]:
        """Get ability by name."""
        return self.abilities.get(name)
    
    def update_abilities(self):
        """Update cooldowns for all abilities."""
        for ability in self.abilities.values():
            ability.update_cooldown()

# Example usage
if __name__ == "__main__":
    # Create abilities
    fireball = CommanderAbility(
        name="Fireball",
        ability_type=CommanderAbilityType.ACTIVE,
        cooldown=3,
        effects=[DamageEffect(damage_amount=5, target_type="enemy")],
        description="Deals 5 damage to enemy units"
    )
    
    healing_aura = CommanderAbility(
        name="Healing Aura",
        ability_type=CommanderAbilityType.PASSIVE,
        cooldown=0,
        effects=[HealEffect(heal_amount=2, target_type="ally")],
        description="Heals all allies for 2 health each turn"
    )
    
    # Create commander
    pyromancer = Commander(
        name="Pyromancer",
        abilities=[fireball, healing_aura]
    )
    
    # Example game state
    game_state = {
        "enemy": [{"name": "Orc", "health": 10}],
        "ally": [{"name": "Knight", "health": 8}]
    }
    
    # Use abilities
    print("Initial state:", game_state)
    
    # Passive ability triggers automatically
    healing_aura.trigger(game_state)
    print("After Healing Aura:", game_state)
    
    # Active ability
    if fireball.is_ready():
        fireball.trigger(game_state)
        print("After Fireball:", game_state)
    
    # Update cooldowns
    pyromancer.update_abilities()
```
