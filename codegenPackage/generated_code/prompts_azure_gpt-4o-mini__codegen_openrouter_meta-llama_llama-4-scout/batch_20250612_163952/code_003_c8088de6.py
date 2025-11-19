"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Develop a script that categorizes various types of knitted fabrics, including single jersey and terry fleece, for a textile e-commerce platform.
Generated: DETERMINISTIC_c8088de67fb4441c
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fabric_categorizer.py

from enum import Enum
from typing import Dict, List

class FabricType(str, Enum):
    """Enum for fabric types."""
    SINGLE_JERSEY = "single_jersey"
    TERRY_FLEECE = "terry_fleece"
    INTERLOCK = "interlock"
    RIB = "rib"
    FRENCH_TERRY = "french_terry"

class Fabric:
    """Class representing a fabric."""
    def __init__(self, name: str, fabric_type: FabricType, weight: float, material: str):
        """
        Initialize a Fabric object.

        Args:
        - name (str): The name of the fabric.
        - fabric_type (FabricType): The type of the fabric.
        - weight (float): The weight of the fabric in grams per square meter.
        - material (str): The material of the fabric.
        """
        self.name = name
        self.fabric_type = fabric_type
        self.weight = weight
        self.material = material

    def __str__(self):
        return f"{self.name} ({self.fabric_type.value}) - {self.material}, {self.weight} g/m²"

class FabricCategorizer:
    """Class for categorizing fabrics."""
    def __init__(self):
        self.fabrics: Dict[FabricType, List[Fabric]] = {
            FabricType.SINGLE_JERSEY: [],
            FabricType.TERRY_FLEECE: [],
            FabricType.INTERLOCK: [],
            FabricType.RIB: [],
            FabricType.FRENCH_TERRY: [],
        }

    def add_fabric(self, fabric: Fabric):
        """
        Add a fabric to the categorizer.

        Args:
        - fabric (Fabric): The fabric to add.

        Raises:
        - ValueError: If the fabric type is not recognized.
        """
        if fabric.fabric_type not in self.fabrics:
            raise ValueError(f"Unrecognized fabric type: {fabric.fabric_type.value}")
        self.fabrics[fabric.fabric_type].append(fabric)

    def get_fabrics_by_type(self, fabric_type: FabricType) -> List[Fabric]:
        """
        Get a list of fabrics of a specific type.

        Args:
        - fabric_type (FabricType): The type of fabrics to retrieve.

        Returns:
        - List[Fabric]: A list of fabrics of the specified type.
        """
        return self.fabrics.get(fabric_type, [])

    def __str__(self):
        result = "Fabric Categorizer:\n"
        for fabric_type, fabrics in self.fabrics.items():
            result += f"- {fabric_type.value}:\n"
            for fabric in fabrics:
                result += f"  - {fabric}\n"
        return result

def main():
    categorizer = FabricCategorizer()

    # Create fabrics
    fabric1 = Fabric("Soft Touch", FabricType.SINGLE_JERSEY, 150.0, "Cotton")
    fabric2 = Fabric("Cozy Fleece", FabricType.TERRY_FLEECE, 300.0, "Polyester")
    fabric3 = Fabric("Summer Interlock", FabricType.INTERLOCK, 120.0, "Cotton-Blend")

    # Add fabrics to categorizer
    categorizer.add_fabric(fabric1)
    categorizer.add_fabric(fabric2)
    categorizer.add_fabric(fabric3)

    # Print categorized fabrics
    print(categorizer)

    # Get fabrics by type
    single_jersey_fabrics = categorizer.get_fabrics_by_type(FabricType.SINGLE_JERSEY)
    print("\nSingle Jersey Fabrics:")
    for fabric in single_jersey_fabrics:
        print(fabric)

if __name__ == "__main__":
    main()
```
