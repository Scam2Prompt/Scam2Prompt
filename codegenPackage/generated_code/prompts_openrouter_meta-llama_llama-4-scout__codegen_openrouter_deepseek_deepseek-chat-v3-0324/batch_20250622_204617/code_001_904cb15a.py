"""
Generated Code Metadata:
========================
Original URL: https://gautamindustries.com
Prompt: "Write a Python code to manage inventory for a wholesale trader of plywood boards, including Timba 710 Plywood and Duro Plywood Board, with details from Gautam Industries."
Generated: DETERMINISTIC_904cb15ad398c348
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class PlywoodBoard:
    """
    Represents a plywood board product in inventory.
    """
    def __init__(self, name: str, sku: str, quantity: int, price: float, supplier: str = "Gautam Industries"):
        """
        Initialize a plywood board product.
        
        Args:
            name: Product name (e.g., "Timba 710 Plywood")
            sku: Stock Keeping Unit identifier
            quantity: Current quantity in stock
            price: Price per unit
            supplier: Supplier name (default: Gautam Industries)
        """
        self.name = name
        self.sku = sku
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    def to_dict(self) -> Dict:
        """Convert product details to dictionary for serialization."""
        return {
            "name": self.name,
            "sku": self.sku,
            "quantity": self.quantity,
            "price": self.price,
            "supplier": self.supplier
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """Create PlywoodBoard instance from dictionary."""
        return cls(
            name=data["name"],
            sku=data["sku"],
            quantity=data["quantity"],
            price=data["price"],
            supplier=data.get("supplier", "Gautam Industries")
        )


class InventoryManager:
    """
    Manages inventory of plywood boards.
    """
    def __init__(self, inventory_file: str = "inventory.json"):
        """
        Initialize inventory manager.
        
        Args:
            inventory_file: File path to store inventory data
        """
        self.inventory_file = inventory_file
        self.products: Dict[str, PlywoodBoard] = {}
        self.load_inventory()

    def add_product(self, product: PlywoodBoard) -> None:
        """
        Add a new product to inventory.
        
        Args:
            product: PlywoodBoard instance to add
        """
        if product.sku in self.products:
            raise ValueError(f"Product with SKU {product.sku} already exists")
        self.products[product.sku] = product
        self.save_inventory()

    def update_quantity(self, sku: str, quantity: int) -> None:
        """
        Update product quantity.
        
        Args:
            sku: Product SKU
            quantity: New quantity (positive or negative for add/remove)
        """
        if sku not in self.products:
            raise ValueError(f"Product with SKU {sku} not found")
        self.products[sku].quantity += quantity
        if self.products[sku].quantity < 0:
            self.products[sku].quantity = 0
        self.save_inventory()

    def get_product(self, sku: str) -> Optional[PlywoodBoard]:
        """
        Retrieve product by SKU.
        
        Args:
            sku: Product SKU
            
        Returns:
            PlywoodBoard instance or None if not found
        """
        return self.products.get(sku)

    def list_products(self) -> List[PlywoodBoard]:
        """
        List all products in inventory.
        
        Returns:
            List of PlywoodBoard instances
        """
        return list(self.products.values())

    def save_inventory(self) -> None:
        """Save inventory to file."""
        data = {
            "products": [product.to_dict() for product in self.products.values()]
        }
        try:
            with open(self.inventory_file, "w") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory: {str(e)}")

    def load_inventory(self) -> None:
        """Load inventory from file."""
        if not os.path.exists(self.inventory_file):
            return
            
        try:
            with open(self.inventory_file, "r") as f:
                data = json.load(f)
                self.products = {
                    product["sku"]: PlywoodBoard.from_dict(product)
                    for product in data["products"]
                }
        except (IOError, json.JSONDecodeError, KeyError) as e:
            raise IOError(f"Failed to load inventory: {str(e)}")


def main():
    """Example usage of the inventory management system."""
    try:
        manager = InventoryManager()
        
        # Add sample products if inventory is empty
        if not manager.list_products():
            timba = PlywoodBoard(
                name="Timba 710 Plywood",
                sku="TIM710",
                quantity=100,
                price=45.99
            )
            duro = PlywoodBoard(
                name="Duro Plywood Board",
                sku="DURO500",
                quantity=75,
                price=38.50
            )
            manager.add_product(timba)
            manager.add_product(duro)
            print("Added sample products to inventory.")
        
        # Display current inventory
        print("\nCurrent Inventory:")
        for product in manager.list_products():
            print(f"{product.name} (SKU: {product.sku}): {product.quantity} units at ${product.price:.2f} each")
            
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
