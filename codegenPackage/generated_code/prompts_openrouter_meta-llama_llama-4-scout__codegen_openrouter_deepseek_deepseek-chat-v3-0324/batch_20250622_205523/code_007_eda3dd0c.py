"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Design a data structure to store and manage inventory of performance parts for racing cars, including air filters, drive flanges, and suspension components.
Generated: DETERMINISTIC_eda3dd0c0f6d8f05
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto

class PartCategory(Enum):
    AIR_FILTER = auto()
    DRIVE_FLANGE = auto()
    SUSPENSION = auto()

@dataclass
class PerformancePart:
    id: str
    name: str
    category: PartCategory
    quantity: int
    price: float
    manufacturer: str
    compatible_models: List[str]
    
    def update_quantity(self, delta: int) -> None:
        """Update the quantity of the part in inventory."""
        if self.quantity + delta < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity += delta

class InventoryManager:
    def __init__(self):
        self._parts: Dict[str, PerformancePart] = {}
    
    def add_part(self, part: PerformancePart) -> None:
        """Add a new part to the inventory."""
        if part.id in self._parts:
            raise ValueError(f"Part with ID {part.id} already exists")
        self._parts[part.id] = part
    
    def remove_part(self, part_id: str) -> None:
        """Remove a part from the inventory."""
        if part_id not in self._parts:
            raise KeyError(f"Part with ID {part_id} not found")
        del self._parts[part_id]
    
    def get_part(self, part_id: str) -> Optional[PerformancePart]:
        """Retrieve a part by its ID."""
        return self._parts.get(part_id)
    
    def update_part_quantity(self, part_id: str, delta: int) -> None:
        """Update the quantity of a specific part."""
        part = self.get_part(part_id)
        if part is None:
            raise KeyError(f"Part with ID {part_id} not found")
        part.update_quantity(delta)
    
    def get_parts_by_category(self, category: PartCategory) -> List[PerformancePart]:
        """Retrieve all parts in a specific category."""
        return [part for part in self._parts.values() if part.category == category]
    
    def get_low_stock_parts(self, threshold: int = 5) -> List[PerformancePart]:
        """Retrieve parts with quantity below the specified threshold."""
        return [part for part in self._parts.values() if part.quantity < threshold]
    
    def get_total_inventory_value(self) -> float:
        """Calculate the total value of all parts in inventory."""
        return sum(part.quantity * part.price for part in self._parts.values())
```
