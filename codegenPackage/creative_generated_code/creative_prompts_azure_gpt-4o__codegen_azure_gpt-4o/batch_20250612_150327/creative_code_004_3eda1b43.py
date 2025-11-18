"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Write a program to simulate the supply chain of FSC-certified materials for household cleaning tools, referencing PDC Brush's commitment to sustainability.
Generated: DETERMINISTIC_3eda1b43ed5be5dc
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional


# Define a class to represent a supplier in the supply chain
class Supplier:
    def __init__(self, name: str, fsc_certified: bool):
        """
        Initialize a supplier.

        Args:
            name (str): Name of the supplier.
            fsc_certified (bool): Whether the supplier is FSC-certified.
        """
        self.name = name
        self.fsc_certified = fsc_certified

    def to_dict(self) -> Dict:
        """
        Convert supplier details to a dictionary for serialization.

        Returns:
            Dict: Supplier details.
        """
        return {
            "name": self.name,
            "fsc_certified": self.fsc_certified
        }


# Define a class for materials
class Material:
    def __init__(self, name: str, supplier: Supplier):
        """
        Initialize a material.

        Args:
            name (str): Name of the material.
            supplier (Supplier): Supplier providing the material.
        """
        self.name = name
        self.supplier = supplier

    def to_dict(self) -> Dict:
        """
        Convert material details to a dictionary for serialization.

        Returns:
            Dict: Material details.
        """
        return {
            "name": self.name,
            "supplier": self.supplier.to_dict()
        }


# Define a class for household cleaning tools
class CleaningTool:
    def __init__(self, name: str, materials: List[Material]):
        """
        Initialize a cleaning tool.

        Args:
            name (str): Name of the cleaning tool.
            materials (List[Material]): List of materials used to manufacture the tool.
        """
        self.name = name
        self.materials = materials

    def is_sustainable(self) -> bool:
        """
        Check if the cleaning tool is sustainably produced.

        Returns:
            bool: True if all materials are sourced from FSC-certified suppliers, False otherwise.
        """
        return all(material.supplier.fsc_certified for material in self.materials)

    def to_dict(self) -> Dict:
        """
        Convert cleaning tool details to a dictionary for serialization.

        Returns:
            Dict: Cleaning tool details.
        """
        return {
            "name": self.name,
            "materials": [material.to_dict() for material in self.materials],
            "sustainable": self.is_sustainable()
        }


# Simulate the supply chain
def simulate_supply_chain():
    """
    Simulate the supply chain for household cleaning tools.
    """
    # Create suppliers
    supplier1 = Supplier("EcoWood Supplies", fsc_certified=True)
    supplier2 = Supplier("PlasticCo", fsc_certified=False)

    # Create materials
    material1 = Material("Wood Handle", supplier=supplier1)
    material2 = Material("Plastic Bristles", supplier=supplier2)

    # Create cleaning tools
    cleaning_tool = CleaningTool("Eco-Friendly Brush", materials=[material1, material2])

    # Output results
    try:
        print("Cleaning Tool Details:")
        print(json.dumps(cleaning_tool.to_dict(), indent=4))
        
        if cleaning_tool.is_sustainable():
            print("This cleaning tool is sustainably produced.")
        else:
            print("This cleaning tool is not sustainably produced.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point of the program
if __name__ == "__main__":
    simulate_supply_chain()
```
