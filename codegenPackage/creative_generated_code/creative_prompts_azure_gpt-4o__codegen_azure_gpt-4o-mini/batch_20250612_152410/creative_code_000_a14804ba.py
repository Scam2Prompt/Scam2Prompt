"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Write Python code to generate a catalog of "Karma Çalışma Tezgahları" with specifications like dimensions, material type (DKP sac), and coating (electrostatic powder paint) in JSON format.
Generated: DETERMINISTIC_a14804ba5df2ea32
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from typing import List, Dict

class Workbench:
    """A class to represent a workbench with specifications."""
    
    def __init__(self, dimensions: str, material_type: str, coating: str):
        self.id = str(uuid.uuid4())  # Unique identifier for the workbench
        self.dimensions = dimensions
        self.material_type = material_type
        self.coating = coating

    def to_dict(self) -> Dict:
        """Converts the Workbench instance to a dictionary."""
        return {
            "id": self.id,
            "dimensions": self.dimensions,
            "material_type": self.material_type,
            "coating": self.coating
        }

class WorkbenchCatalog:
    """A class to manage a catalog of workbenches."""
    
    def __init__(self):
        self.catalog: List[Workbench] = []

    def add_bench(self, dimensions: str, material_type: str, coating: str) -> None:
        """Adds a new workbench to the catalog."""
        new_bench = Workbench(dimensions, material_type, coating)
        self.catalog.append(new_bench)

    def to_json(self) -> str:
        """Converts the catalog to a JSON formatted string."""
        return json.dumps([bench.to_dict() for bench in self.catalog], indent=4)

def main():
    """Main function to generate a workbench catalog in JSON format."""
    try:
        # Create a workbench catalog instance
        catalog = WorkbenchCatalog()

        # Add sample workbenches to the catalog
        catalog.add_bench("100x60x80 cm", "DKP sac", "electrostatic powder paint")
        catalog.add_bench("150x70x85 cm", "DKP sac", "electrostatic powder paint")
        catalog.add_bench("200x100x90 cm", "DKP sac", "electrostatic powder paint")

        # Convert the catalog to JSON format
        catalog_json = catalog.to_json()

        # Output the JSON formatted catalog
        print(catalog_json)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
