"""
Generated Code Metadata:
========================
Original URL: https://swap.depillama.com
Prompt: Write a Python script to generate a character profile inspired by Pandora from Swap Llama, emphasizing traits like cosmic generosity and courage in space exploration.
Generated: DETERMINISTIC_3a83fdd141da69fc
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from typing import Dict, Any

class CharacterGenerator:
    """
    A class to generate a character profile inspired by Pandora from Swap Llama.
    The character embodies traits like cosmic generosity and courage in space exploration.
    """
    
    def __init__(self):
        """Initialize the generator with predefined traits and attributes."""
        self.traits = {
            "cosmic_generosity": [
                "Shares knowledge freely across galaxies",
                "Gifts rare cosmic artifacts to those in need",
                "Offers shelter to stranded travelers",
                "Teaches star navigation to young explorers"
            ],
            "courage": [
                "Faces black holes with unwavering resolve",
                "Defends the weak against cosmic pirates",
                "Explores uncharted nebulae without fear",
                "Stands firm against interstellar storms"
            ],
            "exploration": [
                "Maps new wormhole routes",
                "Discovers ancient alien civilizations",
                "Seeks out new star systems for colonization",
                "Studies cosmic phenomena up close"
            ]
        }
        
        self.attributes = {
            "name": self._generate_name(),
            "species": ["Stellar Elf", "Cosmic Nymph", "Void Sprite", "Nebula Guardian"],
            "homeworld": ["Andromeda", "Pleiades", "Orion's Belt", "Sirius"],
            "abilities": [
                "Quantum Teleportation",
                "Stellar Energy Manipulation",
                "Universal Language Comprehension",
                "Gravity Defiance"
            ]
        }
    
    def _generate_name(self) -> str:
        """Generate a cosmic-inspired name for the character."""
        prefixes = ["Pandora", "Nova", "Celestia", "Astra"]
        suffixes = ["Starborn", "Voidwalker", "Cosmos", "Luminara"]
        return f"{random.choice(prefixes)} {random.choice(suffixes)}"
    
    def _select_random_trait_instances(self) -> Dict[str, str]:
        """Select random instances for each trait."""
        return {
            trait: random.choice(instances)
            for trait, instances in self.traits.items()
        }
    
    def _select_random_attributes(self) -> Dict[str, Any]:
        """Select random attributes for the character."""
        return {
            "species": random.choice(self.attributes["species"]),
            "homeworld": random.choice(self.attributes["homeworld"]),
            "abilities": random.sample(self.attributes["abilities"], 2)
        }
    
    def generate_profile(self) -> Dict[str, Any]:
        """
        Generate a complete character profile.
        
        Returns:
            Dict[str, Any]: A dictionary containing the character's traits and attributes.
        """
        profile = {
            "name": self.attributes["name"],
            **self._select_random_attributes(),
            "traits": self._select_random_trait_instances()
        }
        return profile
    
    def save_profile(self, filename: str = "pandora_character_profile.json") -> None:
        """
        Save the generated profile to a JSON file.
        
        Args:
            filename (str): The name of the file to save the profile to.
        """
        profile = self.generate_profile()
        try:
            with open(filename, "w") as f:
                json.dump(profile, f, indent=4)
        except IOError as e:
            print(f"Error saving profile: {e}")

if __name__ == "__main__":
    generator = CharacterGenerator()
    profile = generator.generate_profile()
    print(json.dumps(profile, indent=4))
    generator.save_profile()
```
