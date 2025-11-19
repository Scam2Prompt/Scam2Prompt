"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: "Write a Python code to manage inventory of dry facade system components, including products like aluminum runners and clips."
Generated: DETERMINISTIC_8bf4a042f349da3d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import os


@dataclass
class Component:
    """Class to represent a dry facade system component."""
    name: str
    sku: str
    quantity: int
    price: float
    description: Optional[str] = None


class InventoryManager:
    """Class to manage inventory of dry facade system components."""
    
    def __init__(self, filename: str = "inventory.json"):
        """Initialize inventory manager with storage file."""
        self.filename = filename
        self.components: Dict[str, Component] = {}
        self._load_inventory()
    
    def _load_inventory(self) -> None:
        """Load inventory from JSON file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    for item in data:
                        component = Component(**item)
                        self.components[component.sku] = component
        except Exception as e:
            print(f"Error loading inventory: {e}")
    
    def _save_inventory(self) -> None:
        """Save inventory to JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(
                    [vars(component) for component in self.components.values()],
                    f,
                    indent=4
                )
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_component(self, component: Component) -> None:
        """Add a new component to inventory."""
        if component.sku in self.components:
            raise ValueError(f"Component with SKU {component.sku} already exists")
        self.components[component.sku] = component
        self._save_inventory()
    
    def update_component(self, sku: str, quantity: Optional[int] = None, 
                        price: Optional[float] = None, 
                        description: Optional[str] = None) -> None:
        """Update existing component properties."""
        if sku not in self.components:
            raise ValueError(f"Component with SKU {sku} not found")
        
        component = self.components[sku]
        if quantity is not None:
            component.quantity = quantity
        if price is not None:
            component.price = price
        if description is not None:
            component.description = description
        
        self._save_inventory()
    
    def remove_component(self, sku: str) -> None:
        """Remove component from inventory."""
        if sku not in self.components:
            raise ValueError(f"Component with SKU {sku} not found")
        del self.components[sku]
        self._save_inventory()
    
    def get_component(self, sku: str) -> Component:
        """Get component by SKU."""
        if sku not in self.components:
            raise ValueError(f"Component with SKU {sku} not found")
        return self.components[sku]
    
    def list_components(self) -> List[Component]:
        """List all components in inventory."""
        return list(self.components.values())
    
    def search_components(self, name: str) -> List[Component]:
        """Search components by name (case-insensitive partial match)."""
        return [
            component for component in self.components.values() 
            if name.lower() in component.name.lower()
        ]
    
    def get_low_stock_components(self, threshold: int = 10) -> List[Component]:
        """Get components with quantity below threshold."""
        return [
            component for component in self.components.values()
            if component.quantity < threshold
        ]


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add some example components
    try:
        manager.add_component(Component(
            name="Aluminum Runner 50mm",
            sku="AR50",
            quantity=100,
            price=12.99,
            description="50mm aluminum runner for dry facade systems"
        ))
        
        manager.add_component(Component(
            name="Stainless Steel Clip",
            sku="SSC20",
            quantity=50,
            price=5.99,
            description="Stainless steel clip for facade mounting"
        ))
    except ValueError as e:
        print(f"Error adding component: {e}")
    
    # List all components
    print("Current Inventory:")
    for component in manager.list_components():
        print(f"{component.name} (SKU: {component.sku}) - Qty: {component.quantity}, Price: ${component.price}")
    
    # Update a component
    try:
        manager.update_component("AR50", quantity=80)
    except ValueError as e:
        print(f"Error updating component: {e}")
    
    # Search for components
    print("\nSearch results for 'aluminum':")
    for component in manager.search_components("aluminum"):
        print(f"{component.name} (SKU: {component.sku})")
    
    # Get low stock items
    print("\nLow stock items:")
    for component in manager.get_low_stock_components(60):
        print(f"{component.name} (SKU: {component.sku}) - Qty: {component.quantity}")
```
