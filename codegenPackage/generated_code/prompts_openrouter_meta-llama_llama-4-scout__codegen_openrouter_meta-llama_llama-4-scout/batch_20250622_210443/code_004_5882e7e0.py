"""
Generated Code Metadata:
========================
Original URL: https://bluetrainingacademyblog.com
Prompt: Compare and contrast different types of personal protective equipment (PPE) for flame resistance, citing examples from Blue Training Academy's PPE-related content.
Generated: DETERMINISTIC_5882e7e0bf7e4ab9
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define Enum for PPE types
class PPEType(Enum):
    """Enum for different types of personal protective equipment."""
    HELMET = "Helmet"
    GLOVES = "Gloves"
    JACKET = "Jacket"
    PANTS = "Pants"
    BOOTS = "Boots"

# Define data class for PPE
@dataclass
class PPE:
    """Data class representing personal protective equipment."""
    type: PPEType
    name: str
    flame_resistance_rating: str
    description: str

# Define a class for comparing PPE
class PPEComparator:
    """Class for comparing PPE flame resistance."""
    def __init__(self):
        self.ppe_list: List[PPE] = []

    def add_ppe(self, ppe: PPE):
        """Add PPE to the comparator."""
        self.ppe_list.append(ppe)

    def compare_flame_resistance(self):
        """Compare flame resistance of different PPE."""
        # Sort PPE by flame resistance rating
        sorted_ppe = sorted(self.ppe_list, key=lambda x: x.flame_resistance_rating)

        # Print comparison results
        print("Flame Resistance Comparison:")
        for i, ppe in enumerate(sorted_ppe):
            print(f"{i+1}. {ppe.name} ({ppe.type.value}): {ppe.flame_resistance_rating}")

    def get_ppe_examples(self):
        """Get examples of PPE from Blue Training Academy's content."""
        # Simulating retrieval of PPE examples from Blue Training Academy's content
        ppe_examples = [
            PPE(PPEType.HELMET, "Firefighter Helmet", "NFPA 2113", "Protects head from flames and heat."),
            PPE(PPEType.GLOVES, "Fire Resistant Gloves", "ASTM F1930", "Protects hands from flames and heat."),
            PPE(PPEType.JACKET, "Firefighter Jacket", "NFPA 2113", "Protects torso from flames and heat."),
            PPE(PPEType.PANTS, "Firefighter Pants", "NFPA 2113", "Protects legs from flames and heat."),
            PPE(PPEType.BOOTS, "Firefighter Boots", "ASTM F2413", "Protects feet from flames and heat."),
        ]
        return ppe_examples

def main():
    try:
        comparator = PPEComparator()
        ppe_examples = comparator.get_ppe_examples()

        # Add PPE examples to comparator
        for ppe in ppe_examples:
            comparator.add_ppe(ppe)

        # Compare flame resistance of PPE
        comparator.compare_flame_resistance()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
