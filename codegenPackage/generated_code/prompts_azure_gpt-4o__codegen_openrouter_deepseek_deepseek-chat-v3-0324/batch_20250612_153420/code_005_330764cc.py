"""
Generated Code Metadata:
========================
Original URL: https://mara-otherside.pages.dev
Prompt: Create a code snippet to randomly select a Parasite visual trait for a Kodamara, ensuring guaranteed application when fragments are used.
Generated: DETERMINISTIC_330764ccab8d940a
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional

class KodamaraParasiteTraits:
    """
    A class to manage and randomly select Parasite visual traits for Kodamara.
    """
    
    def __init__(self):
        self.traits: Dict[str, List[str]] = {
            "eye_color": ["Red", "Black", "White", "Glowing", "Heterochromatic"],
            "skin_markings": ["Veins", "Patches", "Scales", "Cracks", "Bioluminescent"],
            "limb_modification": ["Extra Joints", "Elongated", "Tendrils", "Claws", "Membranes"],
            "movement_style": ["Fluid", "Jerky", "Slithering", "Floating", "Teleporting"]
        }
        self.guaranteed_traits: Dict[str, List[str]] = {
            "fragment_effect": ["Eyes Glow Brighter", "Markings Pulse", "Limbs Shift", "Movement Distorts"]
        }
    
    def get_random_trait(self, category: str) -> Optional[str]:
        """
        Randomly select a trait from the specified category.
        
        Args:
            category: The trait category to select from.
            
        Returns:
            A randomly selected trait or None if category doesn't exist.
        """
        if category not in self.traits:
            return None
        return random.choice(self.traits[category])
    
    def apply_fragment_effect(self) -> str:
        """
        Apply a guaranteed fragment effect trait.
        
        Returns:
            A guaranteed fragment effect trait.
        """
        return random.choice(self.guaranteed_traits["fragment_effect"])
    
    def generate_full_traits(self, use_fragment: bool = False) -> Dict[str, str]:
        """
        Generate a full set of random traits with optional fragment effect.
        
        Args:
            use_fragment: Whether to include a guaranteed fragment effect.
            
        Returns:
            A dictionary of all selected traits.
        """
        traits = {
            "eye_color": self.get_random_trait("eye_color"),
            "skin_markings": self.get_random_trait("skin_markings"),
            "limb_modification": self.get_random_trait("limb_modification"),
            "movement_style": self.get_random_trait("movement_style")
        }
        
        if use_fragment:
            traits["fragment_effect"] = self.apply_fragment_effect()
        
        return traits

# Example usage
if __name__ == "__main__":
    parasite_traits = KodamaraParasiteTraits()
    
    # Random traits without fragment
    print("Random Traits:")
    print(parasite_traits.generate_full_traits())
    
    # Random traits with fragment effect
    print("\nRandom Traits with Fragment Effect:")
    print(parasite_traits.generate_full_traits(use_fragment=True))
```
