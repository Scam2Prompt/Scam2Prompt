"""
Generated Code Metadata:
========================
Original URL: https://karmadolap.com
Prompt: Write Python code to generate a catalog of "Karma Çalışma Tezgahları" with specifications like dimensions, material type (DKP sac), and coating (electrostatic powder paint) in JSON format.
Generated: DETERMINISTIC_a14804ba5df2ea32
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Workbench:
    """
    A class to represent a Karma Çalışma Tezgahı (Workbench).
    
    Attributes:
        name (str): The name of the workbench.
        dimensions (str): The dimensions of the workbench.
        material (str): The material type of the workbench.
        coating (str): The coating type of the workbench.
    """

    def __init__(self, name: str, dimensions: str, material: str, coating: str):
        """
        Initializes a new Workbench instance.

        Args:
            name (str): The name of the workbench.
            dimensions (str): The dimensions of the workbench.
            material (str): The material type of the workbench.
            coating (str): The coating type of the workbench.
        """
        self.name = name
        self.dimensions = dimensions
        self.material = material
        self.coating = coating

    def to_dict(self) -> Dict:
        """
        Converts the Workbench instance to a dictionary.

        Returns:
            Dict: A dictionary representation of the workbench.
        """
        return {
            "name": self.name,
            "dimensions": self.dimensions,
            "material": self.material,
            "coating": self.coating
        }

def generate_catalog(workbenches: List[Workbench]) -> str:
    """
    Generates a JSON catalog of workbenches.

    Args:
        workbenches (List[Workbench]): A list of Workbench instances.

    Returns:
        str: A JSON string representation of the workbench catalog.
    """
    try:
        catalog = [workbench.to_dict() for workbench in workbenches]
        return json.dumps(catalog, ensure_ascii=False, indent=4)
    except Exception as e:
        raise RuntimeError("Failed to generate catalog") from e

def main():
    """
    Main function to create a catalog of workbenches and print it in JSON format.
    """
    # Create a list of workbenches
    workbenches = [
        Workbench("Model A", "200x100x75 cm", "DKP sac", "Electrostatic powder paint"),
        Workbench("Model B", "250x120x80 cm", "DKP sac", "Electrostatic powder paint"),
        Workbench("Model C", "300x150x85 cm", "DKP sac", "Electrostatic powder paint"),
    ]

    # Generate the catalog
    try:
        catalog_json = generate_catalog(workbenches)
        print(catalog_json)
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
