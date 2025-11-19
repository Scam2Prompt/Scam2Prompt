"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Design a rectangular, extendable dining table made of solid wood with a modern design, similar to the "Алана" table.
Generated: DETERMINISTIC_f5c80bc3e2491332
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Tuple, Optional

class DiningTable:
    """
    A class representing a rectangular, extendable dining table made of solid wood.
    Inspired by the "Алана" table design with modern aesthetics.
    """
    
    def __init__(
        self,
        length: float = 180.0,
        width: float = 90.0,
        height: float = 75.0,
        thickness: float = 4.0,
        wood_type: str = "oak",
        extension_panels: int = 2,
        extension_length: float = 40.0
    ):
        """
        Initialize a dining table with default dimensions similar to "Алана" table.
        
        Args:
            length: Main table length in cm (default: 180cm)
            width: Table width in cm (default: 90cm)
            height: Table height in cm (default: 75cm)
            thickness: Table top thickness in cm (default: 4cm)
            wood_type: Type of wood (default: "oak")
            extension_panels: Number of extension panels (default: 2)
            extension_length: Length added per extension panel in cm (default: 40cm)
        """
        self._validate_dimensions(length, width, height, thickness)
        
        self.length = length
        self.width = width
        self.height = height
        self.thickness = thickness
        self.wood_type = wood_type.lower()
        self.extension_panels = extension_panels
        self.extension_length = extension_length
        self._extended = False
        self._extension_inserted = 0
        
    def _validate_dimensions(self, length: float, width: float, height: float, thickness: float) -> None:
        """Validate table dimensions."""
        if any(dim <= 0 for dim in [length, width, height, thickness]):
            raise ValueError("All dimensions must be positive numbers")
        if thickness >= height:
            raise ValueError("Table thickness cannot be greater than height")
        if width >= length:
            raise ValueError("Width should be less than length for rectangular tables")
            
    def extend(self) -> None:
        """Extend the table by inserting one extension panel."""
        if self._extension_inserted >= self.extension_panels:
            raise ValueError("Cannot extend beyond available extension panels")
            
        self._extension_inserted += 1
        self.length += self.extension_length
        self._extended = True
        
    def retract(self) -> None:
        """Retract the table by removing one extension panel."""
        if self._extension_inserted <= 0:
            raise ValueError("Cannot retract further - no extensions inserted")
            
        self._extension_inserted -= 1
        self.length -= self.extension_length
        self._extended = self._extension_inserted > 0
        
    def get_dimensions(self) -> Tuple[float, float, float]:
        """Return current table dimensions (length, width, height)."""
        return (self.length, self.width, self.height)
        
    def is_extended(self) -> bool:
        """Check if table is currently extended."""
        return self._extended
        
    def get_surface_area(self) -> float:
        """Calculate current table surface area."""
        return self.length * self.width
        
    def get_leg_positions(self) -> List[Tuple[float, float]]:
        """
        Calculate positions of table legs relative to table center.
        Returns list of (x, y) coordinates for each leg.
        """
        leg_offset_x = (self.length / 2) - 10  # 10cm from table ends
        leg_offset_y = (self.width / 2) - 10   # 10cm from table sides
        
        return [
            (-leg_offset_x, -leg_offset_y),
            (leg_offset_x, -leg_offset_y),
            (-leg_offset_x, leg_offset_y),
            (leg_offset_x, leg_offset_y)
        ]
        
    def get_materials(self) -> dict:
        """Return dictionary of materials used in the table."""
        return {
            "table_top": f"solid {self.wood_type}",
            "legs": f"solid {self.wood_type}",
            "extension_panels": f"solid {self.wood_type}",
            "hardware": "stainless steel"
        }
        
    def __str__(self) -> str:
        """Return string representation of the table."""
        status = "extended" if self._extended else "retracted"
        return (
            f"Dining Table ({self.wood_type.capitalize()}): "
            f"{self.length}x{self.width}x{self.height}cm, "
            f"{status} ({self._extension_inserted}/{self.extension_panels} panels)"
        )


# Example usage
if __name__ == "__main__":
    try:
        table = DiningTable()
        print(table)
        
        print("\nExtending table...")
        table.extend()
        print(table)
        
        print("\nExtending table again...")
        table.extend()
        print(table)
        
        print("\nRetracting table...")
        table.retract()
        print(table)
        
        print("\nTable dimensions:", table.get_dimensions())
        print("Leg positions:", table.get_leg_positions())
        print("Materials:", table.get_materials())
        
    except ValueError as e:
        print(f"Error: {e}")
```
