"""
Generated Code Metadata:
========================
Original URL: https://presale-artyfact.pages.dev
Prompt: Create a function that simulates the random ability acquisition in Artyfact, such as invisibility or infinite energy, during gameplay.
Generated: DETERMINISTIC_2287c574863569a9
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List

class AbilityType(Enum):
    """Enum for ability types."""
    INVISIBILITY = "invisibility"
    INFINITE_ENERGY = "infinite_energy"
    SUPER_SPEED = "super_speed"
    SHIELD = "shield"
    TELEPORTATION = "teleportation"

class Ability:
    """Class representing an ability."""
    def __init__(self, ability_type: AbilityType, duration: int):
        """
        Initialize an ability.

        Args:
        ability_type (AbilityType): The type of the ability.
        duration (int): The duration of the ability in seconds.
        """
        self.ability_type = ability_type
        self.duration = duration

    def __str__(self):
        return f"{self.ability_type.value} for {self.duration} seconds"

def acquire_random_ability(available_abilities: List[AbilityType], min_duration: int, max_duration: int) -> Ability:
    """
    Simulate the random acquisition of an ability.

    Args:
    available_abilities (List[AbilityType]): A list of available abilities.
    min_duration (int): The minimum duration of the ability in seconds.
    max_duration (int): The maximum duration of the ability in seconds.

    Returns:
    Ability: The acquired ability.

    Raises:
    ValueError: If the list of available abilities is empty.
    """
    if not available_abilities:
        raise ValueError("List of available abilities cannot be empty")

    # Randomly select an ability type from the list of available abilities
    ability_type = random.choice(available_abilities)
    
    # Randomly generate a duration between min_duration and max_duration
    duration = random.randint(min_duration, max_duration)

    return Ability(ability_type, duration)

def main():
    available_abilities = [AbilityType.INVISIBILITY, AbilityType.INFINITE_ENERGY, AbilityType.SUPER_SPEED]
    min_duration = 10
    max_duration = 60

    try:
        acquired_ability = acquire_random_ability(available_abilities, min_duration, max_duration)
        print(f"Acquired ability: {acquired_ability}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
