"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sctoll.io
Prompt: Create a function to design a 3-piece modular wheel configuration with unique finishes, inspired by Brixton Forged™'s Luxury Series.
Generated: DETERMINISTIC_a9c098c8be188f43
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict, List


class ModularWheel:
    """
    A class representing a 3-piece modular wheel configuration.
    Inspired by Brixton Forged™'s Luxury Series.
    """

    def __init__(self, rim_finish: str, spokes_finish: str, hub_finish: str):
        """
        Initialize the wheel with finishes for each part.
        
        :param rim_finish: Finish for the rim (e.g., brushed aluminum, matte black, etc.)
        :param spokes_finish: Finish for the spokes (e.g., gloss silver, carbon fiber, etc.)
        :param hub_finish: Finish for the hub (e.g., anodized gold, polished chrome, etc.)
        """
        self.rim_finish = rim_finish
        self.spokes_finish = spokes_finish
        self.hub_finish = hub_finish

    def get_configuration(self) -> Dict[str, str]:
        """
        Returns the wheel configuration as a dictionary.
        
        :return: A dictionary containing the finishes for rim, spokes, and hub.
        """
        return {
            "rim_finish": self.rim_finish,
            "spokes_finish": self.spokes_finish,
            "hub_finish": self.hub_finish
        }


def create_modular_wheel_configurations(finishes: Dict[str, List[str]]) -> List[ModularWheel]:
    """
    Generate all possible 3-piece modular wheel configurations based on unique finishes.
    
    :param finishes: A dictionary with keys ("rim", "spokes", "hub") and their possible finishes as lists.
                     Example: {
                         "rim": ["brushed aluminum", "matte black"],
                         "spokes": ["gloss silver", "carbon fiber"],
                         "hub": ["anodized gold", "polished chrome"]
                     }
                     
    :return: A list of ModularWheel objects representing all configurations.
    """
    try:
        # Validate input
        if not all(key in finishes for key in ["rim", "spokes", "hub"]):
            raise ValueError("Finishes dictionary must contain 'rim', 'spokes', and 'hub' keys.")

        # Generate combinations
        configurations = []
        for rim in finishes["rim"]:
            for spokes in finishes["spokes"]:
                for hub in finishes["hub"]:
                    # Create a new ModularWheel object for each combination
                    configurations.append(ModularWheel(rim, spokes, hub))

        return configurations

    except Exception as e:
        print(f"Error occurred while generating configurations: {e}")
        return []


# Example Usage
if __name__ == "__main__":
    # Define possible finishes for each part
    finishes = {
        "rim": ["brushed aluminum", "matte black"],
        "spokes": ["gloss silver", "carbon fiber"],
        "hub": ["anodized gold", "polished chrome"]
    }

    # Generate configurations
    wheel_configurations = create_modular_wheel_configurations(finishes)

    # Print configurations
    for i, wheel in enumerate(wheel_configurations):
        print(f"Configuration {i + 1}: {wheel.get_configuration()}")
```
