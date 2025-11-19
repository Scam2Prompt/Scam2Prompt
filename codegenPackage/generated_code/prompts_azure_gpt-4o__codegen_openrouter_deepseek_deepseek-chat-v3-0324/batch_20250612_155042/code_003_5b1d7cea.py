"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Generate a Python-based simulation for the competitive stealing mechanics in SIMemes, where players can steal resources like "chests" and "poop" from others.
Generated: DETERMINISTIC_5b1d7ceaf1dcebfb
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
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum, auto


class ResourceType(Enum):
    CHEST = auto()
    POOP = auto()


@dataclass
class Player:
    id: str
    name: str
    resources: Dict[ResourceType, int]
    last_steal_time: float = 0.0
    steal_cooldown: float = 30.0  # seconds

    def can_steal(self) -> bool:
        """Check if player can perform a steal action."""
        current_time = time.time()
        return current_time - self.last_steal_time >= self.steal_cooldown

    def update_steal_time(self) -> None:
        """Update the last steal time to now."""
        self.last_steal_time = time.time()


class StealSimulator:
    def __init__(self):
        self.players: Dict[str, Player] = {}
        self.steal_success_rate: float = 0.7  # 70% base success rate
        self.resource_steal_amounts = {
            ResourceType.CHEST: (1, 3),  # min, max
            ResourceType.POOP: (1, 5)
        }

    def add_player(self, player_id: str, name: str) -> None:
        """Add a new player to the simulation."""
        if player_id in self.players:
            raise ValueError(f"Player with ID {player_id} already exists")
        
        self.players[player_id] = Player(
            id=player_id,
            name=name,
            resources={
                ResourceType.CHEST: 0,
                ResourceType.POOP: 0
            }
        )

    def add_resources(self, player_id: str, resource_type: ResourceType, amount: int) -> None:
        """Add resources to a player's inventory."""
        if player_id not in self.players:
            raise ValueError(f"Player with ID {player_id} not found")
        
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        self.players[player_id].resources[resource_type] += amount

    def attempt_steal(
        self,
        thief_id: str,
        victim_id: str,
        resource_type: ResourceType
    ) -> Tuple[bool, Optional[Dict[ResourceType, int]]]:
        """
        Attempt to steal resources from another player.
        
        Returns:
            Tuple of (success, stolen_resources) where stolen_resources is None if failed
        """
        if thief_id not in self.players:
            raise ValueError(f"Thief with ID {thief_id} not found")
        
        if victim_id not in self.players:
            raise ValueError(f"Victim with ID {victim_id} not found")
        
        if thief_id == victim_id:
            raise ValueError("Cannot steal from yourself")
        
        thief = self.players[thief_id]
        victim = self.players[victim_id]

        if not thief.can_steal():
            raise ValueError("Thief is on cooldown")
        
        if victim.resources[resource_type] <= 0:
            return False, None

        # Calculate steal success with random factor
        success = random.random() <= self.steal_success_rate

        if success:
            min_amount, max_amount = self.resource_steal_amounts[resource_type]
            steal_amount = random.randint(
                min_amount,
                min(max_amount, victim.resources[resource_type])
            )
            
            # Transfer resources
            victim.resources[resource_type] -= steal_amount
            thief.resources[resource_type] += steal_amount
            thief.update_steal_time()
            
            return True, {resource_type: steal_amount}
        
        thief.update_steal_time()
        return False, None

    def get_player_resources(self, player_id: str) -> Dict[ResourceType, int]:
        """Get a player's current resources."""
        if player_id not in self.players:
            raise ValueError(f"Player with ID {player_id} not found")
        return self.players[player_id].resources.copy()

    def get_leaderboard(self, resource_type: ResourceType) -> List[Tuple[str, int]]:
        """Get a leaderboard sorted by the specified resource type."""
        players = [
            (player.name, player.resources[resource_type])
            for player in self.players.values()
        ]
        return sorted(players, key=lambda x: x[1], reverse=True)


# Example usage
if __name__ == "__main__":
    sim = StealSimulator()
    
    # Add players
    sim.add_player("p1", "Alice")
    sim.add_player("p2", "Bob")
    
    # Give them some resources
    sim.add_resources("p1", ResourceType.CHEST, 5)
    sim.add_resources("p2", ResourceType.POOP, 10)
    
    # Attempt a steal
    success, stolen = sim.attempt_steal("p1", "p2", ResourceType.POOP)
    
    if success:
        print(f"Steal successful! Got {stolen[ResourceType.POOP]} poop!")
    else:
        print("Steal failed!")
    
    # Show leaderboard
    print("\nPoop Leaderboard:")
    for name, amount in sim.get_leaderboard(ResourceType.POOP):
        print(f"{name}: {amount}")
```
