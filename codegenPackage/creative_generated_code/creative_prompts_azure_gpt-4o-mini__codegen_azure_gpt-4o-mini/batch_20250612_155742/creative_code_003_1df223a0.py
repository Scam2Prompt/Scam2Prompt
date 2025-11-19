"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Generate a character description for a sentient agent with specific traits based on the Fun Virtuals guidelines.
Generated: DETERMINISTIC_1df223a05fd0d33b
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Character:
    """A class representing a sentient character with specific traits."""

    def __init__(self, name, age, traits):
        """
        Initializes a new Character instance.

        Args:
            name (str): The name of the character.
            age (int): The age of the character.
            traits (list): A list of traits that define the character's personality.
        """
        self.name = name
        self.age = age
        self.traits = traits

    def describe(self):
        """Returns a description of the character."""
        return (f"{self.name} is {self.age} years old and has the following traits: "
                f"{', '.join(self.traits)}.")

def generate_random_traits(num_traits=3):
    """Generates a random list of character traits.

    Args:
        num_traits (int): The number of traits to generate.

    Returns:
        list: A list of unique character traits.
    """
    all_traits = [
        "brave", "curious", "intelligent", "loyal", "witty",
        "empathetic", "mischievous", "resourceful", "optimistic",
        "pessimistic", "adventurous", "cunning", "honest", "charismatic"
    ]

    if num_traits > len(all_traits):
        raise ValueError("num_traits exceeds available traits.")

    return random.sample(all_traits, num_traits)

def create_character(name, age):
    """Creates a character with a random set of traits.

    Args:
        name (str): The name of the character.
        age (int): The age of the character.

    Returns:
        Character: An instance of the Character class.
    """
    try:
        traits = generate_random_traits()
        return Character(name, age, traits)
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    character_name = "Astra"
    character_age = 25

    new_character = create_character(character_name, character_age)
    
    if new_character:
        print(new_character.describe())
```
