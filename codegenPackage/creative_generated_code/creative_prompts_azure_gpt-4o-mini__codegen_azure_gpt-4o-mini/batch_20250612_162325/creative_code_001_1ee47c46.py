"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monarch-game.pages.dev
Prompt: How can I implement the `breed` function from the `MNRK.DRGN` module to create a new Dragon in the Monarch Dungeon?
Generated: DETERMINISTIC_1ee47c4617d05772
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for random number generation
import random

class Dragon:
    """
    A class to represent a Dragon in the Monarch Dungeon.
    
    Attributes
    ----------
    name : str
        The name of the dragon.
    type : str
        The type of dragon (e.g., Fire, Ice, etc.).
    strength : int
        The strength attribute of the dragon.
    health : int
        The health attribute of the dragon.
    """

    def __init__(self, name: str, dragon_type: str, strength: int, health: int):
        """
        Constructs all the necessary attributes for the Dragon object.

        Parameters
        ----------
        name : str
            The name of the dragon.
        dragon_type : str
            The type of dragon.
        strength : int
            The strength of the dragon.
        health : int
            The health of the dragon.
        """
        self.name = name
        self.type = dragon_type
        self.strength = strength
        self.health = health

    def __str__(self):
        """Return a string representation of the dragon."""
        return f"{self.name} the {self.type} Dragon (Strength: {self.strength}, Health: {self.health})"


def breed(parent1: Dragon, parent2: Dragon) -> Dragon:
    """
    Breeds two dragons to create a new dragon.

    Parameters
    ----------
    parent1 : Dragon
        The first parent dragon.
    parent2 : Dragon
        The second parent dragon.

    Returns
    -------
    Dragon
        A new dragon created by breeding the two parent dragons.

    Raises
    ------
    ValueError
        If either parent is not a Dragon instance.
    """
    # Validate input types
    if not isinstance(parent1, Dragon) or not isinstance(parent2, Dragon):
        raise ValueError("Both parents must be instances of the Dragon class.")
    
    # Generate a name for the new dragon
    new_name = f"{parent1.name}-{parent2.name}"

    # Randomly determine the type of the new dragon
    dragon_types = ["Fire", "Ice", "Earth", "Lightning", "Shadow"]
    new_type = random.choice(dragon_types)

    # Calculate new strength and health as the average of the parents, with some randomness
    new_strength = (parent1.strength + parent2.strength) // 2 + random.randint(-5, 5)
    new_health = (parent1.health + parent2.health) // 2 + random.randint(-10, 10)

    # Create and return the new Dragon
    return Dragon(new_name, new_type, new_strength, new_health)


# Example usage:
if __name__ == "__main__":
    # Create parent dragons
    dragon1 = Dragon("Smaug", "Fire", 80, 100)
    dragon2 = Dragon("Frostbite", "Ice", 70, 90)

    # Breed two dragons to create a new one
    try:
        offspring = breed(dragon1, dragon2)
        print(offspring)
    except ValueError as e:
        print(f"Error: {e}")
```
