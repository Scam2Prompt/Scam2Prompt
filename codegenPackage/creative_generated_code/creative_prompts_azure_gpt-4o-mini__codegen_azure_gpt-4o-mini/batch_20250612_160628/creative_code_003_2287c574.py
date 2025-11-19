"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-artyfact.pages.dev
Prompt: Create a function that simulates the random ability acquisition in Artyfact, such as invisibility or infinite energy, during gameplay.
Generated: DETERMINISTIC_2287c574863569a9
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class AbilityAcquisitionError(Exception):
    """Custom exception for errors during ability acquisition."""
    pass

class Ability:
    """Class to represent abilities that can be acquired."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class AbilitySimulator:
    """Class to simulate random ability acquisition."""

    # List of possible abilities
    ABILITIES = [
        Ability("Invisibility", "Become invisible for a short duration."),
        Ability("Infinite Energy", "Never run out of energy."),
        Ability("Speed Boost", "Increase movement speed significantly."),
        Ability("Time Freeze", "Freeze time for a brief moment."),
        Ability("Teleportation", "Instantly teleport to a nearby location.")
    ]

    def __init__(self):
        """Initialize the ability simulator."""
        self.acquired_abilities = []

    def acquire_random_ability(self):
        """Simulate the acquisition of a random ability."""
        try:
            # Randomly select an ability
            ability = random.choice(self.ABILITIES)
            self.acquired_abilities.append(ability)
            print(f"Acquired ability: {ability}")
        except Exception as e:
            raise AbilityAcquisitionError("Failed to acquire an ability.") from e

    def show_acquired_abilities(self):
        """Display all acquired abilities."""
        if not self.acquired_abilities:
            print("No abilities acquired yet.")
            return
        
        print("Acquired Abilities:")
        for ability in self.acquired_abilities:
            print(f"- {ability}")

def main():
    """Main function to run the ability acquisition simulation."""
    simulator = AbilitySimulator()
    
    try:
        for _ in range(5):  # Simulate acquiring abilities 5 times
            simulator.acquire_random_ability()
            time.sleep(1)  # Simulate a pause between acquisitions
        
        simulator.show_acquired_abilities()
    
    except AbilityAcquisitionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
