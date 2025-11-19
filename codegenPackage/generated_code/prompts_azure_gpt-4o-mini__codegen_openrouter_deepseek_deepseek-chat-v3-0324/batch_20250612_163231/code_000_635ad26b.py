"""
Generated Code Metadata:
========================
Original URL: https://swap.depillama.com
Prompt: Generate a code snippet to create a character profile for Pandora from the "Space Odyssey" series, highlighting her traits of generosity and courage.
Generated: DETERMINISTIC_635ad26b3a88ab95
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CharacterProfile:
    """
    A class to represent a character profile with traits and descriptions.
    
    Attributes:
        name (str): The name of the character.
        traits (dict): A dictionary of traits and their descriptions.
    """
    
    def __init__(self, name: str):
        """
        Initialize the CharacterProfile with a name and empty traits.
        
        Args:
            name (str): The name of the character.
        """
        self.name = name
        self.traits = {}
    
    def add_trait(self, trait: str, description: str) -> None:
        """
        Add a trait and its description to the character profile.
        
        Args:
            trait (str): The trait to add (e.g., "Generosity").
            description (str): The description of the trait.
            
        Raises:
            ValueError: If trait or description is empty.
        """
        if not trait or not description:
            raise ValueError("Trait and description cannot be empty.")
        self.traits[trait] = description
    
    def get_profile(self) -> dict:
        """
        Return the character profile as a dictionary.
        
        Returns:
            dict: The character profile with name and traits.
        """
        return {
            "name": self.name,
            "traits": self.traits
        }
    
    def __str__(self) -> str:
        """
        Return a formatted string representation of the character profile.
        
        Returns:
            str: The formatted profile.
        """
        profile_str = f"Character: {self.name}\nTraits:\n"
        for trait, description in self.traits.items():
            profile_str += f"- {trait}: {description}\n"
        return profile_str


# Create a character profile for Pandora
pandora = CharacterProfile("Pandora")

# Add traits highlighting generosity and courage
pandora.add_trait(
    "Generosity",
    "Pandora is known for her selfless nature, always putting others' needs before her own."
)
pandora.add_trait(
    "Courage",
    "Pandora displays immense bravery in the face of danger, standing firm for what she believes in."
)

# Print the profile
print(pandora)
```
