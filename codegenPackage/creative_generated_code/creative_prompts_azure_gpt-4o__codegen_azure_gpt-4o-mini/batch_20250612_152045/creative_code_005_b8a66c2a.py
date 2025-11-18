"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Write code to generate a catalog of industrial brushes with customizable features, including EU-standardized dimensions and client-specific models, as detailed on the VIRCOMEM website.
Generated: DETERMINISTIC_b8a66c2a9b29be2e
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class Brush:
    """Class representing an industrial brush."""
    model: str
    dimensions: Dict[str, float]  # Dimensions in millimeters (e.g., {'width': 50.0, 'length': 150.0, 'diameter': 30.0})
    bristle_material: str
    handle_material: str
    compliant_with_standard: bool = field(default=False)

    def __post_init__(self):
        """Post-initialization to ensure dimensions are valid."""
        if not self.is_valid_dimensions():
            raise ValueError(f"Invalid dimensions for brush model {self.model}: {self.dimensions}")

    def is_valid_dimensions(self) -> bool:
        """Check if the brush dimensions comply with EU standards."""
        # EU standards for industrial brushes can vary, this is a placeholder for actual checks
        return all(isinstance(value, (int, float)) and value > 0 for value in self.dimensions.values())

    def to_dict(self) -> Dict:
        """Convert the brush instance to a dictionary for JSON serialization."""
        return {
            "model": self.model,
            "dimensions": self.dimensions,
            "bristle_material": self.bristle_material,
            "handle_material": self.handle_material,
            "compliant_with_standard": self.compliant_with_standard,
        }

class BrushCatalog:
    """Class to manage a catalog of industrial brushes."""
    
    def __init__(self):
        """Initialize an empty brush catalog."""
        self.brushes: List[Brush] = []

    def add_brush(self, brush: Brush) -> None:
        """Add a new brush to the catalog."""
        self.brushes.append(brush)

    def find_brush_by_model(self, model: str) -> Optional[Brush]:
        """Find a brush by its model name."""
        for brush in self.brushes:
            if brush.model == model:
                return brush
        return None

    def export_catalog(self, filename: str) -> None:
        """Export the catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([brush.to_dict() for brush in self.brushes], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Error writing to file {filename}: {e}")

# Example usage:
if __name__ == "__main__":
    # Create a brush catalog instance
    catalog = BrushCatalog()

    # Add brushes to the catalog
    try:
        catalog.add_brush(Brush("BrushA", {"width": 50, "length": 150, "diameter": 30}, "Nylon", "Plastic", True))
        catalog.add_brush(Brush("BrushB", {"width": 60, "length": 200, "diameter": 35}, "Natural", "Wood", False))

        # Export the catalog to a JSON file
        catalog.export_catalog("brush_catalog.json")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
