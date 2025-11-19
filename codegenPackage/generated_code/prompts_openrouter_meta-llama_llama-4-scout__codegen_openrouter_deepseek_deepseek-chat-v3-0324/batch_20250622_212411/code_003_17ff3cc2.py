"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Design a simulation-based game like Parallel Colony, where players can interact with their avatars and make decisions that impact the game world.
Generated: DETERMINISTIC_17ff3cc2514f9df7
Batch ID: 20250622_212411
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
from enum import Enum, auto
import uuid


class ResourceType(Enum):
    FOOD = auto()
    WATER = auto()
    ENERGY = auto()
    MATERIALS = auto()


class DecisionType(Enum):
    EXPLORE = auto()
    BUILD = auto()
    GATHER = auto()
    RESEARCH = auto()
    SOCIALIZE = auto()


class AvatarState(Enum):
    IDLE = auto()
    WORKING = auto()
    RESTING = auto()
    SOCIALIZING = auto()


class Avatar:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.state = AvatarState.IDLE
        self.skills: Dict[str, int] = {
            "exploration": random.randint(1, 5),
            "construction": random.randint(1, 5),
            "gathering": random.randint(1, 5),
            "research": random.randint(1, 5),
            "social": random.randint(1, 5),
        }
        self.energy = 100
        self.happiness = 100
        self.inventory: Dict[ResourceType, int] = {
            ResourceType.FOOD: 10,
            ResourceType.WATER: 10,
            ResourceType.ENERGY: 10,
            ResourceType.MATERIALS: 5,
        }

    def update_state(self, new_state: AvatarState) -> None:
        """Update the avatar's current state."""
        self.state = new_state

    def consume_resources(self) -> None:
        """Consume resources over time."""
        self.energy = max(0, self.energy - 5)
        self.happiness = max(0, self.happiness - 2)
        
        if self.inventory[ResourceType.FOOD] > 0:
            self.inventory[ResourceType.FOOD] -= 1
        else:
            self.energy = max(0, self.energy - 10)
            
        if self.inventory[ResourceType.WATER] > 0:
            self.inventory[ResourceType.WATER] -= 1
        else:
            self.energy = max(0, self.energy - 10)

    def perform_action(self, decision: DecisionType) -> Dict[ResourceType, int]:
        """Perform an action based on decision type."""
        self.update_state(AvatarState.WORKING)
        results: Dict[ResourceType, int] = {}
        
        if decision == DecisionType.EXPLORE:
            results[ResourceType.MATERIALS] = random.randint(1, 3) * self.skills["exploration"]
            self.energy = max(0, self.energy - 15)
            
        elif decision == DecisionType.BUILD:
            if self.inventory[ResourceType.MATERIALS] >= 5:
                self.inventory[ResourceType.MATERIALS] -= 5
                results[ResourceType.ENERGY] = 10 * self.skills["construction"]
            self.energy = max(0, self.energy - 20)
            
        elif decision == DecisionType.GATHER:
            results[ResourceType.FOOD] = random.randint(1, 5) * self.skills["gathering"]
            results[ResourceType.WATER] = random.randint(1, 3) * self.skills["gathering"]
            self.energy = max(0, self.energy - 10)
            
        elif decision == DecisionType.RESEARCH:
            skill = random.choice(list(self.skills.keys()))
            self.skills[skill] += 1
            self.energy = max(0, self.energy - 15)
            
        elif decision == DecisionType.SOCIALIZE:
            self.happiness = min(100, self.happiness + 10 * self.skills["social"])
            self.energy = max(0, self.energy - 5)
            self.update_state(AvatarState.SOCIALIZING)
            
        return results

    def rest(self) -> None:
        """Rest to recover energy."""
        self.update_state(AvatarState.RESTING)
        self.energy = min(100, self.energy + 20)
        self.happiness = min(100, self.happiness + 5)


class GameWorld:
    def __init__(self):
        self.avatars: Dict[str, Avatar] = {}
        self.resources: Dict[ResourceType, int] = {
            ResourceType.FOOD: 50,
            ResourceType.WATER: 50,
            ResourceType.ENERGY: 50,
            ResourceType.MATERIALS: 30,
        }
        self.day = 1
        self.events: List[str] = []

    def add_avatar(self, name: str) -> Avatar:
        """Add a new avatar to the game world."""
        avatar = Avatar(name)
        self.avatars[avatar.id] = avatar
        self.events.append(f"New avatar '{name}' joined the colony.")
        return avatar

    def remove_avatar(self, avatar_id: str) -> None:
        """Remove an avatar from the game world."""
        if avatar_id in self.avatars:
            avatar = self.avatars.pop(avatar_id)
            self.events.append(f"Avatar '{avatar.name}' left the colony.")

    def update_world(self) -> None:
        """Update the game world state."""
        self.day += 1
        self.events.append(f"Day {self.day} begins.")
        
        # Process each avatar
        for avatar in self.avatars.values():
            avatar.consume_resources()
            
            # Random event chance
            if random.random() < 0.1:
                event = random.choice([
                    "Found a hidden cache of resources!",
                    "Encountered a friendly traveler.",
                    "Discovered a new area to explore.",
                    "Had a great idea for improvement."
                ])
                self.events.append(f"{avatar.name}: {event}")
                
        # Generate some resources
        self.resources[ResourceType.FOOD] += random.randint(5, 10)
        self.resources[ResourceType.WATER] += random.randint(3, 7)
        
        # Clean up old events
        if len(self.events) > 20:
            self.events = self.events[-20:]

    def distribute_resources(self, avatar_id: str, resources: Dict[ResourceType, int]) -> None:
        """Distribute resources to the colony or avatar."""
        avatar = self.avatars.get(avatar_id)
        if not avatar:
            return
            
        for resource_type, amount in resources.items():
            if resource_type in self.resources:
                self.resources[resource_type] += amount
            else:
                avatar.inventory[resource_type] = avatar.inventory.get(resource_type, 0) + amount


class Game:
    def __init__(self):
        self.world = GameWorld()
        self.is_running = False

    def start(self) -> None:
        """Start the game simulation."""
        self.is_running = True
        print("Parallel Colony simulation started!")
        
        # Add some initial avatars
        self.world.add_avatar("Alex")
        self.world.add_avatar("Sam")
        self.world.add_avatar("Taylor")

    def stop(self) -> None:
        """Stop the game simulation."""
        self.is_running = False
        print("Simulation stopped.")

    def run_simulation(self, days: int) -> None:
        """Run the simulation for a number of days."""
        if not self.is_running:
            print("Simulation not started yet.")
            return
            
        for _ in range(days):
            self.world.update_world()
            self.process_avatar_decisions()
            time.sleep(1)  # Simulate time passing
            
            # Print summary
            print(f"\nDay {self.world.day} Summary:")
            print("Recent events:")
            for event in self.world.events[-5:]:
                print(f"- {event}")
                
            print("\nColony resources:")
            for resource, amount in self.world.resources.items():
                print(f"{resource.name}: {amount}")
                
            print("\nAvatar status:")
            for avatar in self.world.avatars.values():
                print(f"{avatar.name}: Energy={avatar.energy}, Happiness={avatar.happiness}")

    def process_avatar_decisions(self) -> None:
        """Process decisions for all avatars."""
        for avatar in self.world.avatars.values():
            if avatar.energy < 20:
                avatar.rest()
                continue
                
            decision = random.choice(list(DecisionType))
            results = avatar.perform_action(decision)
            self.world.distribute_resources(avatar.id, results)
            
            # Random chance to rest after action
            if random.random() < 0.3:
                avatar.rest()


def main():
    """Main function to run the game."""
    game = Game()
    game.start()
    
    try:
        game.run_simulation(10)
    except KeyboardInterrupt:
        game.stop()
    finally:
        print("Simulation ended.")


if __name__ == "__main__":
    main()
```
