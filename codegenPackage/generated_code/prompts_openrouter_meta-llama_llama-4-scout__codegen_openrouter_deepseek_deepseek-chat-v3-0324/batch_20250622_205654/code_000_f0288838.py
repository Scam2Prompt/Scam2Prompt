"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: "Write a Python code to manage inventory of industrial brushes with different dimensions and characteristics, similar to those offered by Vircomem."
Generated: DETERMINISTIC_f028883801104bb0
Batch ID: 20250622_205654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum


class BrushMaterial(Enum):
    NYLON = "Nylon"
    POLYPROPYLENE = "Polypropylene"
    POLYESTER = "Polyester"
    STEEL = "Steel"
    BRASS = "Brass"


class BrushType(Enum):
    TUBE = "Tube Brush"
    DISC = "Disc Brush"
    END = "End Brush"
    STRIP = "Strip Brush"
    SPIRAL = "Spiral Brush"


@dataclass
class BrushDimensions:
    diameter: float  # in mm
    length: float    # in mm
    wire_diameter: Optional[float] = None  # in mm, for wire brushes


@dataclass
class InventoryItem:
    sku: str
    name: str
    brush_type: BrushType
    material: BrushMaterial
    dimensions: BrushDimensions
    quantity: int
    price: float
    description: Optional[str] = None


class InventoryManager:
    def __init__(self, inventory_file: str = "inventory.json"):
        self.inventory_file = inventory_file
        self.inventory: List[InventoryItem] = []
        self.load_inventory()

    def load_inventory(self) -> None:
        try:
            with open(self.inventory_file, 'r') as f:
                data = json.load(f)
                self.inventory = [
                    InventoryItem(
                        sku=item['sku'],
                        name=item['name'],
                        brush_type=BrushType(item['brush_type']),
                        material=BrushMaterial(item['material']),
                        dimensions=BrushDimensions(**item['dimensions']),
                        quantity=item['quantity'],
                        price=item['price'],
                        description=item.get('description')
                    ) for item in data
                ]
        except FileNotFoundError:
            self.inventory = []
        except json.JSONDecodeError:
            raise ValueError("Invalid inventory file format")
        except Exception as e:
            raise Exception(f"Error loading inventory: {str(e)}")

    def save_inventory(self) -> None:
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(
                    [asdict(item) for item in self.inventory],
                    f,
                    indent=2,
                    default=str
                )
        except Exception as e:
            raise Exception(f"Error saving inventory: {str(e)}")

    def add_item(self, item: InventoryItem) -> None:
        if any(existing.sku == item.sku for existing in self.inventory):
            raise ValueError(f"Item with SKU {item.sku} already exists")
        self.inventory.append(item)
        self.save_inventory()

    def remove_item(self, sku: str) -> None:
        item = self.find_item(sku)
        if item:
            self.inventory.remove(item)
            self.save_inventory()
        else:
            raise ValueError(f"Item with SKU {sku} not found")

    def update_item_quantity(self, sku: str, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        item = self.find_item(sku)
        if item:
            item.quantity = quantity
            self.save_inventory()
        else:
            raise ValueError(f"Item with SKU {sku} not found")

    def find_item(self, sku: str) -> Optional[InventoryItem]:
        for item in self.inventory:
            if item.sku == sku:
                return item
        return None

    def list_items(self) -> List[InventoryItem]:
        return self.inventory.copy()

    def search_by_type(self, brush_type: BrushType) -> List[InventoryItem]:
        return [item for item in self.inventory if item.brush_type == brush_type]

    def search_by_material(self, material: BrushMaterial) -> List[InventoryItem]:
        return [item for item in self.inventory if item.material == material]

    def get_low_stock_items(self, threshold: int = 5) -> List[InventoryItem]:
        return [item for item in self.inventory if item.quantity <= threshold]


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    # Add sample brush
    sample_brush = InventoryItem(
        sku="BR001",
        name="Industrial Tube Brush",
        brush_type=BrushType.TUBE,
        material=BrushMaterial.NYLON,
        dimensions=BrushDimensions(diameter=25.0, length=300.0),
        quantity=10,
        price=12.99,
        description="Heavy-duty tube brush for industrial cleaning"
    )

    try:
        manager.add_item(sample_brush)
        print("Item added successfully")
    except ValueError as e:
        print(f"Error: {e}")

    # List all items
    print("\nCurrent Inventory:")
    for item in manager.list_items():
        print(f"{item.sku}: {item.name} - Qty: {item.quantity}")
```
