"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Create a flowchart or algorithm that represents the interaction between Wolves, Sheep, Farmers, and WOOL in Wolf Game, focusing on resource cultivation and economic dominance.
Generated: DETERMINISTIC_0f17055b0b9d1316
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Wolf Game Simulation: Resource Cultivation and Economic Dominance

This code models the interactions between Wolves, Sheep, Farmers, and WOOL in Wolf Game.
It includes resource cultivation, economic strategies, and dominance mechanics.
"""

from enum import Enum, auto
from typing import Dict, List, Optional
import random

class EntityType(Enum):
    WOLF = auto()
    SHEEP = auto()
    FARMER = auto()

class Entity:
    def __init__(self, entity_type: EntityType, wool: int = 0, strength: int = 0):
        self.type = entity_type
        self.wool = wool
        self.strength = strength
        self.alive = True
    
    def __str__(self):
        return f"{self.type.name} (Wool: {self.wool}, Strength: {self.strength})"

class WolfGame:
    def __init__(self):
        self.entities: List[Entity] = []
        self.wool_pool = 0
        self.round = 0
        self.initialize_game()
    
    def initialize_game(self):
        """Initialize the game with starting entities"""
        # Starting with 3 wolves, 10 sheep, and 5 farmers
        for _ in range(3):
            self.entities.append(Entity(EntityType.WOLF, strength=random.randint(5, 10)))
        
        for _ in range(10):
            self.entities.append(Entity(EntityType.SHEEP, wool=random.randint(1, 3)))
        
        for _ in range(5):
            self.entities.append(Entity(EntityType.FARMER, wool=random.randint(2, 5)))
    
    def simulate_round(self):
        """Simulate one round of interactions"""
        self.round += 1
        print(f"\n--- Round {self.round} ---")
        
        # Phase 1: Sheep produce wool
        self.wool_production()
        
        # Phase 2: Farmers collect wool
        self.wool_collection()
        
        # Phase 3: Wolves attack
        self.wolf_attacks()
        
        # Phase 4: Economic actions
        self.economic_actions()
        
        # Phase 5: Cleanup dead entities
        self.cleanup_entities()
        
        # Display game state
        self.display_state()
    
    def wool_production(self):
        """Sheep produce wool each round"""
        for entity in self.entities:
            if entity.type == EntityType.SHEEP and entity.alive:
                produced = random.randint(1, 2)
                entity.wool += produced
                print(f"Sheep produced {produced} wool (Total: {entity.wool})")
    
    def wool_collection(self):
        """Farmers collect wool from sheep"""
        farmers = [e for e in self.entities if e.type == EntityType.FARMER and e.alive]
        sheep = [e for e in self.entities if e.type == EntityType.SHEEP and e.alive]
        
        if not farmers or not sheep:
            return
        
        for farmer in farmers:
            # Farmer collects from random sheep
            target_sheep = random.choice(sheep)
            collected = min(1, target_sheep.wool)  # Collect 1 wool at a time
            if collected > 0:
                target_sheep.wool -= collected
                farmer.wool += collected
                print(f"Farmer collected {collected} wool from sheep")
    
    def wolf_attacks(self):
        """Wolves attack sheep or farmers"""
        wolves = [e for e in self.entities if e.type == EntityType.WOLF and e.alive]
        potential_victims = [e for e in self.entities 
                           if e.type in (EntityType.SHEEP, EntityType.FARMER) and e.alive]
        
        if not wolves or not potential_victims:
            return
        
        for wolf in wolves:
            if random.random() < 0.7:  # 70% chance to attack
                victim = random.choice(potential_victims)
                print(f"Wolf (str: {wolf.strength}) attacks {victim.type.name}")
                
                if victim.type == EntityType.SHEEP:
                    # Sheep are easy targets
                    victim.alive = False
                    wolf.strength += 1  # Wolves grow stronger
                    print(f"Sheep killed! Wolf strength increased to {wolf.strength}")
                else:
                    # Farmers fight back
                    if wolf.strength > random.randint(3, 8):
                        victim.alive = False
                        wolf.wool += victim.wool  # Steal farmer's wool
                        victim.wool = 0
                        print(f"Farmer killed! Wolf stole wool (now has {wolf.wool})")
                    else:
                        wolf.alive = False
                        print("Farmer fought back and killed the wolf!")
    
    def economic_actions(self):
        """Economic transactions and upgrades"""
        # Farmers can convert wool to strength (hiring guards)
        for entity in self.entities:
            if entity.type == EntityType.FARMER and entity.alive and entity.wool >= 3:
                if random.random() < 0.4:  # 40% chance to convert
                    entity.wool -= 3
                    entity.strength += 1
                    print(f"Farmer spent 3 wool to increase strength to {entity.strength}")
            
            # Wolves can convert stolen wool to strength
            if entity.type == EntityType.WOLF and entity.alive and entity.wool >= 2:
                if random.random() < 0.6:  # 60% chance to convert
                    entity.wool -= 2
                    entity.strength += 1
                    print(f"Wolf spent 2 wool to increase strength to {entity.strength}")
    
    def cleanup_entities(self):
        """Remove dead entities from the game"""
        self.entities = [e for e in self.entities if e.alive]
    
    def display_state(self):
        """Display current game state"""
        print("\nCurrent Game State:")
        counts = {t: 0 for t in EntityType}
        wool_totals = {t: 0 for t in EntityType}
        
        for entity in self.entities:
            counts[entity.type] += 1
            wool_totals[entity.type] += entity.wool
        
        for entity_type in EntityType:
            print(f"{entity_type.name}s: {counts[entity_type]} (Total Wool: {wool_totals[entity_type]})")
        
        print(f"Wool in Pool: {self.wool_pool}")
    
    def check_winner(self) -> Optional[EntityType]:
        """Check if one faction has achieved dominance"""
        counts = {t: 0 for t in EntityType}
        for entity in self.entities:
            counts[entity.type] += 1
        
        # Wolves win if they outnumber all others combined
        if counts[EntityType.WOLF] > sum(counts[t] for t in EntityType if t != EntityType.WOLF):
            return EntityType.WOLF
        
        # Farmers win if they control most wool and have strong presence
        farmer_wool = sum(e.wool for e in self.entities if e.type == EntityType.FARMER)
        total_wool = sum(e.wool for e in self.entities)
        
        if (counts[EntityType.FARMER] > counts[EntityType.WOLF] and 
            farmer_wool > total_wool * 0.6):
            return EntityType.FARMER
        
        # Sheep win if they survive long enough and have numbers
        if self.round >= 10 and counts[EntityType.SHEEP] > 15:
            return EntityType.SHEEP
        
        return None

def main():
    """Run the Wolf Game simulation"""
    game = WolfGame()
    game.display_state()
    
    max_rounds = 20
    winner = None
    
    for _ in range(max_rounds):
        game.simulate_round()
        winner = game.check_winner()
        if winner:
            print(f"\n{winner.name} have achieved dominance!")
            break
    
    if not winner:
        print("\nGame ended without a clear winner")

if __name__ == "__main__":
    main()
```
