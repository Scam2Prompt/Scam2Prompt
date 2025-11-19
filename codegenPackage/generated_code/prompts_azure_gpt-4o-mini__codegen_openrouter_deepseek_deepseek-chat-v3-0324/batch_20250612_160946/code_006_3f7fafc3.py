"""
Generated Code Metadata:
========================
Original URL: https://bigtime-ai.pages.dev
Prompt: How do players access new Adventure Instances in Big Time, and what are the associated challenges?
Generated: DETERMINISTIC_3f7fafc3a617420b
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# adventure_instance_manager.py
"""
Module for handling Adventure Instance access in Big Time game.
Manages player access to new Adventure Instances and associated challenges.
"""

import random
from typing import Dict, List, Optional
from enum import Enum, auto

class AdventureInstanceStatus(Enum):
    """Enum representing the status of an Adventure Instance."""
    LOCKED = auto()
    UNLOCKED = auto()
    COMPLETED = auto()
    FAILED = auto()

class ChallengeDifficulty(Enum):
    """Enum representing the difficulty level of challenges."""
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
    EPIC = auto()

class Challenge:
    """Class representing a challenge within an Adventure Instance."""
    def __init__(self, name: str, difficulty: ChallengeDifficulty, reward: int):
        self.name = name
        self.difficulty = difficulty
        self.reward = reward
        self.completed = False

    def complete_challenge(self) -> None:
        """Mark the challenge as completed."""
        self.completed = True

class AdventureInstance:
    """Class representing an Adventure Instance in Big Time."""
    def __init__(self, instance_id: int, name: str, required_level: int):
        self.instance_id = instance_id
        self.name = name
        self.required_level = required_level
        self.status = AdventureInstanceStatus.LOCKED
        self.challenges: List[Challenge] = []
    
    def add_challenge(self, challenge: Challenge) -> None:
        """Add a challenge to this Adventure Instance."""
        self.challenges.append(challenge)
    
    def unlock(self, player_level: int) -> bool:
        """
        Attempt to unlock the Adventure Instance if player meets level requirement.
        
        Args:
            player_level: The current level of the player
            
        Returns:
            bool: True if successfully unlocked, False otherwise
        """
        if player_level >= self.required_level:
            self.status = AdventureInstanceStatus.UNLOCKED
            return True
        return False
    
    def complete_instance(self) -> None:
        """Mark the Adventure Instance as completed."""
        if self.status == AdventureInstanceStatus.UNLOCKED:
            self.status = AdventureInstanceStatus.COMPLETED
    
    def fail_instance(self) -> None:
        """Mark the Adventure Instance as failed."""
        if self.status == AdventureInstanceStatus.UNLOCKED:
            self.status = AdventureInstanceStatus.FAILED

class Player:
    """Class representing a player in Big Time."""
    def __init__(self, player_id: int, name: str, level: int = 1):
        self.player_id = player_id
        self.name = name
        self.level = level
        self.inventory: Dict[str, int] = {}
        self.completed_instances: List[int] = []
    
    def level_up(self) -> None:
        """Increase the player's level by 1."""
        self.level += 1
    
    def add_to_inventory(self, item: str, quantity: int = 1) -> None:
        """Add items to player's inventory."""
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
    
    def can_access_instance(self, instance: AdventureInstance) -> bool:
        """Check if player can access the given Adventure Instance."""
        return instance.unlock(self.level)
    
    def complete_instance(self, instance: AdventureInstance) -> bool:
        """
        Attempt to complete an Adventure Instance.
        
        Args:
            instance: The AdventureInstance to complete
            
        Returns:
            bool: True if successfully completed, False otherwise
        """
        if instance.status != AdventureInstanceStatus.UNLOCKED:
            return False
        
        # Simulate random success/failure (would be game logic in reality)
        success = random.random() > 0.3  # 70% success rate
        
        if success:
            instance.complete_instance()
            self.completed_instances.append(instance.instance_id)
            for challenge in instance.challenges:
                if not challenge.completed:
                    self.add_to_inventory("XP", challenge.reward)
                    challenge.complete_challenge()
            return True
        else:
            instance.fail_instance()
            return False

class AdventureInstanceManager:
    """Manager class for handling Adventure Instances in the game."""
    def __init__(self):
        self.instances: Dict[int, AdventureInstance] = {}
    
    def add_instance(self, instance: AdventureInstance) -> None:
        """Add an Adventure Instance to the manager."""
        self.instances[instance.instance_id] = instance
    
    def get_instance(self, instance_id: int) -> Optional[AdventureInstance]:
        """Retrieve an Adventure Instance by ID."""
        return self.instances.get(instance_id)
    
    def get_available_instances(self, player: Player) -> List[AdventureInstance]:
        """
        Get all Adventure Instances available to the player based on their level.
        
        Args:
            player: The Player object to check availability for
            
        Returns:
            List[AdventureInstance]: List of available instances
        """
        available = []
        for instance in self.instances.values():
            if instance.required_level <= player.level:
                available.append(instance)
        return available

# Example usage
if __name__ == "__main__":
    # Setup game environment
    manager = AdventureInstanceManager()
    player = Player(1, "Hero", level=5)
    
    # Create some Adventure Instances
    dungeon = AdventureInstance(1, "Forgotten Dungeon", 3)
    dungeon.add_challenge(Challenge("Defeat the Goblin King", ChallengeDifficulty.MEDIUM, 100))
    dungeon.add_challenge(Challenge("Find the Lost Artifact", ChallengeDifficulty.EASY, 50))
    
    tower = AdventureInstance(2, "Wizard's Tower", 7)
    tower.add_challenge(Challenge("Solve the Riddle", ChallengeDifficulty.HARD, 200))
    tower.add_challenge(Challenge("Defeat the Archmage", ChallengeDifficulty.EPIC, 500))
    
    # Add instances to manager
    manager.add_instance(dungeon)
    manager.add_instance(tower)
    
    # Player attempts to access instances
    available_instances = manager.get_available_instances(player)
    print(f"Available instances for {player.name}:")
    for inst in available_instances:
        print(f"- {inst.name} (Level {inst.required_level}+)")
        
        if player.can_access_instance(inst):
            print(f"  {player.name} attempts {inst.name}...")
            success = player.complete_instance(inst)
            if success:
                print(f"  Success! {inst.name} completed!")
            else:
                print(f"  Failed to complete {inst.name}")
```
