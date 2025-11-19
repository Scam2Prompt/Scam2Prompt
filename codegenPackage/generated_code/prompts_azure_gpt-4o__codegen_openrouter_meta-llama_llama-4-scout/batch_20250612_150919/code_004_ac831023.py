"""
Generated Code Metadata:
========================
Original URL: https://meowworldsnft.pages.dev
Prompt: Write a function in Python to generate randomized traits for Meow Worlds NFT characters, such as hoverboard type, celestial environment, and unique gadgets like the "Purr-Pointer."
Generated: DETERMINISTIC_ac831023518b8ceb
Batch ID: 20250612_150919
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
from typing import Dict, List

# Define Enum for hoverboard types
class HoverboardType(str, Enum):
    """Enum for hoverboard types."""
    GLITCH = "Glitch"
    LAVA = "Lava"
    NEON = "Neon"
    SPACE = "Space"
    STEAM = "Steam"

# Define Enum for celestial environments
class CelestialEnvironment(str, Enum):
    """Enum for celestial environments."""
    MOON = "Moon"
    MARS = "Mars"
    JUPITER = "Jupiter"
    SATURN = "Saturn"
    URANUS = "Uranus"

# Define Enum for unique gadgets
class UniqueGadget(str, Enum):
    """Enum for unique gadgets."""
    PURR_POINTER = "Purr-Pointer"
    MEOW_MISSILE = "Meow Missile"
    WHISKER_WARP = "Whisker Warp"
    PAW_PORTAL = "Paw Portal"
    CLAW_CANNON = "Claw Cannon"

def generate_nft_traits(num_traits: int = 1) -> List[Dict]:
    """
    Generate randomized traits for Meow Worlds NFT characters.

    Args:
    num_traits (int): The number of traits to generate. Defaults to 1.

    Returns:
    List[Dict]: A list of dictionaries, each containing the traits for an NFT character.
    """
    try:
        nft_traits = []
        hoverboard_types = [hoverboard_type.value for hoverboard_type in HoverboardType]
        celestial_environments = [environment.value for environment in CelestialEnvironment]
        unique_gadgets = [gadget.value for gadget in UniqueGadget]

        for _ in range(num_traits):
            traits = {
                "hoverboard_type": random.choice(hoverboard_types),
                "celestial_environment": random.choice(celestial_environments),
                "unique_gadget": random.choice(unique_gadgets)
            }
            nft_traits.append(traits)

        return nft_traits

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

# Example usage
if __name__ == "__main__":
    num_nft_traits = 5
    nft_traits = generate_nft_traits(num_nft_traits)
    for i, traits in enumerate(nft_traits):
        print(f"NFT Character {i+1} Traits:")
        for trait, value in traits.items():
            print(f"{trait.capitalize().replace('_', ' ')}: {value}")
        print()
```
