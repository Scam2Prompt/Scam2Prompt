"""
Generated Code Metadata:
========================
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Create a script to generate detailed character profiles for virtual agents, including personality, appearance, and emotional traits, based on the examples provided on the Fun Virtuals Agent site.
Generated: DETERMINISTIC_7114217cc4beb0c5
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import Dict, List, Optional

class CharacterProfileGenerator:
    """
    Generates detailed character profiles for virtual agents.
    Includes personality traits, appearance details, and emotional characteristics.
    """
    
    def __init__(self):
        self.traits = self._load_traits()
    
    def _load_traits(self) -> Dict[str, Dict[str, List[str]]]:
        """Load predefined traits from a JSON file or use defaults."""
        try:
            with open('traits.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self._get_default_traits()
    
    def _get_default_traits(self) -> Dict[str, Dict[str, List[str]]]:
        """Return default traits if no JSON file is found."""
        return {
            "personality": {
                "primary": ["Outgoing", "Reserved", "Analytical", "Creative", "Empathetic"],
                "secondary": ["Witty", "Serious", "Playful", "Skeptical", "Optimistic"]
            },
            "appearance": {
                "gender": ["Male", "Female", "Non-binary"],
                "hair_color": ["Black", "Blonde", "Brown", "Red", "Gray"],
                "eye_color": ["Blue", "Green", "Brown", "Hazel", "Gray"],
                "body_type": ["Slender", "Athletic", "Average", "Stocky"]
            },
            "emotional": {
                "mood": ["Cheerful", "Melancholic", "Calm", "Anxious", "Excited"],
                "response_style": ["Logical", "Emotional", "Neutral", "Humorous"]
            },
            "background": {
                "occupation": ["Scientist", "Artist", "Engineer", "Writer", "Chef"],
                "hobbies": ["Reading", "Gaming", "Cooking", "Hiking", "Painting"]
            }
        }
    
    def _select_random(self, category: str, subcategory: str) -> str:
        """Randomly select a trait from the specified category and subcategory."""
        try:
            return random.choice(self.traits[category][subcategory])
        except KeyError:
            raise ValueError(f"Invalid category or subcategory: {category}/{subcategory}")
    
    def generate_profile(self, name: str, seed: Optional[int] = None) -> Dict[str, Dict[str, str]]:
        """
        Generate a complete character profile.
        
        Args:
            name: Character's name
            seed: Optional seed for reproducible results
            
        Returns:
            Dictionary containing all profile attributes
        """
        if seed is not None:
            random.seed(seed)
        
        return {
            "basic_info": {
                "name": name,
                "gender": self._select_random("appearance", "gender"),
                "age": str(random.randint(18, 65))
            },
            "personality": {
                "primary": self._select_random("personality", "primary"),
                "secondary": self._select_random("personality", "secondary"),
                "traits": f"{self._select_random('emotional', 'mood')}, {self._select_random('emotional', 'response_style')}"
            },
            "appearance": {
                "hair_color": self._select_random("appearance", "hair_color"),
                "eye_color": self._select_random("appearance", "eye_color"),
                "body_type": self._select_random("appearance", "body_type"),
                "distinctive_feature": random.choice(["Tattoo", "Scar", "Glasses", "Piercing", "Unique hairstyle"])
            },
            "background": {
                "occupation": self._select_random("background", "occupation"),
                "hobbies": self._select_random("background", "hobbies"),
                "origin": random.choice(["Urban", "Rural", "Suburban", "Nomadic"])
            },
            "preferences": {
                "likes": random.choice(["Technology", "Nature", "Art", "Music", "Sports"]),
                "dislikes": random.choice(["Loud noises", "Routine", "Conflict", "Messiness"])
            }
        }
    
    def save_profile(self, profile: Dict, filename: str) -> None:
        """Save the generated profile to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(profile, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save profile: {e}")

# Example usage
if __name__ == "__main__":
    generator = CharacterProfileGenerator()
    
    try:
        profile = generator.generate_profile("Alex")
        print(json.dumps(profile, indent=4))
        
        generator.save_profile(profile, "alex_profile.json")
        print("Profile saved successfully.")
    except Exception as e:
        print(f"Error generating profile: {e}")
```
