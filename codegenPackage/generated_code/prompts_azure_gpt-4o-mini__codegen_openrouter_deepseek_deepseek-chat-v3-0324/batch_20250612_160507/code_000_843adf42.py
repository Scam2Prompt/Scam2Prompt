"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Write a Python script that simulates survival scenarios for characters stranded on an island, incorporating elements from "The Cannibals" project, such as resource management and alliance creation.
Generated: DETERMINISTIC_843adf42dc6dd973
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import sys
from typing import Dict, List, Optional, Tuple

class Character:
    """Represents a character stranded on the island."""
    
    def __init__(self, name: str, strength: int, intelligence: int, charisma: int):
        """Initialize a character with attributes.
        
        Args:
            name: Character's name
            strength: Physical capability (1-10)
            intelligence: Mental capability (1-10)
            charisma: Social capability (1-10)
        """
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.charisma = charisma
        self.health = 100
        self.hunger = 0
        self.allies: List['Character'] = []
        self.resources: Dict[str, int] = {
            'food': 0,
            'water': 0,
            'tools': 0
        }
    
    def __str__(self) -> str:
        return (f"{self.name} (Health: {self.health}, Hunger: {self.hunger}, "
                f"Strength: {self.strength}, Intelligence: {self.intelligence}, "
                f"Charisma: {self.charisma})")
    
    def is_alive(self) -> bool:
        """Check if the character is still alive."""
        return self.health > 0
    
    def add_ally(self, ally: 'Character') -> bool:
        """Attempt to add an ally to this character's group.
        
        Args:
            ally: The character to ally with
            
        Returns:
            True if alliance successful, False otherwise
        """
        if ally in self.allies:
            return True
            
        # Higher charisma increases chance of successful alliance
        success_chance = min(90, 30 + (self.charisma * 5))
        if random.randint(1, 100) <= success_chance:
            self.allies.append(ally)
            ally.allies.append(self)
            return True
        return False
    
    def gather_resource(self, resource_type: str) -> bool:
        """Attempt to gather a resource.
        
        Args:
            resource_type: Type of resource to gather ('food', 'water', 'tools')
            
        Returns:
            True if resource gathered successfully, False otherwise
        """
        if resource_type not in self.resources:
            return False
            
        # Higher strength helps with gathering
        success_chance = min(90, 30 + (self.strength * 5))
        if random.randint(1, 100) <= success_chance:
            self.resources[resource_type] += 1
            return True
        return False
    
    def consume_resource(self, resource_type: str) -> bool:
        """Consume a resource to reduce hunger or restore health.
        
        Args:
            resource_type: Type of resource to consume
            
        Returns:
            True if resource consumed successfully, False otherwise
        """
        if resource_type not in self.resources or self.resources[resource_type] <= 0:
            return False
            
        self.resources[resource_type] -= 1
        
        if resource_type == 'food':
            self.hunger = max(0, self.hunger - 20)
            self.health = min(100, self.health + 5)
        elif resource_type == 'water':
            self.health = min(100, self.health + 10)
            
        return True
    
    def daily_update(self) -> None:
        """Update character's status at the end of each day."""
        self.hunger += 10
        if self.hunger >= 100:
            self.health -= 20
        elif self.hunger >= 50:
            self.health -= 5
            
        # Random events
        if random.random() < 0.2:  # 20% chance of random event
            event = random.choice(['injury', 'find_resource', 'nothing'])
            if event == 'injury':
                self.health -= random.randint(5, 20)
            elif event == 'find_resource':
                found_type = random.choice(list(self.resources.keys()))
                self.resources[found_type] += 1

class IslandSimulation:
    """Simulates survival scenarios for characters on an island."""
    
    def __init__(self, num_characters: int = 5, days_to_simulate: int = 30):
        """Initialize the simulation.
        
        Args:
            num_characters: Number of characters to simulate
            days_to_simulate: Number of days to run the simulation
        """
        self.characters: List[Character] = []
        self.days_elapsed = 0
        self.days_to_simulate = days_to_simulate
        self._initialize_characters(num_characters)
    
    def _initialize_characters(self, num_characters: int) -> None:
        """Create initial characters with random attributes."""
        names = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 
                 'Riley', 'Jamie', 'Quinn', 'Dakota', 'Skyler']
        random.shuffle(names)
        
        for i in range(min(num_characters, len(names))):
            strength = random.randint(1, 10)
            intelligence = random.randint(1, 10)
            charisma = random.randint(1, 10)
            self.characters.append(
                Character(names[i], strength, intelligence, charisma)
            )
    
    def _daily_actions(self) -> None:
        """Perform daily actions for all characters."""
        for character in self.characters:
            if not character.is_alive():
                continue
                
            # Decide action based on needs
            if character.hunger > 50 or character.health < 50:
                # Try to consume resources first
                if character.hunger > 50 and character.resources['food'] > 0:
                    character.consume_resource('food')
                elif character.health < 50 and character.resources['water'] > 0:
                    character.consume_resource('water')
                else:
                    # Gather resources if needed
                    resource_to_gather = random.choice(['food', 'water', 'tools'])
                    character.gather_resource(resource_to_gather)
            else:
                # Form alliances if basic needs are met
                potential_allies = [c for c in self.characters 
                                  if c != character and c.is_alive() 
                                  and c not in character.allies]
                if potential_allies:
                    chosen_ally = random.choice(potential_allies)
                    character.add_ally(chosen_ally)
    
    def _daily_update(self) -> None:
        """Update all characters at the end of the day."""
        for character in self.characters:
            if character.is_alive():
                character.daily_update()
    
    def _print_status(self) -> None:
        """Print current status of the simulation."""
        alive_characters = [c for c in self.characters if c.is_alive()]
        print(f"\nDay {self.days_elapsed}/{self.days_to_simulate}")
        print(f"Survivors: {len(alive_characters)}/{len(self.characters)}")
        
        for character in alive_characters:
            print(f"{character.name}: Health={character.health}, Hunger={character.hunger}")
            print(f"  Resources: Food={character.resources['food']}, "
                  f"Water={character.resources['water']}, Tools={character.resources['tools']}")
            if character.allies:
                ally_names = [ally.name for ally in character.allies]
                print(f"  Allies: {', '.join(ally_names)}")
    
    def run_simulation(self) -> None:
        """Run the full simulation."""
        print("Starting Island Survival Simulation")
        print("Initial Survivors:")
        for character in self.characters:
            print(f"- {character}")
        
        while self.days_elapsed < self.days_to_simulate and any(c.is_alive() for c in self.characters):
            self.days_elapsed += 1
            self._daily_actions()
            self._daily_update()
            
            if self.days_elapsed % 5 == 0 or self.days_elapsed == 1:
                self._print_status()
        
        self._print_final_results()
    
    def _print_final_results(self) -> None:
        """Print the final results of the simulation."""
        alive_characters = [c for c in self.characters if c.is_alive()]
        print("\n=== Simulation Results ===")
        print(f"Days survived: {self.days_elapsed}")
        print(f"Survivors remaining: {len(alive_characters)}/{len(self.characters)}")
        
        if alive_characters:
            print("\nSurvivors:")
            for character in alive_characters:
                print(f"- {character.name} (Allies: {len(character.allies)})")
        else:
            print("\nAll characters perished.")

def main():
    """Main function to run the simulation."""
    try:
        num_characters = int(input("Enter number of characters (3-10): "))
        if num_characters < 3 or num_characters > 10:
            print("Invalid input. Using default value (5
